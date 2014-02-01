#!/usr/bin/python

from itertools import *

def powerset(itr):
  """
  Given some iterable, generate its powerset.

  params:
    * itr (iterable) -- iterable to generate powerset from 
  returns:
    * powerset of itr
  """
  s = list(itr)
  return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def is_topology(X, T):
  """
  Checks to see if T is a topology on X

  params:
    X (set) -- some set
    T (list[Set]) -- set to be evaluated as topology on X.
  Note:
    Here we have T as a list[Set], but in real life T is a Set of Sets. It's just that
    python can not have Set[Set] since Sets are unhashable types.

  returns:
    True if T is a topology on X. Else, False
  """
  ## 1. check to see if T contains the empty Set and X. Return false if it does not!
  if (set() not in T) or (X not in T):
    return False

  for sets in powerset(T):
    # ignore empty set returned from powerset(T)
    if len(sets) is 0:
      continue
      
    ## 2. check to see if T is stable by arbitrary unions
    ##    In other words, unions of any elements of T should belong in T
    condition2 = reduce(lambda a,b: a.union(b), sets, EMPTY_SET) in T    

    ## 3. check to see if T is stable by finite intersection.
    ##    In other words, intersections of any elements of T should belong in T
    ##    Note: We generally don't have to worry about the infite case here
    ##    since X is expected to be a finite set. 
    ##    
    ##    Question: what happens when we have an infite set?
    condition3 = reduce(lambda a,b: a.intersection(b), sets, sets[0]) in T
   
    # return False if either conditions 2 or 3 are False
    if (condition2 is False) or (condition3 is False):
      return False

  # good!
  return True


# CONSTANTS
EMPTY_SET = set() # empty set

if __name__ == "__main__":
  # quick checks
  X = set([1,2,3,4,5])
  T1 = [EMPTY_SET, set([1,2]), set([3,4]), set([1,2,3,4]), X]
  T2 = [EMPTY_SET, set([1,2]), set([2,3]), set([2]), set([1,2,3]), X]
  T3 = [EMPTY_SET, set([1,2]), set([2,3]), set([1,2,3]), X]

  print "T1 is a topology on X", is_topology(X, T1)
  print "T2 is a topplogy on X", is_topology(X, T2)
  print "T3 is a topology on X", is_topology(X, T3)
  


