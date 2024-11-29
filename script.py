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
 


def devtype(ipa,username, password,result):
    try:
        ipa=ipa.rstrip()
#model="null"
#wlc="check manually"
        #Uncomment the following to allow login funcitonality----------------------
        # device = ConnectHandler(device_type='cisco_ios', ip=ipa, username=username, password=password)         
        # output = device.send_command("sh run | in hostname")
        #--------------------------------------------------------------------------
        output = "hostname hyd1alregnsw955\n Device name: $(hostname).$(domain)"
         
        output=output.split("\n")
       
        output1=output[0].split(" ")
       
        hostname=output1[1]
        hostname=hostname.rstrip()
              
        result.append(hostname) 
        
        print(result)
        print ("****************")
        
        #print (output)

    except NetmikoAuthenticationException:
           print("login failed")
    
    except Exception as e:
            e=str(e)
            ipa=str(ipa)
            ipa=ipa.rstrip()
            print ("Exception for "+ipa+" :- "+e) 

def calling(username, password, op, devs):
    op.clear()
    print("devs in script")
    print(devs)
    for ip in devs:
        t = Thread(target=devtype, args= (ip, username, password, op))
        t.start()
        threads.append(t)      
       

    for t in threads:
        t.join()

    print("t: ")
    print(t) 
    return op
    
 

     