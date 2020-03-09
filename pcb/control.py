include math

b = 90    # base, centered 90 degrees
l = 90    # left
r = 90    # right
g = 90    # gripper - half open

force = b * l * r / g * math.pi

print("The force is {:.2f} Newton.".format(force))
