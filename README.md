# Robot-Controller-Architecture
## A main module  robot_operation.py that runs the program
## A state module robot_comm.py robot_status method  that handles the robot states
## A driver module robot_driver.py method that enables the activation of robot functions
## A communication module robot_comm.py  method  Robot_Mgmt_protocolthat enables receiving commands and reporting results and statuses to a remote host.

## IDE 
   PyCharm
   Python 3.8

		
### Proposole solution
    robot_comm  class ( which represent the server side )
    robot_driver class
    robot state machine  is function in robot_comm which will handling all messagr from client 

## Getting Started
### open powershell in  windows  and run ./robot_operative.py 
### open powershell in  windows  and run ./arcadia_websokets_client.py enter command  "status" 
## Example result 
![](/images/view_wesokets.PNG)
## Notes
 (*)  when running websokets  under class there is error  after certain time  needed to  fix 

