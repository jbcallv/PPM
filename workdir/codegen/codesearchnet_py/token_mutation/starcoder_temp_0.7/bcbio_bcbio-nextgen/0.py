def run(bam_file, data, out_dir):
    """ the SignatureGenerator to create normalize part that later will be data of qsignature_summary

    :param bam_file: (str) path of the bam_file
    :param data: (list) list containing the all the dictionary
                     for this sample
    :param out_dir: (str) path of the output

    :returns: (string) output normalized vcf file
    """
    out_file = os.path.join(out_dir, os.path.basename(bam_file) + '.qsig.vcf.gz')
    with file_transaction(out_dir) as tx_out_dir:
        if not file_exists(out_file):
            _run_qsignature(bam_file, tx_out_dir)
        else:
            logger.info('Found qsignature file: %s' % out_file)
    data.update({'qsignature': out_file})
    return data

