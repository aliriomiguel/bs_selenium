# -*- coding: utf-8 -*-
import json
from Query import *
import time
import datetime


archivo1='null'
archivo2='null'
fecha1='null'
fecha2='null'
dia = time.strftime("%w")
fecha = time.strftime("%Y-%m-%d")
fecha_hoy=time.strftime("%d-%m-%Y")

with open('../bs_selenium/conectate_com_do.json') as file:
		archivo1=json.load(file)
		#print data["Quiniela Loteka"][0]["resultado1 "]

with open('../bs_selenium/loteriasdominicanas_com.json') as file:
	 	archivo2=json.load(file)

#Quiniela Loteka
try:
    jugada1=archivo1["Quiniela Loteka"][0]["resultado1"]+"-"+archivo1["Quiniela Loteka"][0]["resultado2"]+"-"+archivo1["Quiniela Loteka"][0]["resultado3"] 
    jugada2=archivo2["Quiniela Loteka"][1]["resultado1"]+"-"+archivo2["Quiniela Loteka"][2]["resultado2"]+"-"+archivo2["Quiniela Loteka"][3]["resultado3"] 

    fecha1=archivo1["Quiniela Loteka"][1]["fecha"]+'-2018'
    fecha2=archivo2["Quiniela Loteka"][0]["fecha"]
    query2  = "SELECT COUNT(*) FROM resultados WHERE sorteo='Quiniela Loteka' AND resultado ='"+jugada1+"' AND DATE(fecha) between date_sub('"+fecha+"',INTERVAL 1 DAY) AND '"+fecha+"'"
    query  = "call registrar_resultados('Quiniela Loteka','"+jugada1+"',"+dia+")";

    objeto = Resultado()
    result = objeto.BuscarResultados(query2) 
    print "Comienza el proceso para Quiniela Loteka"
    print "Resultado de conectate_com_do: "+jugada1
    print "Resu de loteriasdominicanas_com: "+jugada2
    if result[0] < 1 and fecha1==fecha_hoy and jugada1==jugada2 and fecha1==fecha2:
       #if time.strftime("%Y-%m-%d",fecha_result)==fecha:
        print "Comienza el proceso para Quiniela Loteka"
        objeto.GuardarDatos(query)
        print "Inicia proceso para modificar jugada"
        objeto.ModificarPremios('Quiniela Loteka',jugada1)
    else: 
         print "Resultados ya registrados"
         print "Resultado: "+jugada1
except Exception as e:
    raise



#New York 12:30
try:
    jugada1=archivo1["New York 1:30"][0]["resultado1"]+"-"+archivo1["New York 1:30"][0]["resultado2"]+"-"+archivo1["New York 1:30"][0]["resultado3"] 
    jugada2=archivo2["New York 1:30"][1]["resultado1"]+"-"+archivo2["New York 1:30"][2]["resultado2"]+"-"+archivo2["New York 1:30"][3]["resultado3"] 

    fecha1=archivo1["New York 1:30"][1]["fecha"]+'-2018'
    fecha2=archivo2["New York 1:30"][0]["fecha"]
    query2  = "SELECT COUNT(*) FROM resultados WHERE sorteo='New York 12:30 PM' AND resultado ='"+jugada1+"' AND DATE(fecha) between date_sub('"+fecha+"',INTERVAL 1 DAY) AND '"+fecha+"'"
    query  = "call registrar_resultados('New York 12:30 PM','"+jugada1+"',"+dia+")";
    objeto = Resultado()
    result = objeto.BuscarResultados(query2) 
    print "Comienza el proceso para New York 12:30 PM"

    if result[0] < 1 and fecha1==fecha_hoy and jugada1==jugada2 and fecha1==fecha2:
       #if time.strftime("%Y-%m-%d",fecha_result)==fecha:
        print "Resultado: "+jugada1
        objeto.GuardarDatos(query)
        print "Inicia proceso para modificar jugada"
        objeto.ModificarPremios('New York 12:30 PM',jugada1)
    else: 
         print "Resultados ya registrados"
         print "Resultado: "+jugada1
except Exception as e:
    raise




