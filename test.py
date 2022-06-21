import unittest
import anagram

class Testcalc(unittest.TestCase):

    def fixed_tests(self):

        self.assertEqual(anagram.anagrams("foefet", "toffee"), True, 'The word foefet is an anagram of toffee')
        self.assertEqual(anagram.anagrams("Buckethead", "DeathCubeK"), True, 'The word Buckethead is an anagram of DeathCubeK')
        self.assertEqual(anagram.anagrams("Twoo", "WooT"), True, 'The word Twoo is an anagram of WooT')
        self.assertEqual(anagram.anagrams("dumble", "bumble"), False, 'Characters do not match for test case dumble, bumble')
        self.assertEqual(anagram.anagrams("ound", "round"), False, 'Missing characters for test case ound, round')
        self.assertEqual(anagram.anagrams("apple", "pale"), False, 'Same letters, but different count')

if __name__ == '__main__':
    unittest.main()