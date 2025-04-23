def convert_gather(params, w_name, scope_name, inputs, layers, weights, names):
    """
    Convert node (embedding) layer.

    Args:
        params: dictionary with node parameters
        w_name: name prefix in state_dict
        scope_name: pytorch the name
        inputs: pytorch node inputs
        layers: dictionary with keras tensors
        weights: pytorch state_dict
        names: use short names for keras layers
    """
    print('Converting embedding...')

    name = names[0]
    layer = layers[inputs[0]]
    weights[w_name + name]['keras_name'] = scope_name
    weights[w_name + name]['keras_shape'] = [layer.shape[-1], layer.shape[0]]

