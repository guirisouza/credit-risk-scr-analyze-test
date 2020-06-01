# QI TECH PYTHON CASE

O objetivo deste case é a criação de uma API RESTful que permita:
* Efetuar uma Consulta SCR de um documento em um site externo e retornar esta informação de maneira consolidada em formato JSON
* Efetuar uma análise simples sobre um documento a partir da consulta de um Documento gerando um relatório simplificado


Por último ao entrar em contato com estes conhecimentos propor uma abordagem sobre estes dados para oferecer um Rank de Risco de crédito para esta consulta onde 0% seria muito confiável e 100% seria muito arriscado.

Para entrega: criar um projeto no github e enviar endereço

### O que é uma Consulta SCR
O SCR é um instrumento de registro e consulta de informações sobre as operações de crédito, avais e fianças prestados e limites de crédito concedidos por instituições financeiras a pessoas físicas e jurídicas no país. O sistema é alimentado mensalmente pelas instituições financeiras e apresenta a situação das operações existentes, estejam em atraso ou em dia, ao final de cada mês.

São objetivos do SCR:
- prover a supervisão do Banco Central com informações que melhorem a capacidade de avaliação da carteira de crédito das instituições, auxiliando a detecção e prevenção de crises bancárias;
- permitir o desenvolvimento de ferramentas que sinalizem instituições com problemas potenciais em relação à carteira de crédito;
- permitir que o Banco Central realize análises sobre o mercado de crédito;
- auxiliar as instituições financeiras na gestão de suas carteiras de crédito, preenchendo a lacuna de informações comportamentais de um cliente.


### Ponto de Partida

Como ponto de partida, fornecemos um setup básico de um framework python para criação de APIs `falcon` . Nele você verá um exemplo de GET e um exemplo de POST. Para rodar basta executar o arquivo  `app.sh`, não se esqueça das dependências necessárias.
 
### Simulação de Consulta em base externa

Numa aplicação real, o sistema deve considerar a entrada de um documento CPF ou CNPJ e consultar baseado neste valor. Para efeitos de simulação, crie um mock no site https://www.mocky.io/ que retorne o JSON fornecido no arquivo `sample_response.json`. Assuma que esta é a resposta de consulta para qualquer documento enviado.

Para ajudar na compreensão dos resultados enviados na consulta, o arquivo `sample_response.pdf` contém um relatorio PDF extraído da base que corresponde à consulta JSON. Nossa API precisa trabalhar com dados em código para obter uma informação igual ou melhor do que o fornecido pelo consolidado PDF.

O valor na caixa `Total` do PDF corresponde à proporção de uso dos limites de crédito e é calculado como sendo Carteira de Crédito / Risco Total 

### Informações Gerais

Fique à vontade para sugerir organização de endpoints, opções de consulta, parametros para trazer dados mais agrupados ou menos agrupados, nomes de variáveis e etc.

## O Algo a mais ...

Com a viabilidade de efetuar as consultas imediatamente nos surge a opção de utilizar estes dados para gerar algum tipo de Rank para avaliar automaticamente algum tomador no momento em que ele solicita uma proposta de dívida por exemplo. Sugira uma maneira possível de avaliar os dados consolidados para chegar à alguma conclusão de risco de crédito sobre o alvo da consulta. Será visto com bons olhos se uma solução em código for apresentada para os dados fornecidos como exemplo.


#### Alguns pontos que serão observados
Nosso objetivo é avaliar sua capacidade de interpretar e abordar um problema, suas características de desenvolvimento, domínio da linguagem, criatividade, organização de código, eficiência e funcionalidade. 

## Boa sorte !
