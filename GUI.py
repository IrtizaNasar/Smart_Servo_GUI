from Ax12 import Ax12
import time
import customtkinter

# e.g 'COM3' windows or '/dev/ttyUSB0' for Linux
Ax12.DEVICENAME = 'COM12'

Ax12.BAUDRATE = 1_000_000

# sets baudrate and opens com port
Ax12.connect()

MAX_DEGREE = 300  # maximum rotation of AX-12 motor in degrees is 0 - 300 degrees
MAX_POS = 1024  # maximum rotation of AX-12 in encoder values is 0 - 1024

# create AX12 instance with ID
motor_id_1 = 6
motor_id_2 = 5
motor_id_test = 4

dxl_1 = Ax12(motor_id_1)
dxl_1.set_moving_speed(400)

dxl_2 = Ax12(motor_id_2)
dxl_2.set_moving_speed(400)


def encoder_to_degree(value):
    """Converts raw dynamixel encoder values to degrees.
    Conversion is derived from pypot's dynamixel module:
    (https://github.com/poppy-project/pypot/blob/master/pypot/dynamixel/conversion.py)

    With this conversion, 0 degrees will equate to the position 512."""

    return round(((300 * float(value)) / (MAX_POS - 1)) - (MAX_DEGREE / 2), 2)


def degree_to_encode(value):
    pos = int(round((MAX_POS - 1) * ((MAX_DEGREE / 2 + float(value)) / MAX_DEGREE), 0))
    pos = min(max(pos, 0), MAX_POS - 1)
    return pos


def motor_1_pos(position):
    raw_position = int(position)
    dxl_1.set_goal_position(raw_position)
    motor_1_label.configure(text=f"Motor 1 Position: {encoder_to_degree(raw_position)} degrees")
    # print(position)
    # print(type(position))


def motor_2_pos(position):
    raw_position = int(position)
    dxl_2.set_goal_position(raw_position)
    motor_2_label.configure(text=f"Motor 2 Position: {encoder_to_degree(raw_position)} degrees")


customtkinter.set_appearance_mode('dark')
root = customtkinter.CTk()
root.minsize(400, 400)
root.title("Smart Servo")

motor_1_label = customtkinter.CTkLabel(master=root, text="Motor 1 Position")
motor_1_label.pack()

motor_1_pos_slider = customtkinter.CTkSlider(master=root, from_=150, to=870,
                                             number_of_steps=99,
                                             command=motor_1_pos)  # Slider shows value in degrees
motor_1_pos_slider.set(0)
motor_1_pos_slider.pack()

motor_2_label = customtkinter.CTkLabel(master=root, text="Motor 2 Position")
motor_2_label.pack()

motor_2_pos_slider = customtkinter.CTkSlider(master=root, from_=150, to=870,
                                             number_of_steps=99,
                                             command=motor_2_pos)
motor_2_pos_slider.set(0)
motor_2_pos_slider.pack()

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
