import tensorflow as tf

# cong hang so
x = tf.constant(4)
y = tf.constant(5)
z = tf.add(x,y)
with tf.Session() as sess:
    # x, y o day bat dau co gia tri
    result = sess.run(z)
    print(z.eval())
# cong bien so
a = tf.Variable(10) #10 -> khoi tao ban dau
b = tf.Variable(12)
c = tf.add(a,b)
init = tf.global_variables_initializer() # khoi tao cac gia tri variable, x,y luc nay duoc khoi tao nhung ko co gia tri
with tf.Session() as sess:
    # x, y co gia tri
    sess.run(init)
    sess.run(c)
    print(c.eval())
    print(c)

