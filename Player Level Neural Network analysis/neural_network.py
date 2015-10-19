import numpy as np
#import glob
#import os
#from PIL import Image
from sklearn.decomposition import PCA
from numpy import *
from sklearn import cross_validation
from sklearn.metrics import accuracy_score
from scipy import optimize
from numpy import genfromtxt
import math
import random
import string
#from __future__ import division

dhoni = genfromtxt("E:\\BTP\\Training_data_dhoni.csv", delimiter = ",")

#print dhoni[1:]
#print dhoni[1:]
#print shape(dhoni[1:])

batting_index = genfromtxt("E:\\BTP\\Dhoni_index.csv", delimiter = ",")
#print batting_index[1:]
#print shape(batting_index[1:])

dhoni = np.array(dhoni[1:]).astype(np.int64)
batting_index = np.array(batting_index[1:]).astype(np.int64)

print type(dhoni[1:])
print type(batting_index[1:])

print shape(dhoni[1:])
print shape(batting_index[1:])










random.seed(0)

# calculate a random number where:  a <= rand < b
def rand(a, b):
    return (b-a)*random.random() + a

# Make a matrix (we could use NumPy to speed this up)
def makeMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill]*J)
    return m

# our sigmoid function, tanh is a little nicer than the standard 1/(1+e^-x)
def sigmoid(x):
    return math.tanh(x)

# derivative of our sigmoid function, in terms of the output (i.e. y)
def dsigmoid(y):
    return 1.0 - y**2

class NN:
    def __init__(self, ni, nh, no):
        # number of input, hidden, and output nodes
        self.ni = ni + 1 # +1 for bias node
        self.nh = nh
        self.no = no

        # activations for nodes
        self.ai = [1.0]*self.ni
        self.ah = [1.0]*self.nh
        self.ao = [1.0]*self.no
        
        # create weights
        self.wi = makeMatrix(self.ni, self.nh)
        self.wo = makeMatrix(self.nh, self.no)
        # set them to random vaules
        for i in range(self.ni):
            for j in range(self.nh):
                self.wi[i][j] = rand(-0.2, 0.2)
        for j in range(self.nh):
            for k in range(self.no):
                self.wo[j][k] = rand(-2.0, 2.0)

        # last change in weights for momentum   
        self.ci = makeMatrix(self.ni, self.nh)
        self.co = makeMatrix(self.nh, self.no)

    def update(self, inputs):
        if len(inputs) != self.ni-1:
            raise ValueError('wrong number of inputs')

        # input activations
        for i in range(self.ni-1):
            #self.ai[i] = sigmoid(inputs[i])
            self.ai[i] = inputs[i]

        # hidden activations
        for j in range(self.nh):
            sum = 0.0
            for i in range(self.ni):
                sum = sum + self.ai[i] * self.wi[i][j]
            self.ah[j] = sigmoid(sum)

        # output activations
        for k in range(self.no):
            sum = 0.0
            for j in range(self.nh):
                sum = sum + self.ah[j] * self.wo[j][k]
            self.ao[k] = sigmoid(sum)

        return self.ao[:]


    def backPropagate(self, targets, N, M):
        if len(targets) != self.no:
            raise ValueError('wrong number of target values')

        # calculate error terms for output
        output_deltas = [0.0] * self.no
        for k in range(self.no):
            error = targets[k]-self.ao[k]
            output_deltas[k] = dsigmoid(self.ao[k]) * error

        # calculate error terms for hidden
        hidden_deltas = [0.0] * self.nh
        for j in range(self.nh):
            error = 0.0
            for k in range(self.no):
                error = error + output_deltas[k]*self.wo[j][k]
            hidden_deltas[j] = dsigmoid(self.ah[j]) * error

        # update output weights
        for j in range(self.nh):
            for k in range(self.no):
                change = output_deltas[k]*self.ah[j]
                self.wo[j][k] = self.wo[j][k] + N*change + M*self.co[j][k]
                self.co[j][k] = change
                #print N*change, M*self.co[j][k]

        # update input weights
        for i in range(self.ni):
            for j in range(self.nh):
                change = hidden_deltas[j]*self.ai[i]
                self.wi[i][j] = self.wi[i][j] + N*change + M*self.ci[i][j]
                self.ci[i][j] = change

        # calculate error
        error = 0.0
        for k in range(len(targets)):
            error = error + 0.5*(targets[k]-self.ao[k])**2
        return error


    def test(self, patterns):
        for p in patterns:
            print(p[0], '->', self.update(p[0]))

    def weights(self):
        print('Input weights:')
        for i in range(self.ni):
            print(self.wi[i])
        print()
        print('Output weights:')
        for j in range(self.nh):
            print(self.wo[j])

    def train(self, patterns, iterations=1000, N=0.5, M=0.1):
        # N: learning rate
        # M: momentum factor
        for i in range(iterations):
            error = 0.0
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.update(inputs)
                error = error + self.backPropagate(targets, N, M)
            if i % 100 == 0:
                print('error %-.5f' % error)


pat = [ 
[ [2, 2, 6],[5.744] ],
[ [2, 2, 6],[3.18] ],
[ [2, 2, 6.5],[1.3064] ],
[ [1, 1, 6],[2.352] ],
[ [2, 2, 5],[9.9328] ],
[ [2, 1, 6.5],[5.06] ],
[ [2, 1, 6],[7.7244] ],
[ [2, 2, 5],[3.6332] ],
[ [2, 1, 5],[5.8836] ],
[ [2, 2, 6.5],[12.1504] ],
[ [2, 2, 7],[7.0364] ],
[ [2, 1, 4.5],[0.5044] ],
[ [2, 1, 8],[6.1] ],
[ [2, 1, 6],[11.6908] ],
[ [2, 2, 6.5],[4.412] ],
[ [2, 2, 6.5],[0] ],
[ [2, 2, 5.5],[7.5628] ],
[ [2, 1, 7],[3.6768] ],
[ [2, 2, 6.5],[4.2251] ],
[ [1, 2, 5],[0] ],
[ [1, 2, 6],[2.2864] ],
[ [2, 2, 6.5],[10.1184] ],
[ [1, 1, 7],[5.8132] ],
[ [2, 2, 5],[5.5064] ],
[ [2, 2, 6],[9.9212] ],
[ [2, 1, 6.5],[7.8104] ],
[ [2, 1, 5],[2.12] ],
[ [2, 1, 5.5],[2.9412] ],
[ [2, 2, 6],[6.6768] ],
[ [2, 2, 6],[4.258] ],
[ [2, 1, 6],[10.6132] ],
[ [2, 2, 6.5],[6.4748] ],
[ [2, 2, 6],[6.7756] ]
]


test_pat = [
[ [2, 2, 8],[3.1112] ],
[ [2, 1, 7],[11.9732] ],
[ [2, 1, 6],[8.222] ],
[ [2, 1, 6],[4.2] ],
[ [2, 2, 6.5],[7.09] ],
[ [2, 2, 5],[1.04] ]
]

#print shape(pat)
nn = NN(3,1,1)
nn.train(pat)
nn.test(test_pat)

#print X_test2
#print accuracy_score(y_test, nn.predict(X_test))
#print nn.predict(X_test)


