import os
import yaml

class YamlToMd:
    def __init__(self, file):
        # string of filepath (i.e., 'data/amazon_comprehend.yaml')
        self.file = file
        self.data = {}
        self.load()

    # loads/updates self.data using given yaml file
    # file : string of filepath (i.e., 'data/amazon_comprehend.yaml')
    def load(self, file=None):
        if file is None:
            file = self.file
        with open(file, "r") as stream:
            try:
                parsed_yaml = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        # update self.data with data from new file
        self.data.update(parsed_yaml)

    # generates the output md file in the cwd
    # name : string of desired filename, with extension (default: uses original filename)
    def generate_md(self, name=None):
        if name is None: # reuse original filename if none provided
            name = os.path.basename(self.file).rsplit(".", 1)[0]
        if name[-3:] != '.md': # add .md extension if not there already
            name = name + '.md'

        
        

