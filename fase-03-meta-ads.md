# Fase 03 — Meta Ads

> **Pré-requisito:** Fases 00, 01 e 02 executadas.
> **Tempo:** 3 semanas (com campanha rodando).
> **Verba:** R$ 300.

---

## Por que Meta primeiro

- É onde está a maior parte dos seus clientes potenciais (pequeno e médio negócio brasileiro)
- Entrada barata: R$ 6/dia já roda
- Resultado visível rápido
- O ciclo de aprendizado é curto — você erra e vê o erro em 48 horas
- Vender Meta é mais fácil: o dono do negócio já usa Instagram e entende o que você está falando

Google tem intenção mais quente e ticket maior, mas exige mais base técnica. Ordem certa: Meta → Google → TikTok.

---

## 1. O Gerenciador de Anúncios: tour rápido

Acesse: **adsmanager.facebook.com**

```
┌─────────────────────────────────────────────────┐
│  [Conta selecionada ▾]           [+ Criar]      │
├─────────────────────────────────────────────────┤
│  CAMPANHAS  │  CONJUNTOS  │  ANÚNCIOS           │  ← as 3 abas
├─────────────────────────────────────────────────┤
│  Nome | Veiculação | Orçamento | Gasto | Result │
│  ...                                             │
└─────────────────────────────────────────────────┘
```

Três coisas para configurar antes de qualquer outra:

**1. Período.** Canto superior direito. Padrão vem "Máximo". Troque para **Últimos 7 dias** — é a janela em que você toma decisão.

**2. Colunas.** Botão `Colunas ▾` → `Personalizar colunas`. O padrão do Meta é inútil. Monte a sua e salve como "Minha visão":

```
Nome │ Veiculação │ Valor gasto │ Impressões │ CPM │
Cliques no link │ CPC │ CTR │ Resultados │ Custo por resultado │
Frequência
```

Salve. Você vai usar isso todo dia pelos próximos anos.

**3. Detalhamento (Breakdown).** Botão `Detalhamento ▾`. Permite quebrar por idade, gênero, posicionamento, dispositivo. É a sua lupa de diagnóstico.

---

## 2. Os objetivos de campanha

O Meta trabalha com 6 objetivos. A escolha aqui determina **para quem** o algoritmo procura — e é o erro nº 1 do iniciante.

| Objetivo | O algoritmo procura | Use quando |
|---|---|---|
| **Reconhecimento** | Quem vê e lembra | Marca grande, branding. **Você quase nunca usa.** |
| **Tráfego** | Quem clica em link | Blog, conteúdo. ⚠️ Armadilha — ver abaixo |
| **Engajamento** | Quem curte/comenta/manda mensagem | Campanha de WhatsApp, prova social inicial |
| **Cadastros (Leads)** | Quem preenche formulário | 🎯 **Serviço local, B2B, alto ticket** |
| **Promoção de app** | Quem instala app | Só se o cliente tem app |
| **Vendas** | Quem compra | 🎯 **E-commerce, infoproduto** |

### 🚨 A armadilha do objetivo "Tráfego"

Esta é a lição mais cara para iniciante. Leia duas vezes.

Você escolhe **Tráfego** porque quer gente no site. Faz sentido, né? O Meta então otimiza para **cliques** — e vai atrás das pessoas que mais clicam em anúncios. Adivinha quem clica muito em anúncio e nunca compra? Curioso, criança, pessoa com dedo solto.

Resultado: você recebe 400 cliques a R$ 0,25 (parece ótimo!) e **zero vendas**.

Se você tivesse escolhido **Vendas** ou **Cadastros**, o CPC seria R$ 1,80 — e você teria 12 conversões.

> **A regra que você nunca esquece:**
> ### Sempre otimize para a AÇÃO QUE VOCÊ QUER, nunca para um passo anterior.
>
> Quer venda? Objetivo Vendas. Quer lead? Objetivo Cadastros. O algoritmo entrega literalmente o que você pede — o problema é quando você pede a coisa errada.

