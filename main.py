#!/usr/bin/env python

from wsat import Wsat
import argparse
from parse_cnf import parse_cnf
from infer import infer
import os


# parse args
parser = argparse.ArgumentParser(
    description='sat solver based on walksat algorithm')
parser.add_argument(
    "--max_flips", type=int, help='max number of flips, defaul 10000')
parser.add_argument(
    "--p", type=float, help='probability to flip a coin, default 0.5')
parser.add_argument(
    "-i", "--infer", type=str, help='inference query, must be negated first')
parser.add_argument(
    "-v", "--verbose", help="print details", action="store_true")
parser.add_argument(
    "input", metavar='INPUT', type=str, help='input in cse573 CNF format')
arguments = parser.parse_args()


def main():
    max_flips = arguments.max_flips if arguments.max_flips else 10000
    seed = os.urandom(4)
    p = arguments.p if arguments.p else 0.5
    (num_lit, clauses, var_map) = parse_cnf(arguments.input)
    problem = Wsat(clauses, num_lit, p, max_flips, seed)
    if arguments.verbose:
        problem.print_info()
    if arguments.infer:
        if problem.solve():
            print "KB is valid."
            if infer(arguments.infer, var_map, problem):
                print "Query is entailed."
            else:
                print "Query is not entailed."
        else:
            print "KB is not valid!"
    else:
        print problem.solve()

if __name__ == "__main__":
    main()
