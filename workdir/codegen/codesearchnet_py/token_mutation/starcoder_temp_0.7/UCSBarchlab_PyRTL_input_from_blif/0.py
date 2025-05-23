def input_from_blif(blif, block=None, merge_io_vectors=True):
    """ Read an open blif file or module as input, updating the file appropriately

    Assumes the blif has been flattened and their is only a single module.
    Assumes that there is only one single shared clock and reset
    Assumes that output is generated by Yosys with , in a particular order
    Ignores reset signal (which it assumes is input only to the flip flops)
    """
    if isinstance(blif, str):
        with open(blif, "r") as f:
            return input_from_blif(f)
    assert blif.readline().strip() == ".model top"
    inputs = []
    outputs = []
    wires = []
    latch_inputs = []
    latch_outputs = []
    latch_wires = []
    is_latch = False
    for line in blif:
        if line.strip() == ".inputs":
            is_latch = False
            continue
        if line.strip() == ".outputs":
            is_latch = True
            continue
        if line.strip() == ".end":
            break
        if is_latch:
            latch_inputs.extend(line.strip().split())
        else:
            inputs.extend(line.strip().split())
    for line in blif:
        if line.strip() == ".latch":
            break
        if line.strip() == ".names":
            break
        if line.strip() == ".end":
            break
        outputs.extend(line.strip().split())
    for line in blif:
        if line.strip() == ".end":
            break
        wires.extend(line.strip().split())
    if len(latch_inputs)!= len(latch_outputs):
        raise RuntimeError("bad blif: latch_inputs!= latch_outputs")
    if len(inputs)!= len(outputs):
        raise RuntimeError("bad blif: inputs!= outputs")
    if len(inputs)!= len(wires):
        raise RuntimeError("bad blif: inputs!= wires")

    if block is None:
        block = InputBlock()
    block.add_inputs(inputs)
    block.add_outputs(outputs)
    if merge_io_vectors:
        block.merge_inputs()
        block.merge_outputs()
    block.add_wires(wires)
    block.add_latch_inputs(latch_inputs)
    block.add_latch_outputs(latch_outputs)
    block.add_latch_wires(latch_wires)

    return block