**A única exceção legítima:** conta nova, pixel sem nenhum dado, e você precisa de volume inicial para alimentar o algoritmo. Mesmo assim, rode Tráfego por no máximo 5–7 dias e migre.

---

## 3. Escolhendo o modelo de campanha

Combine tipo de negócio + destino:

| Negócio | Objetivo | Destino | Por quê |
|---|---|---|---|
| Clínica, dentista, estética | Cadastros | **Formulário instantâneo** | Não sai do app, converte mais |
| Advogado, contador, consultor | Cadastros | Formulário ou WhatsApp | Precisa qualificar |
| Restaurante, comércio local | Engajamento | **WhatsApp** ou Alcance local | Decisão rápida |
| Academia, curso presencial | Cadastros | Formulário | Precisa agendar visita |
| E-commerce | **Vendas** | Site (com pixel) | Compra direta |
| Infoproduto | **Vendas** | Landing page | Precisa da página de venda |
| Imobiliária, alto ticket | Cadastros | Landing page com formulário | Qualificação pesada |

### Formulário instantâneo vs. Landing page vs. WhatsApp

| | Formulário instantâneo | Landing page | WhatsApp |
|---|---|---|---|
| CPL | 🟢 Mais barato (30–50% menos) | 🔴 Mais caro | 🟡 Médio |
| Qualidade do lead | 🔴 Menor (fácil demais) | 🟢 Maior | 🟢 Alta (já quer falar) |
| Precisa de site | Não | Sim | Não |
| Velocidade de montagem | 🟢 Minutos | 🔴 Horas/dias | 🟢 Minutos |
| Melhor para | Volume, ticket baixo/médio | Alto ticket, qualificação | Serviço local, venda consultiva |

> 💡 **Truque para o formulário instantâneo:** dentro dele, troque a opção **"Mais volume"** por **"Maior intenção"**. Isso adiciona uma tela de revisão antes do envio. O volume cai ~20%, a qualidade sobe muito mais que isso. Adicione também **1 ou 2 perguntas personalizadas** ("Qual tratamento você procura?") — filtra curioso e já entrega informação para o vendedor. É a diferença entre entregar 40 leads ruins e 28 bons.

---

## 4. Sua primeira campanha — passo a passo

Cenário: **clínica de estética, captação de leads via formulário, R$ 20/dia.**

### Passo 1 — Criar

Gerenciador → **+ Criar** → objetivo **Cadastros** → **Continuar**.

Se aparecer a escolha entre "Campanha manual" e "Advantage+", escolha **manual** por enquanto. Você precisa entender as alavancas antes de terceirizá-las para a IA.

### Passo 2 — Nível Campanha

```
Nome da campanha:  [LEAD] Estetica - Botox - Set26
Categoria especial: Nenhuma          ← atenção: emprego, crédito e imóvel
                                        obrigam a marcar aqui, por lei
Orçamento CBO:      Desativado       ← por ora, orçamento no conjunto
Teste A/B:          Desativado
```

**Padrão de nomenclatura.** Parece detalhe; não é. Com 6 clientes e 40 campanhas, nomenclatura ruim custa horas.

```
[OBJETIVO] Nicho - Oferta - MêsAno
Conjunto:  Publico | Idade | Local
Anúncio:   Formato - Ângulo - v1
```

### Passo 3 — Nível Conjunto (aqui mora o trabalho)

```
Nome:        Amplo | 25-55 | Curitiba 10km

Conversão
  Local da conversão:      Formulário instantâneo
  Evento de conversão:     Lead

Orçamento
  Orçamento diário:        R$ 20,00
  Programação:             Contínuo

Público
  Local:      Curitiba + 10km          ← sempre "Pessoas que moram aqui"
  Idade:      25 – 55
  Gênero:     Todos
  Detalhado:  (VAZIO)                  ← sim, vazio. Leia abaixo.
  Advantage+ público:  ATIVADO

Posicionamentos
  Advantage+ (automático)              ← deixe automático
```

