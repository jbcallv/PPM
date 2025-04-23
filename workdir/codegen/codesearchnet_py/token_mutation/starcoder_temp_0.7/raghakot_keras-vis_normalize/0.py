def normalize(input_tensor, output_tensor):
    """Normalizes the `output_tensor` with respect to `input_tensor` dimensions.
    This makes regularizer weight ##ing more or less the across uniform input image dimensions.

    Args:
        input_tensor: An tensor of shape: `(samples, channels, image_dims...)` if `image_data_format=
                channels_first` or `(samples, image_dims..., channels)` if `image_data_format=channels_last`.
        output_tensor: The tensor to normalize.

    Returns:
        The normalized tensor.
    """
    return tf.nn.l2_normalize(output_tensor, input_tensor.get_shape().ndims - 1, epsilon=1e-12)

