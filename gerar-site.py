#!/usr/bin/env python3
"""Converte os .md do curso em um site HTML estático dentro de site/.

Uso:  python gerar-site.py
Requer:  pip install markdown

Reexecute sempre que editar qualquer .md — o site é descartável e regenerado do zero.
"""
import re
import shutil
from pathlib import Path

import markdown

RAIZ = Path(__file__).parent
SAIDA = RAIZ / "site"

# Ordem de leitura do curso. Define a navegação anterior/próximo.
ORDEM = [
    ("README.md", "Início", "🏠"),
    ("fase-00-fundamentos.md", "00 · Fundamentos", "🧭"),
    ("fase-01-matematica.md", "01 · A matemática", "🧮"),
    ("fase-02-infraestrutura.md", "02 · Infraestrutura", "🔧"),
    ("fase-03-meta-ads.md", "03 · Meta Ads", "📱"),
    ("fase-04-google-ads.md", "04 · Google Ads", "🔍"),
    ("fase-05-tiktok-kwai.md", "05 · TikTok e Kwai", "🎵"),
    ("fase-06-criativo-copy-oferta.md", "06 · Criativo e oferta", "🎨"),
    ("fase-07-mensuracao.md", "07 · Mensuração", "📊"),
    ("fase-08-otimizacao-escala.md", "08 · Otimização e escala", "📈"),
    ("fase-09-vender-o-servico.md", "09 · Vender o serviço", "💼"),
    ("fase-10-contrato-legal.md", "10 · Contrato e legal", "⚖️"),
    ("fase-11-operacao-rotina.md", "11 · Operação e rotina", "🔄"),
    ("fase-12-problemas-reais.md", "12 · Problemas reais", "🚨"),
    ("fase-13-pacote-saude-ia.md", "13 · Pacote saúde + IA", "🦷"),
    ("templates/proposta-comercial.md", "Proposta comercial", "📄"),
    ("templates/contrato-modelo.md", "Contrato modelo", "📑"),
    ("templates/briefing-onboarding.md", "Briefing e onboarding", "📋"),
    ("templates/relatorio-mensal.md", "Relatório mensal", "📊"),
    ("templates/auditoria-de-conta.md", "Auditoria de conta", "🔎"),
    ("templates/scripts-de-venda.md", "Scripts de venda", "💬"),
]

BLOCOS = [
    ("Fundamento", 1, 4),      # índices em ORDEM (início, fim exclusivo)
    ("Execução técnica", 4, 10),
    ("O negócio", 10, 15),
    ("Templates", 15, 21),
]


def html_de(md_path: Path) -> tuple[str, str]:
    """Converte um .md em (título, corpo html). Título = primeiro H1."""
    texto = md_path.read_text(encoding="utf-8")
    # md_in_html só processa markdown dentro de tags HTML que pedem explicitamente.
    # Sem isto, as respostas dos exercícios saem como texto bruto, sem negrito nem parágrafos.
    texto = texto.replace("<details>", '<details markdown="1">')
    corpo = markdown.markdown(
        texto,
        extensions=["tables", "fenced_code", "md_in_html", "sane_lists", "attr_list"],
    )
    m = re.search(r"<h1[^>]*>(.*?)</h1>", corpo, re.S)
    titulo = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else md_path.stem
    return titulo, corpo


def reescrever_links(corpo: str) -> str:
    """Aponta os links internos .md para os .html gerados.

    A calculadora é copiada mantendo planilhas/calculadora-viabilidade.html,
    então links para ela não precisam de tradução.
    """
    corpo = re.sub(r'(href="[^"]*?)\.md(#|")', r"\1.html\2", corpo)
    corpo = corpo.replace("README.html", "index.html")  # a home é index, não README
    corpo = corpo.replace('href="templates/"', 'href="templates/index.html"')
    # O curso usa muitas tabelas largas; sem wrapper elas estouram a tela do celular.
    corpo = corpo.replace("<table>", '<div class="tabela-rolavel"><table>')
    corpo = corpo.replace("</table>", "</table></div>")
    return corpo


def menu(atual: str, prefixo: str) -> str:
    """Sidebar com os blocos do curso. `prefixo` ajusta a profundidade (../)."""
    partes = []
    for nome_bloco, ini, fim in BLOCOS:
        partes.append(f'<p class="bloco">{nome_bloco}</p><ul>')
        for src, rotulo, emoji in ORDEM[ini:fim]:
            destino = prefixo + src.replace(".md", ".html")
            ativo = ' class="ativo"' if src == atual else ""
            partes.append(f'<li><a href="{destino}"{ativo}><i>{emoji}</i>{rotulo}</a></li>')
        partes.append("</ul>")
    # "Início" e a calculadora ficam fora dos blocos, no topo e no rodapé
    topo = (
        f'<ul class="topo"><li><a href="{prefixo}index.html"'
        f'{" class=\"ativo\"" if atual == "README.md" else ""}><i>🏠</i>Início</a></li></ul>'
    )
    ferramenta = (
        f'<p class="bloco">Ferramenta</p><ul><li>'
        f'<a href="{prefixo}planilhas/calculadora-viabilidade.html"><i>🧮</i>Calculadora</a>'
        f"</li></ul>"
    )
    return topo + "".join(partes) + ferramenta


