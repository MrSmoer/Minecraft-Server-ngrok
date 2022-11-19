#!/usr/bin/python
import json
import requests
from pathlib import Path
import time
import csv
from os.path import exists

file='minecraft/versions.csv'
manifest_link="https://launchermeta.mojang.com/mc/game/version_manifest_v2.json"
proxy = {

    }
noServers=['1.2.4', '1.2.3', '1.2.2', '1.2.1', '1.1', '1.0'] #These Minecraft-releases do not have a server for download

def getOldList():
    list_of_dict=[]
    if not exists(file):
        return list_of_dict
    with open(file, 'r') as f:
        dict_reader = csv.DictReader(f)
        list_of_dict = list(dict_reader)
    return list_of_dict

def writeToFile(data):
    with open(file, 'w') as convert_file:
            data
            csv_writer = csv.writer(convert_file)
            count = 0
            header=data[0].keys()
            csv_writer.writerow(header)
            for i in data:
                if count==0:
                    #Write Headings
                    count+=1
                csv_writer.writerow(i.values())

def getAllPages():
    content=requests.get(manifest_link, proxies=proxy).content
    dict = json.loads(content)
    pages = {}
    for e in dict.get('versions'):
        if(e.get('type')=="release"):
            pages[e.get('id')]=e.get('url')

    return pages

def versionsFromDict(dict):
    versions = []
    for n in dict:
        versions=versions+[n.get('id')]
    return versions

def versionsFromPage(pages):
    versions=pages.keys()
    return versions

def listUnknownVersions(oldVersions, manifestVersions):
    missingVersions=[]
    for i in manifestVersions:
        if not i in oldVersions:
            if not i in noServers:
                missingVersions=missingVersions+[i]
    return missingVersions

def getPageDLink(page_url):
    res=requests.get(page_url, proxies=proxy)
    return res.content.get('downloads').get('server').get('url')



def getUnknownLinks(oldDict, manifestPages):
    dictOfUnknown = []
    oldVs=versionsFromDict(oldDict)
    #print(oldVs)
    
    newVs=versionsFromPage(manifestPages)
    neededVersions = listUnknownVersions(oldVs,newVs)
    if neededVersions == []:
        print("No new Version")
        return []
    for n in neededVersions:
        print("Getting "+n)
        entry={}
        print(manifestPages.get(n))
        page=json.loads(requests.get(manifestPages.get(n),proxies=proxy).content)
        entry['id']=n
        entry['url']=page.get('downloads').get('server').get('url')
        dictOfUnknown+=[entry]
        time.sleep(0.5)
    return dictOfUnknown



# https://launchermeta.mojang.com/mc/game/version_manifest_v2.json
def main():
    result = {}
    
    result["version"]=[]
    oldDict=getOldList()
    #print(oldDict)
    
    manifestPages=getAllPages()
    #print(manifestPages)
    unknownLinks=getUnknownLinks(oldDict,manifestPages)
    newdict=oldDict+unknownLinks
    writeToFile(newdict)
    return

if(__name__=='__main__'):
    main()