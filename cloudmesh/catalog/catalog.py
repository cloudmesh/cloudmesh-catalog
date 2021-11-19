from dataclasses import dataclass, field
import pickle
from fastapi import FastAPI

from pickleable_mixin import PickleableMixin

app = FastAPI()


@app.get("/cloudmesh/v1-0/catalog/{name}")
async def get_name(name):
    catalog = Catalog()
    entry = catalog.query({'name': name})
    return entry


class Catalog(PickleableMixin):
    def __init__(self, directory):
        self.directory = directory #string
        self.data = self.load(directory) #dictionary
        
    def query(search):
        if search.keys([0]) == 'name':
            for entry in self.data:
                if self.data['name'] == search.keys([1]):
                    return entry
        return None

    def add(self, file):
        pass
        # dictionary = yaml.load(file)
        # self.data.add(dictionary)

    def load(self, directory=None):
        if directory is None:
            directory = self.directory
        files = glob.glob(directory)
        for file in files:
            self.add(file)


@dataclass
class CatalogEntry():
    # UUID, globally unique
    id: str
    # Name of the service
    name: str
    # Human readable title
    title: str
    # True if public (needs use case to delineate what pub private means)
    public: bool
    # Human readable short description of the service
    description: str
    # The version number or tag of the service
    version: str
    # The license description
    license: str
    # yes/no/mixed
    microservice: str
    # e.g., REST
    protocol: str
    # Name of the distributing entity, organization or individual. It could be a vendor.
    owner: str
    # Modification timestamp (when unmodified, same as created)
    modified: str
    # Date on which the entry was first created
    created: str
    # Link to documentation/detailed description of service
    documentation: str = 'unknown'
    # Link to the source code if available
    source: str = 'unknown'
    # Human readable common tags that are used to identify the service that are associated with the service
    tags: list = field(default_factory=list)
    # A category that this service belongs to (NLP, Finance, …)
    categories: list = field(default_factory=list)
    # specification/schema: pointer to where schema is located
    specification: str = 'unknown'
    # Additional metadata: Pointer to where additional is located including the one here
    additional_metadata: str = 'unknown'
    # The endpoint of the service
    endpoint: str = 'unknown'
    # SLA/Cost: service level agreement including cost
    sla: str = 'unknown'
    # contact details of the people or organization responsible for the service (freeform string)
    authors: str = 'unknown'
    # description on how data is managed
    data: str = 'unknown'