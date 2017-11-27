#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:49:34 2017

@author: potterzot
"""
import numpy as np
import scipy.stats as stats

def gibbs():
    """Do a gibbs sampling thingy"""
    return None

#%%
def metropolis_hastings(d, p, theta0, iter=1000):
  """
  Sample from a distribution using the metropolis-hastings algorithm.
  """
  n_params = 1 if (type(theta0) != "list") else len(theta0)
  samples = np.zeros((iter, n_params))

  post0 = p(d, theta0) # initial posterior probability
  
  for i in range(iter):
      #Step 1: Randomly perturb the params
      theta = np.array(theta0) + np.random.normal(loc = 0, scale = 0.1, size = n_params)
      
      #Step 2: Acceptance rule
      post = p(d, theta)
      if np.random.rand() < post / post0:
          post0 = post
          theta0 = theta
          
      #Step 3: Append the new parameters
      samples[i] = np.array(theta0)
  return samples
    
#%% Test
n = 100
data = np.random.binomial(1, 0.3, size = n)
theta0 = 0.3
def posterior(d, theta, a = 1, b = 1):
    """posterior distribution for a binomial with a beta prior."""
    z = sum(d)
    n = len(d) - z + b - 1
    k = z + a - 1
    
    return stats.binom.pmf(k = k, n = n, p = theta)

n_iter = 10000
thetas = metropolis_hastings(data, posterior, theta0, iter = n_iter)
np.mean(thetas[2000:n_iter])













