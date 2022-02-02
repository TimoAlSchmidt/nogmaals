from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:

def moveRobot(left, amount):
    for i in range(amount):
        if left:
            robotArm.moveLeft()
        else:
            robotArm.moveRight()

for i in range(2):
    robotArm.grab()
    moveRobot(False, 2)
    robotArm.drop()
    moveRobot(True, 2)

robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for i in range(2):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()