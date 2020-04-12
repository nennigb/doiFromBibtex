![Python package](https://github.com/nennigb/doiFromBibtex/workflows/Python%20package/badge.svg)

# DOI From Bibtex - An utility to parse bibtex files, in order to recover the missing DOI
-----------------------------------------------------------------------------------------

According to the way bibtex files are obtained or build, the DOI field may be missing (e. g. google scholar). This package recovers it. After bibtex file's parsing, [DOI](https://simple.wikipedia.org/wiki/Digital_Object_Identifier) are recovered thanks to cross-references requests, using [REST API](https://github.com/CrossRef/rest-api-doc)'s python version.

> The Crossref API polices for polite requests, recommends using an Etiquette object in http requests. 
> This object should list some information on your project and a contact (see below).


## Dependencies
---------------
  - a python library implementing the Crossref API.  [crossrefapi](https://github.com/fabiobatalha/crossrefapi/)
  - a Bibtex parser for Python 2.7 and 3.3 or newer  [python-bibtexparser](https://github.com/sciunto-org/python-bibtexparser)


## Install 
----------
Without pip, run:
```
python3 setup.py install [--user]
```
For frequent updates (dev), prefer:
```
python3 setup.py develop [--user]
```
Using `pip3`, follow the steps [here](https://pip.pypa.io/en/stable/reference/pip_install/). First download or clone the repo, then run:
```
pip3 install path/to/doiFromBibtex-version.tar.gz [--user]
```
or in _editable_ mode if you want to modify the sources
```
pip3 install -e path/to/doiFromBibtex
```

## Usage example
----------------
To call the package, run:
```
python3 -m doifrombibtex input_file.bib output_file.bib
```
This will create the `output_file.bib` containing missing DOI.
To list syntax variant, run;
```  
python3 -m doifrombibtex -h
````
To run the test, omit `input_file` parameters:
```
python3 -m doifrombibtex
```

To specify your ettiquette (see crossref API recommendation), run:
```
python3 -m doifrombibtex examples/example.bib out.bib --etiquette 'My Project Name', 'My Project version', 'My Project URL', 'b@b.com'

```
To parse one or several bibtex entries, run:
```
python3 -m doifrombibtex /dev/stdin <<<'
@article{xxxx:1998,
	title = ".....",	
	year = ".....",	
	author = "....."
}' /dev/stdout
```
Here, the output in written on standard ouput (`stdout`). You may susbstitute with a path to write to a file.

## License
--------------------
This file is part of doiFromBibtex, An utility to parse bibtex files and recover the missing DOI.

doiFromBibtex is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

doiFromBibtex is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with doiFromBibtex.  If not, see <https://www.gnu.org/licenses/>.
