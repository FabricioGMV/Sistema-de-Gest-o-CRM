**Funcionalidades Projeto Software Product.**



**Critérios de Aceitação**



Épico 1: Gestão de Clientes

US01: Como atendente, eu quero cadastrar, editar e inativar clientes com dados de contato e endereço para que eu tenha um catálogo centralizado e não dependa de planilhas ou cadernos soltos.



US02: Como atendente, eu quero buscar um cliente pelo nome ou telefone rapidamente para que eu possa agilizar o atendimento telefônico ou via WhatsApp.



Épico 2: Gestão de Serviços e Contratos

US03: Como gestor, eu quero cadastrar os tipos de serviços prestados (ex: manutenção preventiva, limpeza, instalações) com seus respectivos prazos de validade para que o sistema saiba como calcular os vencimentos automaticamente.



US04: Como atendente, eu quero vincular um serviço executado a um cliente, informando a data da realização, para que a empresa tenha um histórico exato do que foi feito em cada local.



Épico 3: Controle de Vencimentos (A funcionalidade principal)

US05: Como responsável pelo contato comercial, eu quero visualizar uma lista diária de serviços que estão próximos do vencimento (ex: nos próximos 15 dias) para que eu possa abordar o cliente proativamente e oferecer a renovação do serviço.



US06: Como responsável pelo contato comercial, eu quero ver uma lista destacada de serviços que já passaram do prazo de renovação para que eu possa priorizar essas ligações e recuperar possíveis vendas perdidas.



Épico 4: Acompanhamento e Retenção

US07: Como atendente, eu quero registrar notas rápidas no histórico do cliente após uma ligação (ex: "pediu para retornar na sexta") para que eu não perca o fio da meada das negociações, já que gerencio muitos contatos ao mesmo tempo.



US08: Como gestor, eu quero acessar um painel (dashboard) inicial com o resumo de "Contatos Pendentes" e "Serviços a Vencer no Mês" para que eu saiba exatamente qual é a prioridade da equipe logo ao abrir o sistema.





**Regras de Negócios**



**Cadastro de Clientes**



RN01 – Unicidade de Registro

* Não permitir cadastro de clientes com mesmo CPF ou CNPJ.



RN02 – Exclusão Lógica (Soft Delete)

* Clientes com histórico não podem ser excluídos fisicamente.
* Devem ter status alterado para “Inativo”.



RN03 – Dados Obrigatórios

* Para cadastro é obrigatório:



&nbsp;	Nome

&nbsp;	Telefone Principal



RN04 – Cliente Inativo Não Operacional

* Clientes com status “Inativo”:



&nbsp;	Não podem receber novos serviços

&nbsp;	Não aparecem nas listas operacionais



**Serviços e Vencimentos**



RN05 – Serviço Apenas para Cliente Ativo

* Não é permitido vincular serviço a cliente inativo.



RN06 – Cálculo Automático de Vencimento

* Data Vencimento = Data Execução + Prazo do Serviço
* O cálculo deve ser feito automaticamente pelo back-end.



RN07 – Bloqueio de Data Futura

* Data de Execução não pode ser maior que a data atual.



RN08 – Janela de "A Vencer"

* Serviço é considerado "A Vencer" quando faltarem 30 dias ou menos para o vencimento.



RN09 – Serviço Vencido Permanece Listado

* Serviços vencidos continuam aparecendo até que sejam renovados ou marcados como encerrados.



RN10 – Renovação Gera Novo Registro

* Renovação não altera o registro antigo.
* Deve gerar um novo ciclo de serviço.



RN11 – Atualização de Status Pós-Renovação

* Após renovação:



&nbsp;	Serviço anterior deve ser marcado como “Renovado” ou “Concluído”

&nbsp;	Deve sair da lista de pendências



**Interações e Contatos**



RN12 – Registro Restrito a Cliente Ativo

* Só é permitido registrar interação para cliente ativo.



RN13 – Notas Não Podem Ser Excluídas

* Interações registradas não podem ser apagadas.
* Podem apenas ser arquivadas.
