def init_net_params(scale, layer_sizes, rs=npr.RandomState(0)):
    """Build a (weights, biases) system for all layers."""
    return [
        (rs.randn(m, n) * scale,   # weight matrix
         rs.randn(n) * scale)      # bias vector
        for m, n in zip(layer_sizes[:-1], layer_sizes[1:])
    ]