### 🔑 Por que o público vai VAZIO — a mudança de 2026

Este é o ponto onde a maioria dos cursos está desatualizada.

Você aprendeu (ou vai ouvir por aí) que precisa escolher interesses: "estética", "beleza", "autocuidado". **Em 2026, isso na maioria dos casos piora o resultado.**

O que aconteceu:
- O Meta **removeu as exclusões de segmentação detalhada** — campanhas antigas que usavam essas opções pararam de veicular em 15 de janeiro de 2026
- O sistema de IA da Meta ficou melhor em encontrar compradores do que você em descrever compradores
- Desde fevereiro de 2026, campanhas de vendas, leads e apps nascem com **Advantage+ Creative totalmente ativado**

**Como pensar agora:**

```
Antes (2020–2023)              Agora (2026)
─────────────────              ────────────
Você diz QUEM procurar    →    Você diz O QUE é sucesso
Interesse + comportamento →    Evento de conversão limpo
Testa 8 públicos          →    Testa 8 criativos
Diferencial = segmentação →    Diferencial = criativo + dado
```

**Quando ainda vale restringir:**
- Público muito pequeno (cidade de 20 mil habitantes) — aí a geografia já é o filtro
- Nicho extremamente específico (equipamento industrial B2B)
- Retargeting (que é público personalizado, não interesse)
- Exigência legal (Categoria Especial)

**Teste, não acredite em mim:** rode um conjunto amplo e um conjunto com interesses, mesmo criativo, mesma verba, 7 dias. Anote o resultado no caderno. Na maioria dos casos em 2026, o amplo ganha. Quando não ganhar, você aprendeu algo específico do seu nicho — e isso vale mais que qualquer regra geral.

### Passo 4 — Nível Anúncio

```
Nome:            IMG - Dor de rotina - v1
Identidade:      [Página do Facebook] + [Instagram]
Formato:         Imagem única
Criativo:        (sua peça)
Texto principal: (copy — Fase 06)
Título:          Até 40 caracteres
Descrição:       Opcional
Chamada:         Saiba mais / Cadastre-se
Formulário:      [criar novo]

Advantage+ Creative:   ⚠️ decisão importante — ver 4.1
```

### 4.1 Advantage+ Creative: o que deixar ligado

Desde fevereiro de 2026, isso vem **ligado por padrão** em campanhas novas de vendas, leads e apps. A IA aplica ajustes visuais, gera variações de texto, muda proporção, corta imagem e até adiciona música — cada pessoa vê uma combinação diferente.

Minha recomendação prática:

| Recurso | Ligar? | Motivo |
|---|---|---|
| Ajustes de brilho/contraste, proporção | ✅ Sim | Adapta para cada posicionamento. Ganho real. |
| Variações de texto geradas por IA | ⚠️ Só depois de validar | A IA pode gerar copy que quebra tom de voz ou faz promessa fora da política |
| Música gerada / adicionada | ❌ Não no início | Costuma destoar da peça |
| Sobreposição de texto / templates | ⚠️ Teste | Às vezes cobre elemento importante da imagem |
| Expansão de imagem por IA | ⚠️ Teste | Ótimo às vezes, grotesco outras. **Sempre confira a prévia.** |

> ⚠️ **Regra de ouro:** antes de publicar, abra a **prévia em todos os posicionamentos**. A IA já produziu peça com o rosto do cliente esticado, texto cortado no meio e logo deformado. Você é responsável pelo que sai no ar — inclusive pelo que a IA gerou.
>
> **Para cliente de setor regulado** (saúde, finanças, jurídico), desligue as variações de texto por IA. Um texto que promete resultado médico gerado automaticamente é problema seu, não do Meta.

### Passo 5 — Publicar

