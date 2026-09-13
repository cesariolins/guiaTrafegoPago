#!/usr/bin/env python3
"""Gera criativos estáticos em PNG a partir de um JSON, nos tamanhos do Meta.

Uso:
    python gerar-criativos.py exemplo-clinica.json
    python gerar-criativos.py exemplo-clinica.json --formato story
    python gerar-criativos.py --teste      # roda o autoteste do revisor de copy

Requer: playwright (já instalado) — o layout é HTML/CSS renderizado pelo Chromium,
que é um motor de diagramação muito melhor do que desenhar texto na mão.

Antes de renderizar, cada copy passa pelo revisor de política (CFO/CFM/Meta).
Erro bloqueia a geração; aviso deixa passar e reclama.
"""
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).parent
SAIDA = AQUI / "saida"

# Tamanhos que o Meta usa em 2026. O Advantage+ recorta sozinho, mas entregar
# no formato nativo evita corte feio em rosto e em texto.
FORMATOS = {
    "feed": (1080, 1350),      # vertical, ocupa mais tela — use como padrão
    "quadrado": (1080, 1080),
    "story": (1080, 1920),     # stories e reels
}

# ─────────────────────────────────────────────────────────────────────────────
# Revisor de política
# ─────────────────────────────────────────────────────────────────────────────
# (regex, a quem se aplica, gravidade, motivo)
#   "ambos"  = qualquer conselho      "CFM" = só médico      "CFO" = só dentista
REGRAS = [
    (r"antes\s*[e/]\s*depois", "ambos", "erro",
     "Meta nao aprova antes e depois em anuncio, mesmo com TCLE assinado."),
    (r"\b(garant\w+|100%\s*de\s*sucesso|resultado\s+certo)\b", "ambos", "erro",
     "Promessa de resultado e proibida pelo CFO e pelo CFM."),
    (r"\b(o|a)\s+(melhor|maior|unic[oa]|numero\s*1|referencia)\b", "ambos", "erro",
     "Autopromocao de superioridade e proibida pelos dois conselhos."),
    (r"\b(depoimento|paciente\s+conta|veja\s+o\s+relato)\b", "ambos", "erro",
     "Depoimento de paciente e proibido pelo CFO e pelo CFM."),
    # Atributo pessoal — o Meta ficou mais rigoroso nisso em 2026.
    (r"\b(voce\s+(esta|tem|sofre|e\s+)|cansad[oa]\s+de|sofre\s+com|vergonha|"
     r"complexo|inseguran[çc]a\s+com)\b", "ambos", "erro",
     "Copy sugere condicao pessoal: o Meta reprova. Fale do servico, nao da pessoa."),
    (r"\b(perdeu\s+(o|os)\s+dente|falta\s+(de\s+)?dente|dor\s+de\s+dente)\b", "ambos", "erro",
     "Atributo pessoal implicito. Descreva o procedimento, nao o problema do leitor."),
    # Preço: liberado na odontologia desde a CFO-271/2025, proibido no CFM.
    (r"(R\$\s*\d|\bpor\s+apenas\b|\ba\s+partir\s+de\s+R\$)", "CFM", "erro",
     "CFM 2.336/2023 proibe divulgar preco de forma que estimule consumo."),
    (r"\b(promo[çc][ãa]o|desconto|imperdivel|ultimas?\s+vagas?|so\s+hoje)\b", "CFM", "erro",
     "CFM proibe promocao e desconto na publicidade medica."),
    (r"\b(promo[çc][ãa]o|desconto)\b", "CFO", "aviso",
     "Liberado pela CFO-271/2025, mas o perfil nao pode virar catalogo de ofertas."),
    (r"\b(cura|trata|elimina|acaba\s+com|resolve)\s+(a|o|sua|seu)\b", "ambos", "aviso",
     "Beira promessa de resultado. Prefira descrever o procedimento."),
]


def revisar(texto: str, conselho: str) -> list[tuple[str, str]]:
    """Devolve [(gravidade, motivo)] para a copy. Lista vazia = liberado."""
    # Compara sem acento para uma regra só pegar "você", "voce" e "vôce".
    plano = texto.lower()
    for de, para in zip("áàâãéêíóôõúüç", "aaaaeeiooouuc"):
        plano = plano.replace(de, para)
    achados = []
    for padrao, alvo, gravidade, motivo in REGRAS:
        if alvo in ("ambos", conselho) and re.search(padrao, plano):
            achados.append((gravidade, motivo))
    return achados


