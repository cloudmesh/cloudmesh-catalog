import os
from re import L
import re
import copy
from mdutils.mdutils import MdUtils
import yaml
from datetime import datetime

# returns a list of urls in given string
def extract_urls(text):
    urls = re.findall('(?P<url>https?://[^\s]+)', text)
    return urls

# converts urls to markdown-clickable urls 
# string -> string
def markdownify_urls(text):
    if type(text) != str:
        return text
    output = text
    urls = extract_urls(text)
    for url in urls:
        new_formatted = '[' + url + ']' + '(' + url + ')'
        output = output.replace(url, new_formatted)
    return output


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
    # dir : used only if name is default, signifies the output directory
    def generate_md(self, dir='', name=None):
        if name is None: # reuse original filename if none provided
            name = os.path.basename(self.file).rsplit(".", 1)[0] # strips to only the filename without extension (i.e., 'data/amazon_comprehend.yaml' -> 'amazon_comprehend')
            name = dir + name

        #-- BEGIN THE MD FILE BUILD --#
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
        mdFile.write('description: ' + markdownify_urls(self.data['description'].replace("\n", " ")))
        mdFile.new_line()
        mdFile.write('categories:')
        mdFile.new_line()
        self.md_write_list(mdFile, self.data['categories'])
        mdFile.write('tags:')
        mdFile.new_line()
        self.md_write_list(mdFile, self.data['tags'])
        mdFile.write('---')
        mdFile.new_line()

        # Description
        mdFile.new_header(level=1, title='Description')
        mdFile.new_line()
        mdFile.write(markdownify_urls(self.data['description'].replace("\n", " ")))
        mdFile.new_line()

        # Data
        mdFile.new_header(level=1, title='Data')
        mdFile.new_line()
        mdFile.write(markdownify_urls(self.data['data'].replace("\n", " ")))
        mdFile.new_line()

        # Details
        mdFile.new_header(level=1, title='Details')

        table_keys = ['name', 'public', 'version', 'license', 'microservice', 'protocol', 'owner', 'modified', 'created', 'documentation', 'source', 'specification', 'additional_metadata', 'endpoint', 'sla', 'authors']
        table_columns = ['Attribute', 'Value']

        table_strings = copy.deepcopy(table_columns)
        for k in table_keys:
            table_strings.extend([k, markdownify_urls(self.data[k])])
        mdFile.new_table(columns=len(table_columns), rows=len(table_keys)+1, text=table_strings, text_align='center')


        # write to file
        mdFile.create_md_file()

        # workaround to replace empty three lines at beginning of file added by mdutils
        content = mdFile.read_md_file(name)
        f = open(name+'.md', "w")
        f.write(content[3:])
        f.close()

        

# FOR TESTING/generate md files here
if __name__ == "__main__":
    converter = YamlToMd('data/catalog/amazon_comprehend.yaml')
    converter.generate_md(dir='output/')


    

        
        

