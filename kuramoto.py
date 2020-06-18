# Kuramoto model
#
#
#
#
#
#
#
#
#
#

# CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC

import numpy as np
import os as os

# CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC

def main():

  number_particles_int = 20
  coupling_const_float = 5.0

  angle_pos_ary = np.random.random( number_particles_int )*2*np.pi
  # angle_vel_ary = np.random.random( number_particles_int )
  angle_vel_ary = 2.0*np.ones( number_particles_int ) *abs(np.random.normal(0,1, number_particles_int ))

  max_simulation_time_int = 10
  delta_time = 0.01
  time_ary = np.arange( 0, max_simulation_time_int, delta_time ) 

  oscilator_file = open("kuramoto_oscilator.dat","w")
  order_par_file = open("order_parameter.dat","w")

  for time_int in time_ary:

    for i in np.arange( number_particles_int ):

      angle_pos_float = angle_pos_ary[ i ]
      angle_vel_float = angle_vel_ary[ i ]

      K1 = kuramoto( angle_pos_float , angle_vel_float, angle_pos_ary, number_particles_int, coupling_const_float )

      K2 = kuramoto( angle_pos_float+(delta_time*K1*0.5), angle_vel_float, angle_pos_ary, number_particles_int, coupling_const_float ) 

      K3 = kuramoto( angle_pos_float+(delta_time*K2*0.5), angle_vel_float, angle_pos_ary, number_particles_int, coupling_const_float )

      K4 = kuramoto( angle_pos_float+(delta_time*K3), angle_vel_float, angle_pos_ary, number_particles_int, coupling_const_float )

      angle_pos_ary[i] = angle_pos_float + (delta_time/6.0)*( K1 + (2.0*K2) + (2.0*K3) + K4 )
  
      oscilator_file.write( str(angle_pos_ary[i]) + str("\t") + str(1) + str("\n") )

    r_float, theta_float, x_float, y_float = order_parameter( angle_pos_ary, number_particles_int )

    oscilator_file.write( str(theta_float) + str("\t") + str(r_float) + str("\n") )
    order_par_file.write( str(time_int) + "\t" + str(x_float) + "\t" + str(y_float) + "\n" )
    oscilator_file.write("\n\n")

  order_par_file.close()
  oscilator_file.close()

  os.system("sleep 5")
  
  print("Gnuploy Gif.")

  os.system("gnuplot kuramoto_gif.gp")

# CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC

def kuramoto(
    angle_pos_float_,
    angle_vel_float_, 
    angle_pos_ary_,
    number_particles_int_,
    coupling_const_float_
  ):

    _aux_angle_pos_float = angle_vel_float_ \
    + (coupling_const_float_/number_particles_int_)*np.sum( np.fromiter( map( lambda _x: np.sin( _x - angle_pos_float_ ), angle_pos_ary_), dtype=float) )

    return( _aux_angle_pos_float )

# CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC

def order_parameter(
    angle_pos_ary_,
    number_particles_int_
  ):

  _x_float = (1.0/number_particles_int_)*np.sum( np.fromiter( map( lambda _x: np.cos(_x), angle_pos_ary_), dtype=float) )
  _y_float = (1.0/number_particles_int_)*np.sum( np.fromiter( map( lambda _x: np.sin(_x), angle_pos_ary_), dtype=float) )

  _r_float = np.sqrt( _x_float*_x_float + _y_float*_y_float )
  _theta_float = np.arctan2( _y_float,_x_float )

  return( _r_float, _theta_float, _x_float, _y_float)

# CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC

main()