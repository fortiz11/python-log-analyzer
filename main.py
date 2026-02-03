
# This tells python to not evaluate type hints for now and to treat
# as strings to resolve later
from __future__ import annotations


# This is a regular expression module and allows for text search, pattern match
# and ability to extract data from messy strings such as logs
import re

# specialized dictionary designed for counting things
from collections import Counter

# This is pythons modern file system interface
# Instead of treating paths as raw strings, treat them as objects with methods
from pathlib import Path

# reg expression patterns to detect login outcomes
# The "r" (raw string) is there so that "\b" isn't interpreted incorrectly as part of the string
FAILED_PAT = re.compile(r"\bFailed password\b", re.IGNORECASE)

# The "\b" (word boundary) is there for more precise detection
ACCEPTED_PAT = re.compile(r"\bAccepted password\b", re.IGNORECASE)


# This helps match IPv4 addresses
# The "?:" means group but dont save
# The \d means digit (0-9) and the {1,3} means repeat 1-3 times
# The \. just means the dot is inturrpreted as an actual dot
# The second {3} means to repate this pattern 3 times
# This (?:\d{1,3}\.){3} means repeat number + dot 3 times and not 4 in order to avoid a trialing dot
IP_PAT = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')


# The log_path: is a type hint that specifies what type the parameter will be
# The -> tells us there is no return statement
def analyze_log(log_path: Path, top_n: int = 5) -> None:
    """
    Analyze an authentication log file and print summary statistics 

    :param log_path: the file system path to the log file 
    :type log_path: Path
    :param top_n: Represents how many of the most frequent IP address you want to display 
    :type top_n: int

    Outputs:
    -Total number of log lines 
    -Number of failed logins 
    -Number of successful logins 
    -Top IP Addresses by frequency 
    """

    if not log_path.exists():
        raise FileNotFoundError(f"Log file not found: {log_path}")

    # Log entries
    total_lines = 0
    # failed login attempts
    failed_count = 0
    # succesful logins
    accepted_count = 0

    # which IPs appeared and how often
    # The : means type hint and it means its a Counter whose keys are strings bc Counter is a dictionary
    # The Counter() creates an object (an empty dictionary)
    ip_counter: Counter[str] = Counter()

    #read file line by line


    #The log_path.open works here because log_path is a Path object 
    #so calling .open is a method on the Path Object
    #"utf-8" tells python to interpret bytes in the file as utf-8 so it doesnt guess
    #The replace tells python that if it cant decode a character
    #then just replace instead of crashing
    with log_path.open("r", encoding= "utf-8", errors="replace") as f:
        for line in f:
            total_lines+=1