Revise:
- [ ] Objetivo é o da **ação final**, não de um passo anterior
- [ ] Localização é "pessoas que **moram** neste local"
- [ ] Verba diária está correta (não mensal)
- [ ] Prévia checada em todos os posicionamentos
- [ ] Formulário testado por você mesmo
- [ ] Link com **UTM** (Fase 07)

**Publicar.** Aprovação leva de minutos a 24 h.

---

## 5. A fase de aprendizado — e a regra do não-mexer

Depois de publicar, o conjunto entra em **"Em aprendizado"**.

O algoritmo está testando combinações para descobrir quem converte. Durante essa fase os resultados são **instáveis** e **não representativos**.

```
Dia 1-2   ████░░░░░░  Resultado ruim, CPL alto. NORMAL.
Dia 3-5   ███████░░░  Começa a estabilizar
Dia 6-7   █████████░  Número confiável aparece
```

Ele sai do aprendizado com aproximadamente **50 conversões em 7 dias** naquele conjunto.

### 🚫 As regras do não-mexer

**Nos primeiros 3–4 dias, não faça NADA.** Nem olhe muito.

Qualquer edição significativa **reinicia a fase de aprendizado** e queima a verba já gasta em aprendizado perdido. Reiniciam o aprendizado:
- Mudar público
- Mudar o evento de conversão
- Mudar orçamento em mais de ~20%
- Trocar ou pausar o criativo principal
- Editar o anúncio

**Isso é o erro nº 1 do iniciante ansioso.** Ele mexe todo dia, o aprendizado reinicia todo dia, a campanha nunca estabiliza, e ele conclui que "Meta Ads não funciona".

> 💬 **Como explicar isso ao cliente no dia 2** (e você vai precisar, porque ele vai te cobrar):
>
> *"Estamos nos primeiros dias de calibração. Nesse período o sistema testa combinações e os números oscilam muito — é esperado e faz parte do processo. O número confiável aparece a partir do dia 5. Vou te mandar a primeira leitura real na sexta."*
>
> Dizer isso **antes** dele perguntar é o que separa quem parece no controle de quem parece perdido. Coloque no onboarding: avise no dia 1 que os dias 1–4 serão feios.

### Verba mínima para sair do aprendizado

```
Verba diária mínima ≈ CPA alvo × 3
```

CPL alvo de R$ 25? Mínimo ~R$ 75/dia para o conjunto estabilizar direito. Com R$ 20/dia ele vai funcionar, mas oscilando mais — o que é aceitável para negócio local pequeno, desde que **você e o cliente saibam disso**.

---

## 6. Orçamento: CBO ou ABO?

| | **ABO** (orçamento no conjunto) | **CBO / Advantage+** (orçamento na campanha) |
|---|---|---|
| Quem decide a divisão | Você | O algoritmo |
| Controle | 🟢 Total | 🔴 Baixo |
| Para testar | 🟢 Ideal | 🔴 Ruim (mata o perdedor cedo demais) |
| Para escalar | 🟡 Trabalhoso | 🟢 Ideal |
| Verba baixa (< R$ 50/dia) | 🟢 Melhor | 🔴 Concentra tudo em um conjunto |

**Regra prática:**
- **Testando** (descobrindo o que funciona) → **ABO**, verba igual em cada conjunto
- **Escalando** (já sabe o que funciona) → **CBO**, deixa a IA distribuir

Você está começando. Use **ABO**.

---

## 7. Estrutura de conta recomendada para 2026

Esqueça as estruturas complexas de 2021, com 12 conjuntos por campanha. Hoje é assim:

### Para serviço local (verba R$ 600–3.000/mês)

