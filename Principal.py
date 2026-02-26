from docs import carga_datos, guarda_datos, almacenes
import funcionalidad as funcion

ARCHIVO="almacen.json"
DOCUMENTO= "promedio.json"

def iniciar_programa():
   carga_datos(ARCHIVO, DOCUMENTO)

while True:
    funcion.separador()
    print(f"---GESTION DE ALMACEN ({len(almacenes)}item)---")
    funcion.separador()
    menu="""
    1. Añadir Elementos
    2. Ver todos los elementos
    3. Buscar elementos
    4. Editar elementos
    5. Eliminar elementos
    6. Ver todas las categorias
    7. Guardar y Cargar elementos
    8. Promedio por global
    9. Promedio por tipo
    10. Salir"""
    print(menu)

    opc=funcion.pedir_opcion()

    if opc == 1:
        funcion.añadir_elemento()
    elif opc==2:
        funcion.ver_todos_elementos()
    elif opc==3: 
        funcion.buscar_elemento()
    elif opc==4:
        funcion.editar_elementos()
    elif opc==5:
        funcion.eliminar_elemento()
    elif opc==6:
        funcion.ver_por_categoria()
    elif opc==7:
        print(carga_datos, guarda_datos)
    elif opc==8:
        funcion.promedio_global()
    elif opc==9:
        funcion.promedio_por_categorias()
    elif opc==10:
        break
    
    else: 
        print("Gracias por utilizar nuestro sitio")

if__name=="__main__"
iniciar_programa()