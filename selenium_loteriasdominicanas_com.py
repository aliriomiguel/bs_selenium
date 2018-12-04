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
browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=option)
browser.get("https://loteriasdominicanas.com/")

sorteo_element = browser.find_elements_by_xpath("//div[3]//div[2]//span")
sorteos = [x.text for x in sorteo_element]

data={}
nombreSorteo=''
fecha=''
i=0
for sorteo in zip(sorteos):
    aux = str(sorteo)
    if len(aux)==16 :
    	fecha = aux[3:13]
    	data[nombreSorteo].append({
    		'fecha' : fecha
    	})
    elif len(aux)==8 :
    	i=i+1
    	resultado = 'resultado'+str(i)
    	valor = aux[3:5]
    	data[nombreSorteo].append({
    		resultado : valor
    	})
    else :
    	nombreSorteo = aux[3:len(aux)-3]
    	data[nombreSorteo] = []
    	i=0

with open('loteriasdominicanas_com.json','w') as outfile:
	json.dump(data, outfile)

browser.quit()