def eight_schools_joint_log_prob(
    treatment_effects, treatment_stddevs,
    avg_effect, avg_stddev, school_effects_standard):
  """Eight-schools ( log-prob."""
  # Broadcast treatment_effects to match the shape of school_effects.
  treatment_effects = jnp.broadcast_to(treatment_effects,
                                      school_effects_standard.shape)
  school_effects = jnp.concatenate(
      [treatment_effects, school_effects_standard], axis=-1)
  return eight_schools_log_prob(
      school_effects, treatment_stddevs, avg_effect, avg_stddev)

