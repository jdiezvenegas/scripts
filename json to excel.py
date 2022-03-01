import json
import xlsxwriter
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd


nombre=datetime.now().strftime('home/jacobo/Documentos/euri/sudaderas/tester/Sudaderas %Y-%m-%d %H:%M:%S.xlsx')
#Carga el fichero .json
archivo=fd.askopenfilename()
with open(archivo, 'r') as f:
  data = json.load(f)
#Creacion de la hoja de cálculo
workbook = xlsxwriter.Workbook("/home/jacobo/Documentos/euri/sudaderas/tester/Sudaderas.xlsx")
worksheet = workbook.add_worksheet()
def nombreCol():
  worksheet.write(0,0,"EMAIL")
  max=0
  for i in range(0,len(data)):
    items=data[i]["Items"]
    if len(items)>max:
      max=len(items)
  for i in range(0,max):
    worksheet.write(0,i+1,"DESCRIPCIÓN")
  for i in range(0,max):
    worksheet.write(0,1+max+i,"CANTIDAD")
  worksheet.write(0,1+2*max,"PRECIO TOTAL")
  worksheet.write(0,2+2*max,"PAGO")
  worksheet.write(0,3+2*max,"ENTREGADO")
  worksheet.write(0,4+2*max,"OBSERVACIONES")
#Escribe emails
def email():
  for i in range(0,len(data)):
    worksheet.write(i+1,0,data[i]["Email"])
#Escribe descripciones
def desc():
  for i in range(0,len(data)):
    items=data[i]["Items"]
    for j in range(0,len(items)):
      worksheet.write(i+1, j+1, items[j]["description"])
#Escribe cantidades
def cant():
  max=0
  for i in range(0,len(data)):
    items=data[i]["Items"]
    if len(items)>max:
      max=len(items)
  for i in range(0,len(data)):
    items=data[i]["Items"]
    for j in range(0,len(items)):
      worksheet.write(i+1, max+j+1, items[j]["quantity"])
#Escribe precios totales
def precioTotal():
  max=0
  for i in range(0,len(data)):
    items=data[i]["Items"]
    if len(items)>max:
      max=len(items)
  for i in range(0,len(data)):
    worksheet.write(i+1,2*max+1,data[i]["Price"])
#Escribe pagos
def haPagado():
  cell_format = workbook.add_format()
  cell_format.set_pattern(1)  # This is optional when using a solid fill.
  cell_format.set_bg_color('green')
  max=0
  for i in range(0,len(data)):
    items=data[i]["Items"]
    if len(items)>max:
      max=len(items)
  for i in range(0,len(data)):
    if data[i]["Paid"]:
      worksheet.write(i+1,2*max+2,"Pagado")
    else:
      worksheet.write(i+1,2*max+2,"NO PAGADO")
#Escribe entregado
def entregado():
  max=0
  for i in range(0,len(data)):
    items=data[i]["Items"]
    if len(items)>max:
      max=len(items)
  for i in range(0,len(data)):
    worksheet.write(i+1,2*max+3,"No entregado")
nombreCol()
email()
desc()
cant()
precioTotal()
haPagado()
entregado()
workbook.close()