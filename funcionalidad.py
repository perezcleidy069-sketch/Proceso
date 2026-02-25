from docs import*
data="almacen.json"

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
    separador()
    print("Ver todos los elementos")
    separador()
    menu="""
    1. Ver todos los libros
    2. Ver todos las peliculas
    3. Ver todos las musicas"""
    print(menu)

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

    criterio=input("Ingrese el tèrmino que busca: ").lower()
    resultados=[]

    for i in almacenes:
        if opc=="1" and criterio in i["titulo"].lower():
            resultados.append(i)
        elif opc=="2":
            creador=str(i.get("autor", "")) + str(i.get("artista", "")) + str(i.get("director", ""))
            if criterio in creador.lower():
                resultados.append(i)
        elif opc== "3" and criterio in i["genero"].lower():
            resultados.append(i)

        if resultados:
            for r in resultados:
                print(f"[{r['tipo']}]{r['titulo']}-{r['genero']}")
            else:
                print("¡No se encuntra lo que desea buscar!")

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

    titulo_buscar=input("Ingrese el titulo exacto del elementos que desea editar")

    indice=-1
    for i, item in enumerate(almacenes):
        if item["titulo"].lower()==titulo_buscar
        indice=i
        break

    elemento =almacenes[indice]
    print(f"Editando:{elemento['titulo']}({elemento['tipo']})")
    opciones="""
    1. Editar titulo
    2. Editar Genero
    3. Editar puntaje
    4. Cancelar 
    5. Regresar al menu principal"""
    print(opciones)

    opc=pedir_opcion()

    if opc==1:
        nuevo_titulo=input("Nuevo titulo:")
        if verificacion(nuevo_titulo):
            print("Ese titulo ya existe")
        else:
            elemento["titulo"]= nuevo_titulo
    elif opc==2:
        elemento["genero"]= input(" Nuevo genero: ")
    elif opc==3:
        elemento["puntaje"]=input("Nuevo puntaje (1-10): ")
    elif opc==4:
        print("Edicion cancelada")
        return
    else:
        print("Regresando al menu principal")


def guardar_y_cargar_elementos():
    guarda_datos("almacen.json")
    almacenes.clear()
    datos_nuevos=read_json("almacen.json")
    almacenes.extend(datos_nuevos)

    separador()
    print(f"Datos guardados. {len(almacenes)} elementos en la memoria.")
    separador()