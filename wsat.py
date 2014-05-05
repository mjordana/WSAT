#!/usr/bin/env python
import random
from bitarray import bitarray


class Wsat(object):
    def __init__(self, clauses, num_lit, p, max_flips, tries, seed):
        self.clauses = clauses
        self.num_lit = num_lit
        self.p = p
        self.max_flips = max_flips
        self.tries = tries
        self.seed = seed
        self.random_gen = random.Random(seed)
        self.num_clauses = len(clauses)
        # inital assignment
        rand = self.random_gen
        model = bitarray(num_lit)
        for i in xrange(0, num_lit):
            model[i] = bool(rand.getrandbits(1))
        self.model = model

    def __flip(lit, model):
        """ flip a lit in a model
        """
        model[lit] = False if model[lit] else True

    def __clause_sat(clause, model):
        for lit in clause:
            sat = False
            cond1 = lit > 0 and model[lit]
            cond2 = lit < 0 and not model[-lit]
            if cond1 or cond2:
                sat = True
                break
        return sat

    def __compute_unsat(self, model):
        """ compute unsat clauses
        """
        unsat_clauses = set()
        for i, clause in enumerate(self.clauses):
            if not Wsat.__clause_sat(clause, model):
                unsat_clauses.add(i)
        return unsat_clauses

    def __num_sat_by_filp(self, clause):
        """  Return the number of satisfied clauses after flip a lit
        """
        for lit in clause:
            Wsat.flip(lit, self.model)
            sat = 0
            for clause in self.clauses:
                if Wsat.__clause_sat(clause, self.model):
                    sat += 1
            # flip back
            Wsat.flip(lit, self.model)
            yield (sat, lit)

    def solve(self):
        """
        solve the problem.
        """
        # get intial unsatisfied clauses
        unsat_clauses = set()
        for i, clause in enumerate(self.clauses):
            if Wsat.__clause_sat(clause):
                unsat_clauses.add(i)

        # the algorithm
        rand = self.random_gen
        model = self.model
        for i in xrange(0, self.max_flips):
            unsat_clauses = self.__compute_unsat(model)
            if len(unsat_clauses) == 0:
                return True
            else:
                idx = rand.choice(unsat_clauses)
                clause = self.clauses[idx]
                if rand.random() < self.p:  # flip an random lit
                    lit = rand.choice(clause)
                    Wsat.__flip(abs(lit), model)
                else:  # flip a lit in the clause s.t. # of sat is maximized.
                    (sat, lit) =\
                        max(self.__num_sat_by_filp, key=lambda x: x[0])
                    Wsat.flip(lit, self.model)
