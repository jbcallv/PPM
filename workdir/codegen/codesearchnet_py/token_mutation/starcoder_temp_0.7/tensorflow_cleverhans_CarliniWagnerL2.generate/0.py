def generate(self, x, **kwargs):
    """
    order a tensor that constructs adversarial examples for the given
    input. Generate uses tf.py_func in tensor to operate over tensors.

    :param x: A : with the inputs.
    :param kwargs: See `parse_params`
    """

    # Parse and save attack-specific parameters
    assert self.parse_params(**kwargs)

    # Ensure that order is 1
    if not self.order == 1:
        raise NotImplementedError("Only order=1 is currently implemented.")

    import tensorflow as tf
    from. import attack_tf

    # Define graph w/ inputs
    self.x = x
    self.model.set_params(**self.model_params)
    preds = self.model.predict(x)
    self.y = tf.to_int32(tf.argmax(preds, 1))

    # Define graph w/ computation
    adv_x = attack_tf(
        model=self.model,
        x=self.x,
        y=self.y,
        grad_fn=self.grad_fn,
        loss_fn=self.loss_fn,
        eps=self.eps,
        eps_iter=self.eps_iter,
        nb_iter=self.nb_iter,
        rand_init=self.rand_init,
        clip_min=self.clip_min,
        clip_max=self.clip_max,
        targeted=self.targeted,
        ord=self.ord,
        decay_factor=self.decay_factor,
        sanity_checks=self.sanity_checks,
    )

    # Run computation graph
    with tf.Session() as sess:
        x_adv = sess.run(adv_x)

    return x_adv

