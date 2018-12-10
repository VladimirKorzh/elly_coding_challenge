import re
import itertools


class Solution:
    # I would rather make this function a staticmethod,
    # but there was no way to submit this change to the code checked
    def isMatch(self, s, p):
        """
        The most straight forward solution to this problem would be to
        translate the given wildcard pattern into a Regular Expressions one

        Given conditions:
        '?' Matches any single character.
        '*' Matches any sequence of characters (including the empty sequence).

        :type s: str, could be empty and contains only lowercase letters a-z.
        :type p: str, could be empty and contains only lowercase letters a-z, and characters like ? or *.
        :rtype: bool
        """

        print("Input string: %s" % s)
        print("Input pattern: %s" % p)

        # check the basic situations like someone not passing in the parameters
        if s is None or p is None:
            return False

        sub_lookup = {
            "?": ".",
            "*": ".*?"
        }


        # solving the TLE in test 1708
        # As it turns out one of the tests included a regex DoS attack, nice xD
        # More on that here:
        # http://www.rexegg.com/regex-explosive-quantifiers.html
        # https://stackoverflow.com/questions/12841970/how-can-i-recognize-an-evil-regex
        # One of the solutions would be to use atomic groups to limit the amount of backtracking
        # as well as use the lookahead setting

        pattern = list()
        # Translate the pattern into regex one
        for x, g in itertools.groupby(p):
            if x == "?":
                # replace all the ? marks with "."
                for _ in list(g):
                    pattern.extend(sub_lookup[x])

            elif x == "*":
                # As it turns out one of the subsequent tests have the pattern with duplicate stars in it
                # First we deduplicate only those, preserving the order
                # Bear in mind that having multiple question marks in a row is a valid pattern

                # pattern.extend(sub_lookup[x]) # works till 8
                pattern.extend([sub_lookup[x]])

            # That corresponds to a letter symbol
            else:
                items = [l for l in list(g)]
                pattern.extend(['('.split(), items[0], ')', '{%s}' % len(items)])

        # Flatten the list of lists
        p = ''.join([x for l in pattern for x in l])

        print('re pattern: %s' % p)

        # check if it is a match
        match = re.fullmatch(p, s, re.MULTILINE)

        print(match)
        if match is None:
            return False
        else:
            return True
