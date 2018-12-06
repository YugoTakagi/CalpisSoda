import numpy as np

class synthesis_of_vector(object):
    """docstring for synthesis_of_vector."""
    alfa = 0
    stateX = 0
    stateY = 0
    stateX_of_alfa = 0
    stateY_of_alfa = 0
    r = 0.20
    def __init__(self):
        pass
    def using_algo(self, vell1, vell2, vell3):
        self.stateX += vell1*np.sin(5*np.pi/6 +self.alfa)+vell2*np.sin(3*np.pi/2 +self.alfa)+np.sin(np.pi/6 +self.alfa)
        self.stateY += vell1*np.cos(5*np.pi/6 +self.alfa)+vell2*np.cos(3*np.pi/2 +self.alfa)+np.cos(np.pi/6 +self.alfa)
        #self.stateX = vell1/2 +vell2*-1 +vell3/2
        #self.stateY = vell1*-np.sqrt(3)/2 +vell2*0 +vell3*np.sqrt(3)/2
        self.alfa += (vell1 + vell2 + vell3)/self.r
        return self.stateX*0.08, self.stateY*0.08, self.alfa*0.08
    def get_alfa(self, alfa):
        self.alfa = alfa
    def using_alfa(self):
        r_of_alfa = 0.2

        self.stateX_of_alfa += r_of_alfa*np.sin(alfa)
        self.stateY_of_alfa += r_of_alfa*np.cos(alfa)
        return self.stateX_of_alfa, self.stateY_of_alfa
