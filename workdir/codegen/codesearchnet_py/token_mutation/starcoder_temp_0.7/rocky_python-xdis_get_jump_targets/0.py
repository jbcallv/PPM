def get_jump_targets(code, opc):
    """Returns a list of instruction instructions in the supplied bytecode
    which are the result of some kind of jump instruction.
    """
    jmp_targets = []
    for i in get_instructions(code):
        if i.opcode in opc.JUMP_OPCODES:
            if i.arg is not None:
                jmp_targets.append(i.arg)
        elif i.opcode in opc.COMPARE_OP:
            # compare instructions can also be targets
            jmp_targets.append(i.offset + 3)
    return jmp_targets

