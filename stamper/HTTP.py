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
from stamper import broadcast
import sys
import requests

'''Codes(s)'''
def send(URL, verb, headers=None):
    try:
        return requests.request(verb, headers=headers, url=URL)
    except:
        broadcast.bad("Error happened while connecting to remote host!")
        sys.exit()