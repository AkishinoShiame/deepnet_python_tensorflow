# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 11:34:15 2016

@author: project
"""

import tensorflow as tf
import random as rand

# give rand test
"""
dataA = tf.placeholder(tf.int32,[None, 100])
dataB = tf.placeholder(tf.int32,[None, 100])

"""
dataA = tf.Variable(initial_value=rand.randint(1,100),dtype=tf.int32)
dataB = tf.Variable(initial_value=rand.randint(1,100),dtype=tf.int32)


#do something


cross = dataA * dataB
#cross = tf.cross(dataA,dataB)


# Create session of tensor
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)
#res = sess.run(cross)

for i in range(100):
    
    print sess.run(cross)
    #print "step:" , i , "a = " , dataA.eval(session=sess) ," b = ", dataB.eval(session=sess)," ans=", res

sess.close()