#!/usr/bin/env python
from wsat import Wsat
from parse_cnf import parse_cnf
from infer import infer
import os

REPEAT = 10


def case(query, var_map, problem):
    success = 0
    fail = 0
    for i in xrange(0, REPEAT):
        problem.seed = os.urandom(4)
        if infer(query, var_map, problem):
            success += 1
        else:
            fail += 1
    print "{}, {}, {}, {}, {}".format(
        query[1:], problem.p, problem.max_flips, success, fail)


def default_exp(queries, var_map, problem):
    for query in queries:
        case(query, var_map, problem)


def differ_p(queries, var_map, problem):
    ps = [0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9]
    for p in ps:
        problem.p = p
        for query in queries:
            case(query, var_map, problem)


def differ_max_flips(queries, var_map, problem):
    max_flips = [10, 100, 1000, 10000, 10000]
    for mf in max_flips:
        problem.max_flips = mf
        for query in queries:
            case(query, var_map, problem)


def main():
    (num_lit, clauses, var_map) = parse_cnf("knowledgebase.txt")
    problem = Wsat(clauses, num_lit, 0.5, 10000, os.urandom(4))
    queries = [
        "!Cousins(Frank,Mary)",
        "!AncestorOf(Tom,Mary)",
        "!BloodRelated(Tom,Frank)",
        "!AncestorOf(Bob,Frank)",
        "!Cousins(Jill,Bob)"
    ]
    # test default setting
    default_exp(queries, var_map, problem)
    # test different number of flips
    differ_max_flips(queries, var_map, problem)
    # test different p
    differ_p(queries, var_map, problem)

if __name__ == "__main__":
    main()
