#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 13:34:32 2022

@author: lelandling
"""

import datetime
import unittest
import csv
import random

from most_active_cookie import activecookie
from string import ascii_letters
from random import randint
from datetime import timezone

class generate_data:
    def dategen(self):
        year, month, day = randint(2000, 2021), randint(1, 12), randint(1, 28)
        hour, minute, second = randint(1, 23), randint(1, 59), randint(1, 59)

        date = datetime.datetime(year, month, day, hour, minute, second,
                                 tzinfo=timezone.utc)
        return date.strftime("%Y-%m-%dT%H:%M:%S%z")
    
    def cookiegen(self, numcookies = 16):
        generatedcookies = []
        validchars = list(ascii_letters)
        validchars.extend([0,1,2,3,4,5,6,7,8,9])
        
        for i in range(numcookies):
            cookie = ''.join([str(random.choice(validchars)) for i in range(16)])
            generatedcookies.append(cookie)
            
        return generatedcookies
    
    def writecsv(self, data):
        with open("testdata.csv", "w") as test_file:
            csvwriter = csv.writer(test_file)
            csvwriter.writerow(["cookie", "timestamp"])
            for row in data:
                csvwriter.writerow(row)

class tester(unittest.TestCase):
    def __init__(self):
        self.generatedata = generate_data()


    def test(self):
        
        cookieset = self.generatedata.cookiegen()
        numsamedate = randint(1, 3)
        
        dataset = []
        solutionset = []
        
        saveddate = self.generatedata.dategen()
        date = saveddate
        
        
        for cookie in cookieset:
            if(numsamedate > 0):
                solutionset.append(cookie)
                numsamedate = numsamedate-1
            else:
                date = self.generatedata.dategen()
            
            dataset.append([cookie, date])
        
        self.generatedata.writecsv(dataset)
        
        cookieprocessor = activecookie()
        cookieprocessor.processcookies("testdata.csv")

        calculatedcookies = cookieprocessor.findmaxcookie(saveddate[0:10])
        
        
        if(solutionset == calculatedcookies):
            print("Test passed, test dataset:")
            print(dataset)
            print("solution set:")
            print(solutionset)
            print("calculated cookieset:")
            print(calculatedcookies)
        else:
            print("Test failed, test dataset:")
            print(dataset)
            print("solution set:")
            print(solutionset)
            print("calculated cookieset:")
            print(calculatedcookies)

if __name__ == '__main__':
    thing = tester()
    thing.test()