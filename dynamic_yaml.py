# -*- coding: utf-8 -*-

import yaml
import os

#set wd
os.chdir('/Users/tanyastrydom/Documents/TanyaDoesScience/posts')

#get file names matching specific search string
import glob
for name in glob.glob('2020*'):
    print (name)
    
#define structure of .yml file
dict_file = [{'listing' : 'posts' : [name]},
{'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]

#convert to YAML language
yaml.dump(dict_file)

#conver to .yml file and save to wd
with open(r'/Users/tanyastrydom/Documents/TanyaDoesScience/dynamic_yaml.yml', 'w') as file:
    documents = yaml.dump(dict_file, file)
