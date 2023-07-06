# Snake Game in Python

This is a snake game written in Python using the Turtle graphics library. The game is played by using the arrow keys to move the snake around the screen. The goal of the game is to eat as many dots as possible without hitting the walls or the snake's own tail.

Update v1.2: Added a new snake color, change shape of snake food to turtle. Each spawn of the food will be a random color from the color list.

Update v1.3: Added an event listener to 'Q' key in order to quit the game as well as adding event listeners to the WSAD keys to perform the same actions as the arrow keys. These event listeners are on ".onkeypress" rather then ".onkey" The program will no longer end the loop once the snake has dies, rather a new snake will be created and the game will continue until the user quits. The users high score is now saved to the "high_score.txt" file.

Future Updates: Increasing the speed of the game as it processes, generate a random RGB color rather than it being from a list

## How to play

Start the game by running the main.py file.
Use the arrow keys to move the snake around the screen.
Eat the turtle to score points.
Be careful not to hit the walls or the snake's own tail.

## Requirements

Turtle graphics library
The Turtle graphics documentation: https://docs.python.org/3/library/turtle.html | Turtle graphics comes preinstalled with python, if for some reason it is not, you can install the graphics library by running the following command: pip install PythonTurtle

## Running the game

To run the game, you can use the following command: python main.py

The game will be displayed in a new window. You can then use the arrow keys to move the snake around the screen and eat the apples.

## Controls

Up arrow key: Move the snake up.
Down arrow key: Move the snake down.
Left arrow key: Move the snake left.
Right arrow key: Move the snake right.
Q: To quit the game

## Tips

Try to eat as many apples as possible to score points.
Be careful not to hit the walls or the snake's own tail.
If you hit the walls or the snake's own tail, the game will end.
Enjoy!
I hope this helps! Let me know if you have any other questions.
