# Algorismes en Python

Selecció de tres pràctiques d'algorísmica: compressió de text, cerca d'una subcadena sense caràcters repetits i ordenació. Inclou les implementacions extretes dels quaderns i comprovacions executables amb la biblioteca estàndard.

| Exercici | Mòdul | Quadern | Què treballa |
| --- | --- | --- | --- |
| Run Length Encoding | [compresion.py](algoritmos/compresion.py) | [RLE](notebooks/01-compresion-rle.ipynb) | Agrupar repeticions consecutives i construir una representació compacta. |
| Subcadena més llarga | [cadenas.py](algoritmos/cadenas.py) | [Subcadenes](notebooks/02-subcadena-sin-repeticiones.ipynb) | Fer avançar els límits d'una finestra sense repetir caràcters. |
| Merge sort i quicksort | [ordenacion.py](algoritmos/ordenacion.py) | [Ordenació](notebooks/03-ordenacion.ipynb) | Recursivitat, divisió del problema, fusió i partició. |

## Execució

Els mòduls i els tests no necessiten dependències externes. S'han comprovat amb Python 3.14; el codi utilitza funcionalitats compatibles amb Python 3.10 o posterior.

Des de l'arrel del repositori:

```bash
python -m unittest discover -s tests -v
```

Exemple d'ús:

```python
from algoritmos.compresion import rle
from algoritmos.cadenas import subcadena_mes_llarga
from algoritmos.ordenacion import mergesortParelles, quick_sortParelles

print(rle("AAABB"))                         # A3B2
print(subcadena_mes_llarga("abcabcbb"))     # abc
print(mergesortParelles([4, 1, 3, 1]))        # [1, 1, 3, 4]

valors = [4, 1, 3, 1]
quick_sortParelles(valors)                   # modifica la llista
print(valors)                               # [1, 1, 3, 4]
```

## Comprovacions

- Casos de compressió amb una entrada buida, caràcters repetits i Unicode.
- 1.093 cadenes de longitud zero a sis sobre l'alfabet `abc`, contrastades amb una cerca exhaustiva de la longitud òptima.
- 1.093 llistes de longitud zero a sis amb valors `-1`, `0` i `1`, contrastades amb `sorted` per a les dues ordenacions.

La funció RLE original fallava amb una cadena buida. La correcció retorna una cadena buida i es manté tant al mòdul com al quadern. Les altres implementacions seleccionades es conserven.

## Decisions i límits

El quadern conserva el context de l'exercici; el mòdul facilita l'execució fora de Jupyter. S'han eliminat les sortides i els metadades del dispositiu original.

La fusió recursiva crea talls i llistes noves, i pot arribar al límit de recursivitat en entrades grans. Quicksort també conserva una implementació acadèmica recursiva. Les proves comproven els casos descrits, sense atribuir rendiment mesurat per a grans volums.

La representació RLE d'aquest exercici no defineix un format de fitxer ni un descodificador. La seva utilitat aquí és entendre com es representen seqüències repetides.

Vegeu [l'autoria i la procedència](AUTORIA.md).
