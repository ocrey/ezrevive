## Some test code for the script
## The main intuition is create a autorevive script for PxG
## doc keyboard = https://github.com/boppreh/keyboard#api
## doc mouse = https://thepythoncode.com/article/control-mouse-python


import mouse
import Keyboard


## precisa colocar um while pro programa executar até que seja prescionado
## a tecla "enter"

## Config cordinate

Def getcordinate():
    terminate:
    click_pos = mouse.is_pressed("right")

    if  click_pos == True:
        positions = mouse.get_posistion()
        Print(positions)




        