```
📁 [LEAD] Clinica - Captacao - Set26          ABO
    └── 📂 Amplo | 25-55 | Cidade+10km        R$ 20/dia
          ├── 📄 VID - Dor cotidiana - v1
          ├── 📄 VID - Depoimento - v1
          ├── 📄 IMG - Oferta direta - v1
          ├── 📄 IMG - Prova social - v1
          └── 📄 CAR - Antes/Depois* - v1     *cuidado com política de saúde

📁 [LEAD] Clinica - Remarketing - Set26       (só quando houver volume)
    └── 📂 Engajou 30d + Visitou site 30d     R$ 8/dia
          └── 📄 IMG - Oferta com urgência
```

**Um conjunto. Vários criativos.** É isso.

Por quê? Porque em 2026 o teste que importa é de **criativo**, não de público. Cinco criativos no mesmo conjunto competem entre si e o algoritmo concentra verba no vencedor — que é exatamente o que você quer.

### Para e-commerce (verba R$ 3.000+/mês)

```
📁 [VENDAS] Loja - Aquisicao - Set26          CBO R$ 100/dia
    ├── 📂 Amplo | 18-65 | Brasil
    └── 📂 Lookalike 1% compradores

📁 [VENDAS] Loja - Remarketing - Set26        ABO R$ 30/dia
    └── 📂 Visitou 14d + Carrinho 7d (excl. compradores 30d)

📁 [VENDAS] Loja - Catalogo/DPA - Set26       R$ 40/dia
    └── 📂 Remarketing dinâmico de produto
```

### O princípio: consolide

```
❌ ERRADO                          ✅ CERTO
15 campanhas × 1 conjunto          1–3 campanhas
× 1 anúncio cada                   1–2 conjuntos cada
                                   5–8 anúncios cada
Verba fragmentada                  Verba concentrada
Nenhum conjunto aprende            Algoritmo aprende rápido
```

**Verba fragmentada = nenhum conjunto atinge volume de aprendizado = tudo performa mal.** Essa é a causa raiz de metade das contas ruins que você vai auditar.

---

## 8. Lendo os números: o que fazer com cada cenário

Depois de 5–7 dias, o diagnóstico:

| CTR | CPL | Diagnóstico | Ação |
|---|---|---|---|
| 🟢 Alto (>2%) | 🟢 Bom | Funcionando | **Escale** (+20% a cada 2–3 dias) |
| 🟢 Alto | 🔴 Alto | Atrai mas não converte | Problema no **formulário ou na página**, não no anúncio |
| 🔴 Baixo (<1%) | 🔴 Alto | Criativo ou oferta fracos | **Troque o criativo.** Não mexa em público. |
| 🔴 Baixo | 🟢 Bom | Nicho de baixo volume, mas quem clica compra | Mantenha. Teste criativo novo em paralelo. |

### Os três diagnósticos por Detalhamento

Use `Detalhamento ▾` para achar o vazamento:

1. **Por posicionamento** — Reels custando 4x mais que Feed? Considere excluir. Mas cuidado: em 2026 o Advantage+ automático geralmente ganha do manual no total. Só exclua com diferença grande e sustentada.
2. **Por idade e gênero** — 80% dos leads vêm de 35–44? Crie um conjunto focado ali **em paralelo**, sem matar o amplo.
3. **Por dispositivo** — desktop convertendo muito pior? Provavelmente a landing page está quebrada no mobile (ou vice-versa). Isso é problema de site, não de anúncio.

---

## 9. Escalando sem quebrar

Você achou o vencedor. Agora não estrague.

### Escala vertical (aumentar verba)

```
✅ +20% a cada 2–3 dias        → algoritmo se adapta
❌ dobrar de uma vez           → reinicia aprendizado, CPL dispara
```

Paciência aqui é dinheiro. Um conjunto estável em R$ 50/dia que você dobra para R$ 100 costuma voltar a R$ 50 de performance — e você perde 4 dias reconstruindo.

### Escala horizontal (mais frentes)

- Duplicar o conjunto vencedor para **outra região**
- Novos criativos com o **mesmo ângulo** que venceu
- Novo público (lookalike dos convertidos)
- Outra plataforma (é aqui que entra Google — Fase 04)

