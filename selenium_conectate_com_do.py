# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json

option = webdriver.ChromeOptions()
option.add_argument("--headless")
option.add_argument(" --disable-gpu")
option.add_argument("--window-size=1200x600")
option.add_argument("--disable-dev-shm-usage")
option.add_argument("--disable-gpu-sandbox")
option.add_argument("--disable-accelerated-2d-canvas")
option.add_argument("--disable-accelerated-jpeg-decoding")
option.add_argument("--no-sandbox")
browser = webdriver.Chrome(executable_path='./chromedriver',chrome_options=option)

browser.get("https://www.conectate.com.do/")


sorteo_element = browser.find_elements_by_xpath("//div/table/tbody/tr/td")
sorteos = [x.text for x in sorteo_element]


print("SORTEOS:")
print(sorteos, '\n')
data={}
nombreSorteo=''
fecha=''
i=0
x=0
for sorteo in zip(sorteos):
    aux = str(sorteo)
    if i<24 :
	    if len(aux)==11 :
	    	fecha = aux[3:8]
	    	data[nombreSorteo].append({
	    		'fecha' : fecha
	    	})
	     	print('Fecha: '+ aux[3:8] +'\n' )
	    elif len(aux)==12 :
	    	resultado = 'resultado'+str(i)
	    	valor1 = aux[3:5]
	    	valor2 = aux[5:7]
	    	valor3 = aux[7:9]
	    	data[nombreSorteo].append({
	    		'resultado1' : valor1,
	    		'resultado2' : valor2,
	    		'resultado3' : valor3
	    	})
	    	print('resultado: '+aux[3:9]+'\n')
	    else :
	    	nombreSorteo = aux[3:len(aux)-3]
	    	print('Sorteo: '+aux[3:len(aux)-3]+'\n')
	    	data[nombreSorteo] = []
	    i=i+1
with open('conectate_com_do.json','w') as outfile:
	json.dump(data, outfile)

browser.quit()