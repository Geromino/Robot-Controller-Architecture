# Robot-Controller-Architecture
 1) A main module  robot_operation.py that runs the program
 
 2) A state module robot_comm.py robot_status method  that handles the robot states
 
 3) A driver module robot_driver.py method that enables the activation of robot functions
 
 4) A communication module robot_comm.py  method  Robot_Mgmt_protocolthat enables receiving commands and reporting results 
	and statuses to a remote host.

## IDE and Complier
   ### PyCharm
   ### Python 3.8

		
### Proposole solution
    1) robot_comm  class ( which represent the server side )
    2) robot_driver class
    3) robot state machine  is function in robot_comm which will handling all messagr from client 

## Getting Started
### open powershell in  windows  and run ./robot_operative.py 
### open powershell in  windows  and run ./arcadia_websokets_client.py enter command  "status" 
### Example result 
![](/images/view_wesokets.png)
# Notes
 (*)  when running websokets  under class there is error  after certain time  needed to  fix 

