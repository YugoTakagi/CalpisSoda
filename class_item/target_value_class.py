#from color_class import pycolor as pc
import numpy as np
import matplotlib.pyplot as plt
import csv
from class_item.target_item.bezier_class import bezier

class target_value_class(object):
    """docstring for target_value_class."""
    V = []
    vx = []
    vy = []
    alfa = []
    omega = []
    x = []
    y = []
    theta = []

    new_index_for_bezier=[]
    len_new_index_for_bezier=0
    def __init__(self, bez, tvp, arg):
        self.bez = bez
        self.tvp = tvp
        self.arg = arg
    def get_V(self):
        return self.V
    def get_vx(self):
        return self.vx
    def get_vy(self):
        return self.vy
    def get_alfa(self):
        return self.alfa
    def get_new_index_set(self):
        return self.new_index_for_bezier, self.len_new_index_for_bezier
    def making_vx_and_vy(self,V,ALFA,time):
        self.V = V
        arange_time = np.arange(start=0, stop=time-1, step=1, dtype= int)
        for index in arange_time:#linspace_time:
            if (index - 1) <= 0:
                self.vx.append(V[index] * np.sin(ALFA[index]))
                self.vy.append(V[index] * np.cos(ALFA[index]))
                #print("index = {}".format(index))
            else:
                self.vx.append(V[index] * np.sin(ALFA[index-1]))
                self.vy.append(V[index] * np.cos(ALFA[index-1]))
                #print("index = {}".format(index))
    def making_target_value(self, list_of_bezier1, list_of_bezier2, list_of_bezier3, list_of_bezier4):
        nplist_of_bezier1, list_of_bezier1 = self.bez.bezier_making(list_of_bezier1)
        nplist_of_bezier2, list_of_bezier2 = self.bez.bezier_making(list_of_bezier2)
        nplist_of_bezier3, list_of_bezier3 = self.bez.bezier_making(list_of_bezier3)
        nplist_of_bezier4, list_of_bezier4 = self.bez.bezier_making(list_of_bezier4)

        LOB = []
        LOB.extend(list_of_bezier1)
        LOB.extend(list_of_bezier2)
        LOB.extend(list_of_bezier3)
        LOB.extend(list_of_bezier4)
        npLOB = np.array(LOB)
        plt.plot(npLOB.T[0],npLOB.T[1], marker="*", color="#4278C5")
        plt.axis("equal")
        plt.grid(True)
        plt.show()
        with open('csv_item/x_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(npLOB.T[0])
        with open('csv_item/y_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(npLOB.T[1])
        self.tvp.making_curve_length(npLOB.T[0], npLOB.T[1])
        TVP_of_S = self.tvp.making_TVP(npLOB.T[0], npLOB.T[1], 2.0, 0.0, 0.0, 0.0, 0.0)
        self.tvp.deside()
        plt.show()

        self.new_index_for_bezier, self.len_new_index_for_bezier = self.arg.arrange(npLOB.T[0], npLOB.T[1], TVP_of_S)
        npNEW_LOB, NEW_LOB = self.bez.new_bezier_plt(LOB, self.new_index_for_bezier, self.len_new_index_for_bezier)

        return npLOB, LOB,npNEW_LOB, NEW_LOB
    def making_target_value_test_blue(self):
        #bez = bezier(80)
    	#bez5 = bezier(300)
        new_index_for_bezier = []
        theta = 0#np.pi/4
    	#set_start_point
        ssp=[-0.5,-0.5]
        list_of_bezier_set1 = np.array([[0,0],[1.225+ssp[0],0.7+ssp[1]],[1.725+ssp[0],0.7+ssp[1]],[1.725+ssp[0],2+ssp[1]]], dtype=np.float)
        list_of_bezier_set2 = np.array([[1.725+ssp[0],2.000+ssp[1]],[1.725+ssp[0],2.500+ssp[1]],[0.775+ssp[0],3+ssp[1]],[0.775+ssp[0],3.5+ssp[1]]], dtype=np.float)
        list_of_bezier_set3 = np.array([[0.775+ssp[0],3.5+ssp[1]],[0.775+ssp[0],4+ssp[1]],[1.725+ssp[0],4.5+ssp[1]],[1.725+ssp[0],5+ssp[1]]], dtype=np.float)
        list_of_bezier_set4 = np.array([[1.725+ssp[0],5+ssp[1]],[1.725+ssp[0],5.5+ssp[1]],[1.225+ssp[0],6+ssp[1]],[1.225+ssp[0],6.5+ssp[1]]], dtype=np.float)
        nplist_of_bezier1, list_of_bezier1 = self.bez.bezier_making(list_of_bezier_set1)
        nplist_of_bezier2, list_of_bezier2 = self.bez.bezier_making(list_of_bezier_set2)
        nplist_of_bezier3, list_of_bezier3 = self.bez.bezier_making(list_of_bezier_set3)
        nplist_of_bezier4, list_of_bezier4 = self.bez.bezier_making(list_of_bezier_set4)
        LOB = []
        LOB.extend(list_of_bezier1)
        LOB.extend(list_of_bezier2)
        LOB.extend(list_of_bezier3)
        LOB.extend(list_of_bezier4)
        npLOB = np.array(LOB)
        plt.plot(npLOB.T[0],npLOB.T[1], marker="o", color="#4278C5")

        list_of_bridge_set = np.array([[1.225+ssp[0],6.5+ssp[1]],[1.225+ssp[0],6.5+ssp[1]],[1.225+ssp[0],6.5+ssp[1] +1.5],[1.225+ssp[0],6.5+ssp[1] +1.5]], dtype=np.float)
        nplist_of_bridge, list_of_bridge = self.bez.bezier_making(list_of_bridge_set)
        plt.plot(nplist_of_bridge.T[0],nplist_of_bridge.T[1], marker="o", color="#4278C5")

        list_of_bezier_set5 = np.array([[1.225+ssp[0], 6.5+ssp[1] +1.0],[1.225+ssp[0], 6.5+ssp[1] +1.0 +3],[1.225+ssp[0]+5,6.5+ssp[1] +0.2],[1.225+ssp[0] +1.25 +9.95 +2.0, 6.5+ssp[1] +0.4]], dtype=np.float)
        #nplist_of_bezier5, list_of_bezier5 = bez5.bezier_making(list_of_bezier_set5)
        nplist_of_bezier5, list_of_bezier5 = self.bez.bezier_making(list_of_bezier_set5)
        plt.plot(nplist_of_bezier5.T[0],nplist_of_bezier5.T[1], marker="o", color="#4278C5")
        plt.axis("equal")
        plt.grid((True))
        plt.show()


        LIST = []
        LIST.extend(LOB)
        LIST.extend(list_of_bridge)
        LIST.extend(list_of_bezier5)
        npLIST = np.array(LIST)
        #print('npLIST = {}'.format(npLIST))
        plt.plot(npLIST.T[0],npLIST.T[1], marker="o", color="#F7BE81")
        plt.axis("equal")
        plt.grid((True))
        plt.show()

        self.tvp.making_curve_length(npLIST.T[0], npLIST.T[1])
        TVP_of_S = self.tvp.making_TVP(npLIST.T[0], npLIST.T[1], 2.0, 0.0, 0.0, 0.0, 0.0)
        self.tvp.deside()
        plt.show()

    	#self.arg.arrange(npLIST.T[0], npLIST.T[1], TVP_of_S)
        new_index_for_bezier, len_new_index_for_bezier = self.arg.arrange(npLIST.T[0], npLIST.T[1], TVP_of_S)
        npNEW_LOB, NEW_LOB = self.bez.new_bezier_plt(LIST, new_index_for_bezier, len_new_index_for_bezier)

        return npLOB, LOB,npNEW_LOB, NEW_LOB
    def making_target_value_test_red(self):
        #bez = bezier(80)
        #bez5 = bezier(500000)
        ########################################################################
        ########################################################################
        ######################     maiking X REF     ###########################
        ########################################################################
        ########################################################################
<<<<<<< HEAD
        #bez1 = bezier(200000)
        bez1 = bezier(1000)
=======
        bez1 = bezier(200000)
>>>>>>> four_wheel_steering
        new_index_for_bezier = []
        theta = 0#np.pi/4
        #set_start_point
        ssp=[-0.5,-0.5]
        '''#########################    1st    ################################
        ################################ X #####################################
        list_of_bezier_set1 = np.array([[0,0],[-1*(1.225+ssp[0]),0.7+ssp[1]],[-1*(1.725+ssp[0]),0.7+ssp[1]],[-1*(1.725+ssp[0]),2+ssp[1]]], dtype=np.float)
        list_of_bezier_set2 = np.array([[-1*(1.725+ssp[0]),2.000+ssp[1]],[-1*(1.725+ssp[0]),2.500+ssp[1]],[-1*(0.775+ssp[0]),3+ssp[1]],[-1*(0.725+ssp[0]),3.5+ssp[1]]], dtype=np.float)
        list_of_bezier_set3 = np.array([[-1*(0.725+ssp[0]),3.5+ssp[1]],[-1*(0.775+ssp[0]),4+ssp[1]],[-1*(1.725+ssp[0]),4.5+ssp[1]],[-1*(1.725+ssp[0]),5+ssp[1]]], dtype=np.float)
        list_of_bezier_set4 = np.array([[-1*(1.725+ssp[0]),5+ssp[1]],[-1*(1.725+ssp[0]),5.5+ssp[1]],[-1*(1.225+ssp[0]),6+ssp[1]],[-1*(1.225+ssp[0]),6.5+ssp[1]]], dtype=np.float)
        ########################################################################
        #'''####################################################################

        ############################     2nd     ###############################
        ################################# O ####################################
        list_of_bezier_set1 = np.array([[0,0],[-1*(1.225+ssp[0]),0.7+ssp[1]],[-1*(1.95+ssp[0]),0.7+ssp[1]],[-1*(1.95+ssp[0]),2+ssp[1]]], dtype=np.float)
        list_of_bezier_set2 = np.array([[-1*(1.95+ssp[0]),2.000+ssp[1]],[-1*(1.95+ssp[0]),2.500+ssp[1]],[-1*(0.51+ssp[0]),3+ssp[1]],[-1*(0.51+ssp[0]),3.5+ssp[1]]], dtype=np.float)
        list_of_bezier_set3 = np.array([[-1*(0.51+ssp[0]),3.5+ssp[1]],[-1*(0.51+ssp[0]),4+ssp[1]],[-1*(1.95+ssp[0]),4.5+ssp[1]],[-1*(1.95+ssp[0]),5+ssp[1]]], dtype=np.float)
        list_of_bezier_set4 = np.array([[-1*(1.95+ssp[0]),5+ssp[1]],[-1*(1.95+ssp[0]),5.5+ssp[1]],[-1*(1.225+ssp[0]),5.5+ssp[1]],[-1*(1.225+ssp[0]),6.5+ssp[1]]], dtype=np.float)
        ########################################################################
        ########################################################################

        #nplist_of_bezier1, list_of_bezier1 = self.bez.bezier_making(list_of_bezier_set1)
        nplist_of_bezier1, list_of_bezier1 = bez1.bezier_making(list_of_bezier_set1)
        nplist_of_bezier2, list_of_bezier2 = self.bez.bezier_making(list_of_bezier_set2)
        nplist_of_bezier3, list_of_bezier3 = self.bez.bezier_making(list_of_bezier_set3)
        nplist_of_bezier4, list_of_bezier4 = self.bez.bezier_making(list_of_bezier_set4)
        LOB = []
        LOB.extend(list_of_bezier1)
        LOB.extend(list_of_bezier2)
        LOB.extend(list_of_bezier3)
        LOB.extend(list_of_bezier4)
        npLOB = np.array(LOB)
        plt.plot(npLOB.T[0],npLOB.T[1], marker="o", color="#FA5858")

        list_of_bridge_set = np.array([[-1*(1.225+ssp[0]),6.5+ssp[1]],[-1*(1.225+ssp[0]),6.5+ssp[1]],[-1*(1.225+ssp[0]),6.5+ssp[1] +1.5],[-1*(1.225+ssp[0]),6.5+ssp[1] +1.5]], dtype=np.float)
        nplist_of_bridge, list_of_bridge = self.bez.bezier_making(list_of_bridge_set)
        plt.plot(nplist_of_bridge.T[0],nplist_of_bridge.T[1], marker="o", color="#FA5858")

        list_of_bezier_set5 = np.array([[-1*(1.225+ssp[0]), 6.5+ssp[1] +1.5],[-1*(1.225+ssp[0]), 6.5+ssp[1] +1.5 +2],[-1*(1.225+ssp[0]+1.25),6.5+ssp[1] +1.5 +0.4],[-1*(1.225+ssp[0] +1.25 +2.0 +0.97), 6.5+ssp[1] +1.5 +0.5]], dtype=np.float)
        #farst#list_of_bezier_set5 = np.array([[-1*(1.225+ssp[0]), 6.5+ssp[1] +1.0],[-1*(1.225+ssp[0]), 6.5+ssp[1] +1.0 +3],[-1*(1.225+ssp[0]+5),6.5+ssp[1] +0.2],[-1*(1.225+ssp[0] +1.25 +9.95 +2.0), 6.5+ssp[1] +0.4]], dtype=np.float)
        #nplist_of_bezier5, list_of_bezier5 = bez5.bezier_making(list_of_bezier_set5)
        nplist_of_bezier5, list_of_bezier5 = self.bez.bezier_making(list_of_bezier_set5)
        plt.plot(nplist_of_bezier5.T[0],nplist_of_bezier5.T[1], marker="o", color="#FA5858")
        '''#############################################################################'''
        list_of_bezier_set6 = np.array([[-1*(1.225+ssp[0] +1.25 +2.0 +0.97), 6.5+ssp[1] +1.5 +0.5],[-1*(1.225+ssp[0] +1.25 +2.0 +0.97 -2.5), 6.5+ssp[1] +1.5 +0.5 +0.5],[-1*(1.225+ssp[0] +1.25 +2.0 +0.97 -2.0), 6.5+ssp[1] +1.5 +0.5 -4.0 +2.0],[-1*(1.225+ssp[0] +1.25 +2.0 +0.97 -2.0), 6.5+ssp[1] +1.5 +0.5 -4.0]], dtype=np.float)
        nplist_of_bezier6, list_of_bezier6 = self.bez.bezier_making(list_of_bezier_set6)
        plt.plot(nplist_of_bezier6.T[0],nplist_of_bezier6.T[1], marker="o", color="#FA5858")
        '''#############################################################################'''
        plt.axis("equal")
        plt.grid((True))
        plt.title("ba ra ba ra")
        plt.show()


        LIST = []
        LIST.extend(LOB)
        LIST.extend(list_of_bridge)
        LIST.extend(list_of_bezier5)
        '''########################################################'''
        #LIST.extend(list_of_bezier6)
        '''########################################################'''
        npLIST = np.array(LIST)
        plt.plot(npLIST.T[0],npLIST.T[1], marker="o", color="#F7BE81")
        plt.axis("equal")
        plt.grid((True))
        plt.title("LIST")
        plt.show()

        self.tvp.making_curve_length(npLIST.T[0], npLIST.T[1])
        TVP_of_S = self.tvp.making_TVP(npLIST.T[0], npLIST.T[1], 2.0, 0.0, 0.0, 0.0, 0.0)
        self.tvp.deside()
        plt.show()
        new_index_for_bezier, len_new_index_for_bezier = self.arg.arrange(npLIST.T[0], npLIST.T[1], TVP_of_S)
        npNEW_LOB, NEW_LOB = self.bez.new_bezier_plt(LIST, new_index_for_bezier, len_new_index_for_bezier)
        ########################################################################
        ########################################################################
        ########################################################################
        ########################################################################
        ########################################################################



        ########################################################################
        ########################################################################
        ######################     making V REF     ############################
        ########################################################################
        ########################################################################
        self.alfa = self.tvp.making_angle(npNEW_LOB,len(npNEW_LOB))
        self.making_vx_and_vy(self.tvp.get_V(),self.alfa,len(npNEW_LOB))
        with open('csv_item/vx_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(self.vx)
        with open('csv_item/vy_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(self.vy)
        with open('csv_item/alfa_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(self.alfa)
        ########################################################################
        ########################################################################
        ########################################################################
        ########################################################################
        ########################################################################
        return npLOB, LOB,npNEW_LOB, NEW_LOB
    def making_target_value_test_red_nozaki(self):
        #bez = bezier(80)
        #bez5 = bezier(500000)
        ########################################################################
        ########################################################################
        ######################     maiking X REF     ###########################
        ########################################################################
        ########################################################################
        #bez1 = bezier(200000)
        bez1 = bezier(1000)
        new_index_for_bezier = []
        theta = 0#np.pi/4
        #set_start_point
        ssp=[-0.5,-0.5]
        '''#########################    1st    ################################
        ################################ X #####################################
        list_of_bezier_set1 = np.array([[0,0],[-1*(1.225+ssp[0]),0.7+ssp[1]],[-1*(1.725+ssp[0]),0.7+ssp[1]],[-1*(1.725+ssp[0]),2+ssp[1]]], dtype=np.float)
        list_of_bezier_set2 = np.array([[-1*(1.725+ssp[0]),2.000+ssp[1]],[-1*(1.725+ssp[0]),2.500+ssp[1]],[-1*(0.775+ssp[0]),3+ssp[1]],[-1*(0.725+ssp[0]),3.5+ssp[1]]], dtype=np.float)
        list_of_bezier_set3 = np.array([[-1*(0.725+ssp[0]),3.5+ssp[1]],[-1*(0.775+ssp[0]),4+ssp[1]],[-1*(1.725+ssp[0]),4.5+ssp[1]],[-1*(1.725+ssp[0]),5+ssp[1]]], dtype=np.float)
        list_of_bezier_set4 = np.array([[-1*(1.725+ssp[0]),5+ssp[1]],[-1*(1.725+ssp[0]),5.5+ssp[1]],[-1*(1.225+ssp[0]),6+ssp[1]],[-1*(1.225+ssp[0]),6.5+ssp[1]]], dtype=np.float)
        ########################################################################
        #'''####################################################################

        ############################     2nd     ###############################
        ################################# O ####################################
        list_of_bezier_set1 = np.array([[0,0],[0,1.4],[-1.43,0.1],[-1.43,1.5]], dtype=np.float)
        list_of_bezier_set2 = np.array([[-1.43,1.5],[-1.43,2.9],[-0.01,1.6],[-0.01,3.0]], dtype=np.float)
        list_of_bezier_set3 = np.array([[-0.01,3.0],[-0.01,4.4],[-1.43,3.1],[-1.43,4.5]], dtype=np.float)
        list_of_bezier_set4 = np.array([[-1.43,4.5],[-1.43,5.9],[-0.725,4.6],[-0.725,6.0]], dtype=np.float)
        ########################################################################
        ########################################################################

        #nplist_of_bezier1, list_of_bezier1 = self.bez.bezier_making(list_of_bezier_set1)
        nplist_of_bezier1, list_of_bezier1 = bez1.bezier_making(list_of_bezier_set1)
        nplist_of_bezier2, list_of_bezier2 = self.bez.bezier_making(list_of_bezier_set2)
        nplist_of_bezier3, list_of_bezier3 = self.bez.bezier_making(list_of_bezier_set3)
        nplist_of_bezier4, list_of_bezier4 = self.bez.bezier_making(list_of_bezier_set4)
        LOB = []
        LOB.extend(list_of_bezier1)
        LOB.extend(list_of_bezier2)
        LOB.extend(list_of_bezier3)
        LOB.extend(list_of_bezier4)
        npLOB = np.array(LOB)
        plt.plot(npLOB.T[0],npLOB.T[1], marker="o", color="#FA5858")

        list_of_bridge_set = np.array([[-1*(1.225+ssp[0]),6.5+ssp[1]],[-1*(1.225+ssp[0]),6.5+ssp[1]],[-1*(1.225+ssp[0]),6.5+ssp[1] +1.5],[-1*(1.225+ssp[0]),6.5+ssp[1] +1.5]], dtype=np.float)
        nplist_of_bridge, list_of_bridge = self.bez.bezier_making(list_of_bridge_set)
        plt.plot(nplist_of_bridge.T[0],nplist_of_bridge.T[1], marker="o", color="#FA5858")

        list_of_bezier_set5 = np.array([[-1*(1.225+ssp[0]), 6.5+ssp[1] +1.5],[-1*(1.225+ssp[0]), 6.5+ssp[1] +1.5 +2],[-1*(1.225+ssp[0]+1.25),6.5+ssp[1] +1.5 +0.4],[-1*(1.225+ssp[0] +1.25 +2.0 +0.97), 6.5+ssp[1] +1.5 +0.5]], dtype=np.float)
        #farst#list_of_bezier_set5 = np.array([[-1*(1.225+ssp[0]), 6.5+ssp[1] +1.0],[-1*(1.225+ssp[0]), 6.5+ssp[1] +1.0 +3],[-1*(1.225+ssp[0]+5),6.5+ssp[1] +0.2],[-1*(1.225+ssp[0] +1.25 +9.95 +2.0), 6.5+ssp[1] +0.4]], dtype=np.float)
        #nplist_of_bezier5, list_of_bezier5 = bez5.bezier_making(list_of_bezier_set5)
        nplist_of_bezier5, list_of_bezier5 = self.bez.bezier_making(list_of_bezier_set5)
        plt.plot(nplist_of_bezier5.T[0],nplist_of_bezier5.T[1], marker="o", color="#FA5858")
        '''#############################################################################'''
        list_of_bezier_set6 = np.array([[-1*(1.225+ssp[0] +1.25 +2.0 +0.97), 6.5+ssp[1] +1.5 +0.5],[-1*(1.225+ssp[0] +1.25 +2.0 +0.97 -2.5), 6.5+ssp[1] +1.5 +0.5 +0.5],[-1*(1.225+ssp[0] +1.25 +2.0 +0.97 -2.0), 6.5+ssp[1] +1.5 +0.5 -4.0 +2.0],[-1*(1.225+ssp[0] +1.25 +2.0 +0.97 -2.0), 6.5+ssp[1] +1.5 +0.5 -4.0]], dtype=np.float)
        nplist_of_bezier6, list_of_bezier6 = self.bez.bezier_making(list_of_bezier_set6)
        plt.plot(nplist_of_bezier6.T[0],nplist_of_bezier6.T[1], marker="o", color="#FA5858")
        '''#############################################################################'''
        plt.axis("equal")
        plt.grid((True))
        plt.title("ba ra ba ra")
        plt.show()


        LIST = []
        LIST.extend(LOB)
        LIST.extend(list_of_bridge)
        LIST.extend(list_of_bezier5)
        '''########################################################'''
        LIST.extend(list_of_bezier6)
        '''########################################################'''
        npLIST = np.array(LIST)
        plt.plot(npLIST.T[0],npLIST.T[1], marker="o", color="#F7BE81")
        plt.axis("equal")
        plt.grid((True))
        plt.title("LIST")
        plt.show()

        self.tvp.making_curve_length(npLIST.T[0], npLIST.T[1])
        TVP_of_S = self.tvp.making_TVP(npLIST.T[0], npLIST.T[1], 2.0, 0.0, 0.0, 0.0, 0.0)
        self.tvp.deside()
        plt.show()
        new_index_for_bezier, len_new_index_for_bezier = self.arg.arrange(npLIST.T[0], npLIST.T[1], TVP_of_S)
        npNEW_LOB, NEW_LOB = self.bez.new_bezier_plt(LIST, new_index_for_bezier, len_new_index_for_bezier)
        ########################################################################
        ########################################################################
        ########################################################################
        ########################################################################
        ########################################################################



        ########################################################################
        ########################################################################
        ######################     making V REF     ############################
        ########################################################################
        ########################################################################
        self.alfa = self.tvp.making_angle(npNEW_LOB,len(npNEW_LOB))
        self.making_vx_and_vy(self.tvp.get_V(),self.alfa,len(npNEW_LOB))
        with open('csv_item/vx_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(self.vx)
        with open('csv_item/vy_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(self.vy)
        with open('csv_item/alfa_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(self.alfa)
        ########################################################################
        ########################################################################
        ########################################################################
        ########################################################################
        ########################################################################
        return npLOB, LOB,npNEW_LOB, NEW_LOB
    def making_target_value_video_forest_red(self):
        ########################################################################
        ########################################################################
        ######################     maiking X REF     ###########################
        ########################################################################
        ########################################################################
        new_index_for_bezier = []
        theta = 0#np.pi/4
        #set_start_point
        ssp=[-0.5,-0.5]
        '''#########################    1st    ################################
        ################################ X #####################################
        list_of_bezier_set1 = np.array([[0,0],[-1*(1.225+ssp[0]),0.7+ssp[1]],[-1*(1.725+ssp[0]),0.7+ssp[1]],[-1*(1.725+ssp[0]),2+ssp[1]]], dtype=np.float)
        list_of_bezier_set2 = np.array([[-1*(1.725+ssp[0]),2.000+ssp[1]],[-1*(1.725+ssp[0]),2.500+ssp[1]],[-1*(0.775+ssp[0]),3+ssp[1]],[-1*(0.725+ssp[0]),3.5+ssp[1]]], dtype=np.float)
        list_of_bezier_set3 = np.array([[-1*(0.725+ssp[0]),3.5+ssp[1]],[-1*(0.775+ssp[0]),4+ssp[1]],[-1*(1.725+ssp[0]),4.5+ssp[1]],[-1*(1.725+ssp[0]),5+ssp[1]]], dtype=np.float)
        list_of_bezier_set4 = np.array([[-1*(1.725+ssp[0]),5+ssp[1]],[-1*(1.725+ssp[0]),5.5+ssp[1]],[-1*(1.225+ssp[0]),6+ssp[1]],[-1*(1.225+ssp[0]),6.5+ssp[1]]], dtype=np.float)
        ########################################################################
        #'''####################################################################

        ############################     2nd     ###############################
        ################################# O ####################################
        list_of_bezier_set1 = np.array([[0,0],[-1*(1.225+ssp[0]),0.7+ssp[1]],[-1*(1.95+ssp[0]),0.7+ssp[1]],[-1*(1.95+ssp[0]),2+ssp[1]]], dtype=np.float)
        list_of_bezier_set2 = np.array([[-1*(1.95+ssp[0]),2.000+ssp[1]],[-1*(1.95+ssp[0]),2.500+ssp[1]],[-1*(0.51+ssp[0]),3+ssp[1]],[-1*(0.51+ssp[0]),3.5+ssp[1]]], dtype=np.float)
        list_of_bezier_set3 = np.array([[-1*(0.51+ssp[0]),3.5+ssp[1]],[-1*(0.51+ssp[0]),4+ssp[1]],[-1*(1.95+ssp[0]),4.5+ssp[1]],[-1*(1.95+ssp[0]),5+ssp[1]]], dtype=np.float)
        list_of_bezier_set4 = np.array([[-1*(1.95+ssp[0]),5+ssp[1]],[-1*(1.95+ssp[0]),5.5+ssp[1]],[-1*(1.225+ssp[0]),5.5+ssp[1]],[-1*(1.225+ssp[0]),6.5+ssp[1]]], dtype=np.float)
        ########################################################################
        ########################################################################

        nplist_of_bezier1, list_of_bezier1 = self.bez.bezier_making(list_of_bezier_set1)
        nplist_of_bezier2, list_of_bezier2 = self.bez.bezier_making(list_of_bezier_set2)
        nplist_of_bezier3, list_of_bezier3 = self.bez.bezier_making(list_of_bezier_set3)
        nplist_of_bezier4, list_of_bezier4 = self.bez.bezier_making(list_of_bezier_set4)
        LOB = []
        LOB.extend(list_of_bezier1)
        LOB.extend(list_of_bezier2)
        LOB.extend(list_of_bezier3)
        LOB.extend(list_of_bezier4)
        npLOB = np.array(LOB)
        plt.plot(npLOB.T[0],npLOB.T[1], marker="o", color="#FA5858")
        '''
        list_of_bridge_set = np.array([[-1*(1.225+ssp[0]),6.5+ssp[1]],[-1*(1.225+ssp[0]),6.5+ssp[1]],[-1*(1.225+ssp[0]),6.5+ssp[1] +1.5],[-1*(1.225+ssp[0]),6.5+ssp[1] +1.5]], dtype=np.float)
        nplist_of_bridge, list_of_bridge = self.bez.bezier_making(list_of_bridge_set)
        plt.plot(nplist_of_bridge.T[0],nplist_of_bridge.T[1], marker="o", color="#FA5858")

        list_of_bezier_set5 = np.array([[-1*(1.225+ssp[0]), 6.5+ssp[1] +1.5],[-1*(1.225+ssp[0]), 6.5+ssp[1] +1.5 +2],[-1*(1.225+ssp[0]+1.25),6.5+ssp[1] +1.5 +0.4],[-1*(1.225+ssp[0] +1.25 +2.0 +0.97), 6.5+ssp[1] +1.5 +0.5]], dtype=np.float)
        #farst#list_of_bezier_set5 = np.array([[-1*(1.225+ssp[0]), 6.5+ssp[1] +1.0],[-1*(1.225+ssp[0]), 6.5+ssp[1] +1.0 +3],[-1*(1.225+ssp[0]+5),6.5+ssp[1] +0.2],[-1*(1.225+ssp[0] +1.25 +9.95 +2.0), 6.5+ssp[1] +0.4]], dtype=np.float)
        #nplist_of_bezier5, list_of_bezier5 = bez5.bezier_making(list_of_bezier_set5)
        nplist_of_bezier5, list_of_bezier5 = self.bez.bezier_making(list_of_bezier_set5)
        plt.plot(nplist_of_bezier5.T[0],nplist_of_bezier5.T[1], marker="o", color="#FA5858")
        '''
        plt.axis("equal")
        plt.grid((True))
        plt.title("ba ra ba ra")
        plt.show()


        LIST = []
        LIST.extend(LOB)
        #LIST.extend(list_of_bridge)
        #LIST.extend(list_of_bezier5)
        npLIST = np.array(LIST)
        #print('npLIST = {}'.format(npLIST))
        plt.plot(npLIST.T[0],npLIST.T[1], marker="o", color="#F7BE81")
        plt.axis("equal")
        plt.grid((True))
        plt.title("LIST")
        plt.show()

        self.tvp.making_curve_length(npLIST.T[0], npLIST.T[1])
        TVP_of_S = self.tvp.making_TVP(npLIST.T[0], npLIST.T[1], 2.0, 0.0, 0.0, 0.0, 0.0)
        self.tvp.deside()
        plt.show()

        #self.arg.arrange(npLIST.T[0], npLIST.T[1], TVP_of_S)
        new_index_for_bezier, len_new_index_for_bezier = self.arg.arrange(npLIST.T[0], npLIST.T[1], TVP_of_S)
        #print("new_index_for_bezier = {}".format(new_index_for_bezier))
        npNEW_LOB, NEW_LOB = self.bez.new_bezier_plt(LIST, new_index_for_bezier, len_new_index_for_bezier)
        ########################################################################
        ########################################################################
        ########################################################################
        ########################################################################
        ########################################################################



        ########################################################################
        ########################################################################
        ######################     making V REF     ############################
        ########################################################################
        ########################################################################
        '''
        self.alfa = self.tvp.making_angle(npNEW_LOB,len(npNEW_LOB))
        self.making_vx_and_vy(self.tvp.get_V(),self.alfa,len(npNEW_LOB))
        with open('csv_item/vx_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(self.vx)
        with open('csv_item/vy_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(self.vy)
        with open('csv_item/alfa_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(self.alfa)
        '''
        ########################################################################
        ########################################################################
        ########################################################################
        ########################################################################
        ########################################################################
        return npLOB, LOB,npNEW_LOB, NEW_LOB
    def making_target_value_video_bridge_red(self):
        ########################################################################
        ########################################################################
        ######################     maiking X REF     ###########################
        ########################################################################
        ########################################################################
        new_index_for_bezier = []
        theta = 0#np.pi/4
        #set_start_point
        #ssp=[-0.5,-0.5]
        ssp=[0,0]
        new_ssp=[-1*(1.225+ssp[0]),-6.5+ssp[1]]

        '''#########################    1st    ################################
        ################################ X #####################################
        list_of_bezier_set1 = np.array([[0,0],[-1*(1.225+ssp[0]),0.7+ssp[1]],[-1*(1.725+ssp[0]),0.7+ssp[1]],[-1*(1.725+ssp[0]),2+ssp[1]]], dtype=np.float)
        list_of_bezier_set2 = np.array([[-1*(1.725+ssp[0]),2.000+ssp[1]],[-1*(1.725+ssp[0]),2.500+ssp[1]],[-1*(0.775+ssp[0]),3+ssp[1]],[-1*(0.725+ssp[0]),3.5+ssp[1]]], dtype=np.float)
        list_of_bezier_set3 = np.array([[-1*(0.725+ssp[0]),3.5+ssp[1]],[-1*(0.775+ssp[0]),4+ssp[1]],[-1*(1.725+ssp[0]),4.5+ssp[1]],[-1*(1.725+ssp[0]),5+ssp[1]]], dtype=np.float)
        list_of_bezier_set4 = np.array([[-1*(1.725+ssp[0]),5+ssp[1]],[-1*(1.725+ssp[0]),5.5+ssp[1]],[-1*(1.225+ssp[0]),6+ssp[1]],[-1*(1.225+ssp[0]),6.5+ssp[1]]], dtype=np.float)
        ########################################################################
        #'''####################################################################
        '''
        ############################     2nd     ###############################
        ################################# O ####################################
        list_of_bezier_set1 = np.array([[0,0],[-1*(1.225+ssp[0]),0.7+ssp[1]],[-1*(1.95+ssp[0]),0.7+ssp[1]],[-1*(1.95+ssp[0]),2+ssp[1]]], dtype=np.float)
        list_of_bezier_set2 = np.array([[-1*(1.95+ssp[0]),2.000+ssp[1]],[-1*(1.95+ssp[0]),2.500+ssp[1]],[-1*(0.51+ssp[0]),3+ssp[1]],[-1*(0.51+ssp[0]),3.5+ssp[1]]], dtype=np.float)
        list_of_bezier_set3 = np.array([[-1*(0.51+ssp[0]),3.5+ssp[1]],[-1*(0.51+ssp[0]),4+ssp[1]],[-1*(1.95+ssp[0]),4.5+ssp[1]],[-1*(1.95+ssp[0]),5+ssp[1]]], dtype=np.float)
        list_of_bezier_set4 = np.array([[-1*(1.95+ssp[0]),5+ssp[1]],[-1*(1.95+ssp[0]),5.5+ssp[1]],[-1*(1.225+ssp[0]),5.5+ssp[1]],[-1*(1.225+ssp[0]),6.5+ssp[1]]], dtype=np.float)
        ########################################################################
        ########################################################################

        nplist_of_bezier1, list_of_bezier1 = self.bez.bezier_making(list_of_bezier_set1)
        nplist_of_bezier2, list_of_bezier2 = self.bez.bezier_making(list_of_bezier_set2)
        nplist_of_bezier3, list_of_bezier3 = self.bez.bezier_making(list_of_bezier_set3)
        nplist_of_bezier4, list_of_bezier4 = self.bez.bezier_making(list_of_bezier_set4)
        LOB = []
        LOB.extend(list_of_bezier1)
        LOB.extend(list_of_bezier2)
        LOB.extend(list_of_bezier3)
        LOB.extend(list_of_bezier4)
        npLOB = np.array(LOB)
        plt.plot(npLOB.T[0],npLOB.T[1], marker="o", color="#FA5858")
        '''
        list_of_bridge_set = np.array([[-1*(1.225+new_ssp[0]),6.5+new_ssp[1]],[-1*(1.225+new_ssp[0]),6.5+new_ssp[1]],[-1*(1.225+new_ssp[0]),6.5+new_ssp[1] +1.5],[-1*(1.225+new_ssp[0]),6.5+new_ssp[1] +1.5]], dtype=np.float)
        nplist_of_bridge, list_of_bridge = self.bez.bezier_making(list_of_bridge_set)
        plt.plot(nplist_of_bridge.T[0],nplist_of_bridge.T[1], marker="o", color="#FA5858")

        list_of_bezier_set5 = np.array([[-1*(1.225+new_ssp[0]), 6.5+new_ssp[1] +1.5],[-1*(1.225+new_ssp[0]), 6.5+new_ssp[1] +1.5 +2],[-1*(1.225+new_ssp[0]+1.25),6.5+new_ssp[1] +1.5 +0.4],[-1*(1.225+new_ssp[0] +1.25 +2.0 +0.97), 6.5+new_ssp[1] +1.5 +0.5]], dtype=np.float)
        #farst#list_of_bezier_set5 = np.array([[-1*(1.225+ssp[0]), 6.5+ssp[1] +1.0],[-1*(1.225+ssp[0]), 6.5+ssp[1] +1.0 +3],[-1*(1.225+ssp[0]+5),6.5+ssp[1] +0.2],[-1*(1.225+ssp[0] +1.25 +9.95 +2.0), 6.5+ssp[1] +0.4]], dtype=np.float)
        #nplist_of_bezier5, list_of_bezier5 = bez5.bezier_making(list_of_bezier_set5)
        nplist_of_bezier5, list_of_bezier5 = self.bez.bezier_making(list_of_bezier_set5)
        plt.plot(nplist_of_bezier5.T[0],nplist_of_bezier5.T[1], marker="o", color="#FA5858")

        plt.axis("equal")
        plt.grid((True))
        plt.title("ba ra ba ra")
        plt.show()


        LIST = []
        #LIST.extend(LOB)
        LIST.extend(list_of_bridge)
        LIST.extend(list_of_bezier5)
        npLIST = np.array(LIST)
        #print('npLIST = {}'.format(npLIST))
        plt.plot(npLIST.T[0],npLIST.T[1], marker="o", color="#F7BE81")
        plt.axis("equal")
        plt.grid((True))
        plt.title("LIST")
        plt.show()

        self.tvp.making_curve_length(npLIST.T[0], npLIST.T[1])
        TVP_of_S = self.tvp.making_TVP(npLIST.T[0], npLIST.T[1], 2.0, 0.0, 0.0, 0.0, 0.0)
        self.tvp.deside()
        plt.show()

        #self.arg.arrange(npLIST.T[0], npLIST.T[1], TVP_of_S)
        new_index_for_bezier, len_new_index_for_bezier = self.arg.arrange(npLIST.T[0], npLIST.T[1], TVP_of_S)
        #print("new_index_for_bezier = {}".format(new_index_for_bezier))
        npNEW_LOB, NEW_LOB = self.bez.new_bezier_plt(LIST, new_index_for_bezier, len_new_index_for_bezier)
        ########################################################################
        ########################################################################
        ########################################################################
        ########################################################################
        ########################################################################



        ########################################################################
        ########################################################################
        ######################     making V REF     ############################
        ########################################################################
        ########################################################################
        '''
        self.alfa = self.tvp.making_angle(npNEW_LOB,len(npNEW_LOB))
        self.making_vx_and_vy(self.tvp.get_V(),self.alfa,len(npNEW_LOB))
        with open('csv_item/vx_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(self.vx)
        with open('csv_item/vy_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(self.vy)
        with open('csv_item/alfa_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(self.alfa)
        '''
        ########################################################################
        ########################################################################
        ########################################################################
        ########################################################################
        ########################################################################
        npLOB = []
        LOB = []
        return npLOB, LOB,npNEW_LOB, NEW_LOB
