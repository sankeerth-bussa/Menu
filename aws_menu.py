import os

def aws():
    while True:
        os.system("clear")
        os.system("tput setaf 1")
        print("\t\t\t\t\tAWS\n")
        os.system("tput setaf 7")
        print("\t\t#######################################################")
        print("""\t\t\t1. Configure AWS CLI
                        2. Login
                        3. EC2
                        4. S3
                        9. Back
                        0. Exit""")
        print("\t\t#######################################################")
        os.system("tput setaf 3")
        aws = int(input("\n\t\t\tEntr your choice: "))
        if aws == 1:
            aws_configure()
        elif aws == 2:
            aws_login()
        elif aws == 3:
            aws_ec2_menu()
        elif aws == 4:
            aws_s3_menu()
        elif aws == 9:
            os.system("clear")
            break
        elif aws == 0:
            exit()
        else:
            print("Wrong choice!!!")
    input("Press any key to continue")


def aws_configure():
    os.system("clear")
    os.system("tput setaf 5")
    print("Checking AWS CLI")
    if os.system("ls /usr/local/bin | grep aws") == 0:
        os.system("tput setaf 5")
        print("AWS CLI is already installed")
    else:
        os.system("tput setaf 6")
        print("Installing AWS CLI")
        os.system("curl \"https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip\" -o \"awscliv2.zip\"") 
        os.system("unzip awscliv2.zip")
        os.system("./aws/install")
        print("AWS CLI is successfully installed")
        os.system("aws --version")
    input("Press any key to continue")

def aws_login():
    os.system("tput setaf 1")
    print("Enter the credentials")
    os.system("aws configure")
    input("Press any key to continue")


def aws_ec2_menu():
    while True:
        os.system("clear")
        os.system("tput setaf 1")
        print("\n\t\t\t\t\t\tEC2")
        os.system("tput setaf 7")
        print("\t\t#############################################################")
        print("""\t\t\t\t1. Describe Instance
                        2. Create Key Pair
                        3. Launch Instance
                        4. Start Instance
                        5. Stop Instance
                        9. Back
                        0. Exit""")
        print("\t\t#############################################################")
        os.system("tput setaf 3")
        aws_ec2 = int(input("Enter your choice: "))
        if aws_ec2 == 1:
            ec2_describe()
        elif aws_ec2 == 2:
            ec2_create_key()
        elif aws_ec2 == 3:
            ec2_launch_instance()
        elif aws_ec2 == 4:
            ec2_start_instance()
        elif aws_ec2 == 5:
            ec2_stop_instance()
        elif aws_ec2 == 9:
            os.system("clear")
            break
        elif aws_ec2 == 0:
            exit()
        input("Press any key to continue")

def ec2_describe():
    if os.system("aws ec2 describe instance") == 0:
        print("The details of the specified instance")
        input("Press any key to continue")
    else:
        print("Cannot retrieve details, Try again!!")

def ec2_create_key():
    print("Enter key name: ",end='')
    key = input()
    if os.system("aws ec2 create-key-pair --key-name {key}") == 0:
        print("Key Pair has been created successfully")
    else:
        print("Could not create key pair, Try Again!!")
    input("Press any key to continue")

def ec2_launch_instance():
    print("Eneter image ID: ",end='')
    image = input()
    print("Enter Instance Type: ",end='')
    instance_type = input()
    print("Enter key name: ",end='')
    key = input()
    if os.system("aws ec2 run-instances --image-id {image} --instance-type {instance_type} --key-name {key}") == 0:
        print("Instance launched successfully")
    else:
        print("Could not launch instance, Try again!!")
    input("Press any key to continue")


def ec2_start_instance():
    print("Enter instance ID to start: ",end='')
    ID = input()
    if os.system("aws ec2 start-instances --instance-ids {ID}") == 0:
        print("Instance started successfully")
    else:
        print("Instance could not be started, Try again!!")
    input("Press any key to continue")


def ec2_stop_instance():
    print("Enter instance ID to start: ",end='')
    ID = input()
    if os.system("aws ec2 stop-instances --instance-ids {ID}") == 0:
        print("Instance stopped successfully")
    else:
        print("Instance could not be stopped, Try again!!")
    input("Press any key to continue")


def aws_s3_menu():
    while True:
        os.system("clear")
        print("""\t1. List Buckets
             2. Create Bucket
             3. Add Object to Bucket
             4. Delete Object from Bucket
             5. Delete Bucket
             9. Back
             0. Exit""")
        print("Enter your choice: ",end='')
        aws_s3 = int(input())
        
        if aws_s3 == 1:
            os.system("clear")
            s3_list_buckets()
        elif aws_s3 == 2:
            os.system("clear")
            s3_create_bucket()
        elif aws_s3 == 3: 
            os.system("clear")
            s3_add_object()
        elif aws_s3 == 4:
            os.system("clear")
            s3_delete_object()
        elif aws_s3 == 5:
            os.system("clear")
            s3_delete_bucket()
        elif aws_s3 == 9:
            os.system("clear")
            break
        elif aws_s3 == 0:
            exit()
        else:
            print("Wrong choice!!!")
        input("Press any key to continue")


def s3_list_buckets():
    os.system("clear")
    if os.system("aws s3api list-buckets") == 0:
        print("Active buckets in S3")
    else:
        print("Could not retrieve details, Try again!!")

def s3_create_bucket():
    os.system("clear")
    bname = input("Enter bucket name: ")
    region = input("Enter region: ")
    if os.system("aws s3 api --bucket {bname} --region {region}") == 0:
        print("Bucket created successfully")
    else:
        print("Could not create bucket, Try again!!")
    input("Press any key to continue")

def s3_add_object():
    os.system("clear")
    path = input("Enter path to file")
    key = input("Enter key of file in s3 bucket")
    bname = input("Enter bucket name: ")
    if os.system("aws s3api copy-object --copy-source {path} --key {key} --bucket {bname}"):
        print("Object added successfully")
    else:
        print("Could not add object, Try again!!")
    input("Press any key to continue")

def s3_delete_object():
    os.system("clear")
    print("Enter object to be deleted: ",end='')
    object_name = input("Enter object to be deleted: ")
    bname = input("Enter bucket in which object is located: ")
    if os.system("aws s3api delete-object --bucket {bname] --key {object_name}"):
        print("Object deleted successfully")
    else:
        print("Could not delete object, Try again!!")
    input("Press any key to continue")

def s3_delete_bucket():
    os.system("clear")
    bname = input("Enter bucket name: ")
    region = input("Enter region: ")
    if os.system("aws s3api --bucket {bname} --region {region}"):
        print("Bucket deleted successfully")
    else:
        print("Could not delete bucket, Try again!!")
    input("Press any key to continue")
