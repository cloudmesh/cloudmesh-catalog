# Cloudmesh Catalog

Cloudmesh catalog can be used to store information about a service, software
component, or project. The information included in it can be
categorized so that a comparision is possible.  The catalog is
implemented as REST service so it can be integrated in other projects
and searched programatically.

The catalog depends on the cloudmesh command shell which allows eay
integration of new commands line environment.  It projects a sample
Interface for the catalog from the commandline

We also can create static web pages from the catalog while using the export 
feature and integrating the pages in for example hugo.

We are currently exploring hugo docsy as it provides
an easy way to generate hirarchical web pages, but also leverages 
hugos tags and categories. Other export formats include markdown and 
bibtex.

## Instalation for developers

1. If you do not have yet create an ssh key and upload it to the
   github repository.

   ```ssh-keygen```

   Upload the `~/.ssh/id_rsa.pub` key to github

2. Download cloudmesh with its source repositories

   Make sure you ave python 3.10.2

   On Mac or Linux do

   ```bash
   $ python3.10 -m venv ~/ENV3
   $ source ~/ENV3/bin/activate
   ```

   On Windows 

   ```bash
   $ py --version # make sure its 3.10.2
   $ py -m venv ~/ENV3
   $ source ~/ENV3/bin/activate
   ```

   After that the instalation is the same on all operating systems.

   ```bash
   $ mkdir cm
   $ cd cm
   
   $ pip install cloudmesh-installer
   $ cloudmesh-installer -ssh install catalog
   $ cms help
   ```
   
   This will download all source code for the cloudmesh shell
   and compile from source.

3. Now you are all ready to do programming and enhancing
   cloudmesh-catalog If you have any issues, contact
   laszewski@gmail.com

## Manual page

A manual pasge shoudl be implemented in
`cloudmesh-catalog/catalog/command/catalog.py` This manual page can
be displayed with the following command:

```bash
$ cms help catalog help
```

To just see the usage type in 

```bash
$ cms catalog
```


## Managing the Service

TODO: The integration of data into the service is not yet completed.

TODO: service management on Windows is not yet completed.

On Linux and macOS we can already experiment with an early prototype 
that allows us starting, sopping, and getting the status of the service. 
This service has nnot yet been integrated with a database.


## BUG

TODO: The adat is not yet integrated and we like to use 
cloudmesh/yamldb for it.

## Adding catalog and registry data

TODO: To add catalog and registry data for new services, one must create new
.yaml files in the appropriate folders: 'data/catalog/my_example.yaml'
and 'data/registry/my_example.yaml'. Each file must follow yaml
formatting similar to the following example.

Example file: Amazon Comprehend (Catalog), amazon_comprehend.yaml

```
---
id: amazon_comprehend:
name: Amazon Comprehend
title: Amazon Comprehend
author: Amazon
slug: amazon-comprehend
public: true
description: |
 Comprehend is Amazon's solution for cloud-based NLP.
 It is available with an AWS account. To use,
 it requires use of either the AWS Command Line
 Interface or an AWS SDK for Python, Java, or .NET.
 Notable features include functionality for giving
 batches of documents to be processed as well as
 submission of multiple jobs in a list. The DetectEntities
 function also allows use of a custom-trained
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
# load from pickle file
catalog.from_pickle('catalog.pkl')
# print catalog data
print(catalog.data)
```

## Using the yaml to markdown conversion script

The catalog command includes several prototype export formats 
that takes all files recursively in a directory or an explicit file and converts it to the specified output 

This includes 

```bash
cms catalog export bibtex --souce=SOURCE
cms catalog export hugo --souce=SOURCE
cms catalog export md --souce=SOURCE
```

The commands will create next to the yal file entreies for bibtex, 
hugo markdown, and markdown.

The templates are just suggestions and we may improve them based on our
findings.

## Checking entries

It is very important that any entry be checked for minimal yaml complience.
Hence we implemented a command 

```bash
cms catalog check --souce=SOURCE
```

