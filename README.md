## Refatoração

Foram feitas várias melhorias no código para seguir boas práticas de desenvolvimento, visando a modularidade, a legibilidade e a manutenção do código. Essas mudanças incluem a introdução de novas classes e a separação de responsabilidades, seguindo o princípio de responsabilidade única (SRP) da programação orientada a objetos (OOP).

### Principais Melhorias:
### Separação de Responsabilidades:

**TicTacToeBoard:** Esta classe é responsável por gerenciar o estado do tabuleiro, retornar espaços disponíveis, verificação de linha, coluna e diagonal atrás de um vencedor. Ela também lida com a impressão do tabuleiro e a execução dos movimentos. Isso segue o princípio de responsabilidade única, garantindo que cada classe tenha uma única razão para mudar.

**TicTacToeGame:** Focada na lógica do jogo, esta classe verifica as condições de vitória e verifica os movimentos disponíveis. Isso torna o código mais modular e facilita a adição de novas regras ou modificações no futuro.

**TicTacToePlay:** Transformada de uma função em uma classe, esta gerencia o fluxo do jogo, alternando entre os jogadores e mostra o resultado no final da partida. Essa mudança promove a reutilização e facilita a extensão para suportar diferentes tipos de jogadores (humanos ou máquinas, por exemplo).

### Encapsulamento:
As responsabilidades específicas foram encapsuladas em classes separadas. Isso não só melhora a legibilidade, mas também a manutenção do código, já que mudanças em uma parte do sistema (como o método de impressão do tabuleiro) não afetam outras partes.

### Manutenibilidade:
A divisão em classes menores e específicas torna o código mais fácil de entender e manter. Problemas e bugs podem ser localizados e corrigidos com mais eficiência, já que cada classe tem um propósito bem definido.
