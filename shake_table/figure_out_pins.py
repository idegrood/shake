from shake_table import *


def determine_sensors():
   """
   This function initializes the ShakeTable and allows the user to determine which sensor is which by moving the table until seeing which sensors trigger
   """
   table = ShakeTable()
   while not table.near_sensor.is_pressed and not table.far_sensor.is_pressed:
       time.sleep(0.0005)
       if table.near_sensor.is_pressed:
           print('Near Sensor is Pressed')
       if table.far_sensor.is_pressed:
           print('Far Sensor is Pressed')


def determine_steps():
   """
   This function initializes the ShakeTable and allows the user to determine the number of steps between the two sensors.
   """
   table = ShakeTable()
   num_steps = 0
   while not table.far_sensor.is_pressed and not table.near_sensor.is_pressed:
       time.sleep(0.0005)
       table.step(0)
       num_steps += 1


       if table.near_sensor.is_pressed:
           print('Sensor 0 is Pressed')
       if table.far_sensor.is_pressed:
           print('Sensor 1 is Pressed')


   print('Sensor to sensor is %d steps' % num_steps)


if __name__ == '__main__':
   determine_sensors()






