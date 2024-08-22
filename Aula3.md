Padrões Arquiteturais:
Livros:
- Padres de Arquitetura de Aplicações Corporativas - Martin Fowler
- Aplicações moveis: arquitetura, projetos e desenvolvimento - Valentino Lee
- UML 2 - Uma Abordagem Prática - Gilleanes T. A. Guedes

Padrões Existentes: 
- Monolito
    - Mesmo agindo separadamente continuam LIGADOS transformando conjunto em um único sistema.
    - Facilidade: solução única interligando todas as funcionalidades do sistema.
    - Problemas: escalabilidade, agregação de tecnologias, demora no aculturamento para novos integrantes, aumento da complexidade e do tamanho do código ao longo do tempo, alta dependência de componentes de código, falta de flexibilidade, dificuldade para colocar alterações em produção. 
- Microserviços
    - Separação dos elementos de funcionalidade, colocados em serviços separados, dessa forma tornando-os totalmente autônomos e totalmente independentes, que se comunicam por meio de APIs.
    - Cada funcionalidade é separada em serviços bem definidos que podem ou não complementar outra funcionalidade.
    - Principal dificuldade: necessidade de desenvolvedores qualificados. 
- Modelo-Visão-Controlador (MVC)
    - Model-View-Controller é um padrão de arquitetura de software que separa a representação da informação da intereção do usuário com ele.
    - Alterações feitas no layout não afetam a manipulação de dados, e estes poderão ser reorganizados sem alterar o layout.
    - Provê a separação das tarefas de acesso aos dados e lógica de negócio, lógica de apresentação e de interação com o utilizador, introduzindo um componente entre os dois: o controlador.
    - Modelo: consiste nos dados da aplicação, regras de negócios, lógica e funções.
    - Visão: Pode ser qualquer saída de representação dos dados, como uma tabela ou como um diagrama. É possível ter várias visões do mesmo dado, como um gráfico de barras para gerenciamento e uma visão tabular para contadores.
    - Controlador: Faz a mediação da entrada, convertendo-a em comandos para o modelo ou a visão. As ideias centrais por trás do MVC são a reusabilidades de código e separação de conceitos. 
- Model View Template (MVT)
    - Model: representa a camada de acesso aos dados geralmente é responsavel pelo acesso ao banco de dados.
    - Template: camda de apresentacao da informacao, que lida com a interface para o usuario.
    - View: camada usada para implementar a logica de negocios e interagir com  um modelo para transportar dados e renderizar um template.

Links: https://angular.dev

 
Mapeamento Objeto Relacional 
Livros: 
Python e Django: desenvolvimento web moderno e agil
Object- relational DBMSs
Django ORM Cookbook
- ORM:
    - Tecnica de desenvolvimento utilizada para reduzir a demanda de trabalho em programacao orientada a objetos ao se utilizar banco de dados relacionais.
    - As tabelas do banco de dados sao representadas atraves de classes e os registros de cada tabela sao representados como instancias das classes correspondetes.
    - Com esta tecnica, o programador nao precisa se preocupar com os comandos em linguagem SQL. Ele irá usar uma interface de programacao simples que faz todo o trabalho de pesistencia.
    - Nao é necessaria uma correspondencia direta entre as tabelas de dados e as classes do programa.
    - A relacao entre as tabelas onde originam os dados e o objeto que os disponibiliza é configurada pelo programador, isolando o codigo do programa das alterecaoes a organizacao dos dados nas tabelas do banco de dados. 
    - A forma como este mapeamento é configurado depende da ferramenta utilizada. Como exemplo, o programador que use Hibernate na linguagem Java pode usar arquvios XML ou sistema de anotacoes (annotations) que a linguagem providencia. Em outros casos os mapeamento é feito diretamente no codigo, atraves de heranca de classes especiais como é o caso do ORM do Django e do SqlAlchemy na linguagem Python.
    - Simplicidade, facilidade e produtividade.
    - Algumas ferramentas graficas podem ser usadas para gerar o codigo que representa o modelo do banco, como o ORM Pony tambem da linguagem Python.

Python
Livros:
Introducao a programacao com pythonL algoritmos e logica de programacao para iniciantes
Introducao a computacao usando python - um foco ....

Zen Python Filosofia
- Caracteristicas
    - Alto nível
    - Interpretada
    - Dinamicamente tipada
    - Multi-paradigma

