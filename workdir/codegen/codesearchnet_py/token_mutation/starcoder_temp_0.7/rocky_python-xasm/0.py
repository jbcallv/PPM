def copy_magic_into_pyc(input_pyc, output_pyc,
                        src_version, dest_version):
    """Bytecodes are the same except the serial number, so just change
    that"""
    with open(input_pyc, 'rb') as in_f:
        in_magic = in_f.read(4)
        assert len(in_magic) == 4
        in_magic_int = struct.unpack('>I', in_magic)[0]

        in_magic_int = (in_magic_int & ~0xFFFF0000) | (
            (src_version & 0xFFFF) << 16)
        out_magic = struct.pack('>I', in_magic_int)
        with open(output_pyc, 'wb') as out_f:
            out_f.write(out_magic)
            out_f.write(in_f.read())


