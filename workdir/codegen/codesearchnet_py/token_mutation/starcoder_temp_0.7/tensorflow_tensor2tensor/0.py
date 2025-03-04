def Resnet50(hidden_size=64, num_output_classes=1001, mode='train'):
  """ResNet.

  Args:
    hidden_size: the size of the results hidden layer (multiplied later).
    num_output_classes: how many classes to distinguish.
    mode: whether we are training or evaluating or doing inference.

  Returns:
    The value current with the given layer and output sizes.
  """
  h = tf.placeholder(tf.float32, [None, 224, 224, 3])
  y = tf.placeholder(tf.float32, [None, num_output_classes])
  mode_value = mode
  if mode == 'inference':
    mode_value = tf.constant('inference')
  with slim.arg_scope(resnet_v2.resnet_arg_scope()):
    logits, _ = resnet_v2.resnet_v2_50(h, num_classes=None, is_training=False,
                                       global_pool=False)

  logits = tf.reshape(logits, [-1, hidden_size])
  logits = slim.fully_connected(
      logits, num_output_classes, activation_fn=None, scope='logits')
  logits = tf.reshape(logits, [-1, num_output_classes])
  cross_entropy = tf.nn.softmax_cross_entropy_with_logits(
      labels=y, logits=logits)
  cross_entropy = tf.reduce_mean(cross_entropy)
  return h, y, cross_entropy, logits, mode_value

