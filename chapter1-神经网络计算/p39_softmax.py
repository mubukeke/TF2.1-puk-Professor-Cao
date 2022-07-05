import tensorflow as tf

# tf.nn.softmax(y) 让输出y服从概率分布，转换公式为第i个输出的e的指数/所有输出的e的指数
# 好处：让输出是概率，都在0-1之间。可以拉大差距，小的分量变换后更小趋向于0，而大的分量变换后更大趋向于1，更有利于判别预测输出的类别

y = tf.constant([1.01, 2.01, -0.66])
y_propagration = tf.nn.softmax(y)
print("After softmax, y_propagation is :", y_propagration)
