def readfile():
    op_list= []
    ip_list= []
    hostname_list= []

    new = open("in snmp-server host output.txt", 'r')
    for line in new.readlines():            

        output = line
        # output =  "7.160.127.55\n hostname hyd1alregnsw955\n Device name: $(hostname).$(domain)"
        
        output=output.split("\\n")
         
        op_list.append(output[:-2]) 
        
        ip = output[-1].rstrip()
        ip_list.append(ip)
        hostname_list.append(output[-2])
        

    return ip_list,hostname_list,op_list

# ip, hos, op = readfile()
# print(ip)

    
 