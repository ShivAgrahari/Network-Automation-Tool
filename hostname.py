def readfile():
    ip_list=[]
    hostname_list   = []
    new = open("in hostname output.txt", 'r')
    for line in new.readlines():            
         
            output = line
            # output =  "7.160.127.55\n hostname hyd1alregnsw955\n Device name: $(hostname).$(domain)"
             
            
            output=output.split("\\n")
            
            ip = output[0]
            ip_list.append(ip)

            output1=output[1].split(" ")  

            hostname = output1[2]
            hostname=hostname.rstrip()
            hostname_list.append(hostname)
            
    
    return ip_list, hostname_list
                         
 
        
 