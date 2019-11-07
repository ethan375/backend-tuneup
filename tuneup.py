#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "ethan375"

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""

    def performance_audit(*args, **kwargs):
        p = cProfile.Profile()
        p.enable()
        r = func(*args, **kwargs)
        p.disable()
        stat = pstats.Stats(p).sort_stats('cumulative')
        stat.print_stats()
        return r
    return performance_audit


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    for movie in movies:
        if movie == title:
            return True
    return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    movies = [movie.lower() for movie in movies]
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(main)
    result = t.repeat(repeat=7, number=5)
    final_list = [time / 5 for time in result]
    print('Best time across 7 repeats of 5 runs per repeat: {}'.format(min(final_list)))


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
