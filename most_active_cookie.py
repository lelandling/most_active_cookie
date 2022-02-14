#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:22:12 2022

@author: lelandling
"""


import argparse
import sys
import csv


#def main():
    #script = sys.argv[0]
class activecookie:
    def __init__(self):
        self.storedcookielog = []

    def processcookies(self, path):
        with open(path, 'r') as csvfile:
            cookielog = csv.reader(csvfile)
            for row in cookielog:
                self.storedcookielog.append(row);
              
    def findmaxcookie(self, date):
        
        
        cookiedict = {}
        maxcookie ={}
        for row in self.storedcookielog:
          
            if(row[1][0:10] == date): #usees string manipulation to look at the first 
                if(row[0] not in cookiedict):
                    cookiedict[row[0]] = 1
                else:
                    cookiedict[row[0]] = cookiedict[row[0]] +1

        maxcookie = [key for key, value in cookiedict.items() if value == max(cookiedict.values())]
        
        
        return maxcookie

    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "most active cookie of date given")
    parser.add_argument("file_path")
    parser.add_argument("--date", "-d")
    args = vars(parser.parse_args(sys.argv[1:]))
    
    cookieprocessor = activecookie()
    cookieprocessor.processcookies(args["file_path"])
    cookieset =  cookieprocessor.findmaxcookie(args["date"])
    
    for cookie in cookieset:
        print(cookie)
        
    