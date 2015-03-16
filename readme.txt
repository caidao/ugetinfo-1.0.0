一、功能介绍

主要用于机器信息采集，采集的信息包括：
(1).硬件相关信息：CPU，内存，网络，存储系统情况
(2).系统负载：网络负载，CPU负载，内存占用情况
(3).网络和磁盘子系统性能
(4).操作系统相关信息，包括操作系统主版本，32位或64位
(5).各种备份代理模块的版本情况和安装路径
可以通过命令行参数，指定单检测某一项。

 
分类	              参数	                                    功能说明
  

基本信息	-v   –version                    		 脚本版本信息
	       	 -a   -all	                                 获取代理环境的基本信息
	        -f   -file=[path]	                        将获取得环境配置信息放到指定的文件中，以xml文件格式存放，默认:info.xml
	        -h -help	                                显示帮助文档





硬件基本信息	
        	   -u  -uname	                                        显示操作系统信息（操作系统类型、机器名、发布版本、系统版本号、处理器类型、处理器信息）如：('Windows', 'pan-PC', '7', '6.1.7601', 'AMD64', 'Intel64 Family 6 Model 58 Stepping 9, GenuineIntel')
 		-A -architecture	                       机器架构（机器位数，连接方式）如：('64bit', 'WindowsPE')
		-c -cpu	                                        获取cpu信息(如：Intel(R) Xeon(R) CPU E5-2603 v2 @ 1.80GHz)
		-n -network	                                网络的信息（网卡信息，ip地址，子网，mac地址，最大连接数）
		-m -memory	                                内存信息（物理内存，虚拟内存）
		-d -disk	                              磁盘的基本信息网络和磁盘性能	
       	 	-N –network I/O	                      系统的网络性能（包括bytes_sent（发送字节数）、bytes_recv（接收字节数）、packets_sent（发送数据包数）、packets_recv（接收数据包数）等）
		-D –disk  I/O	                              磁盘读写I/o（磁盘IO信息包括read_count（读IO数）、write_count（写IO数）、read_bytes（IO读字节数）、write_bytes（IO写字节数）、read_time（磁盘读时间）、write_time（磁盘写时间）等）



备份源的基本信息	
 		–mysql                 	 显示本机中mysql的基本信息（版本，程序安装路径，数据存储路径，二进制日志是否开启，二进制日志路径）
		-oracle  			显示本机中oracle的基本信息（版本，程序安装路径，数据存储路径）
	     	–db2				显示本机中db2的基本信息（版本，程序安装路径，数据存储路径）
		-sybase				显示本机中sybase的基本信息（版本，程序安装路径，数据存储路径）
		-sqlserver			显示本机中sqlserver的基本信息（版本，程序安装路径，数据存储路径）


二、使用说明

1、需要下载安装psutil库，下载地址URL：https://pypi.python.org/pypi/psutil#downloads

2、windwos系统需要支持WMI，下载地址URL：https://pypi.python.org/pypi/WMI/#downloads

三、测试情况

1.win7 mysql5.1  正常           （mysql是通过mysqld程序获取信息的）

2.readhat5.6  mysql5.0.77 正常

3.windwos server 2008   oracle11.2.0.1.0 正常 （在windows系统下是通过查询oracl.exe程序来获取信息的）

4.centos6.4  oracle11.2.0.1.0 正常 （在linux系统下是通过查询oracle的监听进程来做获取信息的 ） 

5.windows server 2003  sqlserver2005  正常（通过检测sqlservr.exe程序来获取安装路径）

6.windows server 2003  sybase ase1254 正常（通过检测sqlsrvr.exe程序来获取安装路径）

7.SunOS  sunv440        不支持