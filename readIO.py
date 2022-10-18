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
    mcu = serial.Serial(com_port, 9600, timeout=0.1)
except:
    print("COM port failed to open.")
    exit()


# While Serial port does not ask for keypress 
while True:
    text = str(mcu.readline().decode().strip())
    if text != '':
        keypress = input(text)
        mcu.write(bytes("i", 'utf-8'))
        break

# Take input
file_name = "record.txt"

if num_args == 3:
    file_name = sys.argv[2]
with open(file_name, 'a') as f1:

    while True:
        # read and decode serial values
        text = str(mcu.readline().decode().strip())

        # if reading ends
        if text =='STAAAP!!!':
            break

        # if reading is not empty
        if text !='':
            print(text)
            f1.write(text + '\n')
            # text = text.split(',')
            # f1.write(text[0]+','+text[1]+'\n')

# close the serial connection 
mcu.close()
