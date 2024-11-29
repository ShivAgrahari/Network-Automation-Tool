from flask import Flask, redirect, url_for, request,render_template
import time
# import script 
import set_op_script
import hostname
import snmp_host
import checklines

 
app = Flask(__name__)
    
@app.route("/")
def index():
    return render_template("index.html")


   
def write_to_file(router,filename):
     with open(filename, "w") as f:
        f.write(router) 
        f.flush()
        f.close()
        time.sleep(0.1)
        

def readfile(filename):
    devs = []
    new = open(filename, 'r')
    for line in new.read().splitlines():
        if(line != ''):
            devs.append(line)
    return devs


# def server_script(username, password, op,devs):
#    output = script.calling(username, password,op,devs)
#    return output


def server_setop(username, password,devs, operation, flag):
    set_op_script.calling(username, password,devs,operation, flag)

    #for getop server-----------------------

@app.route('/netcon', methods=['POST', 'GET'])
def netcon():
    if request.method == 'POST':
        # print("Netcon")
        user = request.form['user']
        password = request.form['password'] 
        router = request.form['router']  
        write_to_file(router,"ip adp.txt")
        devs= readfile("ip adp.txt")
         

        config = request.form['config']  
        write_to_file(config,"req configs.txt")
        conf  = readfile("req configs.txt")
         

        
        operation = request.form['operation']
        g=0
        if(operation == "sh run | in snmp-server host (check)"):
            g=1
            operation="sh run | in snmp-server host"
            

        
        flag=[]
        

        server_setop(user, password, devs, operation, flag)
         
         
        if flag[-1]=='1' and operation=='sh run | in hostname':

            ips,hos= hostname.readfile()
            formdata= {'user':user, 'ips':ips,  'operation': operation, 'hostoutput': hos}
            return render_template('hostname back.html', **formdata)
        
        elif flag[-1]=='1' and operation== 'sh run | in snmp-server host' and g==0:

            ips,hos, snmp_op= snmp_host.readfile()
            data= {'ips':ips, 'operation':operation, 'hos':hos, 'snmp_op':snmp_op}             
            return render_template('snmp back.html', **data)


        
        elif flag[-1]=='1' and operation== 'sh run | in snmp-server host' and g==1:

            ips,hos,match, absent, extra= checklines.checklines(conf)
            data= {'ips':ips, 'operation':operation, 'hos':hos, 'match':match, 'absent':absent, 'extra':extra}             
            return render_template('checklines.html', **data)
        
        
        elif flag[-1]=='0':
             
            return render_template('login failed.html')

        
        else:     
        
         return render_template('failed1.html')
        
        
    
    else:
        host = request.args.get('host')
        return redirect(url_for('success', name=host))
    
if __name__ == '__main__':
      app.run(debug=True, port=5001)
    #----------------------

    #for script server

# @app.route('/netcon', methods=['POST', 'GET'])
# def netcon():
#     if request.method == 'POST':
        
#         user = request.form['user']
#         password = request.form['password'] 
#         router = request.form['router']   
#         write_to_file(router)
#         devs= readfile()

#         router= router.split("\r\n")        
#         operation = request.form['operation']
#         op_val =[]        

#         hos= server_script(user, password, op_val, devs)
        
#         print("host name in output: ")
#         print(hos)
                               
#         formdata= {'user':user, 'router':router,  'operation': operation, 'hostoutput':hos}

#         return render_template('back.html', **formdata)
    
#     else:
#         host = request.args.get('host')
#         return redirect(url_for('success', name=host))
    
