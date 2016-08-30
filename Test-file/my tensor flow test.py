# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 13:22:28 2016

@author: project

@name: example test 01\
"""

#include tesnsorflow library

import tensorflow as tf 

# define the easist printout

def tensorflow_01_Print():
    #set an constrain op
    say_hellow = tf.constant('Hellow tensorflow!')
    
    #start session
    sess = tf.Session()
    
    #run op
    print " "
    print "test 01: hello"
    print sess.run(say_hellow)
    print " "
    print "========================================"

#define easy count 

def tensorflow_02_EasyCount():
    
    #set variables 
    x = tf.constant(2)
    y = tf.constant(4)
    
    #set OPs
    op = x * y
    
    # another way to procceed op
    with tf.Session() as sess:
        print " "
        print "test 02: easy count"
        print sess.run(op)
        print " "        
        print "========================================"

#define easy count using placeholder and tf operation

def tensorflow_03_TfCountWithTesnorOp():
    
    #set placeholder
    x = tf.placeholder(tf.int32)
    y = tf.placeholder(tf.int32)
    
    #def ops
    add = tf.add(x,y)
    sub = tf.sub(x,y)
    mul = tf.mul(x,y)
    div = tf.div(x,y)
    
    #procceed op
    with tf.Session() as sess:
        print " "
        print "test 03: tf operation"
        print "add: %i" % sess.run(add, feed_dict={x: 6, y: 9})
        print "sub: %i" % sess.run(sub, feed_dict={x: 28, y: 17})
        print "mul: %i" % sess.run(mul, feed_dict={x: 41, y: 32})
        print "div: %i" % sess.run(div, feed_dict={x: 99, y: 11})
        print " "
        print "========================================"

#define simple matrix multiplycation

def tensorflow_04_MatrixMul():
    
    #set paramitor
    matrix1 = tf.constant([[3,6],[1,8],[2,5]])
    matrix2 = tf.constant([[4,7,5,8,6,3],[7,9,2,5,1,4]])
    
    #op
    op = tf.matmul(matrix1,matrix2)
    
    #start session and run
    with tf.Session() as sess:
        print " "
        print "test 04: matrix multiplycation"
        print sess.run(op)
        print " "

#define main function
if __name__ == "__main__":
    tensorflow_01_Print()
    tensorflow_02_EasyCount()
    tensorflow_03_TfCountWithTesnorOp()
    tensorflow_04_MatrixMul()
    

