# Fase 02 — Infraestrutura

> **Pré-requisito:** Fases 00 e 01.
> **Tempo:** 3 a 5 dias.
> **Verba:** R$ 0 (mas cadastre o cartão).

---

## Por que esta fase existe

Duas histórias reais que se repetem todo mês em grupos de gestores:

> *"Perdi a conta de anúncios. O Meta bloqueou e não consigo recurso. Três clientes parados há 11 dias."*

> *"O cliente me demitiu e levou tudo. O pixel estava no meu Business Manager, a fanpage era minha, e agora ele quer que eu transfira. Ou eu transfiro de graça ou ele vai me processar."*

As duas são **100% evitáveis** — com 40 minutos de setup correto.

Esta é a fase mais chata do curso e a que mais te protege. Faça direito.

---

## 1. A regra de ouro da propriedade dos ativos

Escreva isso e cole no monitor:

> ## 🔒 O CLIENTE É DONO DOS ATIVOS. VOCÊ TEM ACESSO.

**Ativos que são do cliente, sempre, sem exceção:**
- Business Manager (BM) / Conta de Gerenciador
- Conta de anúncios
- Página do Facebook e Instagram
- Pixel / conjunto de dados
- Domínio e site
- Conta do Google Ads e GA4
- Catálogo de produtos
- Listas de público e clientes

**O que é seu:**
- Seu próprio Business Manager (que recebe acesso aos dele)
- Seu conhecimento, seus processos, seus templates
- Sua verba de testes

### Por que isso, se parece pior para você?

Parece que segurar os ativos te dá poder sobre o cliente. Na prática:

| Você segura os ativos | Cliente é dono, você acessa |
|---|---|
| Cliente sente que está refém → desconfia | Cliente se sente seguro → confia |
| Você carrega risco jurídico (LGPD, dados de terceiros na sua conta) | Risco fica com o titular |
| Se **sua** BM é bloqueada, **todos** os clientes param juntos | Bloqueio isolado, um cliente afetado |
| Cliente grande recusa contratar você | Cliente grande te contrata |
| Saída vira briga | Saída vira uma remoção de acesso |

**Retenção não vem de sequestrar ativo. Vem de resultado.** E quem depende de sequestro para reter cliente já perdeu o cliente.

> ⚠️ **A exceção que confirma a regra:** o cliente que *não tem* nada e não quer criar. Nesse caso, você cria tudo **no nome dele, com o e-mail dele, na frente dele**, com você adicionado como parceiro. Leva 20 minutos a mais e evita 100% dos problemas futuros. Coloque isso no contrato (Fase 10).

---

## 2. Meta: montando sua estrutura

### 2.1 Anatomia do ecossistema Meta

Isso confunde todo iniciante. O mapa:

```
CONTA PESSOAL DO FACEBOOK  (você, pessoa física — não pode ser perfil falso)
   │
   └── BUSINESS MANAGER  (a "empresa" dentro do Meta — o cofre)
         ├── Contas de anúncios     ← onde a verba roda
         ├── Páginas (FB/Instagram) ← a identidade que publica
         ├── Conjuntos de dados (pixel)
         ├── Pessoas (sua equipe)
         ├── Parceiros (outras BMs — é assim que você acessa a do cliente)
         └── Domínios verificados
```

**Ponto que quase todo mundo erra:** o Business Manager **não é** sua conta pessoal. Sua conta pessoal é só a chave que abre o cofre. Se sua conta pessoal cair, você perde acesso a tudo — por isso a seção 5 (segurança) não é opcional.

### 2.2 Criando seu Business Manager — passo a passo

1. Acesse **business.facebook.com** com seu Facebook pessoal real
2. **Criar conta** → nome da sua empresa (pode ser seu nome se ainda não tem CNPJ), seu nome, e-mail **profissional**
3. Confirme o e-mail
4. **Configurações do negócio → Informações do negócio** → preencha tudo: endereço, CNPJ (quando tiver), site. Perfil completo = menos chance de bloqueio.
5. **Segurança:** ative autenticação de dois fatores **obrigatória para todos**

> 💡 **Use um e-mail de domínio próprio** (`voce@suaagencia.com.br`) em vez de Gmail. Custa ~R$ 40/ano com o domínio e aumenta perceptivelmente a confiança do Meta e do cliente. Essa é a primeira coisa que separa profissional de amador aos olhos de ambos.

### 2.3 Como pegar acesso à conta do cliente — o jeito certo

🚨 **NUNCA peça a senha do Facebook do cliente.** Isso é:
- Violação dos termos do Meta (pode derrubar as duas contas)
- Risco jurídico seu (você opera como se fosse ele)
- Sinal de amadorismo (cliente que entende do assunto some na hora)

**O jeito certo — Acesso de Parceiro (Partner Access):**

