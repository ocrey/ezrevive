## Some test code for the script
## The main intuition is create a autorevive script for PxG
## doc keyboard = https://github.com/boppreh/keyboard#api
## doc mouse = https://thepythoncode.com/article/control-mouse-python


import mouse
import keyboard
import time


## precisa colocar um while pro programa executar até que seja prescionado
## a tecla "enter"

## Config cordinate

def test():
    log = []
    getinfo = mouse.is_pressed(button='right') ### essa porra não funciona
    while getinfo == False:
        position = mouse.get_position()
        log.append(getinfo)
        for l in log:
            if log[l] ==  True:
                return
        else:


            print(getinfo)
            print(position)
            time.sleep(3)


test()


#def firstpoke():
#    positions = mouse.get_position()
#    print(positions)
#    time.sleep(3)

# while click_pos is not True:
#    if getinfo == True:
#        sendinfo
#    else:
