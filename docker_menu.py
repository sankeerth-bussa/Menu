import os

def docker():
    while True:
        os.system("clear")
        os.system("tput setaf 1")
        print("\t\t\t\t\t\tDOCKER")
        os.system("tput setaf 7")
        print("\t\t#############################################################")
        print("""\t\t\t1. Configure Docker
                        2. Start Docker
                        3. List Images
                        4. Pull Image
                        5. List Running Containers
                        6. Launch Container
                        7. Start Container
                        8. Stop Container
                        9. Delete Container
                        10. Back
                        0. Exit""")
        print("\t\t#############################################################")
        os.system("tput setaf 3")
        ch = int(input("\nEnter your choice: "))
        if ch == 1:
            configure_docker()
        elif ch ==2:
            start_docker()
        elif ch == 3:
            list_images()
        elif ch == 4:
            pull_image()
        elif ch == 5:
            list_containers()
        elif ch == 6:
            launch_container()
        elif ch == 7:
            start_container()
        elif ch == 8:
            stop_container()
        elif ch == 9:
            delete_container()
        elif ch == 10:
            os.system("clear")
            break
        elif ch == 0:
            os.system("clear")
            exit()
        else:
            print("Wrong choice!!!")
    input("Enter any key to continue")

def configure_docker():
    os.system("clear")
    os.system("tput setaf 4")
    if os.system("rpm -q docker-ce") == 0:
        os.system("tput setaf 2")
        print("Docker is already installed")
    else:
        os.system("tput setaf 2")
        print("Installing Docker")
        os.system("echo \"[docker]\" >> /etc/yum.repos.d/docker.repo")
        os.system("echo \"baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\" >> /etc/yum.repos.d/docker.repo")
        os.system("echo \"gpgcheck=0\" >> /etc/yum.repos.d/docker.repo")
        os.system("yum install docker-ce --nobest -y")
        print("Docker installed successfully")
    input("Enter any key to continue")

def start_docker():
    os.system("clear")
    os.system("tput setaf 6")
    if os.system("systemctl start docker") == 0:
        os.system("tput setaf 2")
        print("Docker has started successfully")
    else:
        os.system("tput setaf 1")
        print("Docker could not be started, Try again!!")
    input("Enter any key to continue")

def list_images():
    os.system("clear")
    os.system("tput setaf 6")
    if os.system("docker images") == 0:
        os.system("tput setaf 2")
        print("These are docker images downloaded")
    else:
        os.system("tput setaf 1")
        print("Cannot display images, Try again!!")
    input("Enter any key to continue")

def pull_image():
    os.system("clear")
    os.system("tput setaf 6")
    image = input("Enter image to pull: ")
    if os.system("docker pull {image}") == 0:
        os.system("tput setaf 2")
        print("Image downloaded successfully")
    else:
        os.system("tput setaf 1")
    input("Enter any key to continue")

def list_containers():
    os.system("tput setaf ")
    os.system("clear")
    os.system("docker ps -a")
    input("Enter any key to continue")

def launch_container():
    os.system("clear")
    os.system("tput setaf 6")
    cname = input("Enter container name: ")
    img = input("Enter image: ")
    if os.system("docker run -it --name {cname} {img}") == 0:
        os.system("tput setaf 2")
        print("Container launched successfully")
    else:
        os.system("tput setaf 1")
        print("Container could not be launched, Try again!!")
    input("Enter any key to continue")
    
def start_container():
    os.system("clear")
    os.system("tput setaf 6")
    cname = input("Enter container name start: ")
    if os.system("docker start -a {cname}") == 0:
        os.system("tput setaf 2")
        print("Container started successfully")
    else:
        os.system("tput setaf 1")
        print("Container could not be started, Try again!!")
    input("Enter any key to continue")

def stop_container():
    os.system("clear")
    os.system("tput setaf 6")
    cname = input("Enter container name to stop: ")
    if os.system("docker stop {cname}") == 0:
        os.system("tput setaf 2")
        print("Container stopped succesfully")
    else:
        os.system("tput setaf 1")
        print("Container could not be stopped, Try again!!")
    input("Enter any key to continue")

def delete_container():
    os.system("clear")
    os.system("tput setaf 6")
    cname = input("Enter container name to delete")
    if os.system("docker rm {cname}") == 0:
        os.system("tput setaf 2")
        print("Container deleted succesfully")
    else:
        os.system("tput setaf 1")
        print("Container could not be deleted, Try again!!")
    input("Enter any key to continue")
