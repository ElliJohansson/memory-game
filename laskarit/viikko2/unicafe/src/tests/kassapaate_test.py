import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaate_saldo_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100_000)

    def test_lounaiden_maara_oikein(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_edullinen_kateismaksu_toimii(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100_240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_kateismaksu_toimii(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450), 50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100_400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_kateismaksu_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100_000)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukas_kateismaksu_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100_000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullinen_korttimaksu_toimii(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100_000)

    def test_maukas_korttimaksu_toimii(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100_000)
     
    def test_edullinen_korttimaksu_ei_riittava(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_korttimaksu_ei_riittava(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_rahanlataus_kortille_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100_200)
        
    def test_rahanlataus_kortille_ei_toimi(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100_000)