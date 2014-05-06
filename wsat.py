#!/usr/bin/env python
import random
from bitarray import bitarray
import binascii


class Wsat(object):
    def __init__(self, clauses, num_lit, p, max_flips, seed):
        self.clauses = clauses
        self.num_lit = num_lit
        self.p = p
        self.max_flips = max_flips
        self.seed = seed
        self.random_gen = random.Random(seed)
        self.num_clauses = len(clauses)
        # inital assignment
        rand = self.random_gen
        model = bitarray(num_lit)
        for i in xrange(0, num_lit):
            model[i] = bool(rand.getrandbits(1))
        self.model = model

    @staticmethod
    def __flip(lit, model):
        """ flip a lit in a model
        """
        lit_idx = abs(lit) - 1
        model[lit_idx] = False if model[lit_idx] else True

    @staticmethod
    def __clause_sat(clause, model):
        sat = False
        for lit in clause:
            if (lit > 0) == model[abs(lit)-1]:
                sat = True
                break
        return sat

    def __compute_unsat(self, model):
        """ compute unsat clauses
        """
        unsat_clauses = []
        for i, clause in enumerate(self.clauses):
            if not Wsat.__clause_sat(clause, model):
                unsat_clauses.append(i)
        return unsat_clauses

    def __num_sat_by_filp(self, clause):
        """  Return the number of satisfied clauses after flip a lit
        """
        for lit in clause:
            Wsat.__flip(lit, self.model)
            sat = 0
            for clause in self.clauses:
                if Wsat.__clause_sat(clause, self.model):
                    sat += 1
            # flip back
            Wsat.__flip(lit, self.model)
            yield (sat, lit)

    def solve(self):
        """
        solve the problem.
        """
        # get intial unsatisfied clauses
        unsat_clauses = []
        for i, clause in enumerate(self.clauses):
            if Wsat.__clause_sat(clause, self.model):
                unsat_clauses.append(i)
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
                    Wsat.__flip(lit, model)
                else:  # flip a lit in the clause s.t. # of sat is maximized.
                    (sat, lit) =\
                        max(self.__num_sat_by_filp(clause), key=lambda x: x[0])
                    Wsat.__flip(lit, self.model)
        return False

    def print_info(self):
        print "num_lit: {}".format(self.num_lit)
        print "num_clauses: {}".format(self.num_clauses)
        print "p: {}".format(self.p)
        print "max_flips: {}".format(self.max_flips)
        print "seed:", binascii.hexlify(self.seed)
