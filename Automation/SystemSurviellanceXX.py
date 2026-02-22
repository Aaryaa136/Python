import psutil
import sys
import os
import time
import schedule
import threading

import smtplib
from email.message import EmailMessage

def send_mail(sender , app_password , receiver , subject , body , attachment = None):
    # Step 1 : Create Email object
    msg = EmailMessage()

    # Step 2 : Set mail headers
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    # Step 3 : Add mail body
    msg.set_content(body)

    # Step 4 : Add attachment

    for fname in attachment or []:
        fobj = open(fname,"rb")
        data = fobj.read()

        msg.add_attachment(data , maintype = "application" , subtype = "octet-stream" , filename = os.path.basename(fname))

        fobj.close()

    # Step 5 : Create SMTP SSL connection manually
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)       #(serverlocation , port)

    # Step 6 : Login using Gmail + App password
    smtp.login(sender , app_password)

    # Step 7 : Send the email
    smtp.send_message(msg)

    # Step 8 : Close connection manually
    smtp.quit()

def CreateLog(FolderName):
    Border = "-"*50
    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create folder")
            return

    else:
        os.mkdir(FolderName)
        print("Directory for log files gets created succesfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
    print("Log file gets created with name : ",FileName)

    fobj = open(FileName, "w")

    fobj.write(Border+"\n")
    fobj.write("---- Marvellous Platform Surveillance System -----\n")
    fobj.write("Log created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("----------------- System Report ------------------\n")
    
    #print("CPU Usage : ",psutil.cpu_percent())
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    mem = psutil.virtual_memory()
    #print("RAM usage : ",mem.percent)
    fobj.write("RAM usage : %s %%\n" %mem.percent)
    fobj.write(Border+"\n")

    fobj.write("\nDisk Usage Report\n")
    fobj.write(Border+"\n")

    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            #print(f"{part.mountpoint} used {usage.percent}%%")
            fobj.write("%s -> %s %% used\n" %(part.mountpoint, usage.percent))
        except:
            pass

    fobj.write(Border+"\n")

    net = psutil.net_io_counters()
    fobj.write("\nNetwrk Usage Report\n")
    fobj.write("Sent : %.2f MB\n" % (net.bytes_sent / (1024 * 1024)))
    fobj.write("Recv : %.2f MB\n" % (net.bytes_recv / (1024 * 1024)))
    fobj.write(Border+"\n")

    # Process LOG
    Data = ProcessScan()

    for info in Data:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name %s\n" %info.get("name"))
        fobj.write("Username %s\n" %info.get("username"))
        fobj.write("Status : %s\n" %info.get("status"))
        fobj.write("Start time : %s\n" %info.get("create_time"))
        fobj.write("CPU %% : %.2f\n" %info.get("cpu_percent"))
        fobj.write("Memory %% : %.2f\n" %info.get("memory_percent"))
        fobj.write("Thread Name : %s\n"%threading.current_thread().name)
        fobj.write("Thread PID : %s\n"%threading.get_ident())
        fobj.write("TCount : %s\n"%threading.active_count())
        fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("----------------- End of Log File ----------------\n")
    fobj.write(Border+"\n")

    fobj.close()
    return FileName

    
def ProcessScan():
    listprocess = []

    # Warm up for CPU percent
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid", "name", "username","status","create_time","cpu_percent","memory_percent","num_threads"])
            
            # Convert create_time
            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"
            
            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()

            try:
                open_files = proc.open_files()
                info["open_files_count"] = len(open_files)
            except (psutil.AccessDenied , psutil.NoSuchProcess):
                info["open_files_count"] = 0

            try:
                mem = proc.memory_info()
                info["rss_mb"] = mem.rss / (1024 * 1024)
                info["vms_mb"] = mem.vms / (1024 * 1024)
            except (psutil.AccessDenied , psutil.NoSuchProcess):
                info["rss_mb"] = 0
                info["vms_mb"] = 0
                
            listprocess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess

def CreateLogAndSend(FolderName):
    logfile = CreateLog(FolderName)

    sender_mail = "t3221447@gmail.com"

    # App password generalized generated from google account
    app_password = os.getenv("EMAIL_PASS")

    # Your second email for testing
    receiver_email = "patilaaryaa95@gmail.com"

    subject = "System Surviellance System Report"

    body = """Dear,

Please find attached system log report.

    Regards,
    Aaryaa Patil
    """

    send_mail(sender_mail , app_password , receiver_email , subject , body ,[logfile])

    print("Mail Sent Successfully")

def main():

    Border = "-"*50
    print(Border)
    print("---- Marvellous Platform Surveillance System -----")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This scipt is used to : ")
            print("1 : Create automatic logs")
            print("2 : Executes peroidically")
            print("3 : Sends mail with the log")
            print("4 : Store information about processess")
            print("5 : Store information about CPU")
            print("6 : Store information about RAM usage")
            print("7 : Store information about secondary storage")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("DirectoryName : Name of directory to create auto logs")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
    
    # python Demo.py 5 Marvellous
    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time interval : ",sys.argv[1])
        print("Directory name : ",sys.argv[2])

        # Apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(CreateLogAndSend, sys.argv[2])

        print("Platform Surveillance System started succesfully")
        print("Directory created with name : ",sys.argv[2])
        print("Time interval in minutes: ",sys.argv[1])
        print("Press Ctrl + C to stop the execution")

        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details") 

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)
    
if __name__ == "__main__":
    main()