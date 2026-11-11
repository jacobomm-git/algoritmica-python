"""Algorismes seleccionats de pràctiques acadèmiques. Vegeu AUTORIA.md."""

def rle(text):
    """
    Aquesta funció retorna un text codificat segons run length encoding.
    
    Parameters
    ----------
    text: string
        text a codificar
        
    Returns
    -------
    text: string
        text codificat
    """
    if not text:
        return ''
    t = ''
    lista = []
    for i in text:
      if(i in lista or len(lista)==0):
        lista.append(i)
      else:
        t = t + lista[0] + str(len(lista))
        lista.clear()
        lista.append(i)
    t = t + lista[0] + str(len(lista))
    
    return t
