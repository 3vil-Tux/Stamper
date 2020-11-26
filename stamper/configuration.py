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

'''Codes(s)'''
# Don't touch
URL = None
foundPayloads = []

remoteHost = {
    "request": None,
    "headers": None,
    "code": None,
    "source": None
}

# All verbs, feel free to add as many as you want
HTTPVerbs = [
    "GET",
    "POST",
    "PUT",
    "TRACE",
    "CONNECT", 
    "OPTIONS", 
    "PROPFIND"
]

# All keywords to check the source with, feel free to add more!
badWords = [
    "unauthorized",
    "denied",
    "authenticate",
    "wrong",
    "incorrect"
]