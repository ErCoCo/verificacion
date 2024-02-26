from unittest import TestCase
from radar_meteorologico import alcance_del_radar

class TestRadarMeteorologico(TestCase):

    def test_valores_validos(self):
        """ Test de valores validos """
        self.assertAlmostEqual(alcance_del_radar(0.5, 2), 74999.700)
        self.assertAlmostEqual(alcance_del_radar(0.69, 3.99), 103499.4015)
        self.assertAlmostEqual(alcance_del_radar(0.2, 1),29999.850 )


    def test_valores_fuera_rango(self):
        """ Test ValueError cuando hay valores positivos fuera de rango """
        self.assertRaises(ValueError, alcance_del_radar, 0.2, 5.0)
        self.assertRaises(ValueError, alcance_del_radar, 0.2, 99)
        self.assertRaises(ValueError, alcance_del_radar, 1, 2)

    def test_valores_negativos(self):
        """ Test ValueError cuando hay de valores negativos """
        self.assertRaises(ValueError, alcance_del_radar, 0.5, -2)
        self.assertRaises(ValueError, alcance_del_radar, 0.5, -1)
        self.assertRaises(ValueError, alcance_del_radar, -0.5, 2) 

    def test_T_menor_tau(self):
        """ Test ValueError cuando T es menor que tau """
        self.assertRaises(ValueError, alcance_del_radar, 0.0000000000000000000000002, 0.39)
        self.assertRaises(ValueError, alcance_del_radar,  0.0000000000000000000000001, 0.2) 

    def test_strings(self):
        """ Test TypeError cuando hay entrada de strings """
        self.assertRaises(TypeError, alcance_del_radar, 0.5, "hola")
        self.assertRaises(TypeError, alcance_del_radar, 0.69, "cuatro")
        self.assertRaises(TypeError, alcance_del_radar, 0.2, "six")
        self.assertRaises(TypeError, alcance_del_radar, "verificiacion", 3.99)
        self.assertRaises(TypeError, alcance_del_radar, "software", 1)

    def test_booleanos(self):
        """ Test TypeError cuando hay entrada de booleanos """
        self.assertRaises(TypeError, alcance_del_radar, 0.5, True)
        self.assertRaises(TypeError, alcance_del_radar, False, 2.0)


        


