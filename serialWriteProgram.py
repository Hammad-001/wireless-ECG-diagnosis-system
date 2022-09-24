import sys
import serial

num_args = len(sys.argv)
if num_args < 2:
    print("COM port not selected.")
    exit()

com_port = sys.argv[1]
print("-"*50)
print(f"You have selected {com_port} port for communication")
print("-"*50)

try: 
    mcu = serial.Serial(com_port, timeout=1)
except:
    print("COM port failed to open.")
    exit()

# successfully connected
print(mcu.readline().decode())
keypress = input()
mcu.write(bytes(keypress, 'utf-8'))

file_name = "record.txt"

if num_args == 3:
    file_name = sys.argv[2]

with open(file_name, 'a') as f:
    while True:
        text = mcu.readline().decode()[:-2]
        print(text)
        if text == '':
            continue
        if text != 'STAAAP!!!':
            f.write(text + '\n')
        else:
            break