Peça ao cliente que faça isto (mande como passo a passo, não peça "me dá acesso"):

```
1. Entre em business.facebook.com
2. Configurações do Negócio → Usuários → Parceiros
3. Clique em "Adicionar" → "Conceder acesso a um parceiro"
4. Cole o ID do parceiro:  [SEU ID DE BM AQUI]
5. Selecione os ativos:
     ✓ Conta de anúncios        → Gerenciar campanhas (acesso total)
     ✓ Página                   → Criar conteúdo + Anúncios
     ✓ Conjunto de dados/Pixel  → Ver e gerenciar
     ✓ Catálogo (se houver)
6. Confirmar
```

Seu ID de BM está em **Configurações do Negócio → Informações do Negócio**. É um número longo. Deixe ele salvo numa nota — você vai colar toda semana.

> 📋 **Isso já está pronto em [`templates/briefing-onboarding.md`](templates/briefing-onboarding.md)** — copiar, colar, enviar. Cliente adora receber instrução mastigada; é o primeiro sinal de que você é organizado.

### 2.4 Se o cliente não tem Business Manager

Guie-o pela criação (mesmos passos de 2.2) usando **o e-mail dele**. Faça por chamada de vídeo com ele compartilhando a tela — 15 minutos, e você:
- Garante que o titular é ele (proteção jurídica sua)
- Já ensina algo (percepção de valor antes mesmo de começar)
- Evita o pesadelo de transferência futura

### 2.5 Método de pagamento — decisão comercial importante

Quem coloca o cartão?

| Modelo | Como funciona | Prós | Contras | Recomendo? |
|---|---|---|---|---|
| **Cartão do cliente** | Cliente cadastra o próprio cartão na conta dele | Zero risco financeiro seu, zero antecipação de caixa, transparência total | Cartão recusado = campanha parada e você depende dele resolver | ✅ **Sim, sempre no início** |
| Seu cartão, repassa | Você paga a mídia e cobra depois | Controle total, cliente acha prático | Você vira banco. Inadimplência = seu prejuízo. Risco fiscal (dinheiro que não é seu passando por você) | ❌ Não no início |
| Agência com crédito | Linha de crédito do Meta em nome da agência | Escala grande | Só para operação madura com CNPJ e volume | Depois |

**Regra para você agora:** verba **sempre** no cartão do cliente. Seu fee é cobrado separado, por boleto ou Pix, com nota fiscal. Nunca misture verba de mídia com honorário — nem na conta, nem na conversa, nem no contrato.

---

## 3. Google: Google Ads, Tag e GA4

### 3.1 Conta de gerenciador (MCC)

O equivalente do Business Manager no Google chama-se **Conta de Administrador** (MCC — My Client Center).

1. Acesse **ads.google.com/home/tools/manager-accounts**
2. Crie sua conta de administrador
3. Anote seu **ID de 10 dígitos** (formato `123-456-7890`)

**Para acessar a conta do cliente:** você envia uma solicitação de vínculo pelo ID da conta dele, e ele aprova dentro da conta dele. Mesma filosofia do Meta: ele é dono, você acessa.

> Google Ads → Administrador → Contas → **+** → "Vincular conta existente" → insira o ID do cliente.

### 3.2 O trio de mensuração do Google

| Ferramenta | Para que serve | Obrigatório? |
|---|---|---|
| **Google Ads** | Rodar as campanhas | Sim |
| **Google Analytics 4 (GA4)** | Entender o comportamento no site | Sim, sempre |
| **Google Tag Manager (GTM)** | Instalar e gerenciar todos os códigos de rastreamento sem mexer no site | Muito recomendado |

**Por que GTM muda sua vida:** sem ele, toda vez que você precisar adicionar um pixel novo, você depende do desenvolvedor do cliente. Com ele, você instala **uma vez** e depois gerencia tudo sozinho pelo painel. Em agência, isso é a diferença entre entregar em 10 minutos e esperar 3 semanas por um dev que não responde.

Detalhamento de instalação e configuração de conversões está na **Fase 07 — Mensuração**. Aqui você só cria as contas.

### 3.3 Atenção especial — setembro de 2026

Se você assumir uma conta Google existente **agora**, verifique imediatamente:

- 🔍 A campanha foi **migrada automaticamente para AI Max**? O Google está fazendo upgrade automático entre 1 e 30 de setembro de 2026 em campanhas de Pesquisa que usam correspondência ampla no nível da campanha ou recursos criados automaticamente.
- 🔍 Existe alguma **Dynamic Search Ads (DSA)** rodando? Ela será aposentada e absorvida pelo AI Max, com desligamento a partir de fevereiro de 2027. Planeje a migração com antecedência.

