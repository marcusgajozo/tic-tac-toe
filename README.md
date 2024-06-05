## Tic Tac Toe

### Engenharia Reversa
### Relatório de Análise do Sistema Tic Tac Toe

### Estrutura Atual:
O sistema “Tic Tac Toe” consiste em 3 classes: “TicTacToe”, “Player” e “HumanPlayer”. Um método chamado play é responsável por chamar e executar em um laço de repetição que faz com que o jogo permaneça rodando enquanto não tem vencedor ou empate.

**Classe TicTacToe:** Responsável por manter o estado do jogo, incluindo o tabuleiro atual e o acompanhamento do vencedor. Métodos para imprimir o tabuleiro, obter movimentos disponíveis, verificar se há espaços vazios, contar espaços vazios, fazer movimentos e verificar se há um vencedor.

**Classe Player:** Classe base que define o comportamento de um jogador genérico no jogo. Possui um método “get_move” que deve ser implementado pelas subclasses para obter o próximo movimento do jogador.

**Classe HumanPlayer:** Estende o Player e representa um jogador humano. Implementa o método “get_move” para solicitar uma entrada do usuário através do terminal.

### Dependências:
O módulo não possui dependências externas além da biblioteca padrão do Python.

### Funcionalidades:
**Gerenciamento do Jogo:**
- Inicialização de um jogo Tic Tac Toe.
- Impressão do tabuleiro após cada movimento.
- Verificação de movimentos válidos.
- Verificação de vencedor ou empate.
- Alternância entre jogadores.

