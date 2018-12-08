import numpy as np
class state_class_of_4ste:
    dt = 0.08
    x1 = 0.0
    y1 = 0.0
    x2 = 0.0
    y2 = 0.0
    x3 = 0.0
    y3 = 0.0
    x4 = 0.0
    y4 = 0.0
    def __init__(self, x=0.0, y=0.0, yaw=0.0):
        self.x = x
        self.y = y
        self.yaw = yaw
        self.r = 0.4
    def update(self, vell1=0.0, vell2=0.0, vell3=0.0, vell4=0.0, theta1=0.0, theta2=0.0, theta3=0.0, theta4=0.0):
        self.x1 = vell1*np.cos(theta1)*self.dt+self.r +self.x
        self.y1 = vell1*np.sin(theta1)*self.dt +self.y
        self.x2 = vell2*np.cos(theta2)*self.dt +self.x
        self.y2 = vell2*np.sin(theta2)*self.dt+self.r +self.y
        self.x3 = vell3*np.cos(theta3)*self.dt-self.r +self.x
        self.y3 = vell3*np.sin(theta3)*self.dt +self.y
        self.x4 = vell4*np.cos(theta4)*self.dt +self.x
        self.y4 = vell4*np.sin(theta4)*self.dt-self.r +self.y
