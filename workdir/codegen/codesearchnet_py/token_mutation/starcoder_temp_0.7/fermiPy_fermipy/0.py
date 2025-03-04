def add_summary_stats_to_table(table_in, table_out, colnames):
    """Collect the statisitics from an input data and add them to an output table

     Parameters
    ----------

    table_in : `astropy.table.Table`
        Table with the input data.

    table_out : `astropy.table.Table`
        Table with the output data.

    colnames : list
        List of the column names to get summary table for.

    """
    for col in colnames:
        data = table_in[col]
        name = col + "_sum"
        mean = np.mean(data)
        std = np.std(data)
        n = len(data)
        table_out[name] = [mean, std, n]

