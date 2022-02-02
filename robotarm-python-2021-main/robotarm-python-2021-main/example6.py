from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:

def moveRobot(left, amount):
    for i in range(amount):
        if left:
            robotArm.moveLeft()
        else:
            robotArm.moveRight()

moveRobot(False, 7)

for i in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    moveRobot(True, 2)


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()