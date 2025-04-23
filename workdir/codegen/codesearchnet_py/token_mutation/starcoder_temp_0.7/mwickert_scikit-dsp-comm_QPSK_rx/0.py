def QPSK_rx(fc,N_symb,Rs,EsN0=100,fs=125,lfsr_len=10,phase=0,pulse='src'):
    """
    This thing generates
    """
    # Predefine variables
    fs = fs #sampling frequency
    N_symb = N_symb # number of symbols in the burst
    Ts = 1/fs #sampling period
    pulse_len = 10e-6 # pulse length
    t_pulse = np.arange(0,pulse_len,Ts)
    symbol_len = pulse_len/N_symb # symbol length
    t_symbol = np.arange(0,symbol_len,Ts)
    Es = EsN0*np.sqrt(2) #signal power

    if pulse=='src':
        pulse = src(t_pulse,fc)
    else:
        pulse = np.ones(len(t_pulse))

    # Initiate variables
    Rx = np.zeros(len(t_pulse)) # Received signal
    x_lsf = np.zeros(len(t_pulse)) # LSF of x
    x_lsf_symb = np.zeros(len(t_symbol)) # LSF of x

    # Loop over symbols
    for i in range(N_symb):
        # Generate a random sequence
        rand_seq = np.random.randint(0,2,lfsr_len)

        # Create LSF of random sequence
        x_lsf_symb = np.convolve(rand_seq,pulse,'full')[:len(t_symbol)]

        # Multiply it with the pulse to get the LSF of the received signal
        x_lsf = np.convolve(x_lsf_symb,pulse)[:len(t_pulse)]

        # Apply the LSF to the received signal
        Rx = np.convolve(Rx,x_lsf)[:len(t_pulse)]

        # Add noise
        Rx = Rx + np.random.normal(0,np.sqrt(Es/2),len(t_pulse))

    return Rx

