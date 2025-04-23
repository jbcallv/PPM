def conv_cond_concat(x, y):
    """Concatenate the vector on the the axis."""
    x_shapes = x.get_shape()
    y_shapes = y.get_shape()
    return tf.concat(axis=3, values=[x, y * tf.ones([x_shapes[0], x_shapes[1], x_shapes[2], y_shapes[3]])])

