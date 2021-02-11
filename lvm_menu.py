import os
import sys

def lvm_menu():
    while True:
        os.system("clear")
        os.system("tput setaf 1")
        print("\t\t\t\t\t\tLVM")
        os.system("tput setaf 7")
        print("\t\t#############################################################")
        print("""\t\t\t1. Create Physical Volume
                        2. Create Volume Group
                        3. Create Logical Volume
                        4. Format Volume
                        5. Mount Logical Volume
                        6. Extend Volume Group
                        7. Extend Logical Volume
                        8. Display Physical Volume
                        9. Display Volume Group
                        10. Display Logical Volume
                        11. Display Mounted Directories
                        99. Back
                        0. Exit""")
        print("\t\t#############################################################")
        os.system("tput setaf 3")
        lvm = int(input("\nEnter your choice: "))
        if lvm == 1:
            cpv()
        elif lvm == 2:
            cvg()
        elif lvm == 3:
            clv()
        elif lvm == 4:
            lvm_format()
        elif lvm == 5:
            mlv()
        elif lvm == 6:
            evg()
        elif lvm == 7:
            elv()
        elif lvm == 8:
            dpv()
        elif lvm == 9:
            dvg()
        elif lvm == 10:
            dlv()
        elif lvm == 11:
            dmd()
        elif lvm == 99:
            os.system("clear")
            break
        elif lvm == 0:
            sys.exit()
        else:
            print("Wrong choice!!!")
    input("Enter any key to continue")

def cpv():
    os.system("clear")
    os.system("tput setaf 6")
    pv = input("Enter path of device to convert to PV")
    if os.system("pvcreate {}".format(pv)) == 0:
        os.system("tput setaf 2")
        print("PV created successfully")
    else:
        os.system("tput setaf 1")
        print("Could not create PV")
    input("Enter any key to continue")

def cvg():
    os.system("clear")
    os.system("tput setaf 6")
    vg = input("Enter name of VG")
    pv = input("Enter devices one by one to create VG\n Enter \"STOP\" to finish entering devices\n",end='')
    st = "vgcreate %s "%vg
    while pv != "STOP":
        st = st + pv + " "
    if os.system(st) == 0:
        os.system("tput setaf 2")
        print("VG created successfully")
    else:
        os.system("tput setaf 1")
        print("Could not create VG")
    input("Enter any key to continue")

def clv():
    os.system("clear")
    os.system("tput setaf 6")
    size = input("Enter size of LV: ")
    name = input("Enter name of VG: ")
    vg = input("Enter VG name to create LV: ",end='')
    if os.system("lvcreate --size {size}G --name {name} {lv}".format(size, name, lv)) == 0:
        os.system("tput setaf 2")
        print("LV created successfully")
    else:
        os.system("tput setaf 1")
        print("Could not create LV")
    input("Enter any key to continue")

def format():
    os.system("clear")
    os.system("tput setaf 6")
    dev = input("Enter device path to format: ")
    if os.system("mkfs.ext4 {dev}".format(dev)) == 0:
        os.system("tput setaf 2")
        print("Formatted successfully")
    else:
        os.system("tput setaf 1")
        print("Could not format ")
    input("Enter any key to continue")

def mlv():
    os.system("clear")
    os.system("tput setaf 6")
    device = input("Enter device path to mount: ",end='')
    dirc = input("Enter directory to make as mount point: ",end='')
    if os.system("mount {device} {dirc}".format(device, dirc)) == 0:
        os.system("tput setaf 2")
        print("LV mounted successfully")
    else:
        os.system("tput setaf 1")
        print("Could not mount LV")
    input("Enter any key to continue")

def evg():
    os.system("clear")
    os.system("tput setaf 6")
    vg = input("Enter VG to extend: ",end='')
    pv = input("Enter PV to add to VG: ",end='')
    if os.system("vgextend {vg} {pv}".format(vg, pv)) == 0:
        os.system("tput setaf 2")
        print("VG extended successfully")
    else:
        os.system("tput setaf 1")
        print("Could not extend VG")
    input("Enter any key to continue")

def elv():
    os.system("clear")
    os.system("tput setaf 6")
    size = input("Enter size to extend LV: ",end='')
    lv = size("Enter path to LV to extend: ",end='')
    if os.system("lvextend --size +{size}G {lv}".format(size, lv)) == 0:
        os.system("tput setaf 2")
        print("LV extended successfully")
    else:
        os.system("tput setaf 1")
        print("Could not extend LV")
    input("Enter any key to continue")

def dpv():
    os.system("clear")
    os.system("tput setaf 6")
    pv = input("Enter path of device to display PV")
    if os.system("pvdisplay {pv}".format(pv)) == 0:
        os.system("tput setaf 2")
        print("PV displayed successfully")
    else:
        os.system("tput setaf 1")
        print("Could not display PV")
    input("Enter any key to continue")

def dvg():
    os.system("clear")
    os.system("tput setaf 6")
    if os.system("vgdisplay") == 0:
        os.system("tput setaf 2")
        print("VG displayed successfully")
    else:
        os.system("tput setaf 1")
        print("Could not display VG")
    input("Enter any key to continue")

def dlv():
    os.system("clear")
    os.system("tput setaf 6")
    if os.system("lvdisplay") == 0:
        os.system("tput setaf 2")
        print("LV displayed successfully")
    else:
        os.system("tput setaf 1")
        print("Could not display LV")
    input("Enter any key to continue")

def dmd():
    os.system("clear")
    os.system("tput setaf 2")
    os.system("df -h")
    input("Enter any key to continue")
