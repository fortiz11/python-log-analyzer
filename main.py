
#This tells python to not evaluate type hints for now and to treat
# as strings to resolve later 
from __future__ import annotations 


#This is a regular expression module and allows for text search, pattern match
#and ability to extract data from messy strings such as logs
import re 

#specialized dictionary designed for counting things 
from collections import Counter 

#This is pythons modern file system interface
#Instead of treating paths as raw strings, treat them as objects with methods 
from pathlib import Path 

#reg expression patterns to detect login outcomes 
#The "r" (raw string) is there so that "\b" isn't interpreted incorrectly
FAILED_PAT = re.compile(r"\bFailed password\b" , re.IGNORECASE)

#The "\b" (word boundary) is there for more precise detection
ACCEPTED_PAT = re.compile(r"\bAccepted password\b", re.IGNORECASE)