# Fase 10 — Contrato, CNPJ e questões legais

> **Pré-requisito:** Fase 09, com uma proposta prestes a virar contrato.

> ⚠️ **Aviso necessário:** este material é orientação prática de mercado, não consultoria jurídica ou contábil. Antes de assinar contrato ou abrir empresa, valide com um **contador** e, idealmente, com um **advogado**. O custo é baixo e evita problema caro. Regras tributárias mudam — confirme o que está vigente na data em que você for agir.

---

## 1. CNPJ: a decisão que você precisa acertar de primeira

### 🚨 O ponto crítico: MEI não serve para gestão de tráfego

Este é o erro mais comum de quem está começando, e é caro de corrigir depois.

**Gestão de tráfego não consta entre as atividades permitidas no MEI.** Quem trabalha com isso precisa constituir outro tipo de empresa — normalmente **ME (Microempresa)**.

Muita gente abre MEI com um CNAE aproximado e emite nota assim mesmo. Os riscos: desenquadramento retroativo, cobrança de diferença de tributos com multa, e nota fiscal contestada pelo cliente na hora de deduzir a despesa.

**Confirme com um contador antes de abrir qualquer coisa.** Esta é literalmente a primeira ligação que você deve fazer.

### O caminho comum

| Etapa | O que é |
|---|---|
| **Sem CNPJ** | Só funciona no começo, com pessoa física, e limita clientes empresariais (que precisam de nota) |
| **ME no Simples Nacional** | O caminho padrão de quem trabalha com tráfego |
| **Contabilidade online** | R$ 100–300/mês, resolve abertura e rotina |

### CNAEs normalmente usados

Seu contador vai definir, mas os que costumam aparecer:

| CNAE | Descrição |
|---|---|
| 7319-0/02 | Promoção de vendas |
| 7311-4/00 | Agências de publicidade |
| 7319-0/03 | Marketing direto |
| 6204-0/00 | Consultoria em tecnologia da informação |
| 7020-4/00 | Consultoria em gestão empresarial |

**A escolha do CNAE afeta sua alíquota.** Um contador que entende de negócios digitais pode fazer uma diferença de vários pontos percentuais no imposto — vale procurar um que já atenda gestores de tráfego.

### Simples Nacional — a lógica

Prestação de serviço cai normalmente no **Anexo III** ou **Anexo V**, dependendo do **Fator R**:

```
Fator R = (folha de pagamento + pró-labore dos últimos 12 meses)
          ÷ receita bruta dos últimos 12 meses

Fator R ≥ 28%  →  Anexo III (alíquota inicial ~6%)
Fator R < 28%  →  Anexo V   (alíquota inicial ~15,5%)
```

**Tradução prática:** pagar pró-labore pode reduzir sua alíquota drasticamente. Isso soa contraintuitivo — pagar a si mesmo para pagar menos imposto — mas é uma das otimizações mais comuns e legítimas do setor.

**Peça ao contador para simular os dois cenários.** A diferença entre 6% e 15,5% sobre R$ 10 mil/mês é quase R$ 1.000 mensais.

### Nota fiscal

- **Cliente pessoa jurídica:** emita sempre. Ele precisa para deduzir a despesa, e não emitir te exclui de clientes maiores.
- **Cliente pessoa física:** MEI é dispensado; ME normalmente emite.
- **Emissão:** pelo portal da prefeitura (NFS-e) ou pelo sistema do seu contador.

> 💰 **Regra de ouro que separa amador de profissional: emita nota APENAS sobre o seu honorário, nunca sobre a verba de mídia.**
>
> A verba não é sua receita — é dinheiro do cliente indo para a plataforma. Se ela passar pela sua conta e entrar na sua nota, você paga imposto sobre dinheiro que não é seu, infla artificialmente seu faturamento (podendo estourar o limite do Simples) e cria confusão contábil.
>
> **Solução:** cartão do cliente na conta de anúncios. Sempre. (Fase 02)

---

## 2. O contrato

### Por que você precisa de um, sempre

Não é desconfiança — é clareza. O contrato responde antecipadamente as perguntas que viram briga depois:

- O que exatamente está incluso?
- O que acontece se o resultado não vier?
- De quem é o pixel, a conta, os criativos?
- Quando e como eu recebo?
- Como termina?

**Cliente sério não se incomoda com contrato. Cliente que se incomoda com contrato é exatamente quem você precisa de contrato para enfrentar.**

### Obrigação de MEIO, não de FIM — a cláusula mais importante

Este é o conceito jurídico central da sua atividade.

| Obrigação de **meio** | Obrigação de **fim** (resultado) |
|---|---|
| Você se compromete com o **processo** | Você se compromete com o **resultado** |
| Empregar técnica, diligência e melhores práticas | Entregar X vendas |
| Médico, advogado, gestor de tráfego | Construtora entregando uma obra |
| 🟢 Protege você | 🔴 Te expõe a ação de indenização |

Na maioria dos casos, contratos de tráfego pago são considerados **obrigação de meio**. Uma cláusula expressa nesse sentido protege o gestor, que não é obrigado a garantir captação de leads nem conversão em vendas.

