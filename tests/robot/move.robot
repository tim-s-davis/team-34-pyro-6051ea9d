*** Settings ***
Documentation     
...    I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
...     
...    Here's a picture of one of our working models from the camp:
...    https://raw.githubusercontent.com/level-up-program/team-34-pyro-6051ea9d/main/tests/robot/images/move_function_model-crop.jpeg
...    Here's a link to our github repo:
...    https://github.com/level-up-program/team-34-pyro-6051ea9d

Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  startingX     startingY     startingMoveCount     direction     endingX     endingY     endingMoveCount
Move Top Left Corner NORTH          1             1             1                     NORTH         1           1           2
Move Top Left Corner EAST           1             1             1                     EAST          2           1           2
Move Top Left Corner SOUTH          1             1             1                     SOUTH         1           2           2
Move Top Left Corner WEST           1             1             1                     WEST          1           1           2

Move Top Right Corner NORTH         10            1             1                     NORTH         10          1           2
Move Top Right Corner EAST          10            1             1                     EAST          10          1           2
Move Top Right Corner SOUTH         10            1             1                     SOUTH         10          2           2
Move Top Right Corner WEST          10            1             1                     WEST          9           1           2

Move Bottom Left Corner NORTH       1             10            1                     NORTH         1           9           2
Move Bottom Left Corner EAST        1             10            1                     EAST          2           10          2
Move Bottom Left Corner SOUTH       1             10            1                     SOUTH         1           10          2
Move Bottom Left Corner WEST        1             10            1                     WEST          1           10          2

Move Bottom Right Corner NORTH      10            10            1                     NORTH         9           10          2
Move Bottom Right Corner EAST       10            10            1                     EAST          10          10          2
Move Bottom Right Corner SOUTH      10            10            1                     SOUTH         10          10          2
Move Bottom Right Corner WEST       10            10            1                     WEST          9           10          2

Move Left edge of board NORTH       1             5             5                     NORTH         1           4           6
Move Left edge of board EAST        1             5             5                     EAST          2           5           6
Move Left edge of board SOUTH       1             5             5                     SOUTH         1           6           6
Move Left edge of board WEST        1             5             5                     WEST          1           5           6

Move Top edge of board NORTH        5             1             5                     NORTH         5           1           6
Move Top edge of board EAST         5             1             5                     EAST          6           1           6
Move Top edge of board SOUTH        5             1             5                     SOUTH         5           2           6
Move Top edge of board WEST         5             1             5                     WEST          4           1           6

Move Right edge of board NORTH      10            5             5                     NORTH         10          4           6
Move Right edge of board EAST       10            5             5                     EAST          10          5           6
Move Right edge of board SOUTH      10            5             5                     SOUTH         10          6           6
Move Right edge of board EAST       10            5             5                     WEST          9           5           6

Move Bottom edge of board NORTH     5             10            5                     NORTH         5           9           6
Move Bottom edge of board EAST      5             10            5                     EAST          6           10          6
Move Bottom edge of board SOUTH     5             10            5                     SOUTH         5           10          6
Move Bottom edge of board WEST      5             10            5                     WEST          4           10          6

Move Middle of the board NORTH      5             5             10                    NORTH         5           4           11
Move Middle of the board EAST       5             5             10                    EAST          6           5           11
Move Middle of the board SOUTH      5             5             10                    SOUTH         5           6           11
Move Middle of the board WEST       5             5             10                    WEST          4           5           11


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
