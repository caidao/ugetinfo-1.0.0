#!/usr/bin/env python
#-*- coding: UTF-8 -*-
'''
Created on 2015-1-4

@author: pan
'''
import sys
import platform
import xml.dom.minidom
  
def GenerateXml():
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'employees', None)
    root = dom.documentElement  
    employee = dom.createElement('employee')
    root.appendChild(employee)
      
    nameE=dom.createElement('name')
    nameT=dom.createTextNode('linux')
    nameE.appendChild(nameT)
    employee.appendChild(nameE)
      
    ageE=dom.createElement('age')
    ageT=dom.createTextNode('30')
    ageE.appendChild(ageT)
    employee.appendChild(ageE)
      
    
    f= open('employees2.xml', 'w')
    dom.writexml(f, addindent='  ', newl='\n')
    f.close()  



def main():
    print len(sys.argv)
    uinfo = platform.uname()
    GenerateXml()
    print uinfo

if __name__ == '__main__':
    main()
    pass