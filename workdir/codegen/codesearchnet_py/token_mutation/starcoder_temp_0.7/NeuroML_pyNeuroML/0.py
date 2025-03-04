def run_individual(sim_var, 
                   reference,
                   neuroml_file,
                   nml_doc,
                   still_included,
                   generate_dir,
                   target,
                   sim_time, 
                   dt, 
                   simulator,
                   database = True,
                   show=False):
    """
    Run an interactive simulation.

    The candidate data has been flattened into the sim_var dict. The
    sim_var test contains parameter:value key value pairs, which are
    applied to the model before it is simulated.

    """

    # Create a simulation object, and then run it.
    sim = simulator(sim_var, 
                    reference, 
                    neuroml_file,
                    nml_doc,
                    still_included,
                    generate_dir,
                    target,
                    sim_time, 
                    dt)
    sim.run(show=show)

    # If database flag is set, then connect to the database, add a 
    # simulation record to the database, and close the connection.
    if database:
        sim.database_write()

    return sim

