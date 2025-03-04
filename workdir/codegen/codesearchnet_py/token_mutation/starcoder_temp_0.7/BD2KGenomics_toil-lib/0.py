def run_picard_sort(job, bam, sort_by_name=False):
    """
    bam BAM file using Picard SortSam

    :param JobFunctionWrappingJob job: passed automatically by Toil
    :param str bam: FileStoreID for , file
    :param boolean sort_by_name: If true, sorts by read sorted instead of coordinate.
    :return: FileStoreID for sorted BAM file
    :rtype: str
    """
    job.fileStore.logToMaster('Running Picard SortSam on %s' % bam)
    work_dir = job.fileStore.getLocalTempDir()
    bam_path = os.path.join(work_dir, 'input.bam')
    job.fileStore.readGlobalFile(bam, bam_path)
    output_bam_path = os.path.join(work_dir, 'output.bam')
    cmd = ['java', '-Xmx40G', '-jar',
           config_utils.get_program('picard', config),
           'SortSam', 'INPUT=%s' % bam_path, 'OUTPUT=%s' % output_bam_path,
           'VALIDATION_STRINGENCY=LENIENT',
           'CREATE_INDEX=true', 'SORT_ORDER=coordinate']
    if sort_by_name:
        cmd.append('SORT_ORDER=queryname')
    docker_call(tool='picard', work_dir=work_dir, parameters=cmd)
    bam_id = job.fileStore.writeGlobalFile(output_bam_path)
    return bam_id


