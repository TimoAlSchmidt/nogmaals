from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

# Jouw python instructies zet je vanaf hier:

def moveRobot(left, amount):
    for i in range(amount):
        if left:
            robotArm.moveLeft()
        else:
            robotArm.moveRight()

for i in range(4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()