**Por quê:** você não controla o produto, o preço, o atendimento, a concorrência, o leilão das plataformas nem a economia. Prometer resultado sobre variáveis que você não controla é assumir um risco desproporcional.

⚠️ **Atenção:** se o seu material de venda promete resultado ("garanto 30 leads"), uma cláusula de meio no contrato pode não te proteger — a promessa feita na negociação pode ser considerada parte do acordo. **Seja coerente entre o que você vende e o que você assina.**

### As 12 cláusulas essenciais

Template completo em [`templates/contrato-modelo.md`](templates/contrato-modelo.md). O que não pode faltar:

**1. Objeto e escopo**
Detalhado e específico. Quais plataformas, quantas campanhas, quantos criativos por mês, qual frequência de relatório.

**2. O que NÃO está incluso** ⭐
A cláusula mais subestimada. Evita 80% dos atritos:
> *Não estão inclusos: criação de site ou landing page, produção de fotos e vídeos profissionais, gestão de redes sociais e conteúdo orgânico, atendimento aos leads gerados, design de identidade visual, verba de mídia.*

**3. Obrigação de meio**
> *Os serviços constituem obrigação de meio, não de resultado. A CONTRATADA se compromete a empregar as melhores técnicas e diligência, não sendo responsável por garantir volume de leads, vendas ou faturamento, uma vez que tais resultados dependem de fatores fora de seu controle — incluindo produto, preço, atendimento comercial, concorrência e políticas das plataformas.*

**4. Verba de mídia — separada do honorário**
> *A verba de mídia é de responsabilidade exclusiva do CONTRATANTE, custeada diretamente por ele junto às plataformas, e não integra a remuneração da CONTRATADA. Tributos incidentes sobre a veiculação são debitados da verba.*

Mencione explicitamente os tributos: desde janeiro de 2026, PIS/Cofins e ISS passaram a ser cobrados diretamente do anunciante no Brasil, com impacto de aproximadamente 12% no custo dos anúncios. **O cliente precisa saber que R$ 1.000 de verba não compra R$ 1.000 de mídia.**

**5. Propriedade dos ativos**
> *Todas as contas, páginas, pixels e dados permanecem de titularidade do CONTRATANTE. A CONTRATADA atua mediante acesso concedido, que será revogado ao término do contrato.*

**6. Prazo, renovação e rescisão**
Prazo mínimo (90 dias é o padrão e é defensável tecnicamente), renovação automática, aviso prévio de 30 dias, multa proporcional se houver rescisão antes do prazo mínimo.

**7. Pagamento**
Valor, dia do vencimento, forma, multa e juros por atraso, e — importante — **suspensão dos serviços após X dias de inadimplência**.

**8. Responsabilidades do contratante** ⭐
Também subestimada, e é a que te salva quando o resultado não vem:
> *O CONTRATANTE se compromete a: manter método de pagamento válido nas plataformas; responder os leads gerados em prazo razoável; fornecer as informações e materiais necessários; comunicar alterações relevantes no negócio (preço, capacidade de atendimento, promoções).*

**9. LGPD**
Ver seção 3.

**10. Confidencialidade**
Mútua. Dados, números e estratégias de ambas as partes.

**11. Uso do case** ⭐
> *O CONTRATANTE autoriza a CONTRATADA a mencionar a parceria e utilizar dados de desempenho de forma [identificada / anonimizada] em materiais de divulgação.*

Peça sempre. É como você constrói portfólio. Se o cliente recusar identificação, negocie a versão anonimizada ("clínica odontológica em Curitiba").

**12. Riscos de plataforma** ⭐
> *A CONTRATADA não se responsabiliza por bloqueios, suspensões, reprovações de anúncio ou alterações de política das plataformas, que constituem risco externo ao serviço prestado. Nessas hipóteses, a CONTRATADA empreenderá os esforços cabíveis para restabelecimento, sem prazo garantido.*

**Essa cláusula vai te salvar.** Conta bloqueada acontece com todo mundo, e sem ela você vira o culpado por uma decisão de um algoritmo da Meta.

---

## 3. LGPD na prática

Você trata dados pessoais de terceiros. Não é opcional e não é só burocracia.

### Os papéis

```
CLIENTE      = CONTROLADOR  (decide por que e como os dados são tratados)
VOCÊ         = OPERADOR     (trata os dados em nome dele)
PLATAFORMAS  = terceiros com quem os dados são compartilhados
```

**Isso precisa estar escrito no contrato**, com finalidade, limites, sigilo, e o que acontece com os dados ao fim da relação.

### O que precisa existir

**No site do cliente:**
- [ ] Política de Privacidade publicada
- [ ] Banner de cookies com **recusa real** (não só "OK")
- [ ] Tags de marketing disparando **após** consentimento
- [ ] Finalidade declarada nos formulários
- [ ] Canal para exclusão de dados

**Na sua operação:**
- [ ] Não baixar nem armazenar listas de leads sem necessidade
- [ ] Não compartilhar dados entre clientes (nem "para testar")
- [ ] Ao encerrar o contrato, devolver ou eliminar o que tiver
- [ ] Acessos individuais e com 2FA — nunca senha compartilhada

