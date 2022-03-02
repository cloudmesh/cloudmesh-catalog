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
        return textwrap.dedent(bibtex_entry.format(**self.data)).strip() + "\n"

    def hugo_markdown(self):
        markdown_entry = """
        ---
        author: {author}
        title:  {title}
        ---
        
        ## Description
        
        {description}
        """
        return markdown_entry.format(**self.data)

    def markdown(self):
        markdown_entry = """
        ---
        author: {author}
        title:  {title}
        ---

        ## Description

        {description}
        """
        return markdown_entry.format(**self.data)
