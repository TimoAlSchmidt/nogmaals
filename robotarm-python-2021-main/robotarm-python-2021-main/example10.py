from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
for i in range(9,0,-1):
    if i % 2 == 1:
        robotArm.grab()
    for n in range(i):
        if i % 2 == 0:
            robotArm.moveLeft()
        else: 
            robotArm.moveRight()
    robotArm.drop()
robotArm.wait()