#Author: Yogita Bang

import requests
import json
from playsound import playsound
import time
import sys
import getopt

argumentlist = sys.argv[1:]

options = "hi:d:p:r:"

longoptions = ["help", "districtid", "date", "pincode", "regex"]

districtid = None
pincode = []
regex = None
date = None
    
def usage():
    print("(mandatory)-i/--districtid for district id -> Pune district id is 363")
    print("(mandatory)-d/--date for date in dd-mm-yyyy format only")
    print("(optional)-p/--pincode for the comma separated list of pincodes within the district")
    print("(optional)-r/--regex for the part of pincode to cover a city. For example you can cover Pune city area by just mentioning 411")
    print("If none of regex of pincode or list of pincodes is provided, it looks up for the entire district")
    exit()

try:
    arguments, values = getopt.getopt(argumentlist, options, longoptions)
    
    for curr_arg, curr_val in arguments:
        if curr_arg in ("-h", "--help"):
            usage()
        elif curr_arg in ("-i", "--districtid"):
            districtid = curr_val
        elif curr_arg in ("-d", "--date"):
            date = curr_val
        elif curr_arg in ("-p" , "--pincode"):
            pincode = list(curr_val.split(","))
        elif curr_arg in ("-r", "--regex"):
            regex = curr_val

except getopt.error as err:
    print(str(err))

 
if districtid == None:
    print("Please enter district ID")
    exit()
    
if date == None:
    print("Please enter date in dd-mm-yyyy format")
    exit()

url1="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id="+districtid+"&date="+date
hrs = {'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

while(True):
    response = requests.get(url1,headers=hrs).text
    json_data = json.loads(response)

    li = json_data["sessions"]


    for list_item in li:
        jdata = json.dumps(list_item)
        jdata = json.loads(jdata)
        if (len(pincode) != 0):
            if (jdata["min_age_limit"] == 18  and ((str(jdata["pincode"]) in pincode))):
                playsound("sound.mp3")
                print(jdata["pincode"])
                print(jdata["name"])
                print(jdata["block_name"])
                print("************************************")
        if (regex != None):
            if (jdata["min_age_limit"] == 18  and (regex in str(jdata["pincode"]) )):
                playsound("sound.mp3")
                print(jdata["pincode"])
                print(jdata["name"])
                print(jdata["block_name"])
                print("************************************")
        if (len(pincode) == 0 and regex == None):
            if (jdata["min_age_limit"] == 18):
                playsound("sound.mp3")
                print(jdata["pincode"])
                print(jdata["name"])
                print(jdata["block_name"])
                print("************************************")
            
            
    time.sleep(30)