import getpass
import re
import os
from netmiko.ssh_dispatcher import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException
import time
from netmiko import ConnectHandler
import subprocess
from threading import Thread

threads = []
# devs = []
badlog = []
 

        


def devtype(ipa,username, password, operation, flag):
    try:
        ipa=ipa.rstrip()
 
        #Uncomment the following to allow login funcitonality----------------------
        device = ConnectHandler(device_type='cisco_ios', ip=ipa, username=username, password=password)
        print(operation)         
        output = device.send_command(operation)
        print(output)
        output = repr(output)[1:-1]
      

        flag.append("1")
        
        #storing the output of the device into a text file-----------------------
        
        if(operation == "sh run | in hostname"):

            #comment this 
            # if(ipa =="7.160.127.55"):
            #     output = "hostname hyd1alregnsw955\n Device name: $(hostname).$(domain)" 
            # elif(ipa =="7.160.127.57"):
            #     output = "hostname hyd1alregnsw957" 
            # elif(ipa =="7.160.127.58"):
            #     output = "hostname hyd1alregnsw958" 
            # else:
            #     output = "hostname hyd1alregnsw000"
           

            # output = repr(output)[1:-1]
             #---------------
            
            with open('in hostname output.txt', 'a') as f:
                    f.write(ipa + "\\n "+ output + "\n")


        elif(operation == "sh run | in snmp-server host"): 
            #comment this------------------- 
            #  output ="snmp-server host 7.10.254.67 version 2c R3d50xS\nsnmp-server host 7.10.254.77 version 2c R3d50xS\nsnmp-server host 7.6.254.77 version 2c R3d50xS\nsnmp-server host 7.6.255.217 version 2c R3d50xS\nsnmp-server host 7.7.7.1 version 2c Yank33S\nsnmp-server host 7.10.192.24 version 2c nAc5snmp\nsnmp-server host 7.188.117.38 version 2c nAc5snmp\nsnmp-server host 7.188.117.6 version 2c nAc5snmp\nsnmp-server host 7.6.192.24 version 2c nAc5snmp\nhyd1alregnsw958"
            #  output = repr(output)[1:-1]
            #-------------------------------

             with open('in snmp-server host output.txt', 'a') as f:
                  f.write(output + "\\n"+ ipa+"\n")    

             
       
       
        #--------------------------------------------------------------------------
  
    except NetmikoAuthenticationException:
           print("login failed")
           flag.append("0")
    
    except Exception as e:
            e=str(e)
            ipa=str(ipa)
            ipa=ipa.rstrip()
            print ("Exception for "+ipa+" :- "+e) 

def calling(username, password, devs,operation, flag):
    
    flag.append("-1") 

    #------Output file in login

    if operation=='sh run | in hostname':
            with open('in hostname output.txt', 'w') as file:
                pass 
    elif operation =='sh run | in snmp-server host' or operation == 'sh run | in snmp-check':
             with open('in snmp-server host output.txt', 'w') as f:
                pass

    
   
    for ip in devs:
        t = Thread(target=devtype, args= (ip, username, password,operation, flag))
        t.start()
        threads.append(t)     
       

    for t in threads:
        t.join()

    
    
 

     