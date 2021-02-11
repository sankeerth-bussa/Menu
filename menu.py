#!/usr/bin/python3

import os
import aws_menu
import hadoop_menu
import docker_menu
import lvm_menu

def menu():
    while True:
        os.system("clear")
        os.system("tput setaf 1")
        print("\n\n\t\t\t\t\tCONTROLLER")
        os.system("tput setaf 7")
        print("\n\t\t####################################################################")
        print("""\t\t\t Press 1: AWS
             \t\t Press 2: Hadoop
             \t\t Press 3: Docker
             \t\t Press 4: LVM Partitions
             \t\t Press 0: Exit""")
        print("\t\t####################################################################")

        os.system("tput setaf 3")
        print("\n\t\t\tEnter your Choice : ",end=" ")
        y = int(input())
        if y == 1:
            aws_menu.aws()
        elif y == 2:
            hadoop_menu.hadoop()
        elif y == 3:
            docker_menu.docker()
        elif y == 4:
            lvm_menu.lvm_menu()
        elif y == 0:
            exit()
        else:
            os.system("tput setaf 3")
            print("Wrong choice!!!")
            input("Enter any key to continue")

menu()
