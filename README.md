# QI TECH PYTHON CASE

O objetivo deste case é a criação de uma API RESTful que permita:
* Efetuar uma Consulta SCR de um documento em um site externo e retornar esta informação de maneira consolidada em formato JSON
* Efetuar uma análise simples sobre um documento a partir da consulta de um Documento gerando um relatório simplificado


Por último ao entrar em contato com estes conhecimentos propor uma abordagem sobre estes dados para oferecer um Rank de Risco de crédito para esta consulta onde 0% seria muito confiável e 100% seria muito arriscado.

Para entrega: criar um projeto no github e enviar endereço

# Rodando o projeto

Instalar os pacotes do projeto:
```
pip install -r requirements.txt
```

No root do projeto rodar:
```
./app.sh
```

## guideline da API

(GET) /api/scr/report  ---> gera o relatório em PDF
(GET) /api/scr/        ---> retorna json consolidado do doc scr