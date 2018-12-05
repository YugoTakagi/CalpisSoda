import numpy as np

class synthesis_of_vector(object):
    """docstring for synthesis_of_vector."""
    alfa = 0
    stateX = 0
    stateY = 0
    def __init__(self):
        pass
    def using_algo(self, vell1, vell2, vell3):
        self.stateX = vell1*np.sin(5*np.pi/6 +self.alfa)+vell2*np.sin(3*np.pi/4 +self.alfa)+np.sin(np.pi/6 +self.alfa)
        self.stateY = vell1*np.cos(5*np.pi/6 +self.alfa)+vell2*np.cos(3*np.pi/4 +self.alfa)+np.cos(np.pi/6 +self.alfa)
        return self.stateX, self.stateY
    def get_alfa(self, alfa):
        self.alfa = alfa
