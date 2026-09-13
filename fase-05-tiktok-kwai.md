# Fase 05 — TikTok Ads e Kwai

> **Pré-requisito:** Fases 03 e 04.
> **Tempo:** 1 semana.
> **Verba:** opcional. Só rode se sobrar do orçamento.

---

## Leitura honesta antes de começar

Esta fase é curta de propósito. TikTok é a **terceira prioridade**, não a primeira.

**Por que não priorizar agora:**
- Pouquíssimo cliente de serviço local pede TikTok
- O criativo exige produção de vídeo nativo — mais trabalho por real investido
- Menos maduro em mensuração e atribuição que Meta e Google
- Público comprador de alto ticket ainda está mais no Meta

**Por que você precisa saber mesmo assim:**
- **CPM significativamente mais barato** que Meta — em alguns nichos, metade do preço
- Cliente vai perguntar. Saber responder com propriedade é autoridade.
- Para certos nichos (moda, beleza, food, produto visual, público 18–30) **funciona muito bem**
- É um diferencial de proposta: "eu também rodo TikTok" te separa do gestor genérico
- Quando o CPM do Meta sobe (Black Friday, eleição), o TikTok vira válvula de escape

**A regra:** domine Meta, aprenda Google, **conheça** TikTok. Nesta ordem.

---

## 1. Quando TikTok vale a pena

| ✅ Vale | ❌ Não vale |
|---|---|
| Público 18–35 | Público 45+ |
| Produto visual (moda, beleza, food, decoração) | B2B, industrial, serviço técnico |
| Ticket baixo/médio, decisão rápida | Alto ticket com ciclo longo |
| Cliente consegue produzir vídeo com frequência | Cliente só tem foto de banco de imagem |
| Verba a partir de R$ 1.500/mês | Verba < R$ 1.000 (concentre no Meta) |
| Objetivo: volume e descoberta | Objetivo: colher demanda existente |

**Teste de decisão em 10 segundos:** o cliente consegue gravar 4 vídeos por mês com o celular? Se não, TikTok não é para ele — e insistir só vai gerar frustração dos dois lados.

---

## 2. Diferenças práticas em relação ao Meta

| | Meta | TikTok |
|---|---|---|
| Formato que funciona | Imagem ainda performa | **Só vídeo vertical.** Imagem é ignorada. |
| Estética | Produção polida aceita | **Anúncio que parece anúncio morre.** Precisa parecer conteúdo. |
| Primeiro segundo | Importa | **Decide tudo.** Você tem ~1,5s |
| Duração ideal | Varia | 9–21 segundos na maioria dos casos |
| Vida útil do criativo | 3–6 semanas | **1–3 semanas.** Fadiga muito mais rápida |
| Áudio | Maioria assiste sem som | **Áudio é parte do criativo.** Som e trend importam |

### A regra que define TikTok

> ## Se parece anúncio, ninguém assiste. Se parece conteúdo, vende.

O criativo vencedor no TikTok geralmente é:
- Gravado no celular, vertical, sem produção
- Alguém falando direto para a câmera
- Legenda queimada no vídeo
- Corte rápido nos primeiros 2 segundos
- Trilha ou áudio em alta na plataforma

Um vídeo institucional caro e bem produzido costuma performar **pior** que um vídeo do dono do negócio falando no estoque da loja. Isso é contraintuitivo para o cliente — prepare-se para essa conversa.

---

## 3. Setup rápido

1. **ads.tiktok.com** → criar conta Business
2. Instale o **TikTok Pixel** (via Google Tag Manager — Fase 07)
3. Configure os eventos: `CompletePayment`, `SubmitForm`, `ViewContent`
4. Ative a **Events API** (equivalente da CAPI do Meta) se o cliente tiver e-commerce

### Estrutura de campanha

Mesma lógica de três níveis:

```
📁 CAMPANHA — objetivo
    └── 📂 GRUPO DE ANÚNCIOS — público, verba, posicionamento
          └── 📄 ANÚNCIO — o vídeo
```

**Objetivos principais:** Tráfego, Geração de leads, Conversões, Vendas no catálogo.

**Segmentação:** mesma filosofia de 2026 — vá amplo. Deixe a IA trabalhar. Use `Smart Performance Campaign` (equivalente ao Advantage+) quando quiser simplificar.

**Verba mínima:** o TikTok costuma exigir mínimos por grupo de anúncios (algo em torno de R$ 100/dia na conversão, variável). Isso por si só já exclui cliente de verba pequena.

