# Knutha Morrisa Pratt (KMP) for string matching
# Complexity: O(n)
# Reference used: http://code.activestate.com/recipes/117214/


def kmp(full_string, pattern):
    '''
    It takes two arguments, the main string and the patterb which is to be
    searched and returns the position(s) or the starting indexes of the
    pattern in the main string (if exists)
    
    agrs 'full-string' is the text from where pappern has to be searched
    'pattern' is the string has to be searched
    >>> from pydsa import kmp
    >>> kmp('ababbabbaab', 'abba')
    2
    5
    '''
    # allow indexing into pattern and protect against change during yield
    pattern = list(pattern)

    # build table of shift amounts
    no_of_shifts = [1] * (len(pattern) + 1)
    shift = 1  # initial shift
    for posi in range(len(pattern)):
        while (shift <= posi and pattern[posi] != pattern[posi-shift]):
            shift = shift + no_of_shifts[posi-shift]
        no_of_shifts[posi+1] = shift

    # do the actual search
    start_at = 0
    pattern_match = 0
    for p in full_string:
        while pattern_match == len(pattern) or pattern_match >= 0 and pattern[pattern_match] != p:
            start_at = start_at + no_of_shifts[pattern_match]
            pattern_match = pattern_match - no_of_shifts[pattern_match]
        pattern_match = pattern_match + 1
        if pattern_match == len(pattern):
            print (start_at)
