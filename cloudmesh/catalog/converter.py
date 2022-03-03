import os
import textwrap

import yaml

from cloudmesh.common.util import readfile


class Converter:

    def __init__(self, filename=None):
        # data/catalog/azure/bot_services.yaml"
        if not os.path.exists(filename):
            raise ValueError("file can not be found")
        self.content = readfile(filename)

        self.data = yaml.safe_load(self.content)

        day, month, year = self.data["modified"].split("-")
        import calendar

        self.data["label"] = "wrong"
        self.data["title"] = self.data["name"]
        self.data["year"] = year
        self.data["month"] = calendar.month_abbr[int(month)].lower()

        self.data["url"] = self.data["documentation"]
        if "http" not in self.data["url"]:
            raise ValueError("url not found")

    def dedent(self, text):
        return textwrap.dedent(text).strip() + "\n"

    def bibtex(self):
        bibtex_entry = """
        @misc{{{id},
          title={{{title}}},
          name={{{name}}},
          author={{{author}}},
          howpubllished={{Web Page}},
          month = {month},
          year = {{{year}}},
          url = {{{url}}}
        }}
        """
        return self.dedent(bibtex_entry.format(**self.data))

    def hugo_markdown(self):
        for entry in ["tags", "categories"]:
            self.data[entry] = "\n".join(["- " + value for value in self.data[entry]])


        markdown_entry = textwrap.dedent("""
        ---
        date: {modified}
        title: {title}
        tags: 
        {tags}
        categories: 
        {categories}
        linkTitle: MISSING
        description: {description}
        author: {author}
        draft: False
        ---
                
        ## Description
        
        {description}

        ## Version
        
        {version}

        ## Documentation
        
        {documentation}
        
        ## SLA
        
        {sla}
        
        ## Data
        
        {data}
        """)
        return self.dedent(markdown_entry.format(**self.data))

    def markdown(self):
        self.data["tags"] = ", ".join(self.data["tags"])
        self.data["categories"] = ", ".join(self.data["categories"])
        markdown_entry = """
        # {title}
        
        * Author: {author}
        * Version: {version}
        * Modified: {modified}
        * Created: {created}
        * <{documentation}>
        * Tags: {tags}
        * Categories: {categories}
        
        ## Description

        {description}
        
        ## SLA
        
        {sla}
        
        ## Data
        
        {data}
        """
        return self.dedent(markdown_entry.format(**self.data))
