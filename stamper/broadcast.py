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
from stamper import colors

'''Codes(s)'''
def newLine():
    print("")

def normal(message):
    print("[+] %s" % (message))

def good(message):
    print("%s[+]%s %s" % (colors.good, colors.reset, message))

def info(message):
    print("%s[*]%s %s" % (colors.info, colors.reset, message))

def warning(message):
    print("%s[!]%s %s" % (colors.warning, colors.reset, message))

def bad(message):
    print("%s[!]%s %s" % (colors.bad, colors.reset, message))