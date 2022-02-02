from RobotArm import RobotArm
robotArm = RobotArm('exercise 12') 
scanner = [False,False,False,False,False,False,False,False,False]
for i in range(9):
    robotArm.grab()
    if robotArm.scan() == "red":
        scanner[i] = True
    robotArm.drop()
    robotArm.moveRight()
for i in range(9):
    robotArm.moveLeft()
    if scanner[8-i]:
        robotArm.grab()
        for n in range(i+1):
            robotArm.moveRight()
        robotArm.drop()
        for n in range(i+1):
            robotArm.moveLeft()     
robotArm.wait()