which will check all file sin the specified directory. THIs check will ignore line legth limits if the line contains an http or https refernce. 
We also check the data format for YYYY-MM-DD.

We know that it may be problematic to distingush automatically between YYYY-MM-DD and YYYY-DD-MM.
Hence we encourage you to be careful when adding entries.


## Developer Video Tutorials

We are providing a number of developer video tutorials that help undesrtanding how we develop code and leverage the 
cloudmesh-cmd5 shell features:

* [Cloudmesh Catalog. Who to improve the check feature](https://www.youtube.com/watch?v=OkuYxky2TFo)
* [Cloudmesh Catalog. Overview of the converter](https://www.youtube.com/watch?v=4bKvA3RhWaU)
* [Cloudmesh Catalog. How to use the integration with hugo](https://www.youtube.com/watch?v=LfC5JDddwLI)
* [Cloudmesh Catalog. Managing the server with start, stop, info, status](https://www.youtube.com/watch?v=qr8Yf5qAmV8)
* [Cloudmesh Catalog. Running the Server on a Mac on port 8001](https://www.youtube.com/watch?v=T2im0MeDDKE)
* [Github Tips and Project management](https://www.youtube.com/watch?v=Jce1kYOkd04)
* [Overview Cloudmesh NIST project](https://www.youtube.com/watch?v=BCIE44MDgwE)

Other videos are available at

* <https://www.youtube.com/c/GregorvonLaszewski/videos>


## Manual Page

<!-- START-MANUAL -->
```
Command catalog
===============
::

          Usage:
                catalog info
                catalog start [--docker] [--name=NAME]
                catalog stop [--docker] [--name=NAME] [--pid=PID]
                catalog status [--docker] [--name=NAME]
                catalog list
                catalog default [--name=NAME]
                catalog init  DIR [--name=NAME] [--port=PORT] [--docker]
                catalog query QUERY [--name=NAME]
                catalog table --attributes=ATTRIBUTES [--name=NAME]
                catalog print [--format=FORMAT] [--name=NAME]
                catalog copy [--docker] [--name=NAME] [--source=URL]
                catalog federate [--docker] [--name=NAME] [--source=URL]
                catalog load [--docker] [--name=NAME] [--source=URL]
                catalog export bibtex [--source=SOURCE] [--destination=DESTINATION]
                catalog export md [--source=SOURCE] [--destination=DESTINATION]
                catalog export hugo [--source=SOURCE] [--destination=DESTINATION]
                catalog export --template=TEMPLATE [--source=SOURCE] [--destination=DESTINATION]
                catalog check [--source=SOURCE]

          This command manages the catalog service.

          Arguments:
              DIR   the directory path containing the entries

          Options:
              --docker     docker
              --name=NAME  the name of the entry
              --port=PORT  the port

          Description:

            catalog list
              lists all available catalog services. There could be multiple
              catalog services

            catalog default [--name=NAME]
              sets the default catalog server to the given name.
              The names of all services is stored in a yaml file at
              ~/.cloudmesh/catalog.services.yaml

              > cloudmesh:
              >  catalog:
              >    - name: my-service-a
              >      mode: native
              >      port: 10000
              >    - name: my-service-a
              >      mode: docker
              >      port: 10001

            catalog init  DIR [--name=NAME] [--port=PORT] [--docker]
                This command initializes a given catalog service, while using the
                directory DIR as a content dir for the entries.
                The dir can have multiple subdirectories for better organization.
                Each subdirectory name is automatically a "tag" in the entry.
                Note that it will be added to any tag that is in the entry. If
                the tag is already in the entry it will be ignored.

                The name is the name of the catalog to identify it in case
                multiple catalogs exist

                The port is the port number. The number is identified from the catalog list and is the next
                available port if it is not already used. If no prior catalog service with a port exists
                the port 40000 will be used

                If the docker flag is specified the catalog will not be started natively, but in a
                docker container. uid and gid will be automatically forwarded to the container, so data changes are
                conducted with the host user.

                If the image does not exist, a docker container will be started. The Dockerfile is located in the code
                base and dynamically retrieved from the pip installed package in
                cloudmesh/catalog/Dockerfile

            catalog query QUERY [--name=NAME]
              issues a query to the given catalog services. If the name is omitted the default service is used
              The query is formulated using https://jmespath.org/tutorial.html

            catalog print [--format=FORMAT] [--name=NAME]
                prints all entries of the given catalogs. With attributes you can select a number of attributes.
                If the attributes ae nested a . notation can be used
                The format is by default table, but can also set to json, yaml, csv

            catalog start [--docker] [--name=NAME]
                This command starts the services. If docker is used the service is started
                as container. The name specifies the service so multiple services can be started
                If the name is omitted the default container is used. If only one service is specified
                this is the default

            catalog stop [--docker] [--name=NAME]
                This command stops the services. If docker is used the service is stopped
                as container. The name specifies the service so multiple services can be started
                If the name is omited the default container is used. If only one service is specified
                this is the default

            catalog status [--docker] [--name=NAME]
                This command gets that status of the services. If docker is used the service is stopped
                as container. The name specifies the service so multiple services can be started
                If the name is omited the default container is used. If only one service is specified
                this is the default

            catalog copy [--docker] [--name=NAME] [--source=URL]
                This command copies the contents from all catalogs specified by the
                source urls. Please note that the URLs are of teh form host:port
                However it can also load data from a file or directory when specified as
                file://path. Relative path can be specified as file::../data

            catalog federate [--docker] [--name=NAME] [--source=URL]
                This command federates the contents from all catalogs specified by the
                source urls. Please note that the URLs are of teh form host:port.
                When the federation service is queried, parallel queries will be issued to
                all sources and the query result will be reduced to a single result.
                when the cache option is specified the result will be cached and the next
                time the query is asked it will use also the cached result. A time to live
                is specified to asure the cached result will be deleted after the ttl is expired.

            catalog load [--docker] [--name=NAME] [--source=URL]
                In contrast to the copy command, the LOAD command reads the data from
                directories or files and not from URLs
                However, copy can also do file://path

            catalog export bibtex [--source=SOURCE] [--destination=DESTINATION]
                Exports the information from the catalog as a single bibtex file
                If a name is specified only the named entries are exported.
                The format of the entries will be

                > @misc{id,
                >   author={the author field of the entry},
                >   title={the title of the entry},
                >   abstract={the description of the entry},
                >   url={the url of the entry},
                >   howpublished={Wb Page},
                >   month={the month of the date the entry was created},
                >   year={the year of the date when the entry was created}
                > }

            catalog export md [--source=SOURCE] [--destination=DESTINATION]
                Exports the information from the catalog as a directory tree
                equivalent to the original.
                If a name is specified only the named entries are exported.
                The format of the entries will be

                > # {title}
                >
                > {author}
                >
                > ## Description
                >
                > {description}
                >
                > and so on

            catalog export hugo [--source=SOURCE] [--destination=DESTINATION]

                Format of the entry

                > ---
                > title: "Running GPU Batch jobs on Rivanna"
                > linkTitle: "GPU@Rivanna"
                > author: {author of the technology}
                > date: 2017-01-05
                > weight: 4
                > description: >
                >   Short Description of the entry
                > ---
                >
                > {{% pageinfo %}}
                > Short description from the entry
                > {{% /pageinfo %}}
                > ## Description
                >
                > {description}
                >
                > and so on

            catalog export --template=TEMPLATE [--source=SOURCE] [--destination=DESTINATION]

                formats the source file(s) based on the template that is provided.
                The template is a file that uses curly brakets for replacement of
                the attribute names, If a name is not in the source an error will
                be produced.

            catalog check [--source=SOURCE]
                does some elementary checking an all files in the directory tree
                starting with SOURCE
```
<!-- STOP-MANUAL -->