#New York 7:30 PM
try:
    jugada1=archivo1["New York 8:30"][0]["resultado1"]+"-"+archivo1["New York 8:30"][0]["resultado2"]+"-"+archivo1["New York 8:30"][0]["resultado3"] 
    jugada2=archivo2["New York 8:30"][1]["resultado1"]+"-"+archivo2["New York 8:30"][2]["resultado2"]+"-"+archivo2["New York 8:30"][3]["resultado3"] 

    fecha1=archivo1["New York 8:30"][1]["fecha"]+'-2018'
    fecha2=archivo2["New York 8:30"][0]["fecha"]
    query2  = "SELECT COUNT(*) FROM resultados WHERE sorteo='New York 7:30 PM' AND resultado ='"+jugada1+"' AND DATE(fecha) between date_sub('"+fecha+"',INTERVAL 1 DAY) AND '"+fecha+"'"
    query  = "call registrar_resultados('New York 7:30 PM','"+jugada1+"',"+dia+")";

    objeto = Resultado()
    result = objeto.BuscarResultados(query2) 
    print "Comienza el proceso para New York 7:30 PM"
    print "Resultado de conectate_com_do: "+jugada1
    print "Resu de loteriasdominicanas_com: "+jugada2

    if result[0] < 1 and fecha1==fecha_hoy and jugada1==jugada2 and fecha1==fecha2:
       #if time.strftime("%Y-%m-%d",fecha_result)==fecha:
        print "Comienza el proceso para New York 7:30 PM"
        print "Resultado: "+jugada1
        objeto.GuardarDatos(query)
        print "Inicia proceso para modificar jugada"
        objeto.ModificarPremios('New York 7:30 PM',jugada1)
    else: 
         print "Resultados ya registrados"
         print "Resultado: "+jugada1
except Exception as e:
    raise



#Quiniela Real
try:
    jugada1=archivo1["Quiniela Real"][0]["resultado1"]+"-"+archivo1["Quiniela Real"][0]["resultado2"]+"-"+archivo1["Quiniela Real"][0]["resultado3"] 
    jugada2=archivo2["Quiniela Real"][1]["resultado1"]+"-"+archivo2["Quiniela Real"][2]["resultado2"]+"-"+archivo2["Quiniela Real"][3]["resultado3"] 

    fecha1=archivo1["Quiniela Real"][1]["fecha"]+'-2018'
    fecha2=archivo2["Quiniela Real"][0]["fecha"]
    query2  = "SELECT COUNT(*) FROM resultados WHERE sorteo='Quiniela Real' AND resultado ='"+jugada1+"' AND DATE(fecha) between date_sub('"+fecha+"',INTERVAL 1 DAY) AND '"+fecha+"'"
    query  = "call registrar_resultados('Quiniela Real','"+jugada1+"',"+dia+")";

    objeto = Resultado()
    result = objeto.BuscarResultados(query2) 
    print "Comienza el proceso para Quiniela Real"
    print "Resultado de conectate_com_do: "+jugada1
    print "Resultado de loteriasdominicanas_com: "+jugada2
    print "Fecha de conectate_com_do: "+fecha1
    print "Fecha de loteriasdominicanas_com: "+fecha2
    print "Fecha de Hoy: "+fecha_hoy

    if result[0] < 1 and fecha1==fecha_hoy and jugada1==jugada2 and fecha1==fecha2:
       #if time.strftime("%Y-%m-%d",fecha_result)==fecha:
        print "Comienza el proceso para Quiniela Real"
        print "Resultado: "+jugada1
        objeto.GuardarDatos(query)
        print "Inicia proceso para modificar jugada"
        objeto.ModificarPremios('Quiniela Real',jugada1)
    else: 
         print "Resultados ya registrados"
         print "Resultado: "+jugada1     
except Exception as e:
    raise



#Quiniela Pale
try:
    jugada1=archivo1["Quiniela Leidsa"][0]["resultado1"]+"-"+archivo1["Quiniela Leidsa"][0]["resultado2"]+"-"+archivo1["Quiniela Leidsa"][0]["resultado3"] 
    jugada2=archivo2["Quiniela Leidsa"][1]["resultado1"]+"-"+archivo2["Quiniela Leidsa"][2]["resultado2"]+"-"+archivo2["Quiniela Leidsa"][3]["resultado3"] 

    fecha1=archivo1["Quiniela Leidsa"][1]["fecha"]+'-2018'
    fecha2=archivo2["Quiniela Leidsa"][0]["fecha"]
    query2  = "SELECT COUNT(*) FROM resultados WHERE sorteo='Quiniela Pale' AND resultado ='"+jugada1+"' AND DATE(fecha) between date_sub('"+fecha+"',INTERVAL 1 DAY) AND '"+fecha+"'"
    query  = "call registrar_resultados('Quiniela Pale','"+jugada1+"',"+dia+")";

    objeto = Resultado()
    result = objeto.BuscarResultados(query2) 
    print "Comienza el proceso para Quiniela Pale"
    print "Resultado de conectate_com_do: "+jugada1
    print "Resu de loteriasdominicanas_com: "+jugada2

    if result[0] < 1 and fecha1==fecha_hoy and jugada1==jugada2 and fecha1==fecha2:
       #if time.strftime("%Y-%m-%d",fecha_result)==fecha:
        print "Comienza el proceso para Quiniela Pale"
        print "Resultado: "+jugada1
        objeto.GuardarDatos(query)
        print "Inicia proceso para modificar jugada"
        objeto.ModificarPremios('Quiniela Pale',jugada1)
    else: 
         print "Resultados ya registrados"
         print "Resultado: "+jugada1   
