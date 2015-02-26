#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-1-8

@author: pan
'''
import platform
import os
import subprocess
from __builtin__ import str


def get_cpu_info(sys,infolist): 
    cpuinfo=dict()
    procinfo=dict()
    tempdict = dict()
    if sys == "Linux":
        ''' Return the information in /proc/cpuinfo
    as a dictionary in the following format:
    cpu_info['proc0']={...}
    cpu_info['proc1']={...}
    '''
        nprocs = 0
        f = file("/proc/cpuinfo",'r')
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            if not line.strip():
                # end of one processor
                cpuinfo['proc%s' % nprocs] = procinfo
                nprocs=nprocs+1
                # Reset
                procinfo=dict()
            else:
                if len(line.split(':')) == 2:
                    temp1 = line.split(':')[0].strip()
                    temp2 = line.split(':')[1].strip()
                    tempdict[temp1] = temp2
                    print temp1+" : "+temp2
                else:
                    procinfo[line.split(':')[0].strip()] = ''
        infolist.append(tempdict)
   
    
def get_network_info(sys1,infolist):
    if sys1 == 'Linux':
        tmplist=list()
        ethlist = get_info('ifconfig -s|grep -v Iface|grep -v lo|awk \'{print $1}\'').split("\n")
        ethInfsys = get_info("lspci | grep Ethernet").split("\n")
        i = 0
        for ethi in ethlist:
            if ethi != "":
                tmpdict = dict()
                tmpdict["Description"] = ethInfsys[i].split(":")[2]
                tmpdict["IPAddress"] = get_info('ifconfig %s | awk \'/inet addr:/{ print $2 }\''%(ethi)).split(":")[1]
                tmpdict["IPSubnet"] = get_info('ifconfig %s | awk \'/Mask/{print $4}\''%(ethi)).split(":")[1]
                tmpdict["MAC"] = get_info('ifconfig %s | awk \'/HWaddr/{ print $5 }\''%(ethi))
                tmplist.append(tmpdict)
                i = i + 1
        for i in tmplist:
            print  i["Description"]
            print   '\t' + "MAC :" + '\t' + i["MAC"]
            print  '\t' + "IPAddress :" + '\t' + i["IPAddress"]
            print   '\t' + "IPSubnet :" + '\t' + i["IPSubnet"]
        infolist.append(tmplist)    
            
def get_info(cmd,bShell=True):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=bShell)
    return p.communicate()[0].split("\n")[0]

def get_disk_info(sys,infolist):
    if sys == "Linux":
        tmplist=list()
        devlist = get_info("parted -l |grep Disk").split("\n")
        for dev in devlist:
            if dev != "":
                tmpdict = dict()
                tmpdict["dev"] = dev.split()[1].split(":")[0]
                tmpdict["size"] = dev.split()[2]
                temp = get_info("hdparm -I  %s |awk \'/Model Number:/\'"%(tmpdict["dev"]))
                if temp !="":
                    tmpdict["disk"] = temp.split(":")[1]
                else:
                    tmpdict["disk"] = ""
                tmplist.append(tmpdict)
                print tmpdict["dev"]+":\t"+tmpdict["disk"] + ' :\t' + tmpdict["size"] 
        infolist.append(tmplist)
    
def get_mysql_info(sys,infolist):
    if sys == "Linux":
        templist = list()
        tempdict = dict()
        templist = get_info("ps -ef|grep mysqld|grep basedir").split("--")
        if len(templist)==0:
            tempdict["mysql"]=False
            print "mysql server:"+str(tempdict["mysql"])
        else:
            tempdict["mysql"]=True
            print "mysql server:"+str(tempdict["mysql"])
            for i in templist:
                if i.find("basedir")>=0:
                    tempdict["basedir"]=i.split("=")[1].split()[0]
                    print "basedir:"+tempdict["basedir"]
                if i.find("datadir")>=0:
                    tempdict["datadir"]=i.split("=")[1]
                    print "datadir:"+tempdict["datadir"]
        #version 
            binpath =  tempdict["basedir"]+"/bin/mysql"
            if os.path.exists(binpath):
                ver = get_info(tempdict["basedir"]+"/bin/mysql -V")
                tempdict["version"] = ver.split("mysql")[1]
                print "version:"+tempdict["version"]
            else:
                tempdict["version"]=""
    infolist.append(tempdict)
        
def get_oracle_info(sys,infolist):
    if sys == "Linux":
        tempdict = dict()

        temp = get_info(" ps -ef |grep oracle |awk \'/LISTENER/{print $8}\'")
        if temp=="":
            tempdict["oracle"]=False
            print "oracle server:"+str(tempdict["oracle"])
        else:
            tempdict["oracle"]=True
            print "oracle server:"+str(tempdict["oracle"])
            tempdict["basedir"] = temp.split("bin")[0]
            print "basedir:"+tempdict["basedir"]
        #version
            p = subprocess.Popen("su - oracle -c \'sqlplus -v\'", stdout=subprocess.PIPE, shell=True)
            ver = p.communicate()[0].split("\n")[1]
            tempdict["version"] = ver.split(":")[1]  
            print "version:"+tempdict["version"]         
    infolist.append(tempdict)
  
if __name__ == "__main__":
    sys = platform.system()
    infolist = list()
    get_mysql_info(sys,infolist)
    get_oracle_info(sys, infolist)
        
    