from unittest import TestCase
import data.load as dl
import os
import pandas as pd

os.chdir("..")

class Test(TestCase):


    def test_cwb(self):
        df = dl.comm_well_being('all')
        cwb_1 = dl.comm_well_being(2001)
        cwb_2 = dl.comm_well_being(2006)
        cwb_3 = dl.comm_well_being(2011)
        cwb_4 = dl.comm_well_being(2016)

        self.assertEqual(df.shape[1], cwb_1.shape[1] + cwb_2.shape[1] + cwb_3.shape[1] + cwb_4.shape[1] )
        self.assertEqual('CSD Code',df.index.name)

    def test_cwb_filter_prov(self):
        df = dl.comm_well_being('all')
        cwb_1 = dl.comm_well_being(2001)
        cwb_2 = dl.comm_well_being(2006)
        cwb_3 = dl.comm_well_being(2011)
        cwb_4 = dl.comm_well_being(2016)
        bad_df = pd.DataFrame([1,2,3,4])
        bad_prov = 'NSNB'

        #Check if it runs normally
        try:
            dl.cwb_filter_prov(cwb_1,'NB')
            dl.cwb_filter_prov(df,'NB')
        except:
            self.fail()

        #Check if value raised
        with self.assertRaises(ValueError):
            dl.cwb_filter_prov(bad_df, 'NB')

        #Check if bad prov value raises
        with self.assertRaises(ValueError):
            dl.cwb_filter_prov(bad_df, 'NBNS')






