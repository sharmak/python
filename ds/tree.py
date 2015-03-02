# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 17:10:09 2015

@author: kishor
"""
def do_work():
    mystr = """/a/b/c/test.xml
    /b/c/e/test1.xml
    """
from collections import OrderedDict
val = list()
def generate_path(row, cur_path):
    if not row.has_key("children"):
        val.append(cur_path + "," + row["report"])
    else:
        cur_path = cur_path + "/" + row["report"]
        for child in row["children"]:
            generate_path(child, cur_path)
        
class CsvToTree(object):
    id =0
    @staticmethod
    def _add_node(l, t):
        if len(l) == 1:
            CsvToTree.id = CsvToTree.id + 1
            a = OrderedDict()            
            a["report"] = l[0]
            a["id"] = "id_" + str(CsvToTree.id)
            t.append(a)
        else:
            out = list()
            for row in t:
                if (row["report"] == l[0]):
                    out = row["children"]
            if len(out)  == 0:
                CsvToTree.id = CsvToTree.id + 1
                x = OrderedDict()                
                x["report"] = l[0]
                x["id"] = "id_" + str(CsvToTree.id)
                x["children"] = list()
                t.append(x)
                out = x["children"]
                #["children"]
            CsvToTree._add_node(l[1:], out)             
    @staticmethod         
    def create_tree(rows):
        t = list()
        for row in rows:
            CsvToTree._add_node(row, t)
            #pprint.pprint(t)
            #print("x"*80)
        return t
import pprint
import json
if __name__ == '__main__':
    """
    d = defaultdict(dict)
    rows = [['a', 'd',  'test1.xml'],
            ['b', 'e',  'test2.xml'],
            ['a', 'b', 'test3.xml']
            ]
    x = CsvToTree.create_tree(rows)
    pprint.pprint(x)
    """
    with open("/home/kishor/test/oil.json") as json_file:
        json_data = json.load(json_file)
    generate_path(json_data[0], "")
    pprint.pprint(val)
    """
    #for i, j in x['r'].iteritems():
    #    print i, j
    #mycall(['a', 'b', 'test.xml'], d)
    #mycall(['a', 'c', 'test1.xml'], d)
    #print(d)
