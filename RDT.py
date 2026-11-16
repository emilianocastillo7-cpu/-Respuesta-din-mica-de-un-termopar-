import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data= pd.read_excel(r"C:\Users\LENOVO\Downloads\termopar negro.xlsx")
data=data.drop(columns=["Date and Time Serie # 1" , "Date and Time Serie # 2" , "Date and Time Serie # 3"])
#print(data.head(727)) #muestra las primeras 727  filas 
#print(data.tail(727)) muestra las ulrimas 727 filas 
#print(data.columns) para ver el nombre de la columnas 
print(data.iloc[0:728, 0:15])
plt.plot(data["Time (s) Serie # 1"],data["Temperature (°C) Serie # 1"],label="Frio-Caliente-frio")

plt.plot(data["Time (s) Serie # 2"],data["Temperature (°C) Serie # 2"], label="Frio-Ambiente-frio" )

plt.plot(data["Time (s) Serie # 3"],data["Temperature (°C) Serie # 3"],label="Caliente-Ambiente-Caliente")
plt.legend()#sirve para actibar los  label 
plt.title("Time vs Teperature")
plt.show()
plt.figure() # separo mis dos graficas , creando otra ventana independiente 


x=np.log(data["Time (s) Serie # 1"]) 
y=np.log(data["Temperature (°C) Serie # 1"])
x1=np.log(data["Time (s) Serie # 2"])
y1=np.log(data["Temperature (°C) Serie # 2"])
x2=np.log(data["Time (s) Serie # 3"])
y2=np.log(data["Temperature (°C) Serie # 3"])
plt.plot(x,y,label="Frio-Caliente-frio") 
#plt.xlabel("Logaritmo Tiempo 1") #poniendo titulo a los ejes de la grafica 
#plt.ylabel("Logaritmo Temperatura 1 ")
plt.plot(x1,y1, label="Frio-Ambiente-frio")
plt.plot(x2,y2, label="Caliente-Ambiente-Caliente")
plt.legend()
plt.title("ln(Time) vs ln(Temperature ) ")

plt.show()

plt.figure() 
clear1= (x > 0) & (y > 0)  #filtramos  los datos , pues nuestras operaciones no estan definidas numeros menores que 0
clear2= (x1 > 0) & (y1 > 0)
clear3= (x2> 0) & (y2 > 0) 
xa= x[clear1]
ya = y[clear1 ]
xb=x1[clear2]
yb=y1[clear2]
xc=x2[clear3]
yc=y2[clear3]
pendiente , intercepto =np.polyfit(xa,ya,1) # la tercera entrada es el grado el polinomio 
#me busco la mejor recta con lo valores con que estoy trabajando 
y_ajustada=pendiente* xa + intercepto 
plt.plot(xa , y_ajustada, label="Frio-Caliente-frio")
tau=1/(-pendiente)
print(f"Mi tau para el cambio Frio-Caliente-frio es {tau}")
pendiente1 , intercepto1   =np.polyfit(xb,yb,1)  
y1_ajustada=pendiente1* xb + intercepto1 
plt.plot(xb , y1_ajustada, label="Frio-Ambiente-frio")
tau1=1/(-pendiente1)
print(f"Mi tau para el cambio Frio-Ambiente-frio es  {tau1}")
pendiente2 , intercepto2   =np.polyfit(xc,yc,1)  
y2_ajustada=pendiente2* xc + intercepto2 
plt.plot(xc , y2_ajustada , label="Caliente-Ambiente-Caliente")
tau2=1/(-pendiente2)
print(f"Mi tau para el cambio Caliente-Ambiente-Caliente es  {tau2}")
plt.legend()
plt.title("Ajuste Lineal ")
plt.margins(0)
plt.show() #tenemos que eliminar los datos para las cuales ln no esta definido 







   



































