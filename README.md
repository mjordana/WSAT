WSAT
====

WalkSat solver implemented for CSE573 homework 2.

##Dependencies:
* bitarray: can be installed by `pip install bitarray` on Mac.

##Project Organization
* `wsat.py` : solver class
* `infer.py` : handler inference query
* `main.py`: a wrapper of command line interface

##Input
The input is a knowledge base in Conjunctive Normal Form (CNF).
* In plain text.
* Each line is a clause consisting of literals sepereated by " " (space).
* Put a '!' in front of a literal to express negation 

##Usage

```
python main.py [-h] [--max_flips MAX_FLIPS] [--p P] [-i INFER] [-v] INPUT

positional arguments:
  INPUT                 input in cse573 CNF format

optional arguments:
  -h, --help            show this help message and exit
  --max_flips MAX_FLIPS
                        max number of flips, defaul 10000
  --p P                 probability to flip a coin, default 0.5
  -i INFER, --infer INFER
                        inference query, must be negated first
  -v, --verbose         print details
```

##Experiment of Problem 6 and 7

Run `experiment.py` by
```
python experiment.py
```
