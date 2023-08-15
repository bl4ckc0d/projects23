#!/bin/python

import datetime
import platform
import os

while True:
    try:
        endereco_ip = input("Digite o Endereco da Rede: ")
    except ValueError:
        print("Endereco Nulo! ")
        continue
    else:
        if endereco_ip == "":
           print("Valor Nulo!")
           print("___")     
        break   
try:
    ip_parts = endereco_ip.split('.')
    network_ip = ip_parts[0]+'.'+ip_parts[1]+'.'+ip_parts[2]+'.'
except:
    print("Digite um Endereco Valido! ")  
else:
    primeiro_host = int(input("Digite o Primeiro Host: "))
    if primeiro_host =="":
        print("Primeiro Host Nulo")
finally:
    print("____________________")
try:
    ultimo_host = int(input("Digite o Ultimo Host: "))
    ultimo_host += 1
except:
    print("Digite um Endereco Valido! ")
finally:
    print("____________________")
oper = platform.system()
if(oper == "Windows"): 
   ping = "ping -n 1"
else:
    ping = "ping -c 1"

time1 = datetime.datetime.now()
print("Busca em andamento...")
for ip in range(primeiro_host, ultimo_host):
    addr = network_ip + str(ip)
    command = addr 
    response = os.popen(command)
    list = response.readlines()
    print (command)
    for line in list:
        if(line.count("TTL")):
          print(addr, "-->> Activo") 
        break   
time2 = datetime.datetime.now()  
total = time2 - time1
print("Busca terminada em: ", total)