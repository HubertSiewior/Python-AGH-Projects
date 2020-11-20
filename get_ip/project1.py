#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import socket
import subprocess


def if_the_ip_is_ok(ip):

    i, count = 0, 0

    maska = ip.split("/")
    maska1=maska[0]
    maska = maska[1]
    maska1.split(".")
    xxx=maska1.split(".")


    if not maska.isdigit():
        return False
    for x1 in xxx:
      if not x1.isdigit():
          return False


    if(len(ip)<0 or len(ip)>18):
        return False
    for x in range(0,4):
        j=ip.find(".",i)
        if(j<0):
            j=ip.find("/",i)
        xxx=ip[i:j]
        i=j+1
        count+=1
        if(int(xxx)<0 or int(xxx)>255):
            return False
    if(count!=4):
        return False

    if(int(maska)<0 or int(maska)>32):
        return False
    for x in range(1, len(ip)):
         if ((ip[x] == '.' and ip[x - 1] == '.') or (ip[x] == '/' and ip[x - 1] == '/')):
              return False

    return True

def ping(ip):
    hostname = ip
    response = os.system("ping " + hostname)

    if response == 0 :
        print(hostname, 'is up!')
    else :
        print(hostname, 'is down!')

def to_bin(ip):

    good = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    for x in range(0,len(ip)):
        if(x not in good):
            xx=ip.split("/")
            ip=xx[0]
    result = ""
    i = 0
    for x in range(0, 3) :
        j = ip.find('.', i)
        xxx = ip[i :j]
        i = j + 1
        result += '{0:08b}'.format(int(xxx)) + "."
    result += '{0:08b}'.format(int(ip[i :]))
    return result

def network_class(ip):
    substring = ip[:ip.find('.')]
    if (int(substring)<128) :
        return " This is class A "
    elif (int(substring)<192) :
        return " This is class B "
    elif (int(substring)<224):
        return "This is class C"
    elif (int(substring)<240):
        return "This is class D"
    else:
        return "This is class E"

def maska_na_bin(ip):

    bin_mask=int(ip[ip.find("/") + 1 :])
    maska=""
    for x in range(0, 32) :
        if bin_mask>0:
            maska+="1"
            bin_mask-=1
        else:
            maska+="0"
            bin_mask -= 1

    maska = maska[:8] + '.' + maska[8 :]
    maska = maska[:17] + '.' + maska[17 :]
    maska = maska[:26] + '.' + maska[26 :]

    return maska

def to_dec(bin):
    result,result1,result2,result3=0,0,0,0
    i1,i2,i3,i4=7,7,7,7

    for i in range(0,8):
        if(bin[i]=='1'):
            result+=2**i1
            i1-=1
        else:
            i1-=1
    for j in range(9,17):
        if (bin[j] == '1') :
            result1 += 2 ** i2
            i2 -= 1
        else:
            i2-=1
    for k in range(18,26):
        if (bin[k] == '1') :
            result2 += 2 ** i3
            i3 -= 1
        else:
            i3-=1
    for k in range(27,35):
        if (bin[k] == '1') :
            result3 += 2 ** i4
            i4 -= 1
        else:
            i4-=1
    substring=str(result)+"."+str(result1)+"."+str(result2)+"."+str(result3)
    return substring


def bin_mask_to_int(bin):
    count=0
    for i in range(0,len(bin)):
        if(bin[i]=="1"):
            count+=1

    return count

def network(sub1,sub2):
    if len(sub1) != len(sub2) :
        sys.stderr.write("ERROR ")
        return 0
    result = ""
    for x in range(0, len(sub1)) :
        if sub1[x] == '.' :
            result += '.'
        else :
            if sub1[x] == '1' and sub2[x] == '1' :
                result += '1'
            else :
                result += '0'

    return to_dec(result)

def broadcast(sub1,sub2):

    if len(sub1) != len(sub2) :
        sys.stderr.write("ERROR ")
        return 0
    result = ""
    for x in range(0, len(sub1)) :
        if sub1[x] == '.' :
            result += '.'
        else :
            if sub1[x] == '0' :
                result += '1'
            else :
                result += sub2[x]
    return to_dec(result)



def maxHost(broad):
   tmp = broad.split(".")
   i = 0
   substring=""
   for x in tmp:
       i += 1
       if i==4:
           substring+=str(int(x)-1)
           break
       substring +=str(x)+"."

   return substring

def minHost(net):

    tmp=net.split(".")
    i=0
    substring=""
    for x in tmp:
        i += 1
        if i==4:
            substring+=str(int(x)+1)
            break
        substring += str(x) + "."
    return substring

def allHosts(x):

    result=2**(32-x)-2
    return result



def get_address():
    return get_ip() + "/" + str(to_bin(get_mask()).count('1'))



def get_mask():
    ip = socket.gethostbyname((socket.gethostname()))
    proc = subprocess.Popen('ipconfig', stdout=subprocess.PIPE)
    while True:
        line = proc.stdout.readline()
        if str(ip).encode() in line:
            break
    mask = str(proc.stdout.readline()).rstrip().split(":")[-1].replace(' ', '')
    return mask[:-5]


def get_ip():
    return socket.gethostbyname((socket.gethostname()))

def Private_or_Public(ip):

    ip2 = ip[:ip.find('/')]
    if ip[:ip.find('.')] == "10" :
        return "Is Private"
    elif ip[:ip.find('.')] == "172" :
        ip3 = ip[ip.find('.') + 1 : ip.find('.', ip.find('.') + 1)]
        if (16 <= int(ip3) <= 31) :
            return "Is Private"
    elif ip[:ip.find('.', ip.find('.') + 1)] == "192.168" :
        return "Is Private"
    else :
      return "Is public"







def main():
    ip="192.168.102.241/25"
    ip2 = "aaaa"




    try:

       f = open("file.txt", "w+")
       if not if_the_ip_is_ok(ip):
           ip=get_address()
       print(ip)
       f.write("IP " + Private_or_Public(ip) + "\n")
       f.write("adres   "+ip+"\n")
       f.write("maska dec   "+to_dec(maska_na_bin(ip))+"\n")
       f.write("maska na bin   "+maska_na_bin(ip)+"\n")
       #ping(ip.split("/")[0])
       f.write(network_class(ip)+"\n")
       a = maska_na_bin(ip)
       b = to_bin(ip)
       c = network(a, b)
       x = int(bin_mask_to_int(a))
       d = broadcast(a, b)
       f.write("NETWORK ADDRESS dec   "+c+"\n")
       f.write("NETWORK ADDRESS bin    " +to_bin(c)+"\n")
       f.write("BROADCAST ADDRESS dec   "+d+"\n")
       f.write("BROADCAST ADDRESS bin   " + to_bin(d) + "\n")
       f.write(("MIN HOST dec " +minHost(c)+"\n"))
       f.write(("MIN HOST bin " + to_bin(minHost(c)) + "\n"))
       f.write("MAX HOST  dec  "+maxHost(d)+"\n")
       f.write("MAX HOST  bin  " + to_bin(maxHost(d)) + "\n")
       f.write("Number of all hosts  " + str(allHosts(x))+"\n")



       f.close()
    except ValueError:
            print("Uch! ERROR Spróbuj jeszcze raz...")







if __name__ == '__main__':
        sys.exit(main())



