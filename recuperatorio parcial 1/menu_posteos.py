from funciones_post import * 

bandera_opcion_uno = False
bandera_opcion_tres = False
desea_seguir = "s"
lista_posteos = []
while desea_seguir == "s":
    opcion = menu()
    limpiar_terminal()

    match opcion:
        case "1":
            nombre_arch = input("ingrese el nombre del archivo: ")
            lista_posteos = abrir_archivo(nombre_arch)
            
            if lista_posteos:
                print("Se cargo el archivo correctamente")
                input("presione enter para continuar")
                bandera_opcion_uno = True
            else:
                lista_posteos = []
                print("No se pudo cargar el archivo")
                input("presione enter para continuar")
        
        case "2":
            if bandera_opcion_uno:
                mostrar_posteos(lista_posteos)
                input("presione enter para continuar")
                
            else:
                print("No hay ningun archivo cargado, vuelva a la opcion 1 por favor.")
                input("presione enter para continuar")
        
        case "3":
            if bandera_opcion_uno:
                asignar_estadisticas(lista_posteos)
                mostrar_posteos(lista_posteos)
                input("presione enter para continuar")
                puerta_opcion_tres = True
            
            else:
                print("No hay achivo cargado, vuelva a la opcion 1")
                input("presione enter para continuar")
        
        case "4":
            if bandera_opcion_uno and bandera_opcion_tres:
                if len(lista_posteos) > 0:
                    filtrar_por_likes(lista_posteos)
                    print(f"archivo likes.csv creado correctamente")
                    input("presione enter para continuar")
            
            else:
                print("Verifique que haya datos en la lista, cargue archivo (opcion 1) y asigne estadisticas (opcion 3)")
                input("presione enter para continuar")
        
        case "5":
            if bandera_opcion_uno and bandera_opcion_tres:
                if len(lista_posteos) > 0:
                    filtrar_por_dislike(lista_posteos)
                    print(f"archivo dislikes.csv creado correctamente")
                    input("presione enter para continuar")
            
            else:
                print("Verifique que haya datos en la lista, cargue archivo (opcion 1) y asigne estadisticas (opcion 3)")
                input("presione enter para continuar")


        case "6":
            if bandera_opcion_uno and bandera_opcion_tres:
                if len(lista_posteos) > 0:
                    promedio_followers(lista_posteos)
                    input("presione enter para continuar")
            else:
                print("Verifique que haya datos en la lista, cargue archivo (opcion 1) y asigne estadisticas (opcion 3)")
                input("presione enter para continuar")
        
        case "7":
            if bandera_opcion_uno and bandera_opcion_tres:
                if len(lista_posteos) > 0:
                    cargar_archivo_json(lista_posteos, "usuarios_ordenados")
                    input("presione enter para continuar")
            else:
                print("Verifique que haya datos en la lista, cargue archivo (opcion 1) y asigne estadisticas (opcion 3)")
                input("presione enter para continuar")
        
        case "8":
            if bandera_opcion_uno:
                if len(lista_posteos) > 0:
                    if bandera_opcion_tres:
                        if lista_posteos[0]["tiempo"] > 0:
                            informar_posteo_mas_likeado(lista_posteos)
                            input("presione enter para continuar")
                    else:
                        print("asigne estadisticas")
                        input("presione enter para continuar")
                else:
                    print("No hay competidores, cargue un archivo en opcion 1")
                    input("presione enter para continuar")
            else:
                print("cargue archivo antes de comenzar, opcion 1")
                input("presione enter para continuar")
        
        case "9":
            desea_seguir = input("presione s para continuar, de lo contrario presione n: ")
            if desea_seguir == "n":
                break
    pausar()


