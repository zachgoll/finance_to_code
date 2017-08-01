import cs50

# Validate the user's input and make sure it is between 0 and 23

while True:
    print("Height: ", end="")
    pyramid_height = cs50.get_int()
    if pyramid_height > 0 and pyramid_height < 23:
        break
    

    
for i in range(pyramid_height):
    # print spaces
    for j in range(pyramid_height-i-1):
        print(" ", end="")
    print("#" * (i+2), end="")
    print()