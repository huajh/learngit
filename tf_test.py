import tensorflow as tf
import numpy as np

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a + b))
print('hello world.')
a = np.array([10, 20])

# D:/ProgramData/Anaconda3/envs/python35/Scripts/ipython
