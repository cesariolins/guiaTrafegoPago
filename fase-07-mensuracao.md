# Fase 07 — Mensuração

> **Pré-requisito:** Fases 03 e 04.
> **Tempo:** 1 semana.
> **Verba:** R$ 0.

---

## Por que esta fase vale mais do que parece

Mensuração serve para **duas coisas**, e as duas pagam seu salário:

**1. Alimentar o algoritmo.**
A plataforma só encontra "pessoas parecidas com quem compra" se ela puder **ver quem comprou**. Sem pixel bem instalado, o algoritmo chuta — e cobra caro pelo chute. Pixel ruim é a causa silenciosa de metade das contas que "não performam".

**2. Provar o seu trabalho.**
Sem número confiável, toda conversa com cliente vira opinião. E na disputa entre a opinião dele e a sua, ele ganha — é o dinheiro dele.

> **A frase que vale a fase inteira:** *quem controla a mensuração controla a narrativa do resultado.* Um gestor que mostra dashboard próprio, com números que batem, renova contrato. Um gestor que só manda print do gerenciador é substituível.

---

## 1. O pixel do Meta

### O que é

Um pedaço de código no site que avisa o Meta o que a pessoa fez ali. Hoje o Meta chama de **conjunto de dados**.

```
Pessoa clica no anúncio → entra no site → pixel dispara
    ↓
"Fulano visualizou produto"
"Fulano adicionou ao carrinho"
"Fulano comprou — R$ 340"
    ↓
Meta aprende quem é comprador → encontra mais gente parecida
```

### Eventos padrão que você precisa conhecer

| Evento | Quando dispara | Quem usa |
|---|---|---|
| `PageView` | Qualquer página | Todos (automático) |
| `ViewContent` | Página de produto/serviço | E-commerce, serviço |
| `Lead` | Formulário enviado | 🎯 Serviço, B2B |
| `Contact` | Clique no WhatsApp/telefone | 🎯 Serviço local |
| `AddToCart` | Adicionou ao carrinho | E-commerce |
| `InitiateCheckout` | Iniciou checkout | E-commerce |
| `Purchase` | Compra concluída | 🎯 E-commerce |
| `CompleteRegistration` | Cadastro finalizado | Infoproduto, SaaS |

**Regra:** o evento que você otimiza na campanha precisa ser o evento que representa **dinheiro**. Otimizar para `PageView` é otimizar para gente que visita e não compra.

### Instalação

**Caminho mais comum (e mais seguro): via Google Tag Manager.** Ver seção 3.

**Caminho direto:** Meta Events Manager → Conjuntos de dados → Adicionar → instalar código no `<head>` de todas as páginas.

**Integração nativa:** Shopify, WooCommerce, Nuvemshop, Wix e VTEX têm integração pronta. Use — é mais confiável que instalação manual.

### Verificação (não pule)

Instale a extensão **Meta Pixel Helper** no Chrome. Entre no site do cliente e confirme:
- [ ] O pixel dispara em todas as páginas
- [ ] Não há pixel **duplicado** (dispara duas vezes → conversões infladas → decisão errada)
- [ ] Os eventos de conversão disparam de verdade (teste você mesmo: preencha o formulário)
- [ ] O ID do pixel é o correto (contas com histórico têm vários pixels antigos)

> 🚨 **Pixel duplicado é o erro mais comum em conta herdada.** O cliente contratou 3 gestores nos últimos 2 anos, cada um instalou um pixel, e agora tudo conta em dobro. Encontrar isso numa auditoria é uma vitória imediata e visível.

---

## 2. CAPI — obrigatório, não opcional

### O problema que ela resolve

O pixel roda no **navegador** da pessoa. E o navegador hoje é um campo minado:

```
❌ Bloqueador de anúncio        → pixel não dispara
❌ iOS / Safari (ITP)           → dados limitados
❌ Modo anônimo                 → sem cookie
❌ Cookies de terceiros mortos  → rastreamento quebrado
```

Resultado: você **perde de 20% a 40% das conversões reais**. O algoritmo aprende com dados incompletos e otimiza pior. E você reporta menos resultado do que realmente entregou.

### A solução

**API de Conversões (CAPI)** envia o evento do **servidor** direto para o Meta, sem passar pelo navegador.

```
        NAVEGADOR                    SERVIDOR
           │                            │
        Pixel ──────┐          ┌──── CAPI
                    ↓          ↓
                ┌───────────────────┐
                │   META recebe os   │
                │  dois, faz dedup   │
                │   e fica com o     │
                │   dado completo    │
                └───────────────────┘
```

