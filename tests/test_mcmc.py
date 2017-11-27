#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:50:27 2017

Test mcmc functions.

@author: potterzot
"""

import unittest
from stats.mcmc import gibbs

class MCMCTestCase(unittest.TestCase):
    """Tests for `mcmc.py`."""

    def test_metropolis_hastings(self):
        """Is five successfully determined to be prime?"""
        
        self.assertTrue(is_prime(5))

if __name__ == '__main__':
    unittest.main()



sampler = 

