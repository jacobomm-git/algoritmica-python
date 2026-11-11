"""Algorismes seleccionats de pràctiques acadèmiques. Vegeu AUTORIA.md."""

def merge(x,y):

    if len(x) < 1:
        return y
    if len(y) < 1:
        return x
    if x[0] <= y[0]:
        return [x[0]] + merge(x[1:],y)
    else:
        return [y[0]] + merge(x,y[1:])

def mergesortParelles(llista):
    """
    Aquesta funció va partint la llista en una banda dreta i una esquerra
    fins que aquestes bandes tenen un element quan ho aconsegueix, 
    crida merge per fusionar ambdues bandes de manera ordenada
    fins arribar a fusionar la llista completa original.
    """
    if len(llista) < 2:
        return llista
    else:
      middle = (len(llista) // 2)
      left = mergesortParelles(llista[:middle])
      right = mergesortParelles(llista[middle:])
      return merge(left, right)

def quick_sortParelles(A):
  quick_sort_r(A, 0, len(A) - 1)

def quick_sort_r(A , first, last):
                                      
    if last > first:
        pivot = partition(A, first, last) 
        quick_sort_r(A, first, pivot - 1) 
        quick_sort_r(A, pivot + 1, last)

def partition(A, first, last):

    mid = (first + last)//2  
    if A[first] > A [mid]: A[first], A[mid] = A[mid], A[first]
    if A[first] > A [last]: A[first], A[last] = A[last], A[first]
    if A[mid] > A[last]:   A[mid], A[last] = A[last], A[mid]  
    A[mid], A[first] = A[first], A[mid] 
    pivot = first
    i = first + 1
    j = last
    while True:
        while i <= last and A[i] <= A[pivot]: i += 1
        while j >= first and A[j] > A[pivot]: j -= 1
        if i >= j: break
        else:
            A[i], A[j] = A[j], A[i]
    A[j], A[pivot] = A[pivot], A[j]
    return j