Os dois juntos (com `event_id` para deduplicação) dão a cobertura mais completa.

### Como implementar, do mais fácil ao mais difícil

| Método | Dificuldade | Quando usar |
|---|---|---|
| **Integração de parceiro** (Shopify, WooCommerce, Nuvemshop) | 🟢 Fácil | Sempre que existir. É clicar e conectar. |
| **Conversions API Gateway** | 🟡 Médio | Site próprio, sem dev |
| **Google Tag Manager server-side** | 🔴 Avançado | Operação grande |
| **Implementação manual via dev** | 🔴 Avançado | Sistema próprio |

**Para seus primeiros clientes:** use a integração nativa da plataforma deles. Resolve 90% dos casos em 20 minutos.

### Qualidade da correspondência de eventos

No Events Manager, o Meta dá uma nota de **1 a 10** para a qualidade da correspondência. Quanto mais dados de identificação você enviar (com consentimento), melhor a correspondência e melhor a otimização.

Campos que aumentam a nota: e-mail, telefone, nome, cidade, CEP, ID externo.

**Meta prática:** nota 6+. Abaixo disso, revise o que está sendo enviado.

⚠️ **LGPD:** esses dados precisam ser enviados com base legal válida. Ver seção 7.

---

## 3. Google Tag Manager — a ferramenta que te liberta

### Por que você precisa

**Sem GTM:** cada novo código de rastreamento exige mexer no site → depende do desenvolvedor do cliente → espera de semanas.

**Com GTM:** você instala **um** container uma vez, e depois gerencia todos os códigos pelo painel, sozinho, em minutos.

Em agência, isso é a diferença entre entregar hoje e entregar mês que vem.

### Os três conceitos

```
TAG      = o que dispara      (pixel do Meta, conversão do Google, GA4)
ACIONADOR = quando dispara    (visualizou página, clicou no botão)
VARIÁVEL = informação usada   (valor da compra, URL, texto do clique)
```

### Setup básico

1. **tagmanager.google.com** → criar conta e container Web
2. Instalar os dois trechos de código no site (`<head>` e início do `<body>`)
3. Criar as tags:
   - Meta Pixel — Base (dispara em todas as páginas)
   - Meta Pixel — Lead (dispara no acionador de formulário)
   - Google Ads — Conversão
   - GA4 — Configuração
4. **Testar no modo Preview** antes de publicar
5. Publicar

### Os dois acionadores que resolvem quase tudo em serviço local

**Clique no WhatsApp:**
```
Tipo: Clique — Apenas links
Condição: Click URL contém "wa.me" OU "api.whatsapp.com"
```

**Envio de formulário:**
```
Tipo: Envio de formulário (ou Visualização da página de obrigado)
Condição: URL contém "/obrigado"
```

> 💡 **A página de obrigado é o método mais confiável de todos.** Depois que a pessoa envia o formulário, ela é redirecionada para `/obrigado`. Você dispara a conversão nessa visualização de página. É simples, não quebra, e funciona em qualquer site. Quando puder escolher, escolha esse caminho.

---

## 4. GA4 — o quadro completo

O Google Analytics 4 mostra o que acontece **depois** do clique, unindo todas as fontes.

### O que configurar

1. Criar propriedade em **analytics.google.com**
2. Instalar via GTM (tag "GA4 — Configuração")
3. **Marcar os eventos-chave** (antigas "conversões"): Admin → Eventos → marcar `gerar_lead`, `purchase`, etc.
4. **Vincular ao Google Ads:** Admin → Vinculação de produtos → Google Ads

### Os relatórios que você realmente usa

| Relatório | Para quê |
|---|---|
| **Aquisição → Aquisição de tráfego** | De onde vem o tráfego (aqui suas UTMs aparecem) |
| **Engajamento → Páginas** | Quais páginas retêm, quais expulsam |
| **Monetização** | Receita por canal (e-commerce) |
| **Explorar → Funil** | Onde exatamente as pessoas abandonam |
| **Retenção** | Se os clientes voltam (alimenta o LTV da Fase 01) |

---

## 5. UTM — o padrão que evita caos

UTMs são parâmetros no link que identificam a origem do clique.

```
https://site.com.br/implante
  ?utm_source=facebook
  &utm_medium=cpc
  &utm_campaign=implante-set26
  &utm_content=video-dor-v1
  &utm_term=amplo-25-55
```

