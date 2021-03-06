import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  N = X.shape[0]
  num_classes = W.shape[1]
  for i in range(N):
    scores = X[i].dot(W)
    scores -= np.max(scores)
    s = 0.0
    for j in range(num_classes):
      s += np.exp(scores[j])
      dW[:, j] += (np.exp(scores[j]) * X[i])/ np.sum(np.exp(scores)) 
    loss += -scores[y[i]] + np.log(s)
    dW[:, y[i]] -= X[i, :]

  loss /= N
  loss += reg * np.sum(W * W)
  dW /= N
  dW += 2 * reg * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  N = X.shape[0]
  scores = X.dot(W)
  scores -= np.max(scores)
  #print(scores.shape)
  loss = -scores[range(N),y] +np.log(np.sum(np.exp(scores),axis=1))
  loss = np.sum(loss)
  loss /= N
  loss += reg * np.sum(W * W)

  dW = np.exp(scores) / np.sum(np.exp(scores),axis=1).reshape(-1, 1)
  dW[range(N), y] -= 1
  dW = X.T.dot(dW)
  dW /= N
  dW += 2 * reg * W
  ###################
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

