def variance_increase_distance(cluster1, cluster2, data = None):
    """!
    @brief clusters variance increase distance between two clusters.
    @details Clusters can be represented by list of coordinates (in this case data shouldn't be specified),
             or by average of indexes of points from the data (represented by list of points), in this case 
             data should be specified.
    
    @param[in] cluster1 (list): The first cluster.
    @param[in] cluster2 (list): The second cluster.
    @param[in] data (list): If specified than elements of clusters will be used as indexes,
               otherwise elements of list will be considered as points.
    
    @return (double) Average variance increase distance between two clusters.
    
    """
    return get_distance_between_clusters(cluster1, cluster2, data, variance_increase)
