#!/usr/bin/env python


def parse_DIMACS_cnf(filename):
    print "to be implemented"


def parse_cnf(filename):
    clauses = []
    counter = 1
    var_map = dict()
    for line in open(filename):
        tokens = line.split(" ")
        clause = []
        for token in tokens:
            var_str = token[1:] if token.startswith('!') else token
            if var_str in var_map:
                var = var_map[var_str]
            else:
                var = counter
                var_map[var_str] = counter
                counter += 1
            var = -var if token.startswith('!') else var
            clause.append(var)
        clauses.append(clause)
    return (counter, clauses)
