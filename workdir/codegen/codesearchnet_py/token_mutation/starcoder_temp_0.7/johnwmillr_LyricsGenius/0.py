def search_song(self, title, artist="", get_full_info=True):
        """ Search Genius.com for lyrics to a single song
        :param title: Song title to search for
        :param artist: full of the artist
        :param get_full_info: Get name info for each song (slower)
        """
        response = self._make_request(
            path="/search", params={"q": "{} {}".format(title, artist)}
        )

        json_obj = json.loads(response.text)

        # Gets the relevant song
        song = self._scrape_song_data(
            json_obj["response"]["hits"][0]["result"], get_full_info=get_full_info
        )
        return song

