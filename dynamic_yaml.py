# -*- coding: utf-8 -*-

import yaml
import os

os.chdir('/Users/tanyastrydom/Documents/TanyaDoesScience/posts')

import glob
for name in glob.glob('2020*'):
    print (name)

dict_file = [{'listing' : 'posts' : [name]},
{'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]

yaml.dump(dict_file)

with open(r'/Users/tanyastrydom/Documents/TanyaDoesScience/store_file.yaml', 'w') as file:
    documents = yaml.dump(dict_file, file)