# ─────────────────────────────────────────────────────────────────────────────
# Renderização
# ─────────────────────────────────────────────────────────────────────────────
MODELO = """<!doctype html>
<meta charset="utf-8">
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  html,body{{width:{w}px;height:{h}px;overflow:hidden}}
  body{{
    display:flex;flex-direction:column;justify-content:space-between;
    padding:{pad}px;
    background:linear-gradient(150deg,{cor} 0%,{cor2} 100%);
    color:{tinta};
    font-family:"Segoe UI Variable Display","Segoe UI",system-ui,Arial,sans-serif;
    -webkit-font-smoothing:antialiased;
  }}
  .foto{{position:absolute;inset:0;background:url("{foto}") center/cover;z-index:0}}
  .veu{{position:absolute;inset:0;z-index:1;
    background:linear-gradient(180deg,rgba(0,0,0,.15) 0%,{cor2} 88%)}}
  .camada{{position:relative;z-index:2;display:flex;flex-direction:column;
    justify-content:space-between;height:100%}}
  /* O texto ocupa a sobra e fica centrado: sem isso, copy curta deixa um
     buraco enorme entre o titulo e o rodape. */
  .topo{{flex:1;display:flex;flex-direction:column;justify-content:center}}

  .chapeu{{font-size:{f_chapeu}px;font-weight:700;letter-spacing:.14em;
    text-transform:uppercase;opacity:.82}}
  .barra{{width:{barra}px;height:{barra_h}px;background:{tinta};opacity:.9;
    margin:{gap}px 0 {gap}px}}
  h1{{font-size:{f_titulo}px;font-weight:800;line-height:1.04;letter-spacing:-.025em;
    text-wrap:balance}}
  .apoio{{font-size:{f_apoio}px;font-weight:400;line-height:1.35;opacity:.9;
    margin-top:{gap}px;max-width:88%}}
  ul{{list-style:none;margin-top:{gap}px}}
  li{{font-size:{f_apoio}px;line-height:1.3;padding-left:{f_apoio}px;
    margin-bottom:{meio}px;position:relative;opacity:.94}}
  li::before{{content:"";position:absolute;left:0;top:{ponto_t}px;
    width:{ponto}px;height:{ponto}px;border-radius:50%;background:{tinta};opacity:.75}}

  .rodape{{display:flex;justify-content:space-between;align-items:flex-end;gap:{gap}px}}
  .cta{{display:inline-block;padding:{cta_v}px {cta_h}px;border-radius:{raio}px;
    background:{tinta};color:{cor2};font-size:{f_cta}px;font-weight:700}}
  .assina{{text-align:right;font-size:{f_assina}px;line-height:1.35;opacity:.72}}
  .assina b{{display:block;font-weight:700;opacity:1}}
</style>
{fundo}
<div class="camada">
  <div class="topo">
    <p class="chapeu">{chapeu}</p>
    <div class="barra"></div>
    <h1>{titulo}</h1>
    {corpo}
  </div>
  <div class="rodape">
    <span class="cta">{cta}</span>
    <div class="assina"><b>{cliente}</b>{responsavel}</div>
  </div>
</div>
"""


def escala(w: int, h: int) -> dict:
    """Tamanhos proporcionais ao formato. Base calibrada no 1080x1350."""
    k = min(w, h) / 1080
    alto = h / w > 1.4          # story é mais estreito: título menor, respiro maior
    return dict(
        pad=int(86 * k), gap=int(26 * k), meio=int(14 * k),
        f_chapeu=int(30 * k), f_titulo=int((84 if alto else 96) * k),
        f_apoio=int(36 * k), f_cta=int(34 * k), f_assina=int(24 * k),
        barra=int(96 * k), barra_h=max(3, int(6 * k)),
        ponto=int(11 * k), ponto_t=int(17 * k),
        cta_v=int(22 * k), cta_h=int(38 * k), raio=int(14 * k),
    )


