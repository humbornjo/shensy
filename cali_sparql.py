# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:31:25 2021

@author: 86131
"""

#import requests
#import re
import sparql #pip install sparql-client
#import xml.etree.ElementTree as ET
import json
import string


class CaliSparql:

    def __init__(self, endpoint) -> None:
        self.endpoint = endpoint
        pass

    def get_calitype(self, wiki_entity):

        statement = 'SELECT DISTINCT ?superclass ?subclass '\
            'WHERE { ?subclass a owl:Class .'\
            '?subclass  rdfs:subClassOf  ?superclass}'\
            'ORDER BY  ?superclass ?subclass'
        result = sparql.query(self.endpoint, statement)

    # def 

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
#%%
dbp_prefix = 'http://dbpedia.org/resource/'
dbo_prefix = 'http://dbpedia.org/ontology/'
thing = 'http://www.w3.org/2002/07/owl#Thing'

statement = 'SELECT DISTINCT ?superclass ?subclass '\
            'WHERE { ?subclass a owl:Class .'\
            '?subclass  rdfs:subClassOf  ?superclass}'\
            'ORDER BY  ?superclass ?subclass'
result = sparql.query('http://caligraph.org/sparql', statement)

classlist = []
for row in result:
    sub_str = sparql.unpack_row(row)
    print(sub_str)
    try:
        if sub_str[0] == thing:
            parentclass = 'owl#Thing'
            childclass = sub_str[1].split(dbo_prefix)[1]
        else:
            parentclass = sub_str[0].split(dbo_prefix)[1]
            childclass = sub_str[1].split(dbo_prefix)[1]
        if isEnglish(parentclass) and isEnglish(childclass):
            classlist.append([parentclass,childclass])
    except:
        pass
with open('dbpedia ontology classes parentclass_childclass list.json','w') as load_f:
    all_categories = json.dumps(classlist)
    load_f.write(all_categories)