except Exception as e:
    raise


#Gana Mas
try:
    jugada1=archivo1["Gana M\\xe1s"][0]["resultado1"]+"-"+archivo1["Gana M\\xe1s"][0]["resultado2"]+"-"+archivo1["Gana M\\xe1s"][0]["resultado3"] 
    jugada2=archivo2["Gana M\\xe1s"][1]["resultado1"]+"-"+archivo2["Gana M\\xe1s"][2]["resultado2"]+"-"+archivo2["Gana M\\xe1s"][3]["resultado3"] 

    fecha1=archivo1["Gana M\\xe1s"][1]["fecha"]+'-2018'
    fecha2=archivo2["Gana M\\xe1s"][0]["fecha"]
    query2  = "SELECT COUNT(*) FROM resultados WHERE sorteo='Gana Más' AND resultado ='"+jugada1+"' AND DATE(fecha) between date_sub('"+fecha+"',INTERVAL 1 DAY) AND '"+fecha+"'"
    query  = "call registrar_resultados('Gana Más','"+jugada1+"',"+dia+")";

    objeto = Resultado()
    result = objeto.BuscarResultados(query2) 
    print "Comienza el proceso para Gana Más"
    print "Resultado de conectate_com_do: "+jugada1
    print "Resu de loteriasdominicanas_com: "+jugada2

    if result[0] < 1 and fecha1==fecha_hoy and jugada1==jugada2 and fecha1==fecha2:
       #if time.strftime("%Y-%m-%d",fecha_result)==fecha:
        print "Comienza el proceso para Gana Más"
        print "Resultado: "+jugada1
        objeto.GuardarDatos(query)
        print "Inicia proceso para modificar jugada"
        objeto.ModificarPremios('Gana Más',jugada1)
    else: 
         print "Resultados ya registrados"
         print "Resultado: "+jugada1   
except Exception as e:
    raise

#Loteria Nacional
try:
    jugada1=archivo1["Loter\\xeda Nacional"][0]["resultado1"]+"-"+archivo1["Loter\\xeda Nacional"][0]["resultado2"]+"-"+archivo1["Loter\\xeda Nacional"][0]["resultado3"] 
    jugada2=archivo2["Loter\\xeda Nacional"][1]["resultado1"]+"-"+archivo2["Loter\\xeda Nacional"][2]["resultado2"]+"-"+archivo2["Loter\\xeda Nacional"][3]["resultado3"] 

    fecha1=archivo1["Loter\\xeda Nacional"][1]["fecha"]+'-2018'
    fecha2=archivo2["Loter\\xeda Nacional"][0]["fecha"]
    query2  = "SELECT COUNT(*) FROM resultados WHERE sorteo='Loteria Nacional' AND resultado ='"+jugada1+"' AND DATE(fecha) between date_sub('"+fecha+"',INTERVAL 1 DAY) AND '"+fecha+"'"
    query  = "call registrar_resultados('Loteria Nacional','"+jugada1+"',"+dia+")";

    objeto = Resultado()
    result = objeto.BuscarResultados(query2) 
    print "Comienza el proceso para Loteria Nacional"
    print "Resultado de conectate_com_do: "+jugada1
    print "Resu de loteriasdominicanas_com: "+jugada2

    if result[0] < 1 and fecha1==fecha_hoy and jugada1==jugada2 and fecha1==fecha2:
       #if time.strftime("%Y-%m-%d",fecha_result)==fecha:
        print "Comienza el proceso para Loteria Nacional"
        print "Resultado: "+jugada1
        objeto.GuardarDatos(query)
        print "Inicia proceso para modificar jugada"
        objeto.ModificarPremios('Loteria Nacional',jugada1)
    else: 
         print "Resultados ya registrados"
         print "Resultado: "+jugada1   
except Exception as e:
    raise
