import json
almacenes=[]
    
def read_json(nombre_archivo):
    try: 
        with open(nombre_archivo, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"ERROR: El archivo {nombre_archivo} no tiene un formato vàlido")
    
def write_json(nombre_archivo, contenido):
    with open(nombre_archivo, "w", encondig="utf-8") as file:
      json.dump(contenido, file, ident=4, ensure_ascii=False) 

def carga_datos(nombre_archivo="almacen.json"):
    datos= read_json(nombre_archivo)
    almacenes.clear()
    almacenes.extend(datos)
    print(f"---SIstema: Se han cargado {len(almacenes)}registros de {nombre_archivo}")
    
def guarda_datos(nombre_archivo="almacen.json"):
    write_json(nombre_archivo, almacenes)
    print(f"---Sistema: Datos guardados con èxito en {nombre_archivo}---")