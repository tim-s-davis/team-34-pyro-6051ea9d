*** Settings ***
Documentation     
    I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
    https://github.com/level-up-program/team-34-pyro-6051ea9d/blob/main/tests/robot/images/IMG_4593.jpeg

Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  startingX     startingY     startingMoveCount     direction     endingX     endingY     endingMoveCount
Move in the middle of the board     5             5             1                     NORTH         4           5           2
Move on the edge of the board       1             1             5                     SOUTH         1           2           6


*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}