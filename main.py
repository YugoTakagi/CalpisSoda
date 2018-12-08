from omu3_ikm import omu3
from pid import pid
from synthesis_of_vector import synthesis_of_vector
from game_class import game_class

from class_item.bezier_class import bezier
from class_item.TVP_class import trapezoidal_velocity_profile
from class_item.color_class import pycolor as pc
from class_item.state_class import State
from class_item.arrange_the_point_class import arrange_the_point
from class_item.target_value_class import target_value_class

import numpy as np
import math
import matplotlib.pyplot as plt
import csv

def main():
    number_of_index = 4000
    bez = bezier(number_of_index)
    tvp = trapezoidal_velocity_profile()
    arg = arrange_the_point()
    target = target_value_class(bez=bez, tvp=tvp, arg=arg)

    cy = omu3()
    state = State(x=0.0, y=-0.0, yaw=0.0)
    dt = state.dt
    game = game_class(target=target, state=state, robot=cy)



    game.run_through_the_forest()







if __name__ == '__main__':
    print("++  + start +  ++")
    main()
    print("++  +  end  +  ++")
