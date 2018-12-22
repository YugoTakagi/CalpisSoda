#from color_class import pycolor as pc
import numpy as np
import matplotlib.pyplot as plt
import csv

class target_value_class(object):
    """docstring for target_value_class."""
    vx = []
    vy = []
    omega = []
    x = []
    y = []
    theta = []
    def __init__(self, bez, tvp, arg):
        self.bez = bez
        self.tvp = tvp
        self.arg = arg
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

        new_index_for_bezier, len_new_index_for_bezier = self.arg.arrange(npLOB.T[0], npLOB.T[1], TVP_of_S)
        npNEW_LOB, NEW_LOB = self.bez.new_bezier_plt(LOB, new_index_for_bezier, len_new_index_for_bezier)

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
        #bez5 = bezier(300)

        new_index_for_bezier = []
        theta = 0#np.pi/4
        #set_start_point
        ssp=[-0.5,-0.5]

        list_of_bezier_set1 = np.array([[0,0],[-1*(1.225+ssp[0]),0.7+ssp[1]],[-1*(1.725+ssp[0]),0.7+ssp[1]],[-1*(1.725+ssp[0]),2+ssp[1]]], dtype=np.float)
        list_of_bezier_set2 = np.array([[-1*(1.725+ssp[0]),2.000+ssp[1]],[-1*(1.725+ssp[0]),2.500+ssp[1]],[-1*(0.775+ssp[0]),3+ssp[1]],[-1*(0.725+ssp[0]),3.5+ssp[1]]], dtype=np.float)
        list_of_bezier_set3 = np.array([[-1*(0.725+ssp[0]),3.5+ssp[1]],[-1*(0.775+ssp[0]),4+ssp[1]],[-1*(1.725+ssp[0]),4.5+ssp[1]],[-1*(1.725+ssp[0]),5+ssp[1]]], dtype=np.float)
        list_of_bezier_set4 = np.array([[-1*(1.725+ssp[0]),5+ssp[1]],[-1*(1.725+ssp[0]),5.5+ssp[1]],[-1*(1.225+ssp[0]),6+ssp[1]],[-1*(1.225+ssp[0]),6.5+ssp[1]]], dtype=np.float)
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

        list_of_bridge_set = np.array([[-1*(1.225+ssp[0]),6.5+ssp[1]],[-1*(1.225+ssp[0]),6.5+ssp[1]],[-1*(1.225+ssp[0]),6.5+ssp[1] +1.5],[-1*(1.225+ssp[0]),6.5+ssp[1] +1.5]], dtype=np.float)
        nplist_of_bridge, list_of_bridge = self.bez.bezier_making(list_of_bridge_set)
        plt.plot(nplist_of_bridge.T[0],nplist_of_bridge.T[1], marker="o", color="#FA5858")

        list_of_bezier_set5 = np.array([[-1*(1.225+ssp[0]), 6.5+ssp[1] +1.0],[-1*(1.225+ssp[0]), 6.5+ssp[1] +1.0 +3],[-1*(1.225+ssp[0]+5),6.5+ssp[1] +0.2],[-1*(1.225+ssp[0] +1.25 +9.95 +2.0), 6.5+ssp[1] +0.4]], dtype=np.float)
        #nplist_of_bezier5, list_of_bezier5 = bez5.bezier_making(list_of_bezier_set5)
        nplist_of_bezier5, list_of_bezier5 = self.bez.bezier_making(list_of_bezier_set5)
        plt.plot(nplist_of_bezier5.T[0],nplist_of_bezier5.T[1], marker="o", color="#FA5858")
        plt.axis("equal")
        plt.grid((True))
        plt.show()


        LIST = []
        LIST.extend(LOB)
        LIST.extend(list_of_bridge)
        #LIST.extend(list_of_bezier5)
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
