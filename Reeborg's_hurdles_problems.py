#Hurdle-1 >> problem at >> https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
def turn_rt():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_rt()
    move()
    turn_rt()
    move()
    turn_left()
    
for i in range(0,6):
    jump()

#Hurdle-2 >> problem at >> https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
def turn_rt():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_rt()
    move()
    turn_rt()
    move()
    turn_left()

while not at_goal():
    jump()

#Hurdle-3 >> problem at >> https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
def turn_rt():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_rt()
    move()
    turn_rt()
    move()
    turn_left()

while not at_goal():
    while wall_in_front() == True and not at_goal():
        jump()
    while front_is_clear() == True and not at_goal():
        move()

#Hurdle-4 >> problem at >> https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def turn_rt():
    turn_left()
    turn_left()
    turn_left()
def jump():
    mv_cnt = 0
    turn_left()
    while not right_is_clear():
        mv_cnt += 1
        move()
    turn_rt()
    move()
    turn_rt()
    while mv_cnt > 0:
        move()
        mv_cnt -= 1
    turn_left()
while not at_goal():
    if wall_in_front() == True:
        jump()
    else:
        move()
