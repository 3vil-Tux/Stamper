#!/usr/bin/python3

'''Disclaimer'''
# Copyright 2020 3vil.Tux @ https://github.com/3vil-Tux
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Import(s)'''
from stamper import configuration
from stamper import colors
from stamper import broadcast
from stamper import HTTP
import sys

'''Variable(s)'''

'''Code(s)'''
def checkOperatingSystem():
    if not "linux" in sys.platform:
        sys.stdout.write("Please run AWAT with a Linux Distribution!\nFor compatibility and stability purposes, AWAT is restricted on Windows!")
        sys.stdout.flush()
        sys.exit()

def checkPythonRuntimeVersion():
    if sys.version_info[0] < 3:
        sys.stdout.write("Please run AWAT with Python3!\n")
        sys.stdout.flush()
        sys.exit()

def checkArguments():
    #global configuration.URL
    if not len(sys.argv) == 2:
        sys.stdout.write("Wrong usage!\nExample: python3 "+__file__+" http://my-http-auth-site.com/\n")
        sys.stdout.flush()
        sys.exit()
    else:
        configuration.URL = sys.argv[1]

def Run():
    print("""
  ____  _                                  
 / ___|| |_ __ _ _ __ ___  _ __   ___ _ __   
 \___ \| __/ _` | '_ ` _ \| '_ \ / _ \ '__|
  ___) | || (_| | | | | | | |_) |  __/ |    https://github.com/3vil-Tux/Stamper
 |____/ \__\__,_|_| |_| |_| .__/ \___|_|    (%s@3vil.Tux%s) (%s@vbeta.1.0%s)
 HTTP-Auth Verb Tampering |_| Fuzzing Tool             

""" % (colors.bad, colors.reset, colors.bad, colors.reset))
    '''
    Checking if the host is valid!
    '''
    broadcast.info(f"Checking if {configuration.URL} is a valid HTTP-Auth...")

    configuration.remoteHost["request"] = HTTP.send(configuration.URL, "GET")
    configuration.remoteHost["headers"] = configuration.remoteHost["request"].headers
    configuration.remoteHost["code"]    = configuration.remoteHost["request"].status_code
    configuration.remoteHost["source"]  = configuration.remoteHost["request"].text

    if not configuration.remoteHost["code"] == 401:
        broadcast.bad("Oh oh! The remote host did not return 401 (Forbidden/Unauthorized) status code!")
        sys.exit()
    if not "WWW-Authenticate" in configuration.remoteHost["headers"]:
        broadcast.bad("Oh oh! The remote host did not return WWW-Authentication in their response!")
        sys.exit()
    broadcast.good("Remote host seems a valid HTTP-Auth!")

    '''
    Fuzz fuzz! Fuzzing the host!
    '''
    broadcast.newLine()
    broadcast.info(f"Fuzzing host with the following payloads: {', '.join(configuration.HTTPVerbs)}")


    foundPayloads = []
    for verb in configuration.HTTPVerbs:
        broadcast.info(f"Fuzzing {configuration.URL} with {verb}...")
        fuzzedRequest = {
            "request": None,
            "headers": None,
            "code": None,
            "source": None
        }

        fuzzedRequest["request"] = HTTP.send(configuration.URL, verb)
        fuzzedRequest["headers"] = fuzzedRequest["request"].headers
        fuzzedRequest["code"]    = fuzzedRequest["request"].status_code
        fuzzedRequest["source"]  = fuzzedRequest["request"].text

        # Checks code
        if fuzzedRequest["code"] == 200:
            broadcast.good("Remote host sent 200 (OK)!")

            #Checks for empty response
            if not fuzzedRequest["source"] is None or not fuzzedRequest["source"] == "":
                broadcast.good("Remote host did not respond with empty page!")
                foundPayloads.append(verb)

                # Checks if source is the same
                if len(configuration.remoteHost["source"]) == len(fuzzedRequest["source"]):
                    broadcast.bad("Remote host send a response with the same length of original respond which may means it failed bypassing it!")

                # Checks for bad words!!! :O
                for keyword in configuration.badWords:
                    if keyword in fuzzedRequest["source"].lower():
                        broadcast.warning(f"Remote host response seems to contain '{keyword}'...")

                broadcast.good(f"Possible attack found using verb '{verb}'!")
            else:
                broadcast.bad("Remote host responded with empty page")
        else:
             broadcast.bad(f"Remote host responded with {str(fuzzedRequest['code'])}!")
        broadcast.newLine()

    # Display results
    if not len(foundPayloads) == 0:
        broadcast.warning(f"Found {str(len(foundPayloads))} working verbs!")
        for payload in foundPayloads:
            broadcast.info(f"Payload: {payload}")
            broadcast.info("--------------")
    # Bye bye!
    broadcast.newLine()
    broadcast.good("Thank you for using Stamper! Have a nice day! :-)")

if __name__ == "__main__":
    checkOperatingSystem()
    checkPythonRuntimeVersion()
    checkArguments()
    Run()
