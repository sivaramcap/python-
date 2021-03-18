house_shell_location = 4
device_location = 0
while(device_location != house_shell_location):
    device_location = int(input("plot radies :"))
    if device_location > 0:
        if device_location > house_shell_location:
            print("near")
        elif device_location < house_shell_location:
            print("far")
    else:
        print("try hard")
        break
else:
    print("bell ring")
print(house_shell_location)
