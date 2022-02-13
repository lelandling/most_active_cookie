import argparse
import sys
import csv


#def main():
    #script = sys.argv[0]
cookiedict = {}

parser = argparse.ArgumentParser(description = "most active cookie of date given")
parser.add_argument("file_path")
parser.add_argument("--date", "-d")
args = vars(parser.parse_args(sys.argv[1:]))



with open(args["file_path"], 'r') as csvfile:
    cookielog = csv.reader(csvfile)
    for row in cookielog:
        if(row[1][0:10] == args["date"]): #usees string manipulation to look at the first 
            if(row[0] not in cookiedict):
                cookiedict[row[0]] = 1
            else:
                cookiedict[row[0]] = cookiedict[row[0]] +1
        #if(row[0] not in cookiedict):
        #    cookiedict[row[0]] = [row[1]]
        #else:
        #    cookiedict[row[0]].append(row[1])
maxcookie = [key for key, value in cookiedict.items() if value == max(cookiedict.values())]
for cookie in maxcookie:
    print(cookie)