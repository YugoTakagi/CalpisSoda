from game_class import game_class

from class_item.omu3_ikm import omu3
from class_item.pid import pid
from class_item.color_class import pycolor as pc
from class_item.state_class import State
from class_item.state_class_of_4ste import state_class_of_4ste
from class_item.four_wheel_steering_ikm import four_wheel_steering_ikm
from class_item.target_value_class import target_value_class

from class_item.target_item.bezier_class import bezier
from class_item.target_item.TVP_class import trapezoidal_velocity_profile
from class_item.target_item.arrange_the_point_class import arrange_the_point

import numpy as np
import matplotlib.pyplot as plt
import csv

def main():
    #############################  init target  ################################
    ############################################################################
    bez = bezier(number_of_points=1000)
    tvp = trapezoidal_velocity_profile()
    arg = arrange_the_point()
    target = target_value_class(bez=bez, tvp=tvp, arg=arg)
    ############################################################################
    ############################################################################

    ##########################  init controler  ################################
    ############################################################################
    cy = omu3()
    fws = four_wheel_steering_ikm()
    state = State(x=0.0, y=0.0, yaw=0.0)
    state_4ste = state_class_of_4ste(x=0.0, y=0.0, yaw=np.pi/6)
    dt = state.dt
    #game = game_class(target=target, state=state, robot=cy)
    game = game_class(target=target, state=state_4ste, robot=fws)
    ############################################################################
    ############################################################################

    #game.run_through_the_forest()
    #game.run()
    #game.run_circle()
    #game.run_video_forest()
    #game.run_video_bridge()
    #game.run_video_forest_simple()
    game.run_line()



if __name__ == '__main__':
    print("++  + start main +  ++")
    main()
    print("++  +  end main  +  ++")
