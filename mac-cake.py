import subprocess
import random
import time


print("""
              #    #   ##    ####         ####    ##   #    # ###### 
              ##  ##  #  #  #    #       #    #  #  #  #   #  #      
              # ## # #    # #      ##### #      #    # ####   #####  
              #    # ###### #            #      ###### #  #   #      
              #    # #    # #    #       #    # #    # #   #  #      
              #    # #    #  ####         ####  #    # #    # ######
""")


print(        Fahrenheit)






def change_mac(interface):
    random_mac = [random.choice('0123456789abcdef') for _ in range(6)]
    new_mac = ":".join(random_mac)

    try:
        subprocess.check_call(['ifconfig', interface, 'down'])
        subprocess.check_call(['ifconfig', interface, 'hw', 'ether', new_mac])
        subprocess.check_call(['ifconfig', interface, 'up'])
        print("MAC address of", interface, "changed to", new_mac)
    except subprocess.CalledProcessError:
        print("Error: Failed to change MAC address of", interface)

def get_interfaces():
    interfaces = subprocess.check_output(['ifconfig', '-a']).decode('utf-8')
    interfaces = interfaces.split('\n\n')
    interfaces = [i.split()[0] for i in interfaces if i and not i.startswith('lo')]
    return interfaces

def print_interfaces(interfaces):
    print("Available interfaces:")
    for index, interface in enumerate(interfaces, start=1):
        print(f"{index}) {interface}")
    print(f"{len(interfaces)+1}) Quit")

def main():
    interfaces = get_interfaces()
    print_interfaces(interfaces)

    while True:
        choice = input("Select an interface: ")
        if choice.isdigit() and int(choice) in range(1, len(interfaces)+2):
            index = int(choice) - 1
            if index == len(interfaces):
                print("Quitting...")
                break
            else:
                interface = interfaces[index]
                print("MAC address of", interface, "will be automatically changed every 5 seconds.")
                print("Press Ctrl+C to stop.")
                try:
                    while True:
                        change_mac(interface)
                        time.sleep(5)
                except KeyboardInterrupt:
                    print("\nStopped automatic MAC address changing.")
                    break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()



