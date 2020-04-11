#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file is part of doiFromBibtex, An utility to parse bibtex files in order
to recover the missing DOI.

to get help:
```
python3 -m doifrombibtex -h
````
or consult README file for basic examples.
"""


import argparse
import bibtexparser as bp
from doifrombibtex import parse
import unittest

# define path to example file
EXAMPLE_FILE = 'examples/example.bib'


class TestSuite(unittest.TestCase):
    """ Define test cases for unittest.
    """

    def test_example(self):
        """ Tests bib entries from examples.bib.
        """
        # open bibtex test file as string
        bibdata = bp.loads(pkgutil.get_data('doifrombibtex',
                                            EXAMPLE_FILE), parser)
        # parse it
        bibdata_out, missing, stats = parse(bibdata)
        # check it
        entries = bibdata.entries_dict
        self.assertEqual(entries['Cuyt:1985']['doi'],
                         '10.1016/0377-0427(85)90019-6',
                         'incorrect doi')
        self.assertEqual(entries['Doppler:2016']['doi'],
                         '10.1038/nature18605',
                         'incorrect doi')


if __name__ == '__main__':
    """ Run parser, executed when the module is called.
    """

    import pkgutil
    from bibtexparser.bparser import BibTexParser

    # set output default name
    out_default = 'out.bib'
    my_etiquette = None   # setup it if you make intensive crossref request
    # run command line options parser
    parser = argparse.ArgumentParser(description='An utility to parse bibtex files in order to recover the missing DOI.')
    parser.add_argument('input', help='input bibtex file name (None: run the tests)',
                        nargs='?', default=None)
    parser.add_argument('output', help='output bibtex file name (default: ' + out_default + ')',
                        nargs='?', default=out_default)
    parser.add_argument('--etiquette', help="Provide info on your projet to cross ref :\
                        'My Project Name', 'My Project version', 'My Project URL', \
                        'My contact email'", nargs='+', type=str, default=my_etiquette)
    args = parser.parse_args()
    print("> Running parsing of {}.\n  The ouput will be written in {}\n".format(args.input, args.output))

    # Etiquette parsing
    if args.etiquette:
        if len(args.etiquette) == 4:
            print('> Your etiquette is : {}'.format(args.etiquette))
        else:
            raise ValueError('Etiquette must contains 4 strings. See the doc (-h option)')

    # customize bibtextparser option
    parser = BibTexParser(common_strings=True)
    # parser.ignore_nonstandard_types = True

    # open inputbibfile as file
    if args.input:
        with open(args.input) as file:
            bibdata = bp.load(file, parser)
        # parse it
        bibdata_out, missing, stats = parse(bibdata,
                                            my_etiquette=args.etiquette)
        # export comleted bibtex file
        with open(args.output, 'w') as bibOutputFile:
            # dump
            bp.dump(bibdata_out, bibOutputFile)

    else:
        # run unittest test suite
        unittest.main()

    # summary
    print('\n> stats : {} still missing doi, {} doi searches, in {} bibtex entries'
          .format(stats['doi_missing'], stats['doi_search'], stats['entry']))
    if missing:
        print('> it remains some missing doi :', missing)
