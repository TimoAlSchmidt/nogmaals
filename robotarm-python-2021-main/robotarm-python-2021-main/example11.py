from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
scanner = [False,False,False,False,False,False,False,False,False]
for i in range(9):
    robotArm.grab()
    if robotArm.scan() == "white":
        scanner[i] = True
    robotArm.drop()
    robotArm.moveRight()
for i in range(9):
    robotArm.moveLeft()
    if scanner[8-i]:
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()    
robotArm.wait()