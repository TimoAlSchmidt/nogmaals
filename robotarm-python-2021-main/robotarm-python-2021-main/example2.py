from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:

def moveRobot(left, amount):
    for i in range(amount):
        if left:
            robotArm.moveLeft()
        else:
            robotArm.moveRight()

robotArm.grab()
moveRobot(False, 9)
robotArm.drop()
moveRobot(True, 5)
robotArm.grab()
moveRobot(False, 5)
robotArm.drop()
moveRobot(True, 2)
robotArm.grab()
moveRobot(False, 2)
robotArm.drop()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()