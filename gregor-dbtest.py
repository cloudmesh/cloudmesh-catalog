import yamldb
from cloudmesh.common.util import path_expand
from pathlib import Path
from pprint import pprint

filename = path_expand("~/.cloudmesh/catalog/data.yml")
print (filename)
print(yamldb.__version__)

db = yamldb.YamlDB(filename=filename)

source = path_expand("~/Desktop/cm/nist/catalog")

def _find_sources_from_dir(source=None):
    source = Path(source).resolve()
    result = Path(source).rglob('*.yaml')
    return result

files = _find_sources_from_dir(source=source)

for file in files:
    print (file)
    db.update(file)

pprint (db.data)