**Como isso vira dinheiro para você:** uma auditoria que identifica "sua campanha mudou de comportamento em setembro porque o Google migrou ela sem avisar" é exatamente o tipo de diagnóstico que faz um dono de negócio te contratar na hora. Ninguém mais falou isso para ele.

---

## 4. Domínio, site e verificação

### 4.1 Verificação de domínio (Meta) — não pule

Sem domínio verificado você perde:
- Controle sobre quais eventos de conversão priorizar
- Boa parte da capacidade de mensuração pós-iOS 14
- Credibilidade aos olhos da plataforma

**Como fazer:** Business Manager → Configurações do Negócio → Segurança da Marca → Domínios → Adicionar. Três métodos disponíveis: meta-tag no HTML, registro DNS TXT, ou upload de arquivo. O método DNS é o mais estável.

Se o cliente usa um construtor de sites (Wix, Shopify, WordPress), há integração nativa — procure "verificação de domínio Facebook" na ajuda da plataforma dele.

### 4.2 O site do cliente precisa de mínimos

Antes de rodar qualquer campanha, cheque:

- [ ] **Carrega em menos de 3 segundos no celular** (teste em PageSpeed Insights). Página lenta queima verba em cliques que nunca chegam.
- [ ] **Responsivo** — mais de 85% do tráfego de Meta Ads é mobile
- [ ] **HTTPS ativo** (cadeado). Sem isso, algumas plataformas nem aprovam o anúncio.
- [ ] **Política de Privacidade publicada** — exigência de plataforma **e** da LGPD
- [ ] **Contato visível** — telefone, WhatsApp, endereço se for local
- [ ] **Uma única ação principal por página** — se tem 6 botões diferentes, converte menos

> Se o cliente não tem site, **não é impeditivo**. Campanhas de mensagem para WhatsApp e formulário instantâneo (Lead Ads) funcionam bem para serviço local — às vezes melhor. Cobre um extra para montar uma landing page simples e você adiciona R$ 500–1.500 ao contrato inicial.

---

## 5. Segurança e prevenção de bloqueio

A dor #1 do gestor de tráfego. Vamos prevenir.

### 5.1 Por que contas são bloqueadas

| Causa | Frequência | Evitável? |
|---|---|---|
| Conta nova gastando muito rápido | Alta | ✅ Sim |
| Perfil pessoal sem histórico/atividade | Alta | ✅ Sim |
| Política violada no anúncio (saúde, dinheiro, promessa) | Alta | ✅ Sim |
| Mudança brusca de IP / país | Média | ✅ Sim |
| Página com muitos comentários negativos | Média | ✅ Sim |
| Cartão recusado repetidamente | Média | ✅ Sim |
| Falso positivo do sistema automático | Média | ⚠️ Parcial |

### 5.2 Regras de higiene — siga todas

**Da sua conta pessoal:**
- ✅ Perfil real, com foto, amigos e alguma atividade. Perfil criado ontem e usado só para anúncio é sinal vermelho.
- ✅ **2FA ativado** (obrigatório)
- ✅ Sempre do mesmo dispositivo e mesma rede. Nada de VPN trocando de país.
- ✅ Nunca compre ou alugue conta "aquecida". É a forma mais rápida de perder tudo, e é fraude.

**Do aquecimento de conta nova:**

Conta nova que tenta gastar R$ 500/dia na primeira semana é derrubada. Rampa segura:

```
Dias 1–3    R$ 10–20/dia    objetivo simples (tráfego/alcance)
Dias 4–7    R$ 30–50/dia
Semana 2    R$ 70–100/dia
Semana 3+   aumentos de até 20–30% a cada 2–3 dias
```

**Do pagamento:**
- ✅ Cartão de crédito com limite folgado, **titular = titular da conta**
- ✅ Pague faturas em dia. Histórico de pagamento limpo aumenta o limite de gasto da conta.
- ❌ Evite cartão pré-pago ou virtual descartável — gera recusa e recusa gera bloqueio

**Das políticas de anúncio:**

Categorias com regras rígidas (leia a política antes de anunciar):
- 🏥 Saúde, estética, emagrecimento → proibido "antes e depois", proibido apontar defeito no corpo
- 💰 Finanças, crédito, investimento → promessa de retorno é proibida
- 🎓 Emprego, habitação, crédito → **Categoria Especial de Anúncio**, com segmentação restrita por lei
- 🔞 Conteúdo adulto, apostas, armas → restrito ou proibido

**O teste de 3 segundos:** leia seu anúncio e pergunte *"isso promete resultado, aponta insegurança pessoal, ou faz afirmação sobre a condição da pessoa?"*. Se sim, reescreva.

Exemplos:
- ❌ "Você está acima do peso? Emagreça 10kg em 30 dias!" → afirma condição + promete resultado
- ✅ "Conheça o método que já ajudou 2.000 pessoas a mudarem sua relação com a alimentação"

### 5.3 O plano de contingência (monte hoje, use um dia)

