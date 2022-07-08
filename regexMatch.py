import re

string = 'the text that is searchable. String of text test string for testing'
pattern = (r't[a-z]{2}t') # regex pattern to match the word "text" in the string
                          # r' tells Python to evaluate the characters that follow,
                          # as a regex search pattern

# find all matches for pattern by iterating over the string then return 
# the match including 5 characters before and after, for context
For match in re.finditer(pattern,string):
     # if match index is at the beginning of
     # the string, we need to adjust the start 
     # index to be the first character in the line
     # otherwise the match will not be returned
     matchstart = match.start()
     if matchstart <= 5:
          matchstart = 0
          matchend = match.end() + 7
     else:
          matchstart = match.start() - 5
          matchend = match.end() + 5
     print(string[matchstart:matchend])
