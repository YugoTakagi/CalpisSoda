from omu3_ikm import omu3
from pid import pid
from synthesis_of_vector import synthesis_of_vector

from class_item.bezier_class import bezier
from class_item.TVP_class import trapezoidal_velocity_profile
from class_item.color_class import pycolor as pc
from class_item.state_class import State
from class_item.arrange_the_point_class import arrange_the_point

import numpy as np
import math
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
        self.tvp.making_curve_length(npLOB.T[0], npLOB.T[1])
        TVP_of_S = self.tvp.making_TVP(npLOB.T[0], npLOB.T[1], 2.0, 0.0, 0.0, 0.0, 0.0)
        self.tvp.deside()
        plt.show()

        new_index_for_bezier, len_new_index_for_bezier = self.arg.arrange(npLOB.T[0], npLOB.T[1], TVP_of_S)
        npNEW_LOB, NEW_LOB = self.bez.new_bezier_plt(npLOB, new_index_for_bezier, len_new_index_for_bezier)

        return npNEW_LOB, NEW_LOB
