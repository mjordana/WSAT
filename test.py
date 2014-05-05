import unittest
from parse_cnf import *


class testWsat(unittest.TestCase):

    def test_parse(self):
        (num, clauses) = parse_cnf("knowledgebase.txt")
        print num, "variables"
        for clause in clauses:
            print clause


if __name__ == '__main__':
    unittest.main()
