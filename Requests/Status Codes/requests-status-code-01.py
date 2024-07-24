import requests

#To Do:
#Make 2 part test. First raw server then full link


link = 'http://www.google.com/xWrongAddressx'

try:
    response = requests.get(link, timeout=(3, 5))
    print("Status Code:", response.status_code)
    print("Reason If Given:", response.reason)
    
except requests.exceptions.Timeout:
    print("The request timed out!")




input()