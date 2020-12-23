!/usr/bin/python

"""Status Codes amd elif loops by HexCrtl"""

code = int(input("Please enter an HTTP status code: "))
if (code >= 100) and (code <=199):
    print ("1XX: Informational")
elif (code >= 200) and (code <=299):
    print ("2XX: Success")
elif (code >= 300) and (code <=399):
    print ("3XX: Redirection")
elif (code >= 400) and (code <=499):
    print ("4XX: Client Error")
elif (code >= 500) and (code <=599):
    print ("5XX: Success")
else:
    print ("[!] Unknown HTTP Status Code")
