def checklines(target):
    
    file = "in snmp-server host output.txt"
    # target= ["snmp-server host 7.10.254.67 version 2c R3d50xS",'snmp-server host 7.6.192.24 version 2c nAc5snmp' ,"snmp-server host 7.188.117.6 version 2c nAc5snmp" ,"in target only line"]

    ip_list= []
    hostname_list= []
    match=[]
    absent = []
    extra =[]
    with open(file, 'r') as file:
        for line in file.readlines(): 
            output = line
            output=output.split("\\n")
             
            # print(len(output[:-2]))  
            ip = output[-1].rstrip()
            ip_list.append(ip)
            hostname_list.append(output[-2])           
    
            matchingline = [line for line in target if line.strip() in output[:-2]]
            absentline = [line for line in target if line.strip() not in output[:-2]]            
            extraline = [line for line in output[:-2] if line.strip() not in target]
           
            if matchingline:
                match.append(matchingline)
            else:
                matchingline = ["no match found"]
                match.append(matchingline)

            absent.append(absentline)
            extra.append(extraline)
    
    return ip_list, hostname_list, match, absent, extra
 

