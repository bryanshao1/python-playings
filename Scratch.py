import tensorflow as tf


def oddTuples(aTup):
    oddTup = ()
    for each in aTup[0:len(aTup):2]:
        oddTup = oddTup + (each,)
    return oddTup
