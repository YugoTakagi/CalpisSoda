from pid import pid
from class_item.state_class import State

import numpy as np
class for_weel_steering_ikm(object):
    pidX = pid()
    pidY = pid()
    pidTh = pid()

    adjustmentX=0
    adjustmentY=0
    adjustmentTh=0

    v1=0
    v2=0
    v3=0
    v4=0
    r = 0.40

    theta1=0
    theta2=0
    theta3=0
    theta4=0
    def __init__(self):
    	#//+++++PID GAIN SET+++++//
    	self.pidX.set_gain(1,0,0)
    	self.pidY.set_gain(1,0,0)
    	self.pidTh.set_gain(1,0,0.3)
    	#//++++++++++++++++++++++//
    def inverse_kinematics_model(self, state, vx, vy, omega):#theta := ref, alfa := state
        self.v1 = np.sqrt( (vx-self.r*omega*np.sin(state.yaw))**2 + (vy-self.r*omega*np.sin(state.yaw))**2 )
        self.v2 = np.sqrt( (vx-self.r*omega*np.cos(state.yaw))**2 + (vy-self.r*omega*np.sin(state.yaw))**2 )
        self.v3 = np.sqrt( (vx+self.r*omega*np.sin(state.yaw))**2 + (vy-self.r*omega*np.cos(state.yaw))**2 )
        self.v4 = np.sqrt( (vx+self.r*omega*np.cos(state.yaw))**2 + (vy+self.r*omega*np.sin(state.yaw))**2 )

        self.theta1 = np.arctan( (vy+self.r*omega*np.cos(state.yaw))/(vx-self.r*omega*np.sin(state.yaw)) )
        self.theta2 = np.arctan( (vy-self.r*omega*np.sin(state.yaw))/(vx-self.r*omega*np.cos(state.yaw)) )
        self.theta3 = np.arctan( (vy-self.r*omega*np.cos(state.yaw))/(vx+self.r*omega*np.sin(state.yaw)) )
        self.theta4 = np.arctan( (vy+self.r*omega*np.sin(state.yaw))/(vx+self.r*omega*np.cos(state.yaw)) )
    def get_v1(self):
        return self.v1
    def get_v2(self):
        return self.v2
    def get_v3(self):
        return self.v3
    def get_v4(self):
        return self.v4
    def get_theta1(self):
        return self.theta1
    def get_theta2(self):
        return self.theta2
    def get_theta3(self):
        return self.theta3
    def get_theta4(self):
        return self.theta4
    def using_model(self, state, xref, yref, thref, index):
    	self.pidX.set_present(state.x)
    	self.pidY.set_present(state.y)
    	self.pidTh.set_present(state.yaw)

    	self.adjustmentX = self.pidX.run_pid(xref)
    	self.adjustmentY = self.pidY.run_pid(yref)
    	self.adjustmentTh = self.pidTh.run_pid(thref)

    	self.inverse_kinematics_model(state, self.adjustmentX, self.adjustmentY, self.adjustmentTh)
