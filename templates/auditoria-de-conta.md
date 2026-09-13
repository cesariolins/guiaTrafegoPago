# Template — Auditoria de conta

> **Dois usos:**
> 1. **Prospecção** — versão curta (1 página), gratuita, usada como isca. É sua melhor ferramenta comercial.
> 2. **Onboarding** — versão completa, feita na primeira semana de um cliente novo que já tem conta rodando.

---

# PARTE A — Auditoria externa (prospecção)

> Feita **sem acesso à conta**, só com o que é público. 30–40 minutos. É o que você manda de graça na abordagem fria (Fase 09).

## Como levantar as informações

```
1. Biblioteca de Anúncios do Meta (facebook.com/ads/library)
   → filtre por Brasil + o nome do negócio
   → quantos anúncios? há quanto tempo no ar? imagem ou vídeo?

2. Google — pesquise o serviço + cidade
   → ele aparece nos anúncios? o concorrente aparece?

3. Site
   → PageSpeed Insights (velocidade mobile)
   → a página do anúncio é específica ou é a home?
   → tem Política de Privacidade e banner de cookies?

4. Instagram
   → o perfil converte? bio clara? link funcional?
```

## O documento que você envia

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ANÁLISE RÁPIDA — [Nome do Negócio]
[Seu nome] · [data]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

O QUE VOCÊS JÁ FAZEM BEM
  • [ponto real 1]
  • [ponto real 2]

  (Sempre comece por aqui. Sempre seja verdadeiro —
   elogio genérico é pior que nenhum.)

3 OPORTUNIDADES QUE EU VI

  1. [PROBLEMA]
     Por que importa: [impacto no negócio, em dinheiro
                       ou em clientes perdidos]
     O que eu faria: [ação concreta]

  2. [PROBLEMA]
     Por que importa:
     O que eu faria:

  3. [PROBLEMA]
     Por que importa:
     O que eu faria:

ESTIMATIVA
  Com verba de aproximadamente R$ [X] e os ajustes acima,
  a faixa esperada seria de [Y] a [Z] contatos por mês,
  a um custo entre R$ [A] e R$ [B] cada.

  (Baseado em referência de mercado para o setor.
   Não é garantia — é um cenário de trabalho.)

Qualquer dúvida, estou à disposição.
[nome] · [WhatsApp]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Problemas visíveis de fora (e como traduzir)

| O que você vê | Como escrever no documento |
|---|---|
| 1 anúncio só, no ar há meses | *"O mesmo criativo está no ar há [N] meses. Isso costuma elevar bastante o custo por contato, porque as mesmas pessoas veem o anúncio repetidamente e param de reagir."* |
| Só imagem, nenhum vídeo | *"Todos os anúncios são estáticos. Vídeo curto normalmente entrega custo por contato menor no seu segmento."* |
| Foto de banco de imagem | *"As imagens parecem de banco de imagens. Fotos reais do espaço e da equipe costumam performar melhor porque geram identificação."* |
| Anúncio manda para a home | *"O anúncio leva para a página inicial em vez de uma página do serviço anunciado. Isso costuma derrubar a conversão pela metade, porque a pessoa precisa procurar o que veio buscar."* |
| Sem oferta clara | *"O anúncio comunica os serviços, mas não apresenta um motivo para agir agora. Uma oferta de entrada clara costuma ser o ajuste de maior impacto."* |
| Não anuncia no Google | *"Vocês não aparecem nos anúncios de busca. Quem pesquisa '[termo]' na sua cidade encontra [concorrente] primeiro."* |
| Site lento | *"O site leva [N] segundos para carregar no celular. Acima de 3 segundos, uma parte relevante das pessoas desiste antes de ver a página — e o clique já foi pago."* |
| Sem Política de Privacidade | *"O site não tem Política de Privacidade nem aviso de cookies, o que é exigência da LGPD e das próprias plataformas de anúncio."* |

---

---

# PARTE B — Auditoria completa (cliente novo)

> Com acesso à conta. Primeira semana do contrato. É aqui que você encontra as vitórias rápidas que justificam sua contratação.

## 1. Estrutura e segurança