def montar_html(cfg: dict, cr: dict, w: int, h: int) -> str:
    marca = cfg.get("marca", {})
    foto = cr.get("foto")
    if cr.get("layout") == "lista" and cr.get("itens"):
        corpo = "<ul>" + "".join(f"<li>{i}</li>" for i in cr["itens"]) + "</ul>"
    else:
        corpo = f'<p class="apoio">{cr.get("apoio","")}</p>' if cr.get("apoio") else ""
    fundo = f'<div class="foto"></div><div class="veu"></div>' if foto else ""
    return MODELO.format(
        w=w, h=h, foto=foto or "", fundo=fundo, corpo=corpo,
        cor=marca.get("cor", "#12513f"), cor2=marca.get("cor2", "#0a3327"),
        tinta=marca.get("tinta", "#ffffff"),
        chapeu=cr.get("chapeu", ""), titulo=cr["titulo"],
        cta=cr.get("cta", "Saiba mais"),
        cliente=cfg["cliente"], responsavel=cfg.get("responsavel", ""),
        **escala(w, h),
    )


def gerar(caminho_cfg: Path, formatos: list[str]) -> int:
    cfg = json.loads(caminho_cfg.read_text(encoding="utf-8"))
    conselho = cfg.get("conselho", "CFO").upper()
    SAIDA.mkdir(exist_ok=True)

    aprovados, bloqueados = [], 0
    for cr in cfg["criativos"]:
        copy = " ".join(str(v) for k, v in cr.items()
                        if k in ("chapeu", "titulo", "apoio", "cta"))
        copy += " " + " ".join(cr.get("itens", []))
        problemas = revisar(copy, conselho)
        erros = [m for g, m in problemas if g == "erro"]
        avisos = [m for g, m in problemas if g == "aviso"]
        if erros:
            bloqueados += 1
            print(f"  BLOQUEADO  {cr['id']}")
            for m in erros:
                print(f"             {m}")
            continue
        for m in avisos:
            print(f"  aviso      {cr['id']}: {m}")
        aprovados.append(cr)

    if not aprovados:
        print("\nNada a renderizar.")
        return bloqueados

    from playwright.sync_api import sync_playwright
    tmp = AQUI / ".render.html"
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for cr in aprovados:
            for nome in formatos:
                w, h = FORMATOS[nome]
                tmp.write_text(montar_html(cfg, cr, w, h), encoding="utf-8")
                pg = nav.new_page(viewport={"width": w, "height": h})
                pg.goto(tmp.as_uri())
                destino = SAIDA / f"{cr['id']}-{nome}.png"
                pg.screenshot(path=str(destino))
                pg.close()
                print(f"  ok         {destino.relative_to(AQUI)}")
        nav.close()
    tmp.unlink(missing_ok=True)
    return bloqueados


# ─────────────────────────────────────────────────────────────────────────────
def autoteste():
    """O revisor é o que protege o cliente de um processo ético. Ele tem teste."""
    casos = [
        ("Veja o antes e depois do nosso paciente", "CFO", "erro"),
        ("Resultado garantido em 30 dias", "CFM", "erro"),
        ("Somos a melhor clinica da regiao", "CFO", "erro"),
        ("Voce esta com vergonha do seu sorriso?", "CFO", "erro"),
        ("Cansado de dor nas costas?", "CFM", "erro"),
        ("Consulta por apenas R$ 150", "CFM", "erro"),     # proibido p/ medico
        ("Consulta por apenas R$ 150", "CFO", None),       # liberado p/ dentista
        ("Promocao de clareamento", "CFO", "aviso"),
        ("Promocao de consulta", "CFM", "erro"),
        ("Implante em sessao unica: entenda como funciona", "CFO", None),
        ("Avaliacao ortopedica com exame de imagem no mesmo dia", "CFM", None),
    ]
    falhas = []
    for texto, conselho, esperado in casos:
        achados = revisar(texto, conselho)
        pior = "erro" if any(g == "erro" for g, _ in achados) else (
               "aviso" if achados else None)
        if pior != esperado:
            falhas.append(f"  {conselho}: {texto!r} -> esperado {esperado}, deu {pior}")
    if falhas:
        print("AUTOTESTE FALHOU:"); print("\n".join(falhas)); return 1
    print(f"Autoteste do revisor: {len(casos)} casos conferem.")
    return 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--teste" in args:
        sys.exit(autoteste())
    if not args:
        print(__doc__); sys.exit(1)
    fmt = [args[args.index("--formato") + 1]] if "--formato" in args else list(FORMATOS)
    cfg = AQUI / args[0]
    if not cfg.exists():
        print(f"nao encontrei {cfg}"); sys.exit(1)
    n = gerar(cfg, fmt)
    print(f"\nPronto. Saida em {SAIDA}" + (f"  |  {n} criativo(s) bloqueado(s)" if n else ""))
