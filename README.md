![Python package](https://github.com/nennigb/doiFromBibtex/workflows/Python%20package/badge.svg)

# DOI From Bibtex - An utility to parse bibtex files, in order to recover the missing DOI
-----------------------------------------------------------------------------------------

Depending of the way the bibtex files are obtained or build, the doi field may
be missing (e. g. google scholar). This basic package can be used to recover this
missing field automatically.
After a parsing of the bibtex file, the doi are recovered thank to crossref 
request throught the python version of the [REST API](https://github.com/CrossRef/rest-api-doc).

> The Crossref API polices for polite requests, recommand to use an Etiquette object for your http requests. 
> This object should list some inforation on your project and a contact (see below).


## Dependancies
---------------
  - A python library that implements the Crossref API.  [crossrefapi](https://github.com/fabiobatalha/crossrefapi/)
  - Bibtex parser for Python 2.7 and 3.3 or newer  [python-bibtexparser](https://github.com/sciunto-org/python-bibtexparser)


## Install 
----------
without pip
```
python3 setup.py install [--user]
```
for frequent updates (dev) it is better to use 
```
python3 setup.py develop [--user]
```
or preferably using `pip3` as explain [here](https://pip.pypa.io/en/stable/reference/pip_install/). First download or clone the repo, then
```
pip3 install path/to/doiFromBibtex-version.tar.gz [--user]
```
or in _editable_ mode if you want to modify the sources
```
pip3 install -e path/to/doiFromBibtex
```

## Usage example
----------------
To call the package, just do
```
python3 -m doifrombibtex input_file.bib output_file.bib
```
This will write the `output_file.bib` that contains the missing doi, normally ;-). Or
```  
python3 -m doifrombibtex -h
````
to get help on syntaxe. If `input_file` is not specified,
```
python3 -m doifrombibtex
```
tests are run. 

To specify your ettiquette (see crossref API recomandation), use
```
python3 -m doifrombibtex examples/example.bib out.bib --etiquette 'My Project Name', 'My Project version', 'My Project URL', 'b@b.com'

```
To directily parse from command line one or several bibtex entries, use
```
python3 -m doifrombibtex /dev/stdin <<<'
@article{xxxx:1998,
	title = ".....",	
	year = ".....",	
	author = "....."
}' /dev/stdout
```
The output can be also save in a file or redirected toward `stdout` as in this example.

## License
--------------------
This file is part of doiFromBibtex, An utility to parse bibtex files and
recover the missing DOI.

doiFromBibtex is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

doiFromBibtex is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with doiFromBibtex.  If not, see <https://www.gnu.org/licenses/>.
