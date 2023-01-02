#initialize dictionary with default values

employees=['Anju','Archu','Arun']
defaults={"designation":'Developer',"salary":80000}

data=dict.fromkeys(employees,defaults)
print(data)
print(data["Anju"])


