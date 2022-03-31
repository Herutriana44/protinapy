import numpy as np
from numpy import asarray
from numpy import exp
from numpy.random import randn
from numpy.random import rand
from numpy.random import seed

def _entropy(dist):
  """Entropy of class-distribution matrix"""
  p = dist / np.sum(dist, axis=0)
  pc = np.clip(p, 1e-15, 1)
  return np.sum(np.sum(- p * np.log2(pc), axis=0) * np.sum(dist, axis=0) / np.sum(dist))

class GainRatio(ClassificationScorer):
  """
    Information gain ratio is the ratio between information gain and
    the entropy of the feature's
    value distribution. The score was introduced in [Quinlan1986]_
    to alleviate overestimation for multi-valued features. See `Wikipedia entry on gain ratio
    <http://en.wikipedia.org/wiki/Information_gain_ratio>`_.
    .. [Quinlan1986] J R Quinlan: Induction of Decision Trees, Machine Learning, 1986.
  """
  def from_contingency(self, cont, nan_adjustment):
    h_class = _entropy(np.sum(cont, axis=1))
    h_residual = _entropy(np.compress(np.sum(cont, axis=0), cont, axis=1))
    h_attribute = _entropy(np.sum(cont, axis=0))
    if h_attribute == 0:
      h_attribute = 1
    return nan_adjustment * (h_class - h_residual) / h_attribute

class SimulatedAnnealing:
  def objective(x):
    return x[0]**2.0
  
  def simulated_annealing(objective, bounds, n_iterations, step_size, temp):
    # generate an initial point
    best = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    # evaluate the initial point
    best_eval = objective(best)
    # current working solution
    curr, curr_eval = best, best_eval
    # run the algorithm
    for i in range(n_iterations):
      # take a step
      candidate = curr + randn(len(bounds)) * step_size
      # evaluate candidate point
      candidate_eval = objective(candidate)
      # check for new best solution
      if candidate_eval < best_eval:
        # store new best point
        best, best_eval = candidate, candidate_eval
        # report progress
        print('>%d f(%s) = %.5f' % (i, best, best_eval))
        # difference between candidate and current point evaluation
        diff = candidate_eval - curr_eval
        # calculate temperature for current epoch
        t = temp / float(i + 1)
        # calculate metropolis acceptance criterion
        metropolis = exp(-diff / t)
        # check if we should keep the new point
        if diff < 0 or rand() < metropolis:
          # store the new current point
          curr, curr_eval = candidate, candidate_eval
    return [best, best_eval]
