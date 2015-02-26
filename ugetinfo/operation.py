
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015-1-9

@author: pan
'''

import xml.dom.minidom

def init():
    global dom
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'baseinfo', None)    
    global root
    root = dom.documentElement

def version_xml(infolist):
#version  
    verE = dom.createElement("version")
    verT = dom.createTextNode(infolist[0]["version"])
    verE.appendChild(verT)
    root.appendChild(verE)
#generate_time
    timeE = dom.createElement("generate_time")
    timeT = dom.createTextNode(infolist[0]["generate_time"])
    timeE.appendChild(timeT)
    root.appendChild(timeE)

def os_info_xml(infolist,os):
    OSE = dom.createElement("OS")
    root.appendChild(OSE)
    #type
    systemE = dom.createElement("type")
    systemT = dom.createTextNode(infolist[1]["utype"])
    systemE.appendChild(systemT)
    OSE.appendChild(systemE)
    #dist
    if os == "Linux":
        distE = dom.createElement("dist")
        distT = dom.createTextNode(infolist[1]["udist"])
        distE.appendChild(distT)
        OSE.appendChild(distE)
    #version
    versionE = dom.createElement("version")
    versionT = dom.createTextNode(infolist[1]["uversion"])
    versionE.appendChild(versionT)
    OSE.appendChild(versionE)
    #host name
    hostE = dom.createElement("host_name")
    hostT = dom.createTextNode(infolist[1]["host_name"])
    hostE.appendChild(hostT)
    OSE.appendChild(hostE)

def cpu_info_xml(infolist):
    cpuE = dom.createElement("cpu")
    root.appendChild(cpuE)
    #archb
    archE = dom.createElement("arch")
    archT = dom.createTextNode(infolist[1]["uarch"])
    archE.appendChild(archT)
    cpuE.appendChild(archE)       
    #mode
    modeE = dom.createElement("mode")
    modeT = dom.createTextNode(infolist[1]["umode"])
    modeE.appendChild(modeT)
    cpuE.appendChild(modeE)
    #description
    descE = dom.createElement("description")
    descT = dom.createTextNode(infolist[3]["model name"])
    descE.appendChild(descT)
    cpuE.appendChild(descE)
    #bit
    bitE = dom.createElement("bit")
    bitT = dom.createTextNode(infolist[2]["Abit"])
    bitE.appendChild(bitT)
    cpuE.appendChild(bitE)
    
def network_info_xml(infolist):
    networkE = dom.createElement("network")
    root.appendChild(networkE)
    templist = infolist[4]    
    for i in templist:
        interfaceE = dom.createElement("interface")
        networkE.appendChild(interfaceE)
        #Description
        descE = dom.createElement("Description")
        descT = dom.createTextNode(i["Description"])
        descE.appendChild(descT)
        interfaceE.appendChild(descE)
        #ip
        ipE = dom.createElement("ip")
        ipT = dom.createTextNode(i["IPAddress"])
        ipE.appendChild(ipT)
        interfaceE.appendChild(ipE)
        #mask
        maskE = dom.createElement("mask")
        maskT = dom.createTextNode(i["IPSubnet"])
        maskE.appendChild(maskT)
        interfaceE.appendChild(maskE)
        #mac
        macE = dom.createElement("mac")
        macT = dom.createTextNode(i["MAC"])
        macE.appendChild(macT)
        interfaceE.appendChild(macE)
 
def memory_info_xml(infolist):
    memE = dom.createElement("memory")
    root.appendChild(memE)
    #real_mem
    templist = infolist[5]
    realE = dom.createElement("real_memory")
    for key,value in templist[0].items():
        realE.setAttribute(key, value)
    memE.appendChild(realE)
    #swap_mem
    templist = infolist[6]
    swapE = dom.createElement("swap_memory")
    for key,value in templist[0].items():
        swapE.setAttribute(key, value)
    memE.appendChild(swapE)

def disk_info_xml(infolist):
#storage info
    storeE = dom.createElement("storage")
    root.appendChild(storeE)
    templist = infolist[7]
    #device info
    for i in templist:
        devE = dom.createElement("device")
        devT = dom.createTextNode(i["disk"])
        devE.setAttribute("size",i["size"])
        devE.setAttribute("type",i["dev"])
        devE.appendChild(devT)
        storeE.appendChild(devE)
    #list
    templist = infolist[8]
    for i in templist:
        #partition
        parE = dom.createElement("partition")
        parE.setAttribute("device", i["device"])
        parE.setAttribute("total",i["dtotal"])
        parE.setAttribute("used",i["dused"])
        parE.setAttribute("free",i["free"])
        parE.setAttribute("percent",i["percent"])
        parE.setAttribute("type",i["fstype"])
        parE.setAttribute("mount",i["mountpoint"])
        storeE.appendChild(parE)    

def bksrc_init():
    #backup source
    global bksrcE
    bksrcE = dom.createElement("bk_src_info")
    root.appendChild(bksrcE)
        
def mysql_info_xml(infolist):
#mysql info
    mysqlE = dom.createElement("mysql")
    temp = infolist[9]["mysql"]
    mysqlE.setAttribute("enable", str(temp))
    bksrcE.appendChild(mysqlE)
    if temp:
        #version
        verE = dom.createElement("version")
        verT = dom.createTextNode(infolist[9]["version"])
        verE.appendChild(verT)
        mysqlE.appendChild(verE)
        #basedir
        baseE = dom.createElement("install_path")
        baseT = dom.createTextNode(infolist[9]["basedir"])
        baseE.appendChild(baseT)
        mysqlE.appendChild(baseE)
 
def oracle_info_xml(infolist):
#Oracle info
    oracleE = dom.createElement("oracle")
    temp = infolist[10]["oracle"]
    oracleE.setAttribute("enable", str(temp))
    bksrcE.appendChild(oracleE)
    if temp:
        #version
        verE = dom.createElement("version")
        verT = dom.createTextNode(infolist[10]["version"])
        verE.appendChild(verT)
        oracleE.appendChild(verE)
        #basedir
        baseE = dom.createElement("install_path")
        baseT = dom.createTextNode(infolist[10]["basedir"])
        baseE.appendChild(baseT)
        oracleE.appendChild(baseE)           

def sqlserver_info_xml(infolist):
#sqlserver info
    sqlserverE = dom.createElement("sqlserver")
    temp = infolist[11]["sqlserver"]
    sqlserverE.setAttribute("enable",str(temp))
    bksrcE.appendChild(sqlserverE)
    if temp:
        #versuin
        verE = dom.createElement("version")
        verT = dom.createTextNode(infolist[11]["version"])
        verE.appendChild(verT)
        sqlserverE.appendChild(verE)
        #basedir
        baseE = dom.createElement("install_path")
        baseT = dom.createTextNode(infolist[11]["basedir"])
        baseE.appendChild(baseT)
        sqlserverE.appendChild(baseE)

def sybase_info_xml(infolist):
 #sybase info
    sybaseE = dom.createElement("sybase")
    temp = infolist[12]["sybase"]
    sybaseE.setAttribute("enable", str(temp))
    bksrcE.appendChild(sybaseE)
    if temp:
        #versuin
        verE = dom.createElement("version")
        verT = dom.createTextNode(infolist[12]["version"])
        verE.appendChild(verT)
        sybaseE.appendChild(verE)
        #basedir
        baseE = dom.createElement("install_path")
        baseT = dom.createTextNode(infolist[12]["basedir"])
        baseE.appendChild(baseT)
        sybaseE.appendChild(baseE)
        
def write_xml(xmlfile):
#store to file
    f= open(xmlfile, 'w')
    dom.writexml(f, addindent='  ', newl='\n')
    f.close()         
    
def gerateXml(xmlfile,infolist,os):
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'baseinfo', None)
    root = dom.documentElement
#version
    verE = dom.createElement("version")
    verT = dom.createTextNode(infolist[0]["version"])
    verE.appendChild(verT)
    root.appendChild(verE)
#generate_time
    timeE = dom.createElement("generate_time")
    timeT = dom.createTextNode(infolist[0]["generate_time"])
    timeE.appendChild(timeT)
    root.appendChild(timeE)
#OS
    OSE = dom.createElement("OS")
    root.appendChild(OSE)
    #type
    systemE = dom.createElement("type")
    systemT = dom.createTextNode(infolist[1]["utype"])
    systemE.appendChild(systemT)
    OSE.appendChild(systemE)
    #dist
    if os == "Linux":
        distE = dom.createElement("dist")
        distT = dom.createTextNode(infolist[1]["udist"])
        distE.appendChild(distT)
        OSE.appendChild(distE)
    #version
    versionE = dom.createElement("version")
    versionT = dom.createTextNode(infolist[1]["uversion"])
    versionE.appendChild(versionT)
    OSE.appendChild(versionE)
    #host name
    hostE = dom.createElement("host_name")
    hostT = dom.createTextNode(infolist[1]["host_name"])
    hostE.appendChild(hostT)
    OSE.appendChild(hostE)
#cpu
    cpuE = dom.createElement("cpu")
    root.appendChild(cpuE)
    #arch
    archE = dom.createElement("arch")
    archT = dom.createTextNode(infolist[1]["uarch"])
    archE.appendChild(archT)
    cpuE.appendChild(archE)       
    #mode
    modeE = dom.createElement("mode")
    modeT = dom.createTextNode(infolist[1]["umode"])
    modeE.appendChild(modeT)
    cpuE.appendChild(modeE)
    #description
    descE = dom.createElement("description")
    descT = dom.createTextNode(infolist[3]["model name"])
    descE.appendChild(descT)
    cpuE.appendChild(descE)
    #bit
    bitE = dom.createElement("bit")
    bitT = dom.createTextNode(infolist[2]["Abit"])
    bitE.appendChild(bitT)
    cpuE.appendChild(bitE)
# net work
    networkE = dom.createElement("network")
    root.appendChild(networkE)
    templist = infolist[4]    
    for i in templist:
        interfaceE = dom.createElement("interface")
        networkE.appendChild(interfaceE)
        #Description
        descE = dom.createElement("Description")
        descT = dom.createTextNode(i["Description"])
        descE.appendChild(descT)
        interfaceE.appendChild(descE)
        #ip
        ipE = dom.createElement("ip")
        ipT = dom.createTextNode(i["IPAddress"])
        ipE.appendChild(ipT)
        interfaceE.appendChild(ipE)
        #mask
        maskE = dom.createElement("mask")
        maskT = dom.createTextNode(i["IPSubnet"])
        maskE.appendChild(maskT)
        interfaceE.appendChild(maskE)
        #mac
        macE = dom.createElement("mac")
        macT = dom.createTextNode(i["MAC"])
        macE.appendChild(macT)
        interfaceE.appendChild(macE)
#memory info
    memE = dom.createElement("memory")
    root.appendChild(memE)
    #real_mem
    templist = infolist[5]
    realE = dom.createElement("real_memory")
    for key,value in templist[0].items():
        realE.setAttribute(key, value)
    memE.appendChild(realE)
    #swap_mem
    templist = infolist[6]
    swapE = dom.createElement("swap_memory")
    for key,value in templist[0].items():
        swapE.setAttribute(key, value)
    memE.appendChild(swapE)
#storage info
    storeE = dom.createElement("storage")
    root.appendChild(storeE)
    templist = infolist[7]
    #device info
    for i in templist:
        devE = dom.createElement("device")
        devT = dom.createTextNode(i["disk"])
        devE.setAttribute("size",i["size"])
        devE.setAttribute("type",i["dev"])
        devE.appendChild(devT)
        storeE.appendChild(devE)
    #list
    templist = infolist[8]
    for i in templist:
        #partition
        parE = dom.createElement("partition")
        parE.setAttribute("device", i["device"])
        parE.setAttribute("total",i["dtotal"])
        parE.setAttribute("used",i["dused"])
        parE.setAttribute("free",i["free"])
        parE.setAttribute("percent",i["percent"])
        parE.setAttribute("type",i["fstype"])
        parE.setAttribute("mount",i["mountpoint"])
        storeE.appendChild(parE)
#backup source
    bksrcE = dom.createElement("bk_src_info")
    root.appendChild(bksrcE)
#mysql info
    mysqlE = dom.createElement("mysql")
    temp = infolist[9]["mysql"]
    mysqlE.setAttribute("enable", str(temp))
    bksrcE.appendChild(mysqlE)
    if temp:
        #version
        verE = dom.createElement("version")
        verT = dom.createTextNode(infolist[9]["version"])
        verE.appendChild(verT)
        mysqlE.appendChild(verE)
        #basedir
        baseE = dom.createElement("install_path")
        baseT = dom.createTextNode(infolist[9]["basedir"])
        baseE.appendChild(baseT)
        mysqlE.appendChild(baseE)
 #Oracle info
    oracleE = dom.createElement("oracle")
    temp = infolist[10]["oracle"]
    oracleE.setAttribute("enable", str(temp))
    bksrcE.appendChild(oracleE)
    if temp:
        #version
        verE = dom.createElement("version")
        verT = dom.createTextNode(infolist[10]["version"])
        verE.appendChild(verT)
        oracleE.appendChild(verE)
        #basedir
        baseE = dom.createElement("install_path")
        baseT = dom.createTextNode(infolist[10]["basedir"])
        baseE.appendChild(baseT)
        oracleE.appendChild(baseE)
#sqlserver info
    sqlserverE = dom.createElement("sqlserver")
    temp = infolist[11]["sqlserver"]
    sqlserverE.setAttribute("enable",str(temp))
    bksrcE.appendChild(sqlserverE)
    if temp:
        #versuin
        verE = dom.createElement("version")
        verT = dom.createTextNode(infolist[11]["version"])
        verE.appendChild(verT)
        sqlserverE.appendChild(verE)
        #basedir
        baseE = dom.createElement("install_path")
        baseT = dom.createTextNode(infolist[11]["basedir"])
        baseE.appendChild(baseT)
        sqlserverE.appendChild(baseE)
 #sybase info
    sybaseE = dom.createElement("sybase")
    temp = infolist[12]["sybase"]
    sybaseE.setAttribute("enable", str(temp))
    bksrcE.appendChild(sybaseE)
    if temp:
        #versuin
        verE = dom.createElement("version")
        verT = dom.createTextNode(infolist[12]["version"])
        verE.appendChild(verT)
        sybaseE.appendChild(verE)
        #basedir
        baseE = dom.createElement("install_path")
        baseT = dom.createTextNode(infolist[12]["basedir"])
        baseE.appendChild(baseT)
        sybaseE.appendChild(baseE)
                         
#store to file
    f= open(xmlfile, 'w')
    dom.writexml(f, addindent='  ', newl='\n')
    f.close()     
       

def main():
    print "hello word"

if __name__ == '__main__':
    main()
    pass