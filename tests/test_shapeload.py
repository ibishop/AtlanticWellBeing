from unittest import TestCase
import shapefiles.load as load
import os

#Change directory to right one
os.chdir( os.getcwd()[:-6])

class Test(TestCase):

    def test_cd_shape(self):
        print(os.getcwd())
        df = load.cd_shape()
        # Is non-empty
        self.assertNotEqual( df.shape[0], 0 )
        # Is properly projected
        self.assertEqual( df.crs.name , 'WGS 84')

    def test_csd_shape(self):
        df = load.csd_shape()

        # Is non-empty
        self.assertNotEqual( df.shape[0], 0 )
        # Is properly projected
        self.assertEqual( df.crs.name , 'WGS 84')

    def test_hr_shape(self):
        df = load.hr_shape()
        # Is non-empty
        self.assertNotEqual(df.shape[0], 0)
        # Is properly projected
        self.assertEqual(df.crs.name, 'WGS 84')
        #Ensure it has the correct column
        self.assertTrue('PRUID' in df.columns)

    def test_mun_shape(self):
        self.fail()

    def test_prop_shape(self):

        df = load.nb_prop_shape()
        # Is non-empty
        self.assertNotEqual(df.shape[0], 0)
        # Is properly projected
        self.assertEqual(df.crs.name, 'WGS 84')
