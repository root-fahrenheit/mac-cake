import subprocess
from getmac import get_mac_address as gma
import sys, time, os
import random

print("""
              #    #   ##    ####         ####    ##   #    # ###### 
              ##  ##  #  #  #    #       #    #  #  #  #   #  #      
              # ## # #    # #      ##### #      #    # ####   #####  
              #    # ###### #            #      ###### #  #   #      
              #    # #    # #    #       #    # #    # #   #  #      
              #    # #    #  ####         ####  #    # #    # ######
""")





message = "                github.com/root-fahrenheit\n\n\n"

for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(0.5)


class Format:
    end = '\033[0m'
    underline = '\033[4m'



print("                     Your MAC Address: "  + gma())

time.sleep(1)

print("""
                      [c*]=========Fahrenheit========[c*]
                      |   github.com/root-fahrenheit/   |
                      |     Welcome to MAC-Cake so      |
                      |        my first project.        |
                      |          My teacher is          |
                      |        Atil Samancioglu.        |
                      |        on Udemy platform.       |
                      |=================================| """)


print("""
                       1) Select your interface

                       2) Quit\n\n
""")




def random_mac():
    characters = "0123456789abcdef"
    random_mac_address = "00"
    for i in range(5):
        random_mac_address += ":" + \
                              random.choice(characters) \
                              + random.choice(characters)
    return random_mac_address


def clearscr():
    os.system('clear')


def changer():
    clearscr()
    print("""
                  #    #   ##    ####         ####    ##   #    # ###### 
                  ##  ##  #  #  #    #       #    #  #  #  #   #  #      
                  # ## # #    # #      ##### #      #    # ####   #####  
                  #    # ###### #            #      ###### #  #   #      
                  #    # #    # #    #       #    # #    # #   #  #      
                  #    # #    #  ####         ####  #    # #    # ######
    """)
    print("""\n\n
                                    1) eth0
                           
                                    2) eth1
                           
                                    3) wlan0
                           
                                    4) wlan1

                                    5) Quit\n\n""")


    y_loop = 0

    choice_one = "1"
    choice_two = "2"
    choice_three = "3"
    choice_four = "4"
    choice_five = "5"
    while y_loop == 0:
        userchoice2 = str(input(Format.underline + "Select -->" + Format.end))
        if userchoice2 == choice_one:
            y_loop += 1
            subprocess.call(["ifconfig", "eth0", "down"])
            subprocess.call(["ifconfig", "eth0", "hw", "ether", random_mac()])
            subprocess.call(["ifconfig", "eth0", "up"])
            print("Your MAC Address: " + gma())
            quit()
        elif userchoice2 == choice_two:
            y_loop += 1
            subprocess.call(["ifconfig", "eth1", "down"])
            subprocess.call(["ifconfig", "eth1", "hw", "ether", random_mac()])
            subprocess.call(["ifconfig", "eth1", "up"])
            print("Your MAC Address: " + gma())
            quit()
        elif userchoice2 == choice_three:
            subprocess.call(["ifconfig", "wlan0", "down"])
            subprocess.call(["ifconfig", "wlan0", "hw", "ether", random_mac()])
            subprocess.call(["ifconfig", "wlan0", "up"])
            print("Your MAC Address: " + gma())
            quit()
        elif userchoice2 == choice_four:
            y_loop += 1
            subprocess.call(["ifconfig", "wlan1", "down"])
            subprocess.call(["ifconfig", "wlan1", "hw", "ether", random_mac()])
            subprocess.call(["ifconfig", "wlan1", "up"])
            print("Your MAC Address: " + gma())
            quit()
        elif userchoice2 == choice_five:
            y_loop += 1
            print("Quitting")
            time.sleep(1)
            quit()
        else:
            continue

x_loop = 0
choice1 = "1"
choice2 = "2"
while x_loop == 0:
    userchoice = str(input(Format.underline + "--> Which? 1 , 2: " + Format.end))
    if userchoice == choice1:
        x_loop += 1
        changer()
        break
    elif userchoice == choice2:
        x_loop += 1
        quit()
        break
    else:
        continue






