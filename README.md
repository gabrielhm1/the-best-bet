# TBB - The Best Bet
Engenharia de Software (DCC603) - UFMG 
The Best Bet consiste num comparador de odds (chance de um evento ocorrer) entre as principais casas de apostas desportivas em operação no Brasil, visando possibilitar 
a redução de perdas e maximização dos ganhos dos apostadores.

#  Funcionalidades
1. Buscador de odds
2. Compararador de odds entre as casas
3. Cálculo de lucro/prejuízo certo

#  Time
1. Gabriel Henrique Marques Matos - Fullstack
2. Yuri Junior da Silva Adriano - Scrum Master e Backend
3. Caio Almeida Guimarães - Product Owner e Frontend
4. Thiago Ricardo Oliveira - Frontend

# Tecnologias
1. JavaScript
2. Python
3. AWS
4. HTML
5. CSS

# Backlog

**Tarefas técnicas**
1. UI design
2. Configurar interface web
3. Configurar requisição de dados das casas de aposta

**Como usuário, gostaria de ver os jogos que estão sendo negociados nas casas de aposta**
1. Criar a rota principal(back-end), utilizando flask
2. Criar página inicial(front-end), onde serão exibidos as partidas cotadas
3. Fazer requisição dos dados nas casas de aposta
4. Criar lista interativa, que indexe as partidas dos respectivos campeonatos


**Como usuário, gostaria de ver as odds de uma dada partida**
1. Gerar link na página inicial que redirecione para a página individual da partida
2. Criar a rota de cada partida(back-end).
3. Requisitar dados da partida nas casas de aposta.
4. Tratar os dados e exibí-los em categorias (e.g. quem ganha/perde, dupla-hipótese), com a respectivas odds
5. Gerar página-padrão que exiba as apostas possíveis naquela partida

**Como usuário, quero ver qual estratégia posso adotar para não perder dinheiro**
1. Obter dados de múltiplas casas de aposta
2. Tratar dados e armazenar dados em um banco, categorizados por categoria de aposta, de forma que permita a posterior comparação
3. Calcular a fatia que deve ser apostada em cada casa e em que resultado
4. Exibir "calculadora", que mostra o percentil, de um dado montante, que deve ser apostada em cada casa e resultado, e exibir o percentual de lucro garantido da operação.