Bloqueio vai acontecer com você em algum momento. Tenha isto pronto **antes**:

- [ ] **Duas contas de anúncio** dentro do BM do cliente (uma reserva, sem uso)
- [ ] Um **segundo administrador** em cada BM (o próprio cliente)
- [ ] **Backup semanal** dos criativos e das configurações (pasta no Drive, por cliente)
- [ ] Documento com todos os IDs (BM, conta, pixel) de cada cliente
- [ ] **Cláusula no contrato** dizendo que bloqueio de plataforma é risco externo e o prazo de resolução não depende de você (Fase 10) ← isso te salva de uma briga

Procedimento de recurso quando acontecer: Fase 12.

---

## 6. Suas ferramentas

Mínimo viável para começar. Não compre nada além disso agora.

| Função | Ferramenta | Custo |
|---|---|---|
| Design de criativo | **Canva** (grátis serve) | R$ 0–35/mês |
| Edição de vídeo | **CapCut** | R$ 0 |
| Planilhas e relatórios | **Google Sheets / Looker Studio** | R$ 0 |
| Organização de clientes | **Notion** ou **Trello** | R$ 0 |
| Espionagem de concorrente | **Biblioteca de Anúncios do Meta** | R$ 0 |
| Encurtador com UTM | **Bitly** ou planilha própria | R$ 0 |
| Velocidade de site | **PageSpeed Insights** | R$ 0 |
| Armazenamento | **Google Drive** | R$ 0–10/mês |

**Custo total para começar: praticamente zero.** Ferramenta paga (relatório automatizado, espionagem avançada, automação) só faz sentido a partir de 4–5 clientes. Comprar ferramenta antes de ter cliente é procrastinação disfarçada de preparação.

### Organização de pastas (faça agora)

```
Meu Drive/
├── _AGENCIA/
│   ├── Templates/         (proposta, contrato, relatório)
│   ├── Meus criativos/    (banco de peças reutilizáveis)
│   └── Financeiro/
└── CLIENTES/
    └── [Nome do Cliente]/
        ├── 00-acessos-e-ids.md      (IDs de BM, conta, pixel)
        ├── 01-briefing.md
        ├── 02-criativos/
        ├── 03-relatorios/
        └── 04-contrato-e-nf/
```

Parece exagero com zero clientes. Com cinco, é o que impede você de perder uma tarde procurando um arquivo.

---

## ✅ Tarefas da Fase 02

1. **Crie seu Business Manager** e ative 2FA. Anote seu ID de BM em local fácil.
2. **Crie sua conta de administrador do Google Ads (MCC).** Anote o ID de 10 dígitos.
3. **Registre um domínio** (`.com.br` sai por ~R$ 40/ano no Registro.br) e configure um e-mail profissional. Faça isso mesmo sem site — o e-mail sozinho já vale.
4. **Monte a estrutura de pastas** no Drive.
5. **Crie seu documento de contingência** com a lista da seção 5.3.
6. **Leia as políticas de anúncio do Meta**, focando na categoria do nicho que você quer atacar. Uma hora de leitura hoje evita uma semana de conta bloqueada depois.
7. **Escolha o negócio do seu primeiro teste** (seu, de parente, de amigo) e monte a estrutura completa nele: BM no nome do dono, conta de anúncios, página, pixel instalado. **Não ligue campanha ainda.**

---

## Checagem de entendimento

1. O cliente te manda a senha do Facebook dele por WhatsApp. O que você responde?
2. Por que ter o pixel do cliente dentro do SEU Business Manager é um risco para você, e não uma vantagem?
3. Conta de anúncios criada hoje. O cliente quer começar com R$ 300/dia amanhã. O que você faz?

<details>
<summary>Respostas</summary>

**1.** Você não usa. Responde agradecendo, pede que ele **troque a senha imediatamente por segurança**, e envia o passo a passo de acesso de parceiro. Isso te protege juridicamente, protege ele, e é a primeira demonstração concreta de que você é profissional. Cliente lembra desse momento.

**2.** Três motivos: (a) risco jurídico — você vira controlador de dados pessoais de terceiros sob a LGPD; (b) risco operacional — se sua BM cair, todos os clientes param juntos; (c) risco comercial — vira ponto de conflito na saída e afasta clientes maiores, que exigem propriedade dos próprios ativos.

**3.** Você explica a rampa de aquecimento e propõe: começar em R$ 20–30/dia por 3 dias, subir gradualmente, chegando em R$ 300/dia em ~3 semanas. Se ele insistir, registre por escrito que o risco de bloqueio foi comunicado. Ceder sem registrar é assumir a culpa por um problema que você previu.

</details>

---

**Próxima:** [Fase 03 — Meta Ads](fase-03-meta-ads.md) — sua primeira campanha de verdade.
