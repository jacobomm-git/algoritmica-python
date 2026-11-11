"""Algorismes seleccionats de pràctiques acadèmiques. Vegeu AUTORIA.md."""

def subcadena_mes_llarga(cadena):
    """
    Aquesta funció identifica la subcadena més llarga sense cap caràcter repetit.
    
    Parameters
    ----------
    cadena: string 
        Cadena donada
        
    Returns
    -------
    subcadena: string
        Subcadena més llarga sense caràcters repetits
    """
    lista = []
    i, j = 0 ,0
    iniciSubcadena, finalSubcadena = 0, 0
    maxSubcadena = 0
    #iteramos mientras que el final de la subcadena sea menor que la longitud de la cadena
    #asociamos al final de la subcadena el incdice i
    while i < len(cadena):
      if(cadena[i] not in lista):
        #mientras que la letra no se vaya repitiendo en la lista, vamos añadiendo la siguiente letra
        #de la cadena
        lista.append(cadena[i])
        i+=1
        #la longitud maxima de la subcadena se puede determinar si restamos la posicion del indice del final de la
        #subcadena y lo restamos por el indice del inicio de la subcadena. Si esta resta es mayor a la longitud del
        #la maxima subcadena, substituimos los valores de los indices i y j por los nuevos y substituimos tambien el
        #valor del maximo por la resta de estos.
        if(maxSubcadena < (i-j)):
          maxSubcadena = i-j
          iniciSubcadena = j
          finalSubcadena = i
          #si el valor se repite aumentamos el indice del calor del inicio de la subcadena y quitamos la primera letra
          #que seria la que se repite al final de la subcadena
      elif(cadena[i] in lista):
        lista.remove(cadena[j])
        j+=1
      
    return cadena[iniciSubcadena:finalSubcadena]
