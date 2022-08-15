## program was written by Khasan Rashidov
##
## regular expressions (using https://regex101.com/)
## extracting data from website (https://reports.opengroup.org/all.shtml)
## getting countries, company names
## and counting countries using regex

## Task: all we have to do is to
## 1) extract company and country from the web page
## 2) count how many companies each country has.
print('#' * 50, '\n')

import requests ## to instal requests: pip3 install requests
import re ## importing regular expressions
import matplotlib.pyplot as plt

## printing the contents of the web page
## print(requests.get("https://reports.opengroup.org/all.shtml").text)

## regex example: ## "^([a-zA-Z ]+) ([a-zA-Z ]+)$"gm
## \w - Matches any letter, digit or underscore. Equivalent to [a-zA-Z0-9_].
## a+ - Matches one or more consecutive `a` characters.
## ^ - Matches the "start of a string" without consuming any characters.
## $ - Matches the "end of a string" without consuming any characters.
## gm - 'g' for global and 'm' for multi line
##
## regex for emails: "^([a-zA-Z0-9_.]+)@([a-zA-Z]+)\.([a-zA-Z.]+)$"gm
##

counter = {}

print("Extracted companies and countries:")

for line in requests.get('https://reports.opengroup.org/all.shtml').text.split('\n'):
    ## regex: company name, company example <td>EPAM Systems Inc.</td>
    ## 'r' is saying that it is a regex, \w is a word, \s is a space, + is for a complete word
    ##
    ## search(pattern, string, flags=0)
    ## Scan through string looking for a match to the pattern, returning
    ## a Match object, or None if no match was found.
    r1 = re.search(r'(<td>)([\w\s\.\,\&\'\–\-\(\)\/\+\\ ]+)(</td>)', line)
    
    ## regex: country name, country example <td class="r">United States</td>
    r2 = re.search(r'(<td class="r">)([^0-9][\w\s\(\)\,\.]+)(</td>)', line)
    if r1 is None or r2 is None:
        continue
    else:
        print(r1.group(2), r2.group(2))
        ## group #2 is ([\w\s\.\,\&\-\(\)\/\+ ]+) for company name
        ## grouo #2 is ([^0-9][\w\s\(\)\,\.]+) for country name
        ## group(...)
        ## group([group1, ...]) -> str or tuple.
        ## Return subgroup(s) of the match by indices or names

        company = r1.group(2)
        country = r2.group(2)

        if country not in counter:
            counter[country] = 1
        else:
            counter[country] += 1
        
print('\n' + '#' * 50 + '\n')

print("Number of companies in countries:")
print(counter)

print('\n' + '#' * 50 + '\n')

print("Total number of companies: {}".format(sum(counter.values())))

print('\n' + '#' * 50 + '\n')

countries = list(counter.keys())
print(countries)

number_of_companies = list(counter.values())
print(number_of_companies)

print('\n' + '#' * 50 + '\n')

## plotting
plt.bar(countries, number_of_companies)

plt.xticks(rotation=60)

plt.tick_params(axis="x", labelsize=3)

plt.savefig('number of companies in countries.png', dpi = 1000)

##################################################