### Sinais de que você chegou no teto

- 📈 Frequência subindo acima de 3–4 com CPL subindo junto → público saturado
- 📉 Mesma verba, menos resultado, várias semanas → fadiga de criativo
- 💸 CPM subindo constantemente → competição ou qualidade caindo

**Solução quase sempre é criativo novo.** Não é "mexer na campanha".

---

## 10. Os 10 erros que queimam a verba do iniciante

1. **Objetivo Tráfego quando queria venda** → o erro mais caro de todos
2. **Mexer na campanha todo dia** → aprendizado nunca termina
3. **Desligar no dia 2** → você pagou o aprendizado e jogou fora antes de colher
4. **Verba fragmentada** em 12 conjuntos de R$ 5
5. **Um criativo só** → sem material para o algoritmo otimizar
6. **Público restrito demais** em 2026 → estrangula o alcance sem ganho
7. **Não instalar o pixel** → algoritmo cego, e você também
8. **Landing page lenta** → paga o clique, perde a pessoa
9. **Não checar a prévia** do Advantage+ → anúncio deformado no ar
10. **Prometer resultado sem fazer a conta da Fase 01** → o erro que te custa o cliente, não a verba

---

## ✅ Tarefas da Fase 03

**Semana 1 — Preparação (R$ 0)**
1. Configure suas colunas personalizadas e salve
2. Escolha o negócio de teste (o seu, de parente, de amigo)
3. Faça a conta da Fase 01 para ele: CPA máximo, CPL alvo
4. Produza **5 criativos diferentes** (Canva/CapCut). Ângulos diferentes, não cores diferentes.
5. Escreva 3 variações de copy

**Semana 2 — Rodando (R$ 150)**
6. Suba a campanha: 1 campanha, 1 conjunto amplo, 5 anúncios, R$ 20/dia
7. **Não mexa em nada por 4 dias.** Anote no caderno o que você sentiu vontade de mexer.
8. Dia 5: primeira análise. Preencha no caderno: CPM, CPC, CTR, CPL, frequência.

**Semana 3 — Otimizando (R$ 150)**
9. Pause os 2 criativos piores. Suba 2 novos com o ângulo do vencedor.
10. Rode mais 7 dias
11. **Documente tudo como case:** prints do gerenciador, números de antes e depois, o que você aprendeu

O item 11 é o mais importante. **Esse documento é o que você vai mostrar ao seu primeiro cliente.** Sem ele, você é só mais um dizendo que sabe.

---

## Checagem de entendimento

1. Cliente quer vendas no site. Você escolhe Tráfego porque o CPC é mais barato. O que vai acontecer?
2. Dia 3, CPL está R$ 90 e a meta é R$ 40. Qual a decisão correta?
3. CTR 3,2% (ótimo) e CPL R$ 120 (péssimo). Onde está o problema e onde você NÃO deve mexer?

<details>
<summary>Respostas</summary>

**1.** O Meta vai buscar "clicadores" — pessoas com histórico de clicar em anúncio, não de comprar. Você terá CPC baixo, muito tráfego e conversão próxima de zero. O CPC barato é uma ilusão: o que importa é o custo por **venda**.

**2.** Nada. Dia 3 é fase de aprendizado, o número não é confiável. Qualquer edição reinicia o aprendizado e piora a situação. Espere o dia 5–7. (Exceção: erro grave de setup — link quebrado, formulário com erro, criativo errado no ar. Aí corrija imediatamente.)

**3.** O anúncio está fazendo o trabalho dele (CTR alto = criativo e oferta atraem). O vazamento está **depois do clique**: formulário longo, página lenta, oferta na página diferente da prometida no anúncio, ou preço revelado só lá. **Não mexa no criativo nem no público** — você estaria quebrando a única parte que está funcionando.

</details>

---

**Próxima:** [Fase 04 — Google Ads](fase-04-google-ads.md) — onde está a intenção de compra.