### O padrão que você vai adotar (e nunca mudar)

| Parâmetro | Regra | Exemplos |
|---|---|---|
| `utm_source` | Plataforma | `facebook`, `instagram`, `google`, `tiktok` |
| `utm_medium` | Tipo de mídia | `cpc`, `paid-social`, `display` |
| `utm_campaign` | Nome da campanha | `implante-set26` |
| `utm_content` | Qual criativo | `video-dor-v1` |
| `utm_term` | Público ou palavra | `amplo-25-55` |

**Regras inegociáveis:**
- ✅ Sempre **minúsculas** (UTM diferencia maiúscula — `Facebook` e `facebook` viram duas linhas no relatório)
- ✅ **Hífen**, nunca espaço nem underline
- ✅ **Sem acento e sem caractere especial**
- ✅ **Consistência absoluta** entre clientes e campanhas

> Uma planilha com seu padrão de UTM, preenchida para cada campanha, vale ouro em 6 meses. Sem isso, seu GA4 vira uma lista de 200 origens diferentes que dizem a mesma coisa e não servem para nada.

**Dica Meta:** use parâmetros dinâmicos no campo de URL do anúncio para preencher automático:
```
utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}
```

---

## 6. Atribuição: por que os números nunca batem

**Este é o assunto que mais gera conflito com cliente. Domine-o antes de precisar dele.**

### A cena clássica

```
Meta diz:      47 conversões
Google diz:    23 conversões
GA4 diz:       58 sessões com conversão
Cliente diz:   "fechei 12 vendas"
```

Quatro números diferentes. O cliente conclui que você está inflando resultado. **Você precisa saber explicar isso.**

### Por que acontece

**1. Janela de atribuição.** O Meta conta, por padrão, conversões em até 7 dias após o clique e 1 dia após a visualização. Se a pessoa clicou segunda e comprou sábado, o Meta credita a si mesmo. O cliente vê a venda de sábado e não conecta.

**2. Modelo de atribuição.** Cada plataforma se dá crédito pelo que participou. Se a pessoa viu o anúncio do Meta, depois pesquisou no Google e clicou lá, **as duas** contam a venda. Somar as duas é contar duas vezes.

**3. Conversão fora do rastreamento.** A pessoa vê o anúncio e liga direto para a clínica. O Meta não sabe. Você entregou o resultado e não recebe o crédito.

**4. Problema técnico.** Pixel duplicado infla; bloqueador esconde; CAPI ausente perde.

### Como explicar ao cliente (roteiro pronto)

> *"Vou explicar por que os números não batem, e por que isso é normal em toda operação de tráfego.*
>
> *Cada plataforma mede o que ela influenciou, dentro da janela dela. Se uma pessoa vê seu anúncio no Instagram na segunda, pesquisa seu nome no Google na quinta e compra no sábado, o Meta e o Google contam essa mesma venda — os dois participaram de verdade. Somar os dois é contar duas vezes.*
>
> *Por isso a gente não usa o número da plataforma como verdade final. A gente usa **o seu faturamento**. As plataformas servem para eu decidir onde investir mais; o seu caixa serve para nós dois sabermos se está valendo a pena.*
>
> *Por isso eu vou te pedir uma coisa todo mês: quantas vendas entraram e quanto elas somaram. Com isso a gente fecha a conta de verdade."*

**O que esse roteiro faz:**
1. Elimina a suspeita de que você está inflando número
2. Ancora a métrica no **negócio**, não na plataforma
3. Cria a rotina de o cliente te passar o faturamento — o que te dá o dado para **defender aumento de fee** depois

### A pergunta que resolve na prática

Para serviço local, o método mais confiável de atribuição é o mais simples:

> **"Como você nos conheceu?"** — perguntado pelo atendente, registrado numa planilha.

Combine com o WhatsApp pré-preenchido (`?text=Vi o anúncio sobre implante`) e você tem rastreamento melhor que qualquer dashboard.

---

## 7. LGPD — o mínimo que te protege

Você está tratando dados pessoais de terceiros. Não é opcional.

### O básico obrigatório no site do cliente

- [ ] **Política de Privacidade** publicada e acessível
- [ ] **Banner de consentimento de cookies** com opção real de recusar
- [ ] Tags de marketing **só disparam após consentimento** (o GTM tem modo de consentimento para isso)
- [ ] Formulário com **finalidade declarada** ("usaremos seu contato para retornar sobre o serviço")
- [ ] Canal para o titular solicitar exclusão dos dados

