import itertools
import unittest

from algoritmos.cadenas import subcadena_mes_llarga
from algoritmos.compresion import rle
from algoritmos.ordenacion import mergesortParelles, quick_sortParelles


class AlgoritmosTest(unittest.TestCase):
    def test_rle_casos_de_uso_y_vacio(self):
        for original, esperado in [
            ('', ''), ('A', 'A1'), ('ABBBBNNNEEEDDDZZAAAAA', 'A1B4N3E3D3Z2A5'),
            ('BBBBBBBBBBBBBBBBBWWWWWWZAAA', 'B17W6Z1A3'), ('ññá', 'ñ2á1'),
        ]:
            with self.subTest(original=original):
                self.assertEqual(rle(original), esperado)

    def test_subcadena_contra_busqueda_exhaustiva(self):
        for n in range(7):
            for chars in itertools.product('abc', repeat=n):
                original = ''.join(chars)
                resultado = subcadena_mes_llarga(original)
                maxima = max((j-i for i in range(n+1) for j in range(i,n+1)
                              if len(set(original[i:j])) == j-i), default=0)
                self.assertIn(resultado, original)
                self.assertEqual(len(set(resultado)), len(resultado))
                self.assertEqual(len(resultado), maxima)

    def test_ordenacion_contra_sorted(self):
        for n in range(7):
            for values in itertools.product((-1, 0, 1), repeat=n):
                original = list(values)
                self.assertEqual(mergesortParelles(original), sorted(original))
                self.assertEqual(original, list(values))
                copia = original.copy()
                quick_sortParelles(copia)
                self.assertEqual(copia, sorted(original))


if __name__ == '__main__':
    unittest.main()
