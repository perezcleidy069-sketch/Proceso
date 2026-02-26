from docs import*


def mostrar_todas_categorias():
    if not almacenes:
        print("El almacen està vacìo")
    else:
        for elemento in almacenes:
            print(elemento)
            
            
            
def separador():
    print("*" * 50)

def pedir_opcion():
    try: 
        opcion= int(input("Ingrese la opcion que desea realizar: "))
        return opcion
    except ValueError:
        print("Error: Debe ingresar un nùmero")
        return -1
    

def verificacion(titulo):
    for i in almacenes:
        if i["titulo"].lower() == titulo.lower():
            return True
        return False
    
def añadir_elemento():
  separador()
  print("-----Añadir elementos-----")
  menu="""
  1. Añadir libros
  2. Añadir musica
  3. Añadir pelicula
  4. Menu principal"""
  print(menu)
  separador()
  opc=pedir_opcion()
  separador()
  if opc in [1,2,3]:
      
      titulo=input("Ingrese el titulo: ")
      if verificacion(titulo):
          print("¡¡El elemento '{titulo}' ya existe!!")
          return
      genero=input("Ingrese el genero: ")
      try: 
         puntaje=input("Ingrese el puntaje del 1-10: ")
      except ValueError:
          puntaje=0

      if opc==1:
          autor=input("Ingrese el autor: ")
          paginas= input("Ingrese la cantidad de paginas: ")
          nuevo= {
              "tipo": "Libro", "titulo": titulo, "genero": genero, "autor": autor, "puntaje": puntaje, "paginas": paginas
          }

      elif opc==2:
          artista=input("Ingrese el artista: ")
          try:
             duraciòn=float(input("Ingrese la duracion de la musica: "))
          except ValueError:
              duraciòn=0.0
          nuevo={
              "tipo": "Musica", "titulo": titulo, "genero": genero, "artista": artista,  "puntaje": puntaje, "duraciòn": duraciòn
          }
      elif opc==3:
          director=input("INgrese el nombre del director: ")
          try:
             duraciòn=float(input("Ingrese la duraciòn de la pelicula: ")) 
          except ValueError:
              duraciòn=0.0
          nuevo={
              "tipo": "Pelicula", "titulo": titulo, "genero": genero, "director": director, "puntaje": puntaje,  "duracion": duraciòn
          }
      almacenes.append(nuevo)
      write_json("almacen.json", almacenes)
      print("¡Guardado existosamente!")
      
def ver_todos_elementos():
    carga_datos("almacen.json")
    
    if not almacenes:
        print("El almacen está vacio.")
        
    else:
        print("\n----- LISTADO COMPLETO -----")
        for i in almacenes:
            print(f"Tipo: {i['tipo']} | Título: {i['titulo']} | Género: {i['genero']}")
        print("----------------------------\n")
            
    
def buscar_elemento():
    separador()
    print("-----Buscar elementos-----")
    menu="""
    1.Buscar por titulo
    2. Buscar por autor/artista/director
    3. Buscar por genero
    4. Regresar al menu principal"""
    print(menu)
    separador()
    opc=pedir_opcion()
    separador()

    criterio=input("Ingrese el nombre, autor o genero a buscar: ").lower()
    resultados=[]
    
    for i in almacenes:
        if opc==1:
            if criterio in i.get("titulo", "").lower():
                resultados.append(i)
                
            elif opc==2:
                creador=f"{i.get('auto', '')}{i.get('artista', '')} {i.get('director', '')}"
                if criterio in creador:
                    resultados.append()
                    
            elif opc== 3:
                if criterio in i.get("genero", "").lower():
                    resultados.append(i)
                    
            separador()
            if resultados:
                print(f"Se encontraron{len(resultados)}coincidencia: ")
            for r in resultados:
                responsable=r.get("autor") or r.get("artista") or r.get("genero") or r.get("director") or "N/A"
                print(f"-> [{r['tipo'].upper()}] {r['titulo']} | Género: {r['genero']} | Creador: {responsable}")
            else:
                print(f"¡ No se encontró nada relacionado con '{criterio}' !")
            separador()


