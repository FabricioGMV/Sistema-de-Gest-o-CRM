**Funcionalidades Projeto Software Product.**



##### **Critérios de Aceitação**



Épico 1: Gestão de Clientes

**US01**: Como atendente, eu quero cadastrar clientes com dados de contato e endereço para que eu tenha um catálogo centralizado e não dependa de planilhas ou cadernos.



**US02**: Como atendente, eu quero editar os dados de contato e endereço de um cliente para manter as informações cadastrais sempre atualizadas.



**US03**: Como atendente, eu quero inativar clientes no sistema para que registros antigos não apareçam em operações do dia a dia, mantendo o histórico preservado.



**US04**: Como atendente, eu quero buscar um cliente pelo nome ou telefone para que eu possa agilizar o atendimento telefônico ou via WhatsApp.



Épico 2: Gestão de Serviços e Contratos

**US05**: Como gestor, eu quero cadastrar os tipos de serviços prestados (ex: manutenção preventiva, limpeza e instalações) com seus respectivos prazos de validade para que o sistema possa calcular automaticamente os vencimentos.



**US06**: Como atendente, eu quero vincular um serviço executado a um cliente informando a data de realização para que a empresa tenha um histórico preciso dos serviços realizados em cada local.



Épico 3: Controle de Vencimentos (Funcionalidade Principal)

**US07**: Como responsável pelo contato comercial, eu quero visualizar uma lista diária de serviços próximos do vencimento (ex: próximos 15 dias) para que eu possa abordar o cliente proativamente e oferecer a renovação do serviço.



**US08**: Como responsável pelo contato comercial, eu quero visualizar uma lista de serviços que já ultrapassaram o prazo de renovação para priorizar o contato com esses clientes e recuperar possíveis vendas.



Épico 4: Acompanhamento e Retenção

**US09**: Como atendente, eu quero registrar notas rápidas no histórico do cliente após uma ligação (ex: “pediu para retornar na sexta”) para acompanhar negociações e interações com o cliente.



**US10**: Como gestor, eu quero visualizar um painel inicial (dashboard) com o resumo de contatos pendentes para identificar rapidamente as prioridades da equipe ao acessar o sistema.



**US11**: Como gestor, eu quero gerar automaticamente uma planilha contendo os serviços prestados no mês (US05) e os serviços a vencer no mês (US07) para facilitar o controle e a gestão operacional.



##### **Regras de Negócios**



**Cadastro de Clientes**



RN01 (US01) – Unicidade de Registro

* O sistema não deve permitir o cadastro de clientes com CPF ou CNPJ já existente na base de dados.



RN02 (US01) – Dados Obrigatórios no Cadastro

* Para realizar o cadastro de um cliente, os seguintes dados são obrigatórios:

&#x09;CPF do cliente;

&#x09;CNPJ do cliente;

&#x09;Nome do cliente;

&#x09;Telefone principal.



RN03 (US03) – Exclusão Lógica (Soft Delete)

* Clientes com histórico não podem ser excluídos fisicamente.
* Devem ter status alterado para “Inativo”.



RN04 (US02) – Edição de Dados Cadastrais

* Os dados de contato e endereço do cliente podem ser editados a qualquer momento por usuários autorizados.



RN05 (US03/US06)– Cliente Inativo Não Operacional

* Clientes com status “Inativo”:



 	Não podem receber novos serviços

 	Não aparecem nas listas operacionais



**Serviços e Contratos**



RN06 (US06) – Serviço Apenas para Cliente Ativo

* Não é permitido vincular serviço a clientes com status “Inativo”.



RN07 (US06) – Data de Execução Válida

* A data de execução do serviço não pode ser maior que a data atual.



RN08 (US05/US06/US07/US08)– Cálculo Automático de Vencimento

* A data de vencimento do serviço deve ser calculada automaticamente pelo sistema utilizando a fórmula:

&#x09;Data Vencimento = Data Execução + Prazo do Serviço



RN09 (US06/US08) – Renovação Gera Novo Registro

* A renovação de um serviço não deve alterar o registro original.
* O sistema deve criar um novo registro de serviço, iniciando um novo ciclo.



RN10 (US08) – Atualização de Status Pós-Renovação

* Após renovação de um serviço:

 	O registro anterior deve ser marcado como “Renovado” ou “Concluído”

 	O serviço deve ser removido das listas de pendência ou vencimento.



**Controle de Vencimentos**



RN11 (US07) – Critério para Serviços Próximos do Vencimento

* Um serviço é considerado “Próximo do Vencimento” quando faltarem 15 dias ou menos para sua data de vencimento.



RN12 (US08) – Critério para Serviço Vencido

* Um serviço é considerado “Vencido” quando a data atual ultrapassa a data de vencimento.



RN13 (US08) – Serviço Vencido Permanece Listado

* Serviços vencidos continuam aparecendo até que sejam renovados ou marcados como encerrados.



**Interações e Contatos**



RN14 (US09) – Registro de Interações

* O sistema deve permitir registrar notas ou observações no histórico do cliente após interações de atendimento.



RN15 (US09) – Integridade do Histórico

* Notas registradas no histórico do cliente não podem ser excluídas permanentemente, podendo apenas ser arquivadas ou ocultadas para manter a rastreabilidade.



RN16 (US09) – Registro Restrito a Cliente Ativo

* Só é permitido registrar interação para cliente ativo.



**Relatórios e Dashboard**



RN17 (US10) – Consolidação de Informações no Dashboard

* O painel inicial do sistema deve consolidar informações sobre:

&#x09;contatos pendentes

&#x09;serviços próximos do vencimento



RN18 (US11) – Geração de Relatório Mensal

* O sistema deve permitir a geração automática de uma planilha contendo:

&#x09;serviços prestados no mês

&#x09;serviços com vencimento no mês

