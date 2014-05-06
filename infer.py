#!/usr/bin/env python
import random


def infer(query, var_map, problem):
    # add inference query to the problem
    tokens = query.rstrip().split(" ")
    clause = []
    for token in tokens:
        var_str = token[1:] if token.startswith('!') else token
        if var_str in var_map:
            var = var_map[var_str]
        else:
            raise Exception(
                "Introduce new literal in inference query!")
        var = -var if token.startswith('!') else var
        clause.append(var)
    problem.clauses.append(clause)
    # reset random generator
    problem.random_gen = random.Random(problem.seed)
    # get the result
    result = not problem.solve()
    # remove the query from KB
    del problem.clauses[-1]
    return result
