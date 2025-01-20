# Flappy Puff

"Flappy Puff" is a Python-based game inspired by *Flappy Bird*, where AI characters are trained using Genetic Algorithms to play the game. The project generates 100 AI players, and over three generations, the best-performing AIs evolve and become the starting point for the next round. After three generations, the user (Player) can compete against the AI in an exciting head-to-head game. The entire game is built using Python and features a graphical user interface (GUI).

## Features

- **Genetic Algorithm**: 100 AI characters are created and evolve over three generations based on their performance, using Genetic Algorithms.
- **AI Evolution**: The best-performing AIs are selected and used as the foundation for the next generation.
- **User Interaction**: After three rounds of AI evolution, the user can compete against the evolved AI in a fun game of *Flappy Puff*.
- **Python GUI**: A user-friendly graphical interface is created using Python to control the game and visualize the AI evolution.

## Installation

To run this project, ensure you have Python 3.x installed. You can download Python from [here](https://www.python.org/downloads/).

Clone the repository to your local machine:
git clone https://github.com/yourusername/flappy-puff.git

Navigate to the project directory:
cd flappy-puff

Install the necessary dependencies (Pygame etc.):
pip install -r requirements.txt

Run the project:
python main.py


## How to Play

1. **AI Evolution**: The game starts with 100 AI players that will play and evolve over three generations.
2. **Gameplay**: The AI players attempt to navigate through obstacles (similar to *Flappy Bird*) by using genetic algorithms to improve their skills over time.
3. **User Competition**: After three generations of AI evolution, the user can play against the best-performing AI.
4. **Objective**: Avoid hitting obstacles and keep the bird flying to achieve the highest score.

## Technologies Used

- **Python**: The main programming language for game logic and AI development.
- **Pygame**: Used to create the graphical interface and render the game.
- **Genetic Algorithms**: To evolve and improve the AI players over generations.
- **Tkinter**: Used for the GUI to interact with the game.

## Contributing

Feel free to fork this project and submit your improvements, bug fixes, or new features. You can contribute by:

- Reporting issues or bugs
- Adding new features or optimizations
- Enhancing the user interface

Please create a pull request for any contributions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.