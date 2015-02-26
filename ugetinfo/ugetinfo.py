#!/usr/bin/env python
#-*- coding: UTF-8 -*-
'''
Created on 2015-1-4

@author: pan
'''
import platform
import WinInfo
import linuxInfo
import memInfo
import diskInfo
import time
import operation
from optparse import OptionParser
try:
    import wmi
except ImportError:
    wmi = None

#version list0
def version(option, opt_str, value, parser):
    ver = "ugetinfo version v1.0.0.1 20150106"
    print ver
#store to dictionary
    if option == True:
        infoDict = dict()
        infoDict["version"]=ver
        infoDict["generate_time"]=str(int(time.time()))
        infolist.append(infoDict)
    
#show all information
def all_info(option, opt_str, value, parser):
    print "----all information----"
    operation.init()
    
    version(True, opt_str, value, parser)
    operation.version_xml(infolist)
    
    uname(True, opt_str, value, parser)
    architecture(True, opt_str, value, parser)
    operation.os_info_xml(infolist, os)
    
    cpu(True, opt_str, value, parser)
    try:
        operation.cpu_info_xml(infolist)
    except Exception,e:
        print "Error:",e
    
    network(True, opt_str, value, parser)
    try:
        operation.network_info_xml(infolist)
    except Exception,e:
        print "Error:",e
   
    
    memory(True, opt_str, value, parser)
    try:
        operation.memory_info_xml(infolist)
    except Exception,e:
        print "Error:",e

    
    disk(True, opt_str, value, parser)
    try:
        operation.disk_info_xml(infolist)
    except Exception,e:
        print "Error:",e
    
    
    operation.bksrc_init()
    
    mysql(True, opt_str, value, parser)
    try:
        operation.mysql_info_xml(infolist)
    except Exception,e:
        print "Error:",e
    
    oracle(True, opt_str, value, parser)
    try:
        operation.oracle_info_xml(infolist)
    except Exception,e:
        print "Error:",e
    
    sqlserver(True, opt_str, value, parser)
    try:
        operation.sqlserver_info_xml(infolist)
    except Exception,e:
        print "Error:",e  
    
    sybase(True, opt_str, value, parser)
    try:
        operation.sybase_info_xml(infolist)
    except Exception,e:
        print "Error:",e     
    
    operation.write_xml(xmlFile)
    
#show define file name
def fileName(option, opt_str, value, parser):
    xmlFile = value

#uname list1
def uname(option, opt_str, value, parser):
    print "------uname information------" 
    tempInfo = platform.uname()
    print "system:\t"+tempInfo[0]
    print "machine name:\t"+tempInfo[1]
    print "release version:\t"+tempInfo[2]
    print "system version:\t"+tempInfo[3]
    print "machine:\t"+tempInfo[4]
    print "processor:\t"+tempInfo[5]
    temp = ""
    if os != "Windows":
        dist = platform.dist()
        temp = dist[0]
        print "linux_distribution:\t"+temp
    
#store to dictionary
    if option == True:
        infoDict = dict()
        infoDict["utype"]=tempInfo[0]
        infoDict["host_name"] = tempInfo[1]
        infoDict["uversion"] = tempInfo[3]
        infoDict["uarch"] = tempInfo[4]
        infoDict["umode"] = tempInfo[5]
        if os == "Linux":
            infoDict["udist"]=temp
        infolist.append(infoDict)
    
#architecture list2
def architecture(option, opt_str, value, parser):
    print "------architecture information------"
    tempinfo = platform.architecture()
    print "system bit:\t"+tempinfo[0]
    print "system linkage:\t"+tempinfo[1]
#store to dictionary
    if option == True:
        infoDict = dict()
        infoDict["Abit"]=tempinfo[0]
        infoDict["Alink"]=tempinfo[1]
        infolist.append(infoDict)

#cpu list3
def cpu(option, opt_str, value, parser):
    print "------cpu information------"
    if os == "Windows":
        WinInfo.get_cpu_info(c,os,infolist)
    if os == "Linux":
        linuxInfo.get_cpu_info(os,infolist)
 

#network list4
def network(option, opt_str, value, parser):
    print "------network information------"
    if os == "Windows":
        WinInfo.get_network_info(c,os,infolist)
    if os == "Linux":
        linuxInfo.get_network_info(os,infolist)
    
        
#memory list5 6
def memory(option, opt_str, value, parser):
    print "------memory information------"
    return memInfo.memory_info(infolist)

#disk list7 list8
def disk(option, opt_str, value, parser):
    print "------disk information------"
    if os == "Windows":
        WinInfo.get_disk_info(c,os,infolist)
    if os == "Linux":
        linuxInfo.get_disk_info(os,infolist)
    diskInfo.disk_info(infolist)

