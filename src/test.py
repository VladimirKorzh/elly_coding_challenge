import unittest

from src.main import Solution


class TestWildcardMatching(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.isMatch("aa", "a"), False,
                         'Explanation: "a" does not match the entire string "aa".')

    def test_example_2(self):
        self.assertEqual(self.solution.isMatch("aa", "*"), True,
                         'Explanation: "*" matches any sequence.')

    def test_example_3(self):
        self.assertEqual(self.solution.isMatch("cb", "?a"), False,
                         "Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.")

    def test_example_4(self):
        self.assertEqual(self.solution.isMatch("adceb", "*a*b"), True,
                         "Explanation: The first '*' matches the empty sequence,"
                         " while the second '*' matches the substring 'dce'.")

    def test_example_5(self):
        self.assertEqual(self.solution.isMatch("acdcb", "a*c?b"), False,
                         'No explanation given')

    def test_example_6(self):
        self.assertEqual(self.solution.isMatch("aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba", "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*"), True,
                         'Test #940')

    def test_example_7(self):
        self.assertEqual(self.solution.isMatch("mississippi", "m??*ss*?i*pi"), False,
                         'Test #1605')

    def test_example_8(self):
        self.assertEqual(self.solution.isMatch("abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb", "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"), True,
                         'Test #1708')

    def test_example_9(self):
        self.assertEqual(self.solution.isMatch("aab", "c*a*b"), False,
                         'Test #890')

    def test_example_10(self):
        self.assertEqual(self.solution.isMatch("missingtest", "mi*ing?s*t"), False,
                         'Test #1560')

    def test_example_11(self):
        self.assertEqual(self.solution.isMatch("abce", "abc*??"), False,
                         'Test #1691')

    def test_example_12(self):
        self.assertEqual(self.solution.isMatch("abc", "abc*defghijk"), False,
                         'Test #1649')

    def test_example_13(self):
        self.assertEqual(self.solution.isMatch("zacabz", "*a?b*"), False,
                         'Test #1402')

    def test_example_14(self):
        self.assertEqual(self.solution.isMatch("abc", "*?*?*?*?"), False,
                         'Test #1533')

    def test_example_15(self):
        self.assertEqual(self.solution.isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab", "***bba**a*bbba**aab**b"), True,
                         'Test #1686')

    def test_example_16(self):
        self.assertEqual(self.solution.isMatch("abbaaaabbbbbababbbbbbbbaaabaabbabaabbaaabbbbabbbbab", "a*aaba***b**a*a********b"), True,
                         'Test #1681')

    def test_example_17(self):
        self.assertEqual(self.solution.isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab", "***bba**a*bbba**aab**b"), False,
                         'Test #1666')


if __name__ == '__main__':
    unittest.main()
