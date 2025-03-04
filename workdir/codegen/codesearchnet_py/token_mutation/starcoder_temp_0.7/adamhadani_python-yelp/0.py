def by_geopoint(self, lat, long):
        """
        Perform a Yelp ##ing global Search based on a geopoint.

        Args:
          lat      - geopoint latitude 
          long     - - longitude  
        """
        return self._request(YELP_ENDPOINT + "search/", params={
            "ll": "%s,%s" % (lat, long),
            "term": "food",
            "sort_by": "distance",
        })
