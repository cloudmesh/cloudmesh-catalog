import os
from re import L
from mdutils.mdutils import MdUtils
import yaml
from datetime import datetime

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
        if len(parsed_yaml.keys()) == 1:
            for key in parsed_yaml.keys():
                data = parsed_yaml[key]
        else:
            raise ValueError('invalid input yaml format: more than 1 base-level key')
        self.data.update(data)

    # list of strings to a string of a dashed markdown list
    def md_write_list(self, md_file, list: list):
        for str in list:
            md_file.write('- '+str+'\n')

    # generates the output md file in the cwd
    # name : string of desired filename (default: uses original filename)
    def generate_md(self, name=None):
        if name is None: # reuse original filename if none provided
            name = os.path.basename(self.file).rsplit(".", 1)[0]

        #-- BEGIN THE MD FILE BUILD --#
        print(self.data)
        mdFile = MdUtils(file_name=name,title='')

        # Metadata 
        mdFile.write('---')
        mdFile.new_line()
        mdFile.write('title: ' + self.data['title'])
        mdFile.new_line()
        mdFile.write('author: ' + self.data['author'])
        mdFile.new_line()
        mdFile.write('slug: ' + self.data['slug'])
        mdFile.new_line()
        mdFile.write('date: ' + datetime.today().strftime('%Y-%m-%d'))
        mdFile.new_line()
        mdFile.write('description: ' + self.data['description'].replace("\n", " "))
        mdFile.new_line()
        mdFile.write('categories:')
        mdFile.new_line()
        self.md_write_list(mdFile, self.data['categories'])
        mdFile.write('tags:')
        mdFile.new_line()
        self.md_write_list(mdFile, self.data['tags'])
        mdFile.write('---')
        mdFile.new_line()
        # Data
        mdFile.new_header(level=1, title='Data')
        mdFile.new_line()
        mdFile.write(self.data['data'].replace("\n", " "))
        mdFile.new_line()
        mdFile.new_header(level=1, title='Details')

        # write to file
        mdFile.create_md_file()



        

# FOR TESTING
if __name__ == "__main__":
    converter = YamlToMd('data/amazon_comprehend.yaml')
    converter.generate_md()


    

        
        

