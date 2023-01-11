import requests                 
new_measurement = {
   "carat": 0.23,
  "cut": 0,
  "color": 1,
  "clarity": 2,
  "depth": 61.5,
  "table": 55.0,
  "x": 3.95,
  "y": 3.98,
  "z": 2.43
 }
response = requests.post('http://127.0.0.1:8000/predict', json=new_measurement)           
print(response.content)  
                 
