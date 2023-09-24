# Solution for problem at >>  https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_rt():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if not front_is_clear() and right_is_clear() == True:
        turn_rt()
    if front_is_clear() == True and right_is_clear() == True:
        move()
    if not front_is_clear() and wall_on_right() == True:
        turn_left()
    if front_is_clear() == True:
        move()
