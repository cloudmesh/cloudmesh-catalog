Documentation
=============


[![image](https://img.shields.io/travis/TankerHQ/cloudmesh-bar.svg?branch=main)](https://travis-ci.org/TankerHQ/cloudmesn-bar)

[![image](https://img.shields.io/pypi/pyversions/cloudmesh-bar.svg)](https://pypi.org/project/cloudmesh-bar)

[![image](https://img.shields.io/pypi/v/cloudmesh-bar.svg)](https://pypi.org/project/cloudmesh-bar/)

[![image](https://img.shields.io/github/license/TankerHQ/python-cloudmesh-bar.svg)](https://github.com/TankerHQ/python-cloudmesh-bar/blob/main/LICENSE)

see cloudmesh.cmd5

* https://github.com/cloudmesh/cloudmesh.cmd5

## Adding catalog & registry data

To add catalog and registry data for new services, one must create new .yaml files in the appropriate folders: 'data/catalog/my_example.yaml' and 'data/registry/my_example.yaml'. Each file must follow yaml formatting similar to the following example.

Example file: Amazon Comprehend (Catalog), amazon_comprehend.yaml

```
amazon_comprehend:
  id: unknown
  name: Amazon Comprehend
  title: Amazon Comprehend
  author: Amazon
  slug: amazon-comprehend
  public: true
  description: |
    Comprehend is Amazon's solution for cloud-based NLP. It is available with an AWS account. To use,
    it requires use of either the AWS Command Line Interface or an AWS SDK for Python, Java, or .NET.
    Notable features include functionality for giving batches of documents to be processed as well as
    submission of multiple jobs in a list. The DetectEntities function also allows use of a custom-trained
    model, but many other functions do not.
  version: unknown
  license: unknown
  microservice: no
  protocol: AWS API
  owner: Amazon Web Services
  modified: 9/29/2021
  created: 11/29/2017
  documentation: https://docs.aws.amazon.com/comprehend/index.html
  source: unknown
  specification: unknown
  tags: ["nlp", "nlp service", "machine learning", "cloud service", "nlp api",
        "deep learning", "natural language processing", "artificial intelligence"]
  categories: ["NLP"]
  additional_metadata: unknown
  endpoint: unknown
  sla: https://aws.amazon.com/machine-learning/language/sla/
  authors: The AWS team can be contacted through support ticket at https://aws.amazon.com/contact-us/
  data: |
    User data is stored on Amazon servers under the associated AWS account and is protected under the AWS
    shared responsibility model as detailed here https://aws.amazon.com/compliance/shared-responsibility-model/
```

## Using the Catalog and Registry classes

Written in catalog.py and registry.py are classes capable of reading and storing the data written in the .yaml files. Both use the same interface.
Here is an example of the Catalog class in action:

```
# initialize the catalog using data found in the given directory
catalog = Catalog('data/catalog/')
# query the catalog for Amazon Comprehend data, save result to amazon_catalog_data
amazon_catalog_data = cat.query({'name': 'Amazon Comprehend'})
# add a new data file to the catalog
catalog.add('new_example/azure_language.yaml')
# save entire catalog to a pickle file
catalog.to_pickle('catalog.pkl')
# print catalog data
print(catalog.data)
```

## Using the yaml to markdown conversion script

In 'scripts/yaml_to_md.py' is a class YamlToMd used to assist in the conversion of .yaml catalog data to a readable markdown page.
Here is an example which takes the catalog data entry 'data/catalog/amazon_comprehend.yaml' and produces 'output/amazon_comprehend.md':

```
converter = YamlToMd('data/catalog/amazon_comprehend.yaml')
converter.generate_md(dir='output/')
```
