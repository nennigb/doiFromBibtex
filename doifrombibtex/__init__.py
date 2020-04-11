# -*- coding: utf-8 -*-
r"""
doifrombibtex  -- An utility to parse bibtex files in order to recover the missing DOI
==============================================================================


.. include::../README.md
    :start-line:2
    :raw:
"""

import bibtexparser as bp
from crossref.restful import Works, Etiquette
from difflib import SequenceMatcher as SM
import warnings

# default options
TOL_MATCH = 0.8  # 80% of matching for title
# sleep Time for crossref api
# sleep = 0.05
# max number of tested record in crossref api
COUNT = 50


def getDoiWithCrossRef(entry, my_etiquette):
    """ Get the doi of a bibtex entry thanks to crossref.

    Parameters
    ----------
    entry : BibDatabase
        The bibtex record with  missing doi.
    my_etiquette : tuple
        A record that contains all require fields to create Etiqette object.

    Returns
    -------
    doi : string
        the doi code.

    """
    # tries counter for each entry
    count = 0
    # store if a match has been found
    match = False
    # if provide create the Etiquette object
    if my_etiquette:
        etiquette = Etiquette(*my_etiquette)
        print(etiquette)
    else:
        etiquette = None

    # create crossref api instance for request
    works = Works(etiquette=etiquette)
    # convert entry to unicode for searching
    entry_unicode = bp.customization.convert_to_unicode(entry.copy())

    # Check for mandatory field
    try:
        # extract basic fields
        author1 = entry_unicode['author'].split(',')[0].strip()
        title = entry_unicode['title'].strip()
        year = entry_unicode['year'].strip()
    except Exception:
        warnings.warn("author, title and year fields are missing in entry {}\
                      ".format(entry_unicode))
        doi = None
        return doi

    w1 = works.query(author=author1,
                     bibliographic=title).filter(until_pub_date=year,
                                                 from_pub_date=year,
                                                 type='journal-article').sort('score').order('desc')
    # parse the crossref record to find the "best" match
    for item in w1:
        count += 1
        # fuzzy comprare
        ratio = SM(None, title, item['title'][0]).ratio()
        if ratio > TOL_MATCH:
            match = True
            break
        # limit the number of query
        if count > COUNT:
            print('  Reach maximal number of tries ({}) \
for this record  {}'.format(COUNT, entry_unicode))
            break

    if match:
        doi = item['DOI']
    else:
        print("  MISSING : {}, {}".format(entry_unicode['author'],
                                          entry_unicode['title']))
        doi = None

    return doi


def parse(bibdata, my_etiquette=None):
    """ Run the doi research.

    Parameters
    ----------
    bibdata: BibDatabase
        The bibtex record with  missing doi.
    my_etiquette : tuple
        A record that contains all require fields to create Etiqette object.

    Returns
    -------
    bibdata : BibDatabase
        Output bibtex file with doi field completed.
    missing : list
        A list of missing bibtex entry id
    stats : dict
        Summurize some stats about the requests number and succes.

    """

    # list to store not found doi
    missing = []
    # init stats
    stats = {'entry': 0, 'doi_search': 0, 'doi_missing': 0}
    # parse it
    print('> Start to process...')
    for entry in bibdata.entries:
        # only journal article are looked for
        if entry['ENTRYTYPE'] == 'article':
            stats['entry'] += 1
            # is there a doi
            try:
                entry['doi']
            # if no making a request on cross ref
            except Exception:
                stats['doi_search'] += 1
                doi = getDoiWithCrossRef(entry, my_etiquette)
                if doi:
                    entry['doi'] = doi
                    print('  FOUND :', entry['author'], entry['title'],
                          entry['doi'])
                else:
                    stats['doi_missing'] += 1
                    missing.append(entry['ID'])

    return bibdata, missing, stats