---

## 4. Spark Ads: o recurso que mais vale a pena

**Spark Ads** permite impulsionar um post orgânico real — do perfil do cliente ou de um creator (com autorização).

Por que é o melhor formato do TikTok:
- Mantém curtidas, comentários e compartilhamentos reais → prova social embutida
- Parece conteúdo, não anúncio (que é a regra da seção 2)
- Direciona para o perfil, gerando seguidores além da conversão
- Costuma ter custo por resultado melhor que anúncio criado do zero

**Fluxo:** cliente posta orgânico → você identifica o que teve melhor retenção → impulsiona como Spark Ad.

> **Isso vira um serviço vendável:** *"eu monitoro seus posts orgânicos e impulsiono os que já provaram que funcionam"*. É fácil de explicar, barato de executar, e o cliente enxerga o valor.

---

## 5. Kwai Ads — o nicho negligenciado

Kwai tem presença forte no Brasil, especialmente:
- Fora dos grandes centros urbanos
- Classes C e D
- Público 25–45

**Quando considerar:** produto de ticket baixo, apelo popular, alcance nacional, verba que precisa render muito CPM.

**Vantagem:** CPM baixíssimo e concorrência muito menor — quase ninguém anuncia lá.

**Desvantagem:** plataforma menos madura, menos recursos de mensuração, suporte fraco.

**Veredito honesto:** não é prioridade, mas é **uma ótima carta na manga** para cliente com produto popular e verba apertada. Saber que existe já te diferencia.

---

## 6. A decisão de alocação entre plataformas

Quando o cliente pergunta "onde eu invisto?", esta tabela responde:

| Verba mensal | Alocação recomendada |
|---|---|
| Até R$ 1.500 | **100% Meta.** Fragmentar mata o aprendizado em todas. |
| R$ 1.500–3.000 | 70% Meta / 30% Google (marca + principais serviços) |
| R$ 3.000–8.000 | 50% Meta / 40% Google / 10% teste (TikTok) |
| R$ 8.000+ | 40% Meta / 40% Google / 20% TikTok e Demand Gen |

> **O princípio:** cada plataforma precisa de verba suficiente para sair da fase de aprendizado. **Três plataformas com verba insuficiente performam pior que uma plataforma bem alimentada.** Essa frase já ganhou discussão com cliente para mim — use.

---

## ✅ Tarefas da Fase 05

1. Crie a conta no TikTok Ads (mesmo sem rodar) — conhecer a interface é parte do trabalho
2. Passe 20 minutos no **TikTok Creative Center** (gratuito, público) vendo os anúncios de melhor performance do Brasil. Anote o padrão dos 3 primeiros segundos.
3. Escreva no caderno: dos negócios que você conhece, quais se beneficiariam de TikTok e quais não? **Justifique.** Essa justificativa é o que você vai falar na reunião.
4. *(Opcional)* Se sobrar verba: grave 3 vídeos verticais de 15s do seu negócio de teste e rode R$ 100 no TikTok. Compare o CPM com o do Meta.

---

## Checagem de entendimento

1. Cliente com clínica de implante dentário, ticket R$ 4.000, quer anunciar no TikTok porque "está todo mundo lá". O que você responde?
2. Por que o vídeo institucional bem produzido costuma performar pior que o vídeo caseiro no TikTok?

<details>
<summary>Respostas</summary>

**1.** Não é um "não", é um "ainda não". Alto ticket com ciclo de decisão longo converte mal em plataforma de descoberta rápida, e o público de implante tende a ser mais velho que o núcleo do TikTok. Proposta: consolidar Meta e Google primeiro (onde está a intenção), e reservar de 10% a 15% da verba para testar TikTok **depois** que a base estiver estável — com vídeos de autoridade, não de oferta. Você não recusou o cliente, você sequenciou. E ancorou uma verba maior no futuro.

**2.** Porque o usuário do TikTok está em modo de consumo de conteúdo, não de propaganda. Produção polida sinaliza "isto é um anúncio" no primeiro quadro, e o dedo desce antes do segundo 2. O vídeo caseiro passa pelo filtro mental e ganha os 3 segundos necessários para a mensagem entrar.

</details>

---

**Próxima:** [Fase 06 — Criativo, copy e oferta](fase-06-criativo-copy-oferta.md) — o que decide 80% do resultado em 2026.
