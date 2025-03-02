import requests 
reqdat = requests.post("http://192.168.50.193:5889/outdoor_navigation",json={'email':'kornbot380@hotmail.com','project_name':'Smart_Robots','payloaddat':
{'radar':{'radar_1':{'X':160,'Y':520,'Z':20,'Xo':0,'Yo':0,'Zo':0,'roll':180,'pitch':90,'yaw':180}}}})