### Sua posição jurídica

Você é, em regra, **operador** de dados — trata os dados em nome do cliente, que é o **controlador**. Isso precisa estar escrito no contrato, junto com:
- Finalidade e limites do tratamento
- Obrigação de sigilo
- O que acontece com os dados ao fim do contrato
- Responsabilidade de cada parte em caso de incidente

⚠️ **Em caso de incidente de segurança, as duas partes podem ser responsabilizadas.** Por isso a cláusula de LGPD não é burocracia — é o que define quem responde pelo quê. Detalhamento na [Fase 10](fase-10-contrato-legal.md).

> **Mais um motivo prático para a regra da Fase 02:** ativos no nome do cliente. Se o pixel e as listas de público estão no **seu** Business Manager, você está armazenando dados pessoais de clientes de terceiros sob sua titularidade. É exposição desnecessária.

---

## 8. Dashboard: como entregar o resultado

Print do Gerenciador não é relatório. Monte um dashboard no **Looker Studio** (gratuito):

1. Conecte as fontes: Meta Ads, Google Ads, GA4
2. Monte **uma página só**, com o essencial:

```
┌────────────────────────────────────────────────┐
│  [Cliente] — Setembro 2026                     │
├────────────┬────────────┬──────────┬───────────┤
│ Investido  │   Leads    │   CPL    │  Vendas   │
│  R$ 3.200  │     78     │  R$ 41   │    14     │
├────────────┴────────────┴──────────┴───────────┤
│  Evolução do CPL (gráfico de linha)             │
│  Leads por plataforma (pizza)                   │
│  Top 5 criativos (tabela)                       │
└────────────────────────────────────────────────┘
```

3. Compartilhe o link com o cliente — **acesso permanente, atualização automática**

> **Por que isso retém cliente:** transparência total remove a ansiedade. Cliente que pode olhar quando quiser para de mandar "e aí, como estão as campanhas?" no sábado à noite. E percebe valor continuamente, não só no dia do relatório.

---

## ✅ Tarefas da Fase 07

1. Instale o **GTM** no site do seu negócio de teste
2. Configure via GTM: pixel do Meta (base + Lead), conversão do Google Ads, GA4
3. Instale o **Meta Pixel Helper** e valide tudo — inclusive checando pixel duplicado
4. Configure a **CAPI** pela integração nativa disponível
5. Crie o **acionador de clique no WhatsApp** no GTM
6. Monte sua **planilha-padrão de UTM** e comece a usar em todos os links
7. Crie um **dashboard no Looker Studio** com Meta + Google + GA4
8. **Escreva o roteiro de explicação de discrepância** (seção 6) com suas palavras e decore. Você vai usar.

---

## Checagem de entendimento

1. Meta reporta 40 vendas, GA4 reporta 25, cliente contou 18. Quem está mentindo?
2. Por que a CAPI deixou de ser opcional?
3. O cliente pede para otimizar a campanha para `PageView` porque "gera mais volume e fica mais barato". O que você responde?

<details>
<summary>Respostas</summary>

**1.** Ninguém. Meta usa janela de 7 dias pós-clique e 1 dia pós-visualização, creditando a si mesmo conversões que aconteceram depois; GA4 usa outro modelo e perde sessões por bloqueador e cookie; o cliente conta só o que fechou e reconheceu como vindo do anúncio. **A verdade operacional é o faturamento do cliente.** As plataformas servem para decidir onde investir, não para prestar contas de caixa.

**2.** Porque o rastreamento pelo navegador perde de 20% a 40% dos eventos (bloqueadores, ITP do Safari/iOS, fim dos cookies de terceiros). Sem CAPI, o algoritmo aprende com dado incompleto — otimiza pior e encarece o resultado — e você reporta menos do que realmente entregou.

**3.** Que ele está confundindo preço com custo. Otimizar para `PageView` faz o Meta buscar quem visita páginas, não quem compra — você terá mais volume, mais barato, e menos vendas. O número que importa é o custo por **venda**, não por visita. Mostre a conta da Fase 01: com CPA de R$ 80 e 10 vendas, R$ 800 gastos valem mais que R$ 400 gastos com 2 vendas.

</details>

---

**Próxima:** [Fase 08 — Otimização e escala](fase-08-otimizacao-escala.md)
