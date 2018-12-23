import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

#'''
#%matplotlib notebook
import matplotlib.animation as animation
from matplotlib import animation
#'''
class game_class(object):
    """docstring for game_class."""
    def __init__(self, target, state, robot):
        self.target = target
        self.state = state
        self.robo = robot
    def run_through_the_forest(self):
        ##############################  making_ref  ################################
        ############################################################################
        new_index_for_bezier = []
        theta = 0#np.pi/4
        #set_start_point
        ssp=[-0.5,-0.5]
        #'''
        list_of_bezier_set1 = np.array([[0,0],[1.225+ssp[0],0.7+ssp[1]],[1.725+ssp[0],0.7+ssp[1]],[1.725+ssp[0],2+ssp[1]]], dtype=np.float)
        list_of_bezier_set2 = np.array([[1.725+ssp[0],2.000+ssp[1]],[1.725+ssp[0],2.500+ssp[1]],[0.775+ssp[0],3+ssp[1]],[0.775+ssp[0],3.5+ssp[1]]], dtype=np.float)
        list_of_bezier_set3 = np.array([[0.775+ssp[0],3.5+ssp[1]],[0.775+ssp[0],4+ssp[1]],[1.725+ssp[0],4.5+ssp[1]],[1.725+ssp[0],5+ssp[1]]], dtype=np.float)
        list_of_bezier_set4 = np.array([[1.725+ssp[0],5+ssp[1]],[1.725+ssp[0],5.5+ssp[1]],[1.225+ssp[0],6+ssp[1]],[1.225+ssp[0],6.5+ssp[1]]], dtype=np.float)
        #'''
        r_of_stateAlfa = 0.005

        npLOB, LOB, npNEW_LOB, NEW_LOB = self.target.making_target_value(list_of_bezier_set1, list_of_bezier_set2, list_of_bezier_set3, list_of_bezier_set4)
        ############################################################################
        ############################################################################
        model = '4ste'
        #model = '3omu'
        check = 1
        anime = 0
        if model=='4ste':
            if check == 0:
                print("len(LOB) = {}".format(len(LOB)))
                IND = np.arange(start = 0,stop = len(LOB), step = 1, dtype = int)
                for index in IND:
                    #self.state.update(self.robo.get_v1(), self.robo.get_v2(), self.robo.get_v3())
                    self.state.update(vell1=self.robo.get_v1(), vell2=self.robo.get_v2(), vell3=self.robo.get_v3(), vell4=self.robo.get_v4(), theta1=self.robo.get_theta1(), theta2=self.robo.get_theta2(), theta3=self.robo.get_theta3(), theta4=self.robo.get_theta2())
                    self.robo.using_model(self.state, npLOB.T[0][index], npLOB.T[1][index], theta, index)
                    if anime == 1:
                        if index==0:
                            plt.plot(self.state.x1, self.state.y1, marker="*")
                            plt.plot(self.state.x2, self.state.y2, marker="*")
                            plt.plot(self.state.x3, self.state.y3, marker="*")
                            plt.plot(self.state.x4, self.state.y4, marker="*")

                        elif index < len(LOB)/2:
                            plt.plot(self.state.x1, self.state.y1, marker="p", color="#ff9393")
                            plt.plot(self.state.x2, self.state.y2, marker="p", color="#ff93c9")
                            plt.plot(self.state.x3, self.state.y3, marker="p", color="#ff93ff")
                            plt.plot(self.state.x4, self.state.y4, marker="p", color="#c993ff")
                        else:
                            plt.plot(self.state.x1, self.state.y1, marker="o", color="#9393ff")
                            plt.plot(self.state.x2, self.state.y2, marker="o", color="#93c9ff")
                            plt.plot(self.state.x3, self.state.y3, marker="o", color="#93ffff")
                            plt.plot(self.state.x4, self.state.y4, marker="o", color="#93ffc9")
                        plt.pause(0.01)
                        plt.axis("equal")
                        plt.grid(True)
                        plt.show
            elif check == 1:
                print("len(NEW_LOB) = {}".format(len(NEW_LOB)))
                IND = np.arange(start = 0,stop = len(NEW_LOB), step = 1, dtype = int)
                for index in IND:
                    #self.state.update(self.robo.get_v1(), self.robo.get_v2(), self.robo.get_v3())
                    self.state.update(vell1=self.robo.get_v1(), vell2=self.robo.get_v2(), vell3=self.robo.get_v3(), vell4=self.robo.get_v4(), theta1=self.robo.get_theta1(), theta2=self.robo.get_theta2(), theta3=self.robo.get_theta3(), theta4=self.robo.get_theta2())
                    self.robo.using_model(self.state, npNEW_LOB.T[0][index], npNEW_LOB.T[1][index], theta, index)
                    if anime == 1:
                        if index==0:
                            plt.plot(self.state.x1, self.state.y1, marker="*")
                            plt.plot(self.state.x2, self.state.y2, marker="*")
                            plt.plot(self.state.x3, self.state.y3, marker="*")
                            plt.plot(self.state.x4, self.state.y4, marker="*")

                        elif index < len(LOB)/2:
                            plt.plot(self.state.x1, self.state.y1, marker="p", color="#ff9393")
                            plt.plot(self.state.x2, self.state.y2, marker="p", color="#ff93c9")
                            plt.plot(self.state.x3, self.state.y3, marker="p", color="#ff93ff")
                            plt.plot(self.state.x4, self.state.y4, marker="p", color="#c993ff")
                        else:
                            plt.plot(self.state.x1, self.state.y1, marker="o", color="#9393ff")
                            plt.plot(self.state.x2, self.state.y2, marker="o", color="#93c9ff")
                            plt.plot(self.state.x3, self.state.y3, marker="o", color="#93ffff")
                            plt.plot(self.state.x4, self.state.y4, marker="o", color="#93ffc9")
                        plt.pause(0.001)
                        plt.axis("equal")
                        plt.grid(True)
                        plt.show
        elif model=='3omu':
            if check == 0:
                print("len(LOB) = {}".format(len(LOB)))
                IND = np.arange(start = 0,stop = len(LOB), step = 1, dtype = int)
                for index in IND:
                    self.state.update(self.robo.get_v1(), self.robo.get_v2(), self.robo.get_v3())
                    self.robo.using_model(self.state, npLOB.T[0][index], npLOB.T[1][index], theta, index)
                    if anime == 1:
                        if index==0:
                            plt.plot(self.state.x, self.state.y, marker="*")
                            plt.plot(self.state.x+r_of_stateAlfa*np.sin(self.state.yaw), self.state.y+r_of_stateAlfa*np.cos(self.state.yaw), marker=".", color="#0AB721")
                        elif index < len(LOB)/2:
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
                    self.state.update(self.robo.get_v1(), self.robo.get_v2(), self.robo.get_v3())
                    self.robo.using_model(self.state, npNEW_LOB.T[0][index], npNEW_LOB.T[1][index], theta, index)
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
        else:
            print("model error")
    def run(self):
        #npLOB, LOB, npNEW_LOB, NEW_LOB = self.target.making_target_value_test_blue()
        npLOB, LOB, npNEW_LOB, NEW_LOB = self.target.making_target_value_test_red()
        plt.plot(npNEW_LOB.T[0],npNEW_LOB.T[1], marker="o", color="#B40404")
        plt.title("already arrange")
        ########################################################################
        ########################################################################
        ###########################     model     ##############################
        ########################################################################
        #'''
        ax = plt.axes()
        COUNT = np.arange(start=0, stop=1054, step=1, dtype= int)
        ssp=[-0.5,-0.5]
        for count in COUNT:
            r = patches.Rectangle(xy=(npNEW_LOB.T[0][count] -0.35,npNEW_LOB.T[1][count] -0.35), width=0.7, height=0.7, ec='#F5A9A9', fill=False)
            ax.add_patch(r)
            #c = patches.Circle(xy=(npNEW_LOB.T[0][count],npNEW_LOB.T[1][count]), radius=0.4, ec='#F5A9A9',fill=False)
            #ax.add_patch(c)
        ############################     field     #############################
        ########################################################################
        sotowaku = patches.Rectangle(xy=(-13.3+0.5,-0.5), width=13.3, height=10, ec='#FAAC58',fill=False)
        ax.add_patch(sotowaku)
        forest = patches.Rectangle(xy=(-2.45+0.5,-0.5), width=2.45, height=8, ec='#FAAC58',fill=False)
        ax.add_patch(forest)
        bridge = patches.Rectangle(xy=(-1.725 +0.5, 6.5 -0.5), width=1, height=1.5, ec='#FAAC58',fill=False)
        ax.add_patch(bridge)
        bri1 = patches.Circle(xy=(-1.725 +0.5, 6.5 -0.5), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(bri1)
        bri2 = patches.Circle(xy=(-1.725 +0.5, 6.5+1.5 -0.5), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(bri2)


        d = patches.Circle(xy=(-1*(1.225+ssp[0]),2+ssp[1]), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(d)
        e = patches.Circle(xy=(-1*(1.225+ssp[0]),3.5+ssp[1]), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(e)
        f = patches.Circle(xy=(-1*(1.225+ssp[0]),5+ssp[1]), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(f)
        #'''
        ########################################################################
        ########################################################################
        ########################################################################
        plt.axis("equal")
        plt.grid(True)
        plt.show()
        INDEX = np.arange(start=1, stop=len(npNEW_LOB)-1, step=1, dtype= int)
        #INDEX,len_INDEX = self.target.get_new_index_set()
        '''
        V = self.target.get_V()
        for index in INDEX:
            print("V[{}] = {}m/s".format(index,V[index]))
        '''
        '''#FF
        fig = plt.figure()
        ims = []
        INDEX = np.arange(start=1, stop=len(npNEW_LOB)-1, step=1, dtype= int)
        X = []
        Y = []
        x=0
        y=0
        vx=self.target.get_vx()
        vy=self.target.get_vy()
        alfa=self.target.get_alfa()
        V = self.target.get_V()
        #print("V = {}".format(V))
        for index in INDEX:
            x = x + vx[index] * 0.008
            y = y + vy[index] * 0.008
            X.append(x)
            Y.append(y)

            #vehi = np.matrix([[0.4, 0.4, -0.4, -0.4],[0.4, -0.4, -0.4, 0.4]])
            vehi = np.matrix([[0, 0.35, 0.35, -0.35, -0.35, 0],[0.7, 0.35, -0.35, -0.35, 0.35, 0.7]])
            Rot = np.matrix([[np.cos(-alfa[index]),-np.sin(-alfa[index])],[np.sin(-alfa[index]),np.cos(-alfa[index])]])
            STATE = [[x],[y]]
            newvehi = Rot * vehi + STATE
            img = plt.plot(X,Y,marker=".",color="#FAAC58") + plt.plot(newvehi[0,:],newvehi[1,:],marker="p",color="#FAAC58")

            plt.title("V = {}m/s".format(V[index]))
            #print("V = {}m/s".format(V[index]))
            #plt.title("V = "+ str(V[index])[:4])
            plt.axis("equal")
            plt.grid(True)
            ims.append(img)
        #plt.pause(0.01)
        ani = animation.ArtistAnimation(fig, ims, interval=8)
        ####
        ax = plt.axes()
        ############################     field     #############################
        ########################################################################
        sotowaku = patches.Rectangle(xy=(-13.3+0.5,-0.5), width=13.3, height=10, ec='#FAAC58',fill=False)
        ax.add_patch(sotowaku)
        forest = patches.Rectangle(xy=(-2.45+0.5,-0.5), width=2.45, height=8, ec='#FAAC58',fill=False)
        ax.add_patch(forest)
        bridge = patches.Rectangle(xy=(-1.725 +0.5, 6.5 -0.5), width=1, height=1.5, ec='#FAAC58',fill=False)
        ax.add_patch(bridge)
        bri1 = patches.Circle(xy=(-1.725 +0.5, 6.5 -0.5), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(bri1)
        bri2 = patches.Circle(xy=(-1.725 +0.5, 6.5+1.5 -0.5), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(bri2)


        d = patches.Circle(xy=(-1*(1.225+ssp[0]),2+ssp[1]), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(d)
        e = patches.Circle(xy=(-1*(1.225+ssp[0]),3.5+ssp[1]), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(e)
        f = patches.Circle(xy=(-1*(1.225+ssp[0]),5+ssp[1]), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(f)
        ########################################################################
        ########################################################################
        #'''

        plt.show()
        #ani.save("output.gif", writer="imagemagick")
        #'''
    def run_FF(self):
        pass
