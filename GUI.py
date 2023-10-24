from Ax12 import Ax12
import time

# e.g 'COM3' windows or '/dev/ttyUSB0' for Linux
Ax12.DEVICENAME = '/dev/tty.usbserial-FT6S4H67'

Ax12.BAUDRATE = 1_000_000

# sets baudrate and opens com port
Ax12.connect()

# create AX12 instance with ID 10 
motor_id = 1
my_dxl = Ax12(motor_id)  
my_dxl.set_moving_speed(400)

import customtkinter

def pos(position):
    position = int(position)
    my_dxl.set_goal_position(position)
    amount_label.configure(text="Position: "+str(position))
    # print(position)
    # print(type(position))
        


customtkinter.set_appearance_mode('dark')
root = customtkinter.CTk()
root.minsize(400,400)
root.title("Smart Servo")

amount_label = customtkinter.CTkLabel(master=root,text="Position: 30")
amount_label.pack()

amount_slider = customtkinter.CTkSlider(master=root, from_=30, to=512, 
                                        number_of_steps=99,
                                        command=pos)
amount_slider.set(0)
amount_slider.pack()

root.mainloop()


# def user_input():
#     """Check to see if user wants to continue"""
#     ans = input('Continue? : y/n ')
#     if ans == 'n':
#         return False
#     else:
#         return True


# def main(motor_object):
#     """ sets goal position based on user input """

#     for i in range(10):
#         motor_object.set_goal_position(15)
#         time.sleep(1)
#         motor_object.set_goal_position(512)
#         time.sleep(1)

#     # bool_test = True
#     # while bool_test:

#         # print("\nPosition of dxl ID: %d is %d " %
#             #   (motor_object.id, motor_object.get_present_position()))
#         # desired angle input
#         # input_pos = int(input("goal pos: "))
#         # motor_object.set_goal_position(input_pos)
#         # print("Position of dxl ID: %d is now: %d " %
#         #       (motor_object.id, motor_object.get_present_position()))
#         # bool_test = user_input()

# # pass in AX12 object
# main(my_dxl)

# disconnect
# my_dxl.set_torque_enable(0)
# Ax12.disconnect()