def rodape_nav(i: int, prefixo: str) -> str:
    """Links anterior/próximo, na ordem do curso."""
    links = []
    if i > 0:
        src, rotulo, _ = ORDEM[i - 1]
        alvo = prefixo + ("index.html" if src == "README.md" else src.replace(".md", ".html"))
        links.append(f'<a class="nav-ant" href="{alvo}"><span>← Anterior</span>{rotulo}</a>')
    else:
        links.append("<span></span>")
    if i < len(ORDEM) - 1:
        src, rotulo, _ = ORDEM[i + 1]
        alvo = prefixo + src.replace(".md", ".html")
        links.append(f'<a class="nav-prox" href="{alvo}"><span>Próximo →</span>{rotulo}</a>')
    return f'<nav class="paginacao">{"".join(links)}</nav>'


PAGINA = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<!-- Fora de busca. robots.txt não serve em site de projeto do GitHub Pages:
     só vale na raiz do domínio. Para indexar um dia, apague esta linha. -->
<meta name="robots" content="noindex, nofollow">
<title>{titulo}</title>
<link rel="stylesheet" href="{prefixo}assets/estilo.css">
<script>
/* Roda antes do primeiro pixel, senão a página pisca no tema errado.
   Sem argumento, alterna. localStorage em try/catch: file:// pode bloquear. */
function tema(t){{var h=document.documentElement;
t=t||(h.dataset.tema=='escuro'?'claro':'escuro');h.dataset.tema=t;
try{{localStorage.setItem('tema',t)}}catch(e){{}}}}
try{{var _t=localStorage.getItem('tema')}}catch(e){{}}
document.documentElement.dataset.tema=_t||(matchMedia('(prefers-color-scheme:dark)').matches?'escuro':'claro');
</script>
</head>
<body>
<input type="checkbox" id="abrir-menu" hidden>
<label for="abrir-menu" class="botao-menu" aria-label="Abrir menu">☰</label>
<label for="abrir-menu" class="fundo-menu"></label>
<button class="botao-tema" onclick="tema()" aria-label="Alternar tema claro/escuro"
        title="Alternar tema claro/escuro"><span class="i-claro">🌙</span><span class="i-escuro">☀️</span></button>

<aside>
  <a class="marca" href="{prefixo}index.html">Tráfego Pago<small>do zero ao primeiro cliente</small></a>
  {menu}
</aside>

<main>
  <article>{corpo}</article>
  {paginacao}
  <footer class="rodape">Curso de tráfego pago · conteúdo de setembro de 2026</footer>
</main>
</body>
</html>
"""


def gerar():
    if SAIDA.exists():
        # Limpa apenas o que este script gera, preservando qualquer coisa que o usuário tenha posto lá.
        for alvo in ["index.html", "assets", "templates", "planilhas"]:
            p = SAIDA / alvo
            shutil.rmtree(p) if p.is_dir() else p.unlink(missing_ok=True)
        for p in SAIDA.glob("fase-*.html"):
            p.unlink()
    SAIDA.mkdir(exist_ok=True)
    (SAIDA / "assets").mkdir(exist_ok=True)
    (SAIDA / "templates").mkdir(exist_ok=True)
    (SAIDA / "planilhas").mkdir(exist_ok=True)

    (SAIDA / "assets" / "estilo.css").write_text(CSS, encoding="utf-8")
    shutil.copy2(
        RAIZ / "planilhas" / "calculadora-viabilidade.html",
        SAIDA / "planilhas" / "calculadora-viabilidade.html",
    )

    for i, (src, rotulo, _) in enumerate(ORDEM):
        origem = RAIZ / src
        if not origem.exists():
            print(f"  !!  faltando: {src}")
            continue
        titulo, corpo = html_de(origem)
        # A home já se chama "Tráfego Pago..."; evita "X — Tráfego Pago — Tráfego Pago".
        titulo = titulo if "Tráfego Pago" in titulo else f"{titulo} — Tráfego Pago"
        corpo = reescrever_links(corpo)
        prefixo = "../" if "/" in src else ""
        destino = SAIDA / ("index.html" if src == "README.md" else src.replace(".md", ".html"))
        destino.write_text(
            PAGINA.format(
                titulo=titulo,
                prefixo=prefixo,
                menu=menu(src, prefixo),
                corpo=corpo,
                paginacao=rodape_nav(i, prefixo),
            ),
            encoding="utf-8",
        )
        print(f"  ok  {destino.relative_to(RAIZ)}")

    # Índice dos templates, para o link "templates/" do README ter destino.
    # Fatia vem de BLOCOS para não dessincronizar quando uma fase nova entra no meio.
    _, tpl_ini, tpl_fim = BLOCOS[-1]
    itens = "".join(
        f'<li><a href="{s.split("/")[1].replace(".md", ".html")}"><i>{e}</i>{r}</a></li>'
        for s, r, e in ORDEM[tpl_ini:tpl_fim]
    )
    (SAIDA / "templates" / "index.html").write_text(
        PAGINA.format(
            titulo="Templates — Tráfego Pago",
            prefixo="../",
            menu=menu("", "../"),
            corpo=f"<h1>Templates</h1><p>Documentos prontos para preencher e usar.</p>"
                  f'<ul class="cartoes">{itens}</ul>',
            paginacao="",
        ),
        encoding="utf-8",
    )
    print("  ok  site/templates/index.html")
    print(f"\nPronto. Abra: {SAIDA / 'index.html'}")


CSS = """/* Gerado por gerar-site.py — não edite aqui, edite o script. */
/* light-dark() resolve pelo color-scheme, então os dois temas cabem numa lista só
   e o botão só precisa trocar o color-scheme. Sem JS, cai no tema do sistema. */
