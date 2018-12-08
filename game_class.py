import numpy as np
import matplotlib.pyplot as plt

class game_class(object):
    """docstring for game_class."""
    def __init__(self, target, state, robot):
        self.target = target
        self.state = state
        self.omu3 = robot
    def run_through_the_forest(self):
        ##############################  making_ref  ################################
        ############################################################################
        new_index_for_bezier = []
        theta = 0#np.pi/4
        list_of_bezier_set1 = np.array([[0,0],[1.225,0],[1.225+0.5,2.000-1.225],[1.225+0.500,2.000]], dtype=np.float)
        list_of_bezier_set2 = np.array([[1.225+0.500,2.000],[1.225+0.500,2.000+0.500],[1.225-0.500,2.000+1.500-0.500],[1.225-0.500,2.000+1.500]], dtype=np.float)
        list_of_bezier_set3 = np.array([[1.225-0.500,2.000+1.500],[1.225-0.500,2.000+1.500+0.500],[1.225+0.500,2.000+1.500+1.500-0.500],[1.225+0.500,2.000+1.500+1.500]], dtype=np.float)
        list_of_bezier_set4 = np.array([[1.225+0.500,2.000+1.500+1.500],[1.225+0.500,2.000+1.500+1.500+0.500],[1.225,2.000+1.500+1.500+1.500-0.500],[1.225,2.000+1.500+1.500+1.500]], dtype=np.float)
        r_of_stateAlfa = 0.005
        npLOB, LOB, npNEW_LOB, NEW_LOB = self.target.making_target_value(list_of_bezier_set1, list_of_bezier_set2, list_of_bezier_set3, list_of_bezier_set4)
        ############################################################################
        ############################################################################
        #plt.plot(npNEW_LOB.T[0], npNEW_LOB.T[1], marker=".")
        print('npNEW_LOB.T[0] = {}'.format(npNEW_LOB.T[0]))
        check = 0
        if check == 0:
            print("len(LOB) = {}".format(len(LOB)))
            IND = np.arange(start = 0,stop = len(LOB), step = 1, dtype = int)
            for index in IND:
                self.state.update(self.omu3.get_v1(), self.omu3.get_v2(), self.omu3.get_v3())
                self.omu3.using_model(self.state, npLOB.T[0][index], npLOB.T[1][index], theta, index)
                if index==0:
                    plt.plot(self.state.x, self.state.y, marker="*")
                    plt.plot(self.state.x+r_of_stateAlfa*np.sin(self.state.yaw), self.state.y+r_of_stateAlfa*np.cos(self.state.yaw), marker=".", color="#0AB721")
                elif index < len(NEW_LOB)/2:
                    plt.plot(self.state.x, self.state.y, marker="p", color="#4278C5")
                    plt.plot(self.state.x+r_of_stateAlfa*np.sin(self.state.yaw), self.state.y+r_of_stateAlfa*np.cos(self.state.yaw), marker=".", color="#0AB721")
                    r_of_stateAlfa += 0.0002
                else:
                    plt.plot(self.state.x, self.state.y, marker="o", color="#F56260")
                    plt.plot(self.state.x+r_of_stateAlfa*np.sin(self.state.yaw), self.state.y+r_of_stateAlfa*np.cos(self.state.yaw), marker=".", color="#0AB721")
                    r_of_stateAlfa += 0.0002
                plt.pause(0.01)
                plt.axis("equal")
                plt.grid(True)
                plt.show
        if check==1:
            print("len(NEW_LOB) = {}".format(len(NEW_LOB)))
            plt.plot(0, 0, marker="$start$", markersize="20")
            IND = np.arange(start = 0,stop = len(NEW_LOB), step = 1, dtype = int)
            plt.plot(npNEW_LOB.T[0],npNEW_LOB.T[1], marker="*", color="#4278C5")
            plt.axis("equal")
            plt.grid(True)
            plt.show()
            for index in IND:
                self.state.update(self.omu3.get_v1(), self.omu3.get_v2(), self.omu3.get_v3())
                self.omu3.using_model(self.state, npNEW_LOB.T[0][index], npNEW_LOB.T[1][index], theta, index)
                if index==0:
                    plt.plot(self.state.x, self.state.y, marker="*")
                    plt.plot(self.state.x+r_of_stateAlfa*np.sin(self.state.yaw), self.state.y+r_of_stateAlfa*np.cos(self.state.yaw), marker=".", color="#0AB721")
                elif index < len(NEW_LOB)/2:
                    plt.plot(self.state.x, self.state.y, marker="p", color="#4278C5")
                    plt.plot(self.state.x+r_of_stateAlfa*np.sin(self.state.yaw), self.state.y+r_of_stateAlfa*np.cos(self.state.yaw), marker=".", color="#0AB721")
                    r_of_stateAlfa += 0.0002
                else:
                    plt.plot(self.state.x, self.state.y, marker="o", color="#F56260")
                    plt.plot(self.state.x+r_of_stateAlfa*np.sin(self.state.yaw), self.state.y+r_of_stateAlfa*np.cos(self.state.yaw), marker=".", color="#0AB721")
                    r_of_stateAlfa += 0.0002
                plt.pause(0.01)
                plt.axis("equal")
                plt.grid(True)
                plt.show
