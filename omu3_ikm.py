from pid import pid
from class_item.state_class import State

import numpy as np
class omu3(object):
    """docstring fs 3omu."""
    pidX = pid()
    pidY = pid()
    pidTh = pid()

    adjustmentX=0
    adjustmentY=0
    adjustmentTh=0

    enlargement_vx=0
    enlargement_vy=0

    v1=0
    v2=0
    v3=0
    r = 0.40

    sqrt3 = np.sqrt(3)
    xsta = 0
    ysta = 0
    alfasta = 0
    def __init__(self):
    	#//+++++PID GAIN SET+++++//
    	self.pidX.set_gain(1,0,0.3)
    	self.pidY.set_gain(1,0,0.3)
    	self.pidTh.set_gain(0.1,0,0)
    	#//++++++++++++++++++++++//
        pass
        #sups 3omu, self).__init__()
    def inverse_kinematics_model(self, state, vx, vy, omega):#theta := ref, alfa := state
        #4-omuni no inverse_kinematics_model
        self.enlargement_vx = vx*np.cos(state.yaw) + vy*np.sin(state.yaw)
        self.enlargement_vy = -1*vx*np.sin(state.yaw) + vy*np.cos(state.yaw)
        #self.enlargement_vx = vx
        #self.enlargement_vy = vy
        #'''
        self.v1 = 1/2*self.enlargement_vx - self.sqrt3/2*self.enlargement_vy +self.r*omega
        self.v2 = -1*self.enlargement_vx - 0*self.enlargement_vy +self.r*omega
        self.v3 = 1/2*self.enlargement_vx + self.sqrt3/2*self.enlargement_vy +self.r*omega
        #'''
        '''
        self.v1 = -vx*np.cos(state.yaw) -vy*np.sin(state.yaw) +self.r*omega
        self.v2 = -vx*np.cos(state.yaw+2*np.pi/3) +vy*np.sin(state.yaw+2*np.pi/3) +self.r*omega
        self.v3 = vx*np.cos(state.yaw+np.pi/3) +vy*np.sin(state.yaw + np.pi/3) +self.r*omega
        #'''
    def get_v1(self):
        return self.v1
    def get_v2(self):
        return self.v2
    def get_v3(self):
        return self.v3
    def using_model(self, state, xref, yref, thref, index):
    	self.pidX.set_present(state.x)
    	self.pidY.set_present(state.y)
    	self.pidTh.set_present(state.yaw)

    	self.adjustmentX = self.pidX.run_pid(xref)
    	self.adjustmentY = self.pidY.run_pid(yref)
    	self.adjustmentTh = self.pidTh.run_pid(thref)

    	self.inverse_kinematics_model(state, self.adjustmentX, self.adjustmentY, self.adjustmentTh)

        #print("SetVelocity(get_v1()) = {}".format(self.get_v1()))
        #print("SetVelocity(get_v2()) = {}".format(self.get_v2()))
        #print("SetVelocity(get_v3()) = {}".format(self.get_v3()))
