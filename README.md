# SnailJumper-GA

## Project Details

**Project Name:** Snail Jumper Evolution

**Description:** Snail Jumper Evolution is a Python-based game that combines gaming and artificial intelligence. Players control a character that can jump between columns while avoiding obstacles. The game offers two modes: manual control and neuroevolution. In neuroevolution mode, players are evolved through generations using a neural network-based evolutionary algorithm.

**Main Components:**

1. **Game Mechanics:** The core gameplay involves a snail character navigating between columns. The player can switch gravity direction (left or right) to avoid obstacles. Obstacles include snails and flies, each with unique movement patterns. Players aim to achieve the highest possible score by surviving as long as possible.

2. **Neural Network:** The game uses a neural network to control player actions in the neuroevolution mode. The network receives inputs such as player position and obstacle locations and outputs a decision on which direction to switch gravity. The neural network architecture includes input, hidden, and output layers.

3. **Evolutionary Algorithm:** The neuroevolution mode utilizes an evolutionary algorithm to improve player performance over generations. The algorithm consists of parent selection, crossover, and mutation steps. The algorithm evolves a population of players with varying neural network weights and biases to enhance their ability to navigate obstacles.

4. **Scoring and Fitness:** Player fitness is calculated based on their in-game performance. In manual mode, players control the character directly, while in neuroevolution mode, fitness is determined by the score achieved. The evolutionary algorithm selects parents for the next generation based on their fitness values.

5. **User Interface:** The game features an intuitive user interface with options to start the game, choose neuroevolution mode, or exit the game. The player's score, best score, and generation number are displayed during gameplay.

**Implementation Details:**

- The game utilizes the Pygame library for graphical rendering and user input handling.
- Obstacles are generated at specific intervals, adding challenge and variety to the gameplay.
- Players in the neuroevolution mode evolve over generations by inheriting the neural network weights and biases from their parents.
- The project includes multiple Python files to separate different components, such as the game logic, player behavior, neural network, and evolutionary algorithm.

**Future Enhancements:**

- Visual improvements such as background graphics and more diverse obstacles.
- Fine-tuning the neural network architecture for better performance and learning.
- Experimentation with different evolutionary algorithms and selection strategies.
- Incorporation of additional gameplay mechanics to make the game more engaging.

**Conclusion:**

"Snail Jumper Evolution" is a creative fusion of gaming and artificial intelligence. It provides an interactive and educational way to showcase the principles of neuroevolution and evolutionary algorithms. By allowing players to witness the evolution of virtual characters within a game, the project highlights the potential of AI algorithms in real-world scenarios.
