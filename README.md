## Reengenharia

As implementações introduzidas visam aprimorar a jogabilidade, aumentar a flexibilidade e fornecer informações aos jogadores(placar de vitórias). Para as melhorias foi necessário a criação de classe nova, mudar a estrutura de algumas funções e mudança nomenclatura de algumas funções e variáveis, todas as melhorias foram descritas abaixo.

**Menu inicial com opções:**
A primeira grande mudança reside na implementação de um menu inicial, proporcionando ao jogador maior controle sobre sua experiência. Através deste menu, o usuário pode escolher entre iniciar um jogo contra um outro jogador ou a máquina, consultar o placar de vitórias ou sair. Essa funcionalidade oferece mais autonomia e flexibilidade ao jogador.

**Reiniciar o jogo:**
A opção de reiniciar o jogo em andamento permite que o jogador recomece a partida sem precisar sair do jogo e iniciar um novo. Essa funcionalidade é especialmente útil para testar diferentes estratégias ou simplesmente para se divertir jogando novamente contra um outro jogador ou a máquina.

**Adicionar um Jogador CPU:**
A introdução de um jogador CPU oferece uma nova opção de oponente, permitindo que o jogador jogue sozinho. Essa funcionalidade torna o jogo mais versátil e atende a diferentes perfis de jogadores, desde aqueles que preferem a companhia de um amigo até os que desejam testar suas habilidades.

**Placar de Vitórias:**
O placar de vitórias registra o histórico de vitórias de cada jogador, fornecendo uma maneira de acompanhar o desempenho individual e a evolução das habilidades. Essa funcionalidade adiciona um elemento competitivo ao jogo e incentiva os jogadores a se aperfeiçoarem, buscando superar seus próprios recordes e os de seus oponentes.

## Documento atualizado
### Classes e atributos

#### TicTacToeGame

**Atributos:** game, winner e scoreboard

A classe TicTacToeGame representa o jogo da velha em si. Ela gerencia o tabuleiro do jogo, verifica se há jogadas disponíveis, reinicia o jogo, determina se o jogo deve continuar (verificando se há vencedor ou espaços vazios), exibe o resultado (vitória ou empate), mostra o placar, imprime o tabuleiro na tela e processa as jogadas dos jogadores. Ao validar uma jogada, ela verifica se resulta em um vencedor e atualiza o placar de acordo.


#### TicTacToeBoard

**Atributos:** board

A classe TicTacToeBoard representa o tabuleiro do jogo da velha. Ela é responsável por armazenar o estado do jogo (quem jogou em cada posição), imprimir o tabuleiro na tela, processar as jogadas dos jogadores (verificando se a posição está vazia e atualizando o tabuleiro), reiniciar o tabuleiro para um novo jogo, verificar se existem espaços vazios para continuar jogando e, por fim, a parte mais complexa: checar se a última jogada resultou em um vencedor. Para checar o vencedor, a classe analisa as linhas, colunas e diagonais do tabuleiro para verificar se há 3 símbolos iguais (do jogador que realizou a última jogada).

#### Scoreboard

**Atributos:** x, o

A classe Scoreboard é responsável por manter o placar do jogo da velha. Ela armazena separadamente a pontuação do jogador "X" e do jogador "O", representados por variáveis internas. O método set_victory atualiza o placar de acordo com o vencedor da última jogada, incrementando o contador do jogador "X" ou "O". Por fim, o método show_scoreboard exibe o placar na tela, mostrando a pontuação de cada jogador.

#### TicTacToePlay
**Atributos:** game, human_player, opponent, letter

A classe TicTacToePlay é responsável por controlar o fluxo principal do jogo da velha. Ela cuida de exibir o menu inicial, permitindo ao jogador escolher jogar sozinho contra o computador, jogar contra outro humano ou ver o placar. Também define os jogadores, inicializa e reinicia o jogo, alterna as jogadas entre o jogador humano e o computador (dependendo da opção escolhida), verifica o vencedor e o fim do jogo, e finaliza o programa.

#### Player

**Atributos:** letter

A classe Player representa um jogador genérico no jogo da velha. Ela possui um atributo letter que indica a letra que o jogador utiliza no jogo ("X" ou "O"). No entanto, o método get_move é um método abstrato, ou seja, não possui implementação nesta classe. 

### HumanPlayer

A classe HumanPlayer herda da classe base Player e representa um jogador humano no jogo da velha.  Ela define o método get_move, que é responsável por obter a jogada do jogador humano. Esse método entra em um loop até que uma jogada válida seja fornecida. Primeiramente, ele solicita a jogada do jogador por meio do input, indicando a letra do jogador e os valores válidos (de 0 a 8).  Em seguida, ele tenta converter a entrada do usuário para um valor inteiro. Se a conversão for bem-sucedida, ele verifica se a jogada escolhida está entre as jogadas disponíveis no tabuleiro (game.available_moves()). Caso a jogada seja válida, o loop termina e o valor é retornado. Se houver algum erro (valor não numérico ou jogada indisponível), uma mensagem de erro é exibida e o loop continua solicitando uma jogada válida.

### RandomComputerPlayer

A classe RandomComputerPlayer herda da classe base Player e representa um jogador controlado por computador no jogo da velha.  Ela define o método get_move, que simula o computador pensando em sua jogada.  Ao invés de pedir a escolha do usuário, o método get_move utiliza a função random.choice para selecionar aleatoriamente uma jogada dentre as disponíveis no tabuleiro (game.available_moves()). Para dar a impressão de um computador pensando, ele exibe a mensagem "CPU playing..." e usa a função time.sleep(2) para introduzir uma pausa de 2 segundos antes de retornar a jogada escolhida.
