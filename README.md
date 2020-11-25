# Rock-Paper-Scissors-with-Myo-Armband-Pose-Detection(GAMYO)
This is a game based project using Myo. This game has 2 ways to play one with hand gesture and another with voice command (for physically challenged people).This detects the poses of user’s hand using Myo , it also recognizes the voice and gives the winner of the game.
## Technolgies Used
- Python3
- MYO
- Machine Learning
- pygame
## Description
Gestures can be identified using pose identification api by myo or by making a data set for 3 hand gestures(Rock, paper and scissors) using data send by emg MYO and predict using machine learning models. As myo is not able to recognize the scissors gesture so for making prediction better we use machine learning models to identify gestures.
- Dataset has been made using train_gesture.py(required Myo in hand). Testdata prediction and model pridiction has been done using test_gesture.py. 
- Pose identification using MYO and voice identification using google api has been done with full UI using RPSgame.py
### Installation
- Unzip the MYO library files.
- install MYO, sklearn on python
