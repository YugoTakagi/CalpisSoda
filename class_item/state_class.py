import numpy as np

class State:
    dt = 0.08
    def __init__(self, x=0.0, y=0.0, yaw=0.0):
        self.x = x
        self.y = y
        self.yaw = yaw
        self.r = 0.4
    def update(self, vell1, vell2, vell3):
        #dt wo kaketa houga yoi no ka?
        self.x += vell1*np.sin(5*np.pi/6 +self.yaw)*self.dt +vell2*np.sin(3*np.pi/2 +self.yaw)*self.dt +np.sin(np.pi/6 +self.yaw)*self.dt
        self.y += vell1*np.cos(5*np.pi/6 +self.yaw)*self.dt +vell2*np.cos(3*np.pi/2 +self.yaw)*self.dt +np.cos(np.pi/6 +self.yaw)*self.dt

        #self.x += vell1*np.sin(3*np.pi/2 -self.yaw)*self.dt +vell2*np.sin(5*np.pi/6 -self.yaw)*self.dt +np.sin(np.pi/6 -self.yaw)*self.dt
        #self.y += vell1*np.cos(3*np.pi/2 -self.yaw)*self.dt +vell2*np.cos(5*np.pi/6 -self.yaw)*self.dt +np.cos(np.pi/6 -self.yaw)*self.dt
        self.yaw += (vell1 +vell2 +vell3)*self.dt/self.r
        #self.yaw = 0
        return self.x, self.y, self.yaw
