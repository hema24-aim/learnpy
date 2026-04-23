def control_system(temp, humidity):
    
    if temp > 35:
        action = "AC ON"
    elif temp < 20:
        action = "Heater ON"
    else:
        action = "Normal"
    
    if humidity > 70:
        action += " + Dehumidifier ON"
    
    return action


data = [(18, 60), (30, 80), (40, 50)]

for t, h in data:
    print(control_system(t, h))