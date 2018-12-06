from pid import pid
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
    r = 0.20

    sqrt3 = np.sqrt(3)
    xsta = 0
    ysta = 0
    thsta = 0
    def __init__(self):
    	#//+++++PID GAIN SET+++++//
    	self.pidX.set_gain(1,0,0.3)
    	self.pidY.set_gain(1,0,0.3)
    	self.pidTh.set_gain(1,0,0)
    	#//++++++++++++++++++++++//
        pass
        #sups 3omu, self).__init__()
    def inverse_kinematics_model(self, vx, vy, theta, alfa):
        #4-omuni no inverse_kinematics_model
        self.enlargement_vx = vx*np.cos(alfa) + vy*np.sin(alfa)
        self.enlargement_vy = vx*np.sin(alfa) + vy*np.cos(alfa)
        self.v1 = 1/2*self.enlargement_vx - self.sqrt3/2*self.enlargement_vy -self.r*theta
        self.v2 = -1*self.enlargement_vx - 0*self.enlargement_vy -self.r*theta
        self.v3 = 1/2*self.enlargement_vx + self.sqrt3/2*self.enlargement_vy -self.r*theta
    def get_v1(self):
        return self.v1
    def get_v2(self):
        return self.v2
    def get_v3(self):
        return self.v3
    def set_state(self, xsta, ysta, thsta):
        self.xsta = xsta
        self.ysta = ysta
        self.thsta = thsta
    def using_model(self, xref, yref, thref, index):
    	self.pidX.set_present(self.xsta)
    	self.pidY.set_present(self.ysta)
    	self.pidTh.set_present(self.thsta)

    	self.adjustmentX = self.pidX.run_pid(xref)
    	self.adjustmentY = self.pidY.run_pid(yref)
    	self.adjustmentTh = self.pidTh.run_pid(thref)

    	self.inverse_kinematics_model(self.adjustmentX, self.adjustmentY, self.adjustmentTh, self.thsta)#theta to alfa no tigai ga wakaranai.

        #print("SetVelocity(get_v1()) = {}".format(self.get_v1()))
        #print("SetVelocity(get_v2()) = {}".format(self.get_v2()))
        #print("SetVelocity(get_v3()) = {}".format(self.get_v3()))
