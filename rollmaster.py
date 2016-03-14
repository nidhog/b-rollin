#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json
import datetime
import os

storage_file = os.path.dirname(os.path.abspath(__file__))+'/temp/tasks.brl'

def insert_task(task):
    f =  open(storage_file, 'a')
    f.write(task+'\n')
    f.close()
    
def get_task(O, P, A):
    return O+','+P+','+A

def show_current_tasks():
    tasks = {}
    f =  open(storage_file, 'r')
    i = 0
    for line in f:
        tasks[i]=line.strip().split(',')
        i+=1
    f.close()
    for key in tasks.keys():
        print '-> '
        print key
        print '\n ----- '
        print tasks[key]
        print ' ----- \n'
        

class FileHandler(object):
    """FileHandler class
    Manages storage in a file.
    
    """
    def __init__(self, output_file):
        """
        The output directory should be given.
        
        :param output_dir: output directory path
        
        """
        self.output_file = output_file
        
    def append_list(self, element_list):
        pass
        
    def append_element(self, element):
        data_store_file = open( (self.output_file), "r")
        try:
            data_buffer = json.load(data_store_file)
        except ValueError: 
            data_buffer = {}
        data_store_file.close()
        if("elements" not in data_buffer.keys()):
            data_buffer["elements"]=[]
        data_buffer["elements"].append(element)
        data_store_file = open((self.output_file), "w+")
        json.dump(data_buffer, data_store_file)
        data_store_file.close()
        
    def clear_file(self):
        pass
        
    def show_goals(self):
        pass
        
class RollMaster(object):
    """
    """
    def __init__(self, output_file = storage_file):
        self.output_file = output_file
        self.file_handler = FileHandler(self.output_file)
    def append(self, O, P, A, adate):
        print "[.] Appending Goal : ", O," - ", P," - ", A," - ", adate, "..."
        adict = {}
        adict["outcome"]=O
        adict["purpose"]=P
        adict["actions"]=A
        adict["date"]=adate
        self.file_handler.append_element(adict)
        print "[¤] Successfully appended goal."
        
    def run(self):
        activity = raw_input("[*] Enter Goal, e.g. '>Gildarts; Rule Them All; PavelTsats Strength- Hyperthro - Clean' :\n>").strip().split(';')
        if len(activity)==3:
            outcome = activity[0]
            purpose = activity[1]
            actions = activity[2]
            current_date = datetime.datetime.now()
            self.append(outcome, purpose, actions, current_date.strftime("%B %d, %Y"))
        else:
            print "[!] Enter at least 3 entries: Outcome;Purpose;Actions\n"
            
def main():
    os.system('clear') 
    print "=============================="
    print "== One App To Rule Them All =="
    print "=============================="
    print " WHAT A GREAT DAY TODAY"
    print "=============================="
    b_rollin = RollMaster()
    while(True):
        task = raw_input("\nDo this or that? (For this enter 'this', for that enter 'that')\n").strip()
        if task == 'this':
            b_rollin.run()
        if task == 'show':
            show_current_tasks()
        if task == 'that':
            break
            
    
        
        
        
        
        
        
        
        
        
        

        
    
if __name__ == "__main__":
    main()





