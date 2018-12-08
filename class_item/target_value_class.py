from color_class import pycolor as pc
import numpy as np
import matplotlib.pyplot as plt

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
        self.tvp.making_curve_length(npLOB.T[0], npLOB.T[1])
        TVP_of_S = self.tvp.making_TVP(npLOB.T[0], npLOB.T[1], 2.0, 0.0, 0.0, 0.0, 0.0)
        self.tvp.deside()
        plt.show()

        new_index_for_bezier, len_new_index_for_bezier = self.arg.arrange(npLOB.T[0], npLOB.T[1], TVP_of_S)
        npNEW_LOB, NEW_LOB = self.bez.new_bezier_plt(LOB, new_index_for_bezier, len_new_index_for_bezier)

        return npLOB, LOB,npNEW_LOB, NEW_LOB
