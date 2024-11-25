# Projeto de Cibersegurança - Ambiente Seguro na AWS

## Descrição do Projeto

Este projeto foi desenvolvido como parte da Avaliação Final da disciplina de **Cibersegurança** no Insper. O objetivo é projetar um ambiente seguro e escalável na AWS para hospedar um ambiente de desenvolvimento e testes, seguindo boas práticas de segurança. O projeto contempla a configuração de instâncias separadas para desenvolvimento e banco de dados, segurança baseada em grupos, e monitoramento do ambiente.

## Funcionalidades Implementadas (Conceito C)

- **Instâncias Separadas**:
  - Configuração de instâncias dedicadas para o ambiente de desenvolvimento e o banco de dados, garantindo isolamento e segurança.
- **Security Groups Configurados**:
  - Controle de tráfego configurado nos grupos de segurança para permitir apenas acessos autorizados.
  - Restrições baseadas no IP de origem para conexões SSH.
- **Sistema de Monitoramento Zabbix**:
  - Implementação do Zabbix para monitoramento do ambiente, com alertas configurados para eventos críticos.

## Arquitetura do Sistema

- Instâncias AWS configuradas para:
  - Ambiente de desenvolvimento.
  - Banco de dados de teste.
- Grupos de segurança para controle de tráfego.
- Monitoramento com Zabbix.

### Diagrama de Arquitetura
*(Adicione aqui uma imagem ou link para o diagrama de arquitetura do projeto.)*

## Tecnologias Utilizadas

- **AWS**: Hospedagem e configuração das instâncias.
- **Zabbix**: Monitoramento do ambiente.
- **Grupos de Segurança (AWS)**: Configuração de regras de segurança.
- **Python/Bash**: Para scripts auxiliares (se aplicável).

## Próximos Passos (Conceitos B e A)

- Configuração de um **Jump Server** para controle de acesso.
- Implementação do **Wazuh** para monitoramento de segurança.
- Desenvolvimento da infraestrutura como código utilizando **Terraform**.

## Vídeo

[Clique aqui](https://youtu.be/uylXgdZXe-g)

## Documentação


- [Relatório de Técnico.pdf](https://github.com/user-attachments/files/17895655/Relatorio.de.Tecnico.pdf)
- [Vídeo Demonstrativo](#) *(Adicione o link para o vídeo aqui)*

