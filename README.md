# sendalert_desktop
Send alert if vaccination is available for age group 18-44


Prerequisites:
Python 3.x
The following packages should be present: 
playsound and requests.
If these python packages are not present install it using 
1. pip install playsound 
2. pip install requests

Usage:
python .\cowin.py -h
(mandatory)-i/--districtid for district id -> Pune district id is 363
(mandatory)-d/--date for date in dd-mm-yyyy format only
(optional)-p/--pincode for the comma separated list of pincodes within the district
(optional)-r/--regex for the part of pincode to cover a city. For example you can cover Pune city area by just mentioning 411
If none of regex of pincode or list of pincodes is provided, it looks up for the entire district
