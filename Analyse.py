import openpyxl
import re
import pathlib
import pandas as pd
import random
from tkinter import *
from tkinter import ttk

import numpy as np
import math
from brand import brand
from extract import *
Analyse={"Error Image Not found": [],"Error Title no well formulate":[],
         "Error marque dans le titre et distributeur":[],"wrong Tags":[],
         "Empty Contenance" :[],"Status to set draft":[],
         "Error Copie in": [],"Er Standard":[]
         ,"ERROR HANDLE":[],"Eroor ImageAlt":[],"to Adjust Custom":[],
         "EAN ?":[]}
list_of_brand=[]
def AnalyseEAN():
    for i in product_nbr:
        prod=Product(i)
        if any([len(str(prod.barcode).replace("'",""))==i for i in["13","11"]]):
            Analyse["EAN ?"].append(i)
def AnalyseImageAlt():
    for i in product_nbr:
        prod=Product(i)
        if prod.imgalt!=prod.procImageAlt():
            Analyse["Eroor ImageAlt"].append(i)
def AnalyseHandle():
    for i in product_nbr:
        prod=Product(i)
        if prod.handle!=prod.procHandle().lower():
            Analyse["ERROR HANDLE"].append(i)
        
def Pattern(i):
        if i==nb_rows-1:
            return False
        prod=Product(i+1)
        if not pd.isnull(prod.contenance) and prod.imgpos==2:
            return True
def AnalyseKeyword():
    for i in product_nbr:
        prod=Product(i)
        if prod.tags!=",".join(Product(i).procTags()):
            Analyse["wrong Tags"].append(i)
def AnalyseContenance():
    for i in product_nbr:
        prod=Product(i)
        if prod.contenance!=prod.variableContenance().replace("ml","") and not Pattern(i):
            Analyse["Empty Contenance"].append(i)
def AnalyseStatus():

    for i in product_nbr:
        prod=Product(i)
        if pd.isnull(prod.imgpos) and prod.status=="active":
            Analyse["Status to set draft"].append(i)

def AnalyseWellFormulateStandard():
    for i in product_nbr:
        prod=Product(i)
        typeproduct=prod.typeproducte()
        if '>' in typeproduct:
            if typeproduct!=prod.standard:
                Analyse["Er Standard"].append(i)
        else:
            if typeproduct!=prod.custom:
                Analyse["to Adjust Custom"].append(i)
        
def AnalyseTitle():
    for i in product_nbr:
        if not '-' in Product(i).title:
                Analyse["Error Title no well formulate"].append(i)
            
    
def AnalyseImage():
    for i in range(nb_rows):

        if pd.isnull(Product(i).imgpos):
            Analyse["Error Image Not found"].append(i)
def getBrand():
    for i in iter(product_nbr):
        prod=Product(i)
        if '-' not in prod.title:
            continue
        if type(prod.title) is float or type(prod.brand) is float:
            Analyse.append("Error empty case " + str(i))
        else:
            brand=prod.title[:prod.title.index('-')-1]
            vendor=prod.brand
            if vendor != brand:
                Analyse["Error marque dans le titre et distributeur"].append(i)
            list_of_brand.append(brand)
            list_of_brand.append(vendor)
def AnalyseCatalogue():
    global brandi
    AnalyseImage()
    AnalyseContenance()
    AnalyseKeyword()
    AnalyseTitle()
    AnalyseEAN()
    AnalyseWellFormulateStandard()
    AnalyseStatus()
    AnalyseHandle()
    getBrand()
    AnalyseImageAlt()
    brandi=set(list_of_brand)


AnalyseCatalogue()

