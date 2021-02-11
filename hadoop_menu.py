import os

def hadoop():
    while True:
        os.system("clear")
        os.system("tput setaf 1")
        print("\t\t\t\t\t\tS3")
        os.system("tput setaf 7")
        print("\t\t#############################################################")
        print("""\t\t\t1. Configure Hadoop
                        2. Format
                        3. Start Hadoop
                        4. Display Report
                        5. List files in Cluster
                        6. Read a File in Cluster
                        7. Upload a File into Cluster
                        8. Stop Hadoop
                        9. Back
                        0. Exit""")
        print("\t\t#############################################################")
        os.system("tput setaf 3")
        had = int(input("\nEnter your choice: "))
        if had == 1:
            had_configure()
        elif had == 2:
            had_format()
        elif had == 3:
            had_start()
        elif had == 4:
            had_report()
        elif had == 5:
            had_list()
        elif had == 6:
            had_read()
        elif had == 7:
            had_upload()
        elif had == 8:
            had_stop()
        elif had == 9:
            os.system("clear")
            break
        elif had == 0:
            exit()
        else:
            print("Wrong choice!!!")
    input("Enter any key to continue")

def had_configure():
    os.system("clear")
    os.system("tput setaf 4")
    if os.system("rpm -q jdk1.8") != 0:
        jdk = input("Provide path to JDK: ")
        if os.system("rpm -i jdk-8u171-linux-x64.rpm") == 0:
            os.system("tput setaf 2")
            print("JDK installed successfully")
        else:
            os.system("tput setaf 1")
            print("JDK could not be installed, Try again")
    if os.system("rpm -q hadoop") != 0:
        hadoop = input("Provide path to hadoop:")
        if os.system("rpm -i hadoop-1.2.1-1.x86_64.rpm --force"):
            os.system("tput setaf 2")
            print("Hadoop installed successfuly")
        else:
            os.system("tput setaf 1")
            print("Hadoop could not be installed, Try again!")
        print("Hadoop installed successfully")
    
    os.system("tput setaf 4")
    print("Configuring hdfs-site.xml")
    node = input("Select master or data")
    os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
    os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
    os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
    os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/hdfs-site.xml")
    os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
    os.system("echo '<configuration>' >> /etc/hadoop/hdfs-site.xml")
    os.system("echo '<property>' >> /etc/hadoop/hdfs-site.xml")
    dirc = input("Enter the directory you want to assign: ")
    if node == "name":
        os.system("echo '<name>dfs.name.dir</name>' >> /etc/hadoop/hdfs-site.xml")
    elif node == "data":
        os.system("echo '<name>dfs.data.dir</name>' >> /etc/hadoop/hdfs-site.xml")
    os.system("echo '<value>%s</value>' >> /etc/hadoop/hdfs-site.xml" %dirc)
    os.system("echo '</property>' >> /etc/hadoop/hdfs-site.xml")
    os.system("echo '</configuration>' >> /etc/hadoop/hdfs-site.xml")
    print("Finished configuring hdfs-site.xml")
    
    os.system("tput setaf 6")
    print("Configuring core-site.xml")
    os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
    os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
    os.system("echo ' ' >> /etc/hadoop/core-site.xml")
    os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/core-site.xml")
    os.system("echo ' ' >> /etc/hadoop/core-site.xml")
    os.system("echo '<configuration>' >> /etc/hadoop/core-site.xml")
    os.system("echo '<property>' >> /etc/hadoop/core-site.xml")
    os.system("echo '<name>fs.default.name</name>' >> /etc/hadoop/core-site.xml")
    master_ip = input("Enter the IP of the Namenode : ")
    os.system("echo '<value>hdfs://%s:9001</value>' >> /etc/hadoop/core-site.xml" %(master_ip))
    os.system("echo '</property>' >> /etc/hadoop/core-site.xml")
    os.system("echo '</configuration>' >> /etc/hadoop/core-site.xml")
    print("Finished configuring core-site.xml")
    input("Enter any key to continue")

def had_format():
    os.system("clear")
    os.system("tput setaf 4")
    print("Formatting namenode")
    if os.system("hadoop namenode -format") ==0:
        os.system("tput setaf 2")
        print("Formatting namenode completed")
    else:
        os.system("tput setaf 1")
        print("Unsuccessful in formatting namenode")

def had_start():
    os.system("clear")
    os.system("tput setaf 4")
    node = input("Select master or data")
    if node == "name":
        print("Starting namenode")
        if os.system("hadoop-daemon.sh start namenode") == 0:
            os.system("tput setaf 2")
            print("Namenode started successfully")
        else:
            os.system("tput setaf 1")
            print("Could not start namenode, Try again!!")
    elif node == "data":
        print("Starting datanode")
        if os.system("hadoop-daemon.sh start datanode") == 0:
            os.system("tput setaf 2")
            print("Datanode started successfully")
        else:
            os.system("tput setaf 1")
            print("Could not start datanode, Try again!!")
    input("Enter any key to continue")

def had_report():
    os.system("clear")
    os.system("tput setaf 4")
    if os.system("hadoop dfsadmin -report") == 0:
        os.system("tput setaf 2")
    else:
        os.system("tput setaf 1")
        print("Could not retrieve cluster report")
    input("Enter any key to continue")

def had_list():
    os.system("clear")
    os.system("tput setaf 4")
    if os.system("hadoop fs -ls /") == 0:
        os.system("tput setaf 2")
        print("Files in cluster")
    else:
        os.system("tput setaf 1")
        print("Could not retrieve, Try again!!")
    input("Enter any key to continue")

def had_read():
    os.system("clear")
        os.system("tput setaf 4")
    f = input("Enter file to read: ")
    if os.system("hadoop fs -cat /{f}".format(f)) == 0:
        os.system("tput setaf 2")
        print("File retrieved successfully")
    else:
        os.system("tput setaf 1")
        print("Could not retrieve file")
    input("Enter any key to continue")

def had_upload():
    os.system("clear")
        os.system("tput setaf 4")
    f = input("Enter file to upload: ")
    if os.system("hadoop fs -put {f} /".format(f))
        os.system("tput setaf 2")
        print("File uploaded successfully")
    else:
        os.system("tput setaf 1")
        print("Could not upload file, Try again")
    input("Enter any key to continue")

def had_stop():
    os.system("clear")
        os.system("tput setaf 4")
    node = input("Select master or data")
    if node == "name":
        if os.system("hadoop-daemon.sh stop namenode") == 0:
            os.system("tput setaf 2")
            print("Namenode stopped successfully")
        else:
            os.system("tput setaf 1")
            print("Failed to stop namenode, Try again!!")
    elif node == "data":
        if os.system("hadoop-daemon.sh stop datanode") == 0:
            os.system("tput setaf 2")
            print("Datanode stopped successfully")
        else:
            os.system("tput setaf 1")
            print("Failed to stop datanode, Try again!!")
    input("Enter any key to continue")
