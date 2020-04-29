#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:51:41 2020

@author: bn
"""

import doifrombibtex
import bibtexparser as bp
from crossref.restful import Works, Etiquette
from difflib import SequenceMatcher as SM
import warnings
import argparse
import unittest
import pkgutil

class TestSuite(unittest.TestCase):
    """ Define test cases for unittest.
    """

    def test_example(self):
        """ Tests bib entries from examples.bib.
        """
        # open bibtex test file as string
        bibdata = bp.loads(pkgutil.get_data('doifrombibtex',
                                            doifrombibtex.EXAMPLE_FILE),
                                            doifrombibtex.parser)
        test_etiquette = ('doifrombibtex',
                          doifrombibtex.__version__,
                          doifrombibtex.__url__, '')
        # parse it
        bibdata_out, missing, stats = doifrombibtex.parse(bibdata,
                                                          test_etiquette)
        # check it
        entries = bibdata.entries_dict
        self.assertEqual(entries['Cuyt:1985']['doi'],
                         '10.1016/0377-0427(85)90019-6',
                         'incorrect doi')
        self.assertEqual(entries['Doppler:2016']['doi'],
                         '10.1038/nature18605',
                         'incorrect doi')