import requests 
reqdat = requests.post("http://192.168.50.193:5889/outdoor_navigation",json={'email':'kornbot380@hotmail.com','project_name':'Smart_Robots','payloaddat':{
'radar':{'radar_1':{'X':170,'Y':672,'Z':340,'Xo':11,'Yo':10,'Zo':0,'Xc':0,'Yc':0,'Zc':0,'roll':180,'pitch':90,'yaw':180}}}})

