from yamldb import YamlDB


class DataBase:

    def __init__(self, name="~/.cloudmesh/catalog/data.yaml", kind=YamlDB):
        self = YamlDB(filename=name)
        #
        # TODO: create the database if it does not exists
        # check if yamldb already does this
        #