:root{
  color-scheme:light dark;
  --bg:light-dark(#f7f8fa,#0f1217);
  --card:light-dark(#fff,#171b22);
  --ink:light-dark(#16191f,#e7ebf1);
  --muted:light-dark(#5f6b7a,#96a0b0);
  --line:light-dark(#e3e7ed,#262c36);
  --accent:light-dark(#1a56db,#8ab0ff);
  --accent-suave:light-dark(#eaf0ff,#1a2233);
  --code-bg:light-dark(#f0f2f5,#1b2029);
  --sidebar:light-dark(#fbfcfd,#131720);
}
:root[data-tema=claro]{color-scheme:light}
:root[data-tema=escuro]{color-scheme:dark}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);
  font:16px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  -webkit-text-size-adjust:100%}

/* ─── Sidebar ─────────────────────────────────────── */
aside{position:fixed;top:0;left:0;width:272px;height:100vh;overflow-y:auto;
  background:var(--sidebar);border-right:1px solid var(--line);padding:22px 0 40px;z-index:20}
.marca{display:block;padding:0 20px 18px;margin-bottom:6px;border-bottom:1px solid var(--line);
  font-weight:700;font-size:16px;color:var(--ink);text-decoration:none;letter-spacing:-.01em}
.marca small{display:block;font-weight:400;font-size:12px;color:var(--muted);margin-top:2px}
aside .bloco{margin:20px 20px 6px;font-size:11px;font-weight:700;letter-spacing:.09em;
  text-transform:uppercase;color:var(--muted)}
aside ul{list-style:none;margin:0;padding:0}
aside ul.topo{margin-top:4px}
aside a{display:flex;align-items:center;gap:9px;padding:7px 20px;color:var(--ink);
  text-decoration:none;font-size:14.5px;border-left:3px solid transparent}
aside a i{font-style:normal;font-size:15px;width:19px;text-align:center;flex:none}
aside a:hover{background:var(--accent-suave)}
aside a.ativo{background:var(--accent-suave);border-left-color:var(--accent);
  color:var(--accent);font-weight:600}

.botao-menu,.fundo-menu{display:none}

/* Botão de tema — fica na faixa da sidebar no desktop, vira canto direito no celular */
.botao-tema{position:fixed;top:14px;left:214px;width:36px;height:36px;z-index:22;
  display:flex;align-items:center;justify-content:center;padding:0;line-height:1;
  background:var(--card);border:1px solid var(--line);border-radius:9px;
  font-size:15px;cursor:pointer;color:var(--ink)}
.botao-tema:hover{border-color:var(--accent)}
.botao-tema .i-escuro{display:none}
[data-tema=escuro] .botao-tema .i-claro{display:none}
[data-tema=escuro] .botao-tema .i-escuro{display:inline}

/* ─── Conteúdo ────────────────────────────────────── */
main{margin-left:272px;padding:44px 40px 72px;max-width:1180px}
article{max-width:800px}

h1{font-size:31px;line-height:1.25;letter-spacing:-.02em;margin:0 0 22px}
h2{font-size:22px;letter-spacing:-.01em;margin:44px 0 14px;padding-top:14px;
  border-top:1px solid var(--line)}
h2:first-of-type{border-top:0;padding-top:0}
h3{font-size:17.5px;margin:30px 0 10px}
h4{font-size:15.5px;margin:22px 0 8px;color:var(--muted)}
p{margin:0 0 14px}
a{color:var(--accent)}
strong{font-weight:650}
hr{border:0;border-top:1px solid var(--line);margin:34px 0}

ul,ol{margin:0 0 14px;padding-left:22px}
li{margin-bottom:5px}
li>ul,li>ol{margin-top:5px}

/* Blockquote — usado para as caixas de destaque do curso */
blockquote{margin:20px 0;padding:14px 18px;background:var(--card);
  border-left:3px solid var(--accent);border-radius:0 8px 8px 0}
blockquote>:last-child{margin-bottom:0}
blockquote h2,blockquote h3{margin-top:0;border:0;padding-top:0;font-size:17px}

/* Tabelas — o curso usa muitas; precisam rolar no celular */
.tabela-rolavel{overflow-x:auto;margin:0 0 18px;border:1px solid var(--line);
  border-radius:9px;background:var(--card)}
table{border-collapse:collapse;width:100%;font-size:14.5px}
th,td{padding:9px 13px;text-align:left;border-bottom:1px solid var(--line);
  vertical-align:top}
th{background:var(--bg);font-weight:650;font-size:13px;white-space:nowrap}
tr:last-child td{border-bottom:0}

/* Código e os diagramas ASCII */
code{background:var(--code-bg);padding:2px 6px;border-radius:5px;
  font:13.5px/1.5 ui-monospace,"Cascadia Code",Consolas,monospace}
pre{background:var(--code-bg);border:1px solid var(--line);border-radius:9px;
  padding:15px 17px;overflow-x:auto;margin:0 0 18px}
pre code{background:0;padding:0;font-size:13px;line-height:1.55;white-space:pre}

/* Respostas dos exercícios */
details{background:var(--card);border:1px solid var(--line);border-radius:9px;
  padding:13px 17px;margin:18px 0}
details[open]{padding-bottom:6px}
summary{cursor:pointer;font-weight:600;color:var(--accent);list-style:none}
summary::-webkit-details-marker{display:none}
summary::before{content:"▸ ";display:inline-block;transition:transform .15s}
details[open] summary::before{transform:rotate(90deg)}
details>:not(summary){margin-top:12px}

/* Checkboxes dos checklists (texto puro no md, viram marcadores) */
article input[type=checkbox]{margin-right:7px}

/* ─── Paginação ───────────────────────────────────── */
.paginacao{display:flex;justify-content:space-between;gap:14px;max-width:800px;
  margin:52px 0 0;padding-top:24px;border-top:1px solid var(--line)}
.paginacao a{flex:1;max-width:47%;padding:13px 16px;background:var(--card);
  border:1px solid var(--line);border-radius:9px;text-decoration:none;
  color:var(--ink);font-weight:600;font-size:14.5px}
.paginacao a:hover{border-color:var(--accent)}
.paginacao span{display:block;font-size:12px;font-weight:400;color:var(--muted);
  margin-bottom:3px}
.nav-prox{text-align:right}
.rodape{max-width:800px;margin-top:46px;padding-top:20px;border-top:1px solid var(--line);
  color:var(--muted);font-size:13px}

/* Índice de templates */
.cartoes{list-style:none;padding:0;display:grid;
  grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px}
.cartoes a{display:flex;align-items:center;gap:11px;padding:17px;background:var(--card);
  border:1px solid var(--line);border-radius:10px;text-decoration:none;
  color:var(--ink);font-weight:600}
.cartoes a:hover{border-color:var(--accent)}
.cartoes i{font-style:normal;font-size:21px}

/* ─── Mobile ──────────────────────────────────────── */
@media (max-width:900px){
  aside{transform:translateX(-100%);transition:transform .22s ease;
    box-shadow:0 0 40px rgba(0,0,0,.22)}
  #abrir-menu:checked~aside{transform:translateX(0)}
  #abrir-menu:checked~.fundo-menu{display:block;position:fixed;inset:0;
    background:rgba(0,0,0,.45);z-index:15}
  .botao-menu{display:flex;align-items:center;justify-content:center;
    position:fixed;top:12px;left:12px;width:42px;height:42px;z-index:25;
    background:var(--card);border:1px solid var(--line);border-radius:9px;
    font-size:19px;cursor:pointer;color:var(--ink)}
  .botao-tema{left:auto;right:12px;top:12px;width:42px;height:42px;z-index:25}
  main{margin-left:0;padding:66px 17px 56px}
  h1{font-size:25px}
  h2{font-size:19.5px}
  .paginacao{flex-direction:column}
  .paginacao a{max-width:100%}
  .nav-prox{text-align:left}
}
@media print{
  aside,.botao-menu,.botao-tema,.paginacao{display:none}
  main{margin:0;padding:0}
  details{page-break-inside:avoid}
  details[open] summary{display:none}
}
"""

if __name__ == "__main__":
    gerar()