#mysql information list9
def mysql(option, opt_str, value, parser):
    print "------mysql information------"
    if os == "Windows":
        WinInfo.get_mysql_info(c,os, infolist, "mysqld")
    if os == "Linux":
        linuxInfo.get_mysql_info(os, infolist)
 
 #oralce information list10
def oracle(option, opt_str, value, parser):
    print "------oracle information------"
    if os == "Windows":
        WinInfo.get_oracle_info(c,os, infolist)
    if os == "Linux":
        linuxInfo.get_oracle_info(os, infolist)

#sqlserver information list11
def sqlserver(option, opt_str, value, parser):
    if os == "Windows":
        print "------sqlserver information------"
        WinInfo.get_sqlserver_info(c, os, infolist)
        
#sybase information list12
def sybase(option, opt_str, value, parser):
    print "------sybase information------"
    if os == "Windows":
        WinInfo.get_sybase_info(c, os, infolist)
        
def init():
    global os
    global xmlFile
    global infolist
    global c
    xmlFile = "./baseinfo.xml"
    os = platform.system()
    infolist = list()
    if os == "Windows":
        c = wmi.WMI ()
        
def main():
#initation
    init()
    parser = OptionParser()
#version
    parser.add_option("-v", "--version", action="callback", 
                  callback=version, 
                  default=False, 
                  help="The basic information of the script.")
#all information
    parser.add_option("-a", "--all", action="callback", 
                  callback=all_info, 
                  default=False, 
                  help="For all the basic information, coexist in the file. Used with the -f option,"
                  +"can deposit to the specified file")
    #获取所有的基本信息，并存放到文件中.配合-f选项使用，可存放到指定文件中
#file name
    parser.add_option("-f", "--file", action="callback", 
                  callback=fileName, 
                  type="string",
                  default=False, 
                  help="Will get to the specified information stored to the specified XML file,"
                  +"the default file name: info.xml")
    #将获取到指定的信息存放到指定xml文件中，默认文件名：info.xml
#uname
    parser.add_option("-u", "--uname", action="callback", 
                  callback=uname, 
                  default=False, 
                  help="According to the basic information of the operating system (operating system type,"
                 +" the name of the machine, the release, system version number, type, CPU information)")
    #显示操作系统的基本信息（操作系统类型、机器名、发布版本、系统版本号、处理器类型、处理器信息）
#architecture
    parser.add_option("-A", "--architecture", action="callback", 
                  callback=architecture, 
                  default=False, 
                  help="According to machine architecture (machine bit, connection mode)")
    #显示机器架构（机器位数，连接方式）
#cpu
    parser.add_option("-c", "--cpu", action="callback", 
                  callback=cpu, 
                  default=False, 
                  help="The CPU information ")
    #获取cpu的信息（物理个数和逻辑个数）
    
#network
    parser.add_option("-n", "--network", action="callback", 
                  callback=network, 
                  default=False, 
                  help="Network information, network card information, "
                 +" IP address, subnet, MAC address, the maximum number of connections)")
    #网络的信息（网卡信息，ip地址，子网，mac地址，最大连接数）

#memory
    parser.add_option("-m", "--memory", action="callback", 
                  callback=memory, 
                  default=False, 
                  help="Memory information (physical memory, swap memory)")
    #内存信息（物理内存，虚拟内存）
    
#disk
    parser.add_option("-d", "--disk", action="callback", 
                  callback=disk, 
                  default=False, 
                  help="The basic information of the disk")
    #磁盘的基本信息
    
#mysql info
    parser.add_option("--mysql", action="callback", 
              callback=mysql, 
              default=False, 
              help="Used to test whether the mysql installation service system.If you have "
              +"installed, obtain the relevant information")
    #获取mysql的安装路径和版本信息

#oralce info
    parser.add_option("--oracle", action="callback", 
              callback=oracle, 
              default=False, 
              help="Used to test whether the oralce installation service system.If you have "
              +"installed, obtain the relevant information")  

#sqlserver info
    parser.add_option("--sqlserver", action="callback", 
              callback=sqlserver, 
              default=False, 
              help="Used to test whether the sqlserver installation service system.If you have "
              +"installed, obtain the relevant information")  

#sybase info
    parser.add_option("--sybase", action="callback", 
              callback=sybase, 
              default=False, 
              help="Used to test whether the sqlserver installation service system.If you have "
              +"installed, obtain the relevant information") 

    (options, args) = parser.parse_args()
    
if __name__ == '__main__':
    main()
    pass
