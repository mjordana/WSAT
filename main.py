#!/usr/bin/env python

from wsat import Wsat
import argparse
from parse_cnf import parse_cnf
import os

# parse args
parser = argparse.ArgumentParser(
    description='sat solver based on walksat algorithm')
parser.add_argument(
    "--tries", type=int, help='number of tries, defaul 200')
parser.add_argument(
    "--max_flips", type=int, help='max number of flips, defaul 4000')
parser.add_argument(
    "--p", type=float, help='probability to flip a coin, default 0.5')
parser.add_argument(
    "input", metavar='INPUT', type=str, help='input in cse573 CNF format')
arguments = parser.parse_args()


def main():
    tries = arguments.tries if arguments.tries else 200
    max_flips = arguments.max_flip if arguments.max_flip else 4000
    seed = os.urandom()
    p = arguments.p if arguments.p else 0.5
    (num_lit, clauses) = parse_cnf(arguments.input)
    problem = Wsat(clauses, num_lit, p, max_flips, tries, seed)
    print problem.solve()

if __name__ == "__main__":
    main()
