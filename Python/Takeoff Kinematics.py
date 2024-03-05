#Kinematics of an F-15 Eagle taking off
from matplotlib import pyplot as plt
x = 0
vZero = 0
maxThrust = 130400
y = 0
m = 20185
t = 0
v = 0
a = maxThrust/m
for t in range(0, 60):
    v = vZero + (a*t)
    print(str(v) + ' m/s')
