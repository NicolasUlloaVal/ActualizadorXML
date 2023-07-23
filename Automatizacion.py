import xml.etree.ElementTree as ET
import os

#Ruta de prueba
#ruta = "C:/Users/nicolasu/OneDrive - gourmet.cl/Escritorio/auto"
#ruta de la carpeta
ruta='//servidor12c/XML'

#iterar por cada archivo en la carpeta
for nombre_archivo in os.listdir(ruta):
    if nombre_archivo.endswith(".xml"):
        #analiza el archivo xml
        tree = ET.parse(os.path.join(ruta, nombre_archivo))
        root = tree.getroot()

        #especificar el namespace correcto
        namespace = {"ns0":"http://www.sii.cl/SiiDte"}

        #buscar el elemento "TipoDTE" utilizando el namespace especificado
        TipoDTE = root.find(".//ns0:TipoDTE",namespace).text
        
        #buscar el elemento "Folio" utilizando el namespace especificado
        Folio = root.find(".//ns0:Folio",namespace).text
        
        #buscar el elemento "FchEmis" utilizando el namespace especificado
        FchEmis = root.find(".//ns0:FchEmis",namespace).text
        FchEmis = FchEmis.replace("-","")
        
        #buscar el elemento "RUTEmisor" utilizando el namespace especificado
        RUTEmisor = root.find(".//ns0:RUTEmisor",namespace).text
        RUTEmisor = RUTEmisor.replace("-","")

        # verificar si el RUT tiene menos de 10 dígitos
        while len(RUTEmisor) < 10:
            RUTEmisor = "0" + RUTEmisor

        #crear el nuevo nombre del archivo
        nuevo_nombre = FchEmis + "112323" + "-" +RUTEmisor + "-" + TipoDTE + "-" + Folio + ".xml"

        #renombrar el archivo
        os.rename(os.path.join(ruta, nombre_archivo), os.path.join(ruta, nuevo_nombre))