def eliminar_elemento():
    if not almacenes:
        print("NO hay nada que eliminar")
        return
    
    for idx, item in enumerate(almacenes):
        print(f"{idx}. {item['titulo']} {item['tipo']})")

    try:
        seleccion=int(input("Numero del elemento que desea borrar"))
        if 0 <= seleccion< len(almacenes):
            eliminado=almacenes.pop(seleccion)
            write_json("almace.json", almacenes)
            print(f"Eliminado:{eliminado['titulo']}")
        else:
            print("Numero no vàlido")
    except ValueError:
        print("Debe ingresar un nùmero entero y positvo")

def editar_elementos():
    separador()
    print("----Editar Elementos----")
    opciones="""
     1. Editar titulo
    2. Editar Genero
    3. Editar puntaje
    4. Cancelar 
    5. Regresar al menu principal"""
    print(opciones)

    titulo_buscar=input("Ingrese el titulo exacto del elementos que desea editar")
    
    elemento=next((item for item in almacenes if item ["titulo"].lower()== titulo_buscar), None)
    
    if not elemento:
        print("Elemento no encontrado.")
        return
    print(f"Editando: {elemento['titulo']} [{elemento['tipo']}]")
    
    if opciones == 1:
        nuevo = input("Nuevo título: ").strip()
        if any(i["titulo"].lower() == nuevo.lower() for i in almacenes):
            print("⚠️ Ese título ya existe.")
        else:
            elemento["titulo"] = nuevo
            print("✅ Título actualizado.")
    elif opciones == 2:
        elemento["genero"] = input("Nuevo género: ")
    elif opciones == 3:
        elemento["puntaje"] = input("Nuevo puntaje (1-10): ")
    else:
        print("Operación cancelada.")
        return
    guarda_datos("almacen.json")
    
        
def ver_por_categoria(tipo_deseado):
    separador()
    print("Ver todos los elementos")
    separador()
    menu = """1. Ver Libros
2. Ver Películas
3. Ver Música
4. Regresar al menú principal"""
    print(menu)
        
    opcion = input("Ingrese la opción: ") 
    carga_datos("almacen.json") # Cargamos los datos más recientes
    
    # Filtramos: creamos una lista solo con los elementos del tipo elegido
    elementos = [i for i in almacenes if i.get("tipo") == tipo_deseado]
    
    separador()
    print(f"--- LISTADO DE {tipo_deseado.upper()}S ---")
    
    if not elementos:
        print(f"No hay {tipo_deseado}s registrados.")
        return

    # Mostramos los elementos numerados
    for idx, item in enumerate(elementos, 1):
        # Datos comunes
        info = f"{idx}. Título: {item['nombre']} | Género: {item['genero']}"
        
        # Datos específicos según el tipo
        if tipo_deseado == "Libro":
            info += f" | Autor: {item.get('Autor', 'N/A')}"
        elif tipo_deseado == "Pelicula":
            info += f" | Director: {item.get('Director', 'N/A')}"
        elif tipo_deseado == "Musica":
            info += f" | Artista: {item.get('Artista', 'N/A')}"
            
        print(info)
    separador()

def verificacion_puntaje(puntaje):
    for e in almacenes:
        if e ["puntaje"].lower()== puntaje.lower():
            return True
        return False
        

def promedio_global(tipo)
   
   for puntaje in almacenes:
       suma= puntaje + puntaje/tipo
       print(suma)   
       
       guarda_datos("promedio.json")


def verificacion_tipo(tipo):
    for j in almacenes:
        if j ["tipo"].lower()== tipo.lower():
            return True
        return False

def promedio_por_categorias(puntaje):
    carga_datos(almacenes)
    separador()
    print("Valoraciones por categorias")
    separador()

    opcion="""1
    1. Valoracion por Libros
    2. Valoracion por musica
    3. Valoracion por pelicula
    4. Volver al menu principal"""
    print(opcion)
    separador()
    opc=pedir_opcion()
    separador()

    criterio=input("Ingrese el tipo de categoria que desea: ")
    resultados=[]


    for j in almacenes:
        if opc==1:
            if criterio in j.get("Libro", "").lower():
                 promedio= puntaje + puntaje /criterio
                 print(promedio)
        elif opc==2:
            if criterio in j.get("musica","").lower():
                 promedio= puntaje + puntaje /criterio
                 print(promedio)

        elif opc==3:
            if criterio in j.get("pelicula", "").lower():
                promedio=puntaje + puntaje/criterio
                print(promedio)

        elif opc==4:
            break
        else:
            print("En el archivo esta vacio por ende no hay voloraciones por tiopo")

        guarda_datos("promedio.json")