```
□ Quem é o titular do Business Manager? (deve ser o cliente)
□ O cliente é administrador da própria conta?
□ 2FA ativado?
□ Quantos usuários e parceiros têm acesso? Algum antigo esquecido?
□ Existe conta de anúncios reserva?
□ Domínio verificado no Meta?
□ Meio de pagamento válido, no nome do titular?
□ Histórico de bloqueios ou restrições?
```

**Achados comuns:** gestor anterior ainda com acesso total (remova); BM no nome do gestor anterior (problema sério — resolva primeiro).

## 2. Mensuração ⭐ *onde estão as maiores vitórias*

```
□ Pixel instalado e disparando? (Meta Pixel Helper)
□ ⭐ EXISTE PIXEL DUPLICADO?
□ Quantos pixels na conta? Qual está realmente em uso?
□ Eventos de conversão configurados corretamente?
□ O evento otimizado representa dinheiro, ou é só PageView?
□ CAPI configurada? Qualidade da correspondência?
□ Google Ads: conversões configuradas?
□ Conversões duplicadas no Google? (mesma ação contada 2x)
□ GA4 instalado e vinculado ao Google Ads?
□ UTMs padronizadas?
□ ⭐ O fluxo funciona? (teste você mesmo: preencha o formulário)
```

> **Pixel duplicado e conversão duplicada são os achados mais frequentes em conta herdada.** Ambos inflam os números e fazem o gestor otimizar com base em mentira. Encontrar isso na primeira semana é uma vitória imediata e fácil de demonstrar.

## 3. Campanhas — Meta

```
□ Objetivo correto? (⭐ há campanha de venda rodando em Tráfego?)
□ Quantas campanhas ativas? Verba fragmentada?
□ Quantos conjuntos por campanha? Quantos anúncios por conjunto?
□ Públicos sobrepostos competindo entre si?
□ Segmentação detalhada restringindo sem necessidade? (2026)
□ Advantage+ Creative: as variações geradas estão adequadas?
□ Prévia dos posicionamentos: alguma peça deformada?
□ Frequência acima de 3–4?
□ Quantos criativos novos nos últimos 30 dias?
□ Remarketing existe? Está excluindo quem já converteu?
```

## 4. Campanhas — Google

```
□ ⭐ Rede de Display marcada em campanha de Pesquisa?
□ ⭐ Localização em "interesse" em vez de presença física?
□ Correspondência das palavras-chave
□ ⭐ Termos de pesquisa: quanto está sendo desperdiçado?
□ Lista de negativas existe e é mantida?
□ Índice de qualidade das principais palavras
□ Recursos/extensões preenchidos?
□ Existe campanha de marca?
□ Estratégia de lance compatível com o volume de dado?
□ ⭐ A conta foi migrada para AI Max em setembro/2026?
□ Alguma DSA rodando? (aposentadoria a partir de fev/2027)
□ PMax rodando sem exclusões de marca e URL?
```

## 5. Destino e conversão

```
□ Velocidade mobile (PageSpeed Insights)
□ Página específica ou home genérica?
□ A promessa do anúncio aparece no título da página?
□ Quantos campos no formulário?
□ Uma única ação principal por página?
□ WhatsApp com mensagem pré-preenchida?
□ Prova social acima da dobra?
□ Política de Privacidade e banner de cookies?
```

## 6. Números históricos

| Métrica | Últimos 30d | 30d anteriores | Tendência |
|---|---|---|---|
| Investimento | | | |
| CPM | | | |
| CTR | | | |
| Custo por resultado | | | |
| Frequência | | | |

## 7. Relatório de achados

Organize por impacto, não por ordem de descoberta:

```
🔴 CRÍTICO — corrigir esta semana
   1. [problema] → [impacto estimado] → [correção]

🟡 IMPORTANTE — corrigir este mês
   1.

🟢 MELHORIA — quando houver espaço
   1.

💰 DESPERDÍCIO IDENTIFICADO
   Aproximadamente R$ [valor]/mês em [origem do desperdício]
```

> **A linha de desperdício é a mais poderosa do documento.** *"Encontrei R$ 640 por mês indo para termos de busca que nunca viram cliente"* é uma frase que justifica seu fee inteiro na primeira semana — e que o cliente repete para outras pessoas.