### Por que isso importa concretamente

**Em incidente de segurança, as duas partes podem ser responsabilizadas.** A cláusula de LGPD não elimina sua responsabilidade, mas define quem responde pelo quê — e demonstra diligência, que é o que conta numa eventual apuração.

> **É também argumento comercial.** Cliente de porte médio pergunta sobre LGPD. Ter resposta pronta e uma cláusula bem redigida te coloca num patamar acima de 90% dos concorrentes.

---

## 4. Cobrança e inadimplência

### Como estruturar

```
Cobrança:     ANTECIPADA (dia 1 do mês de serviço)
Forma:        Pix ou boleto (recorrência, se possível)
Vencimento:   dia fixo, sempre o mesmo
Setup:        100% antes de iniciar
Atraso:       multa de 2% + juros de 1% ao mês
Suspensão:    após 10 dias corridos de atraso
```

**Cobre antecipado.** Você presta serviço contínuo; receber depois é financiar o cliente. Se ele não pode pagar no dia 1, provavelmente não deveria estar investindo em tráfego.

### O protocolo de inadimplência

```
Dia 1  do atraso  → Mensagem leve. ("Oi [nome], vi que o boleto
                     de setembro está em aberto — deve ter passado
                     batido. Consegue dar uma olhada?")
Dia 5             → Cobrança formal por escrito, com o valor e a multa
Dia 10            → Aviso de suspensão + suspensão efetiva
Dia 30            → Rescisão + protesto ou cobrança judicial
```

**Não trabalhe de graça esperando "resolver na conversa".** Gestor de tráfego inadimplente por 3 meses é um gestor que perdeu 3 meses de faturamento e vai perder o cliente de qualquer forma.

### A pergunta que previne inadimplência

Na reunião de fechamento:

> *"Como funciona o pagamento aí? Quem aprova e em que dia do mês costuma sair?"*

A resposta te diz se ele tem processo financeiro ou se paga por impulso. E te permite ajustar o vencimento ao ciclo dele — o que reduz atraso pela metade.

---

## 5. Encerramento de contrato

Como você sai define se o cliente te indica ou te difama. **Saia bem, sempre.**

```
□ Aviso prévio conforme o contrato
□ Entregar relatório final consolidado
□ Documentar o que está rodando e por quê (para o próximo gestor)
□ Remover seus acessos (não espere que ele remova)
□ Devolver ou eliminar dados pessoais em sua posse
□ Deixar campanhas pausadas ou funcionando, conforme combinado
□ Pedir depoimento se a relação foi boa
```

> **O gestor que entrega uma documentação organizada na saída é o gestor que recebe indicação mesmo depois de sair.** O mercado local é pequeno e todo mundo se conhece. Sua reputação de saída vale mais que um mês de fee.

---

## ✅ Tarefas da Fase 10

1. **Ligue para um contador** (procure um que atenda negócios digitais) e confirme: tipo de empresa, CNAE, anexo do Simples e simulação de Fator R. **Esta é a tarefa mais importante da fase.**
2. **Adapte o contrato modelo** de `templates/contrato-modelo.md` para a sua realidade
3. **Peça a um advogado para revisar** — uma revisão de contrato simples custa pouco e você usa o mesmo documento por anos
4. Defina sua **política de pagamento** e escreva-a
5. Monte seu **checklist de encerramento** (seção 5)
6. Verifique se os sites dos seus clientes-alvo têm Política de Privacidade e banner de cookies — **é item de auditoria e argumento de venda**

---

## Checagem de entendimento

1. Por que emitir nota sobre a verba de mídia é um erro caro?
2. Cliente cancela no mês 2 dizendo que "não veio resultado". Quais cláusulas te protegem?
3. Você abriu MEI com CNAE de "promoção de vendas" e está emitindo nota há 6 meses. Qual o risco?

<details>
<summary>Respostas</summary>

**1.** Porque a verba não é sua receita — é dinheiro do cliente destinado à plataforma. Incluí-la na nota faz você pagar imposto sobre dinheiro alheio, infla artificialmente seu faturamento (podendo te aproximar ou estourar o limite do Simples) e cria confusão contábil difícil de desfazer. A solução correta é o cartão do cliente na conta de anúncios.

**2.** Quatro: (a) **obrigação de meio** — você se comprometeu com o processo, não com o resultado; (b) **prazo mínimo de 90 dias** com multa proporcional — 2 meses não é tempo suficiente para julgar uma campanha; (c) **responsabilidades do contratante** — se ele não respondeu os leads, o descumprimento é dele; (d) **escopo e exclusões** — se ele esperava algo que nunca esteve incluso, está escrito que não estava.

**3.** Gestão de tráfego não é atividade permitida no MEI. Os riscos são desenquadramento (inclusive retroativo), cobrança da diferença de tributos com multa e juros, e notas contestadas por clientes na hora de deduzir a despesa. **Procure um contador imediatamente** para avaliar a migração para ME e regularizar o período.

</details>

---

**Próxima:** [Fase 11 — Operação e rotina](fase-11-operacao-rotina.md)
