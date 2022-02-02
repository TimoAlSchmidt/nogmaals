from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)
# Jouw python instructies zet je vanaf hier:

n = 1
robotArm.grab()
while robotArm.scan() != "":
    for i in range(n):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(n):
        robotArm.moveLeft()
    n += 1
    robotArm.grab()
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()