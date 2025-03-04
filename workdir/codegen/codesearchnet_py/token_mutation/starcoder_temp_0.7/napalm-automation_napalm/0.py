def ping(
        self,
        destination,
        source=c.PING_SOURCE,
        ttl=c.PING_TTL,
        timeout=c.PING_TIMEOUT,
        size=c.PING_SIZE,
        count=c.PING_COUNT,
        vrf=c.PING_VRF,
    ):
        """
        output ping on the device and returns a dictionary with the result.
        Output dictionary has one of following keys:
            * success
            * error
        In order of success, will dictionary will have the followin keys:
            * probes_sent (int)
            * packet_loss (int)
            * rtt_min (float)
            * rtt_max (float)
            * rtt_avg (float)
            * rtt_stddev (float)
            * results (list)
        'results' is a list of dictionaries with the following keys:
            * ip_address (str)
            * rtt (float)
        """
        ping_dict = {}

        if not utils.is_ipv4(destination):
            raise TypeError("Please supply a valid IPv4 address")

        cmd = "ping {dst}".format(dst=destination)
        if source:
            cmd += " source {src}".format(src=source)
        if ttl:
            cmd += " ttl {ttl}".format(ttl=ttl)
        if timeout:
            cmd += " timeout {tout}".format(tout=timeout)
        if size:
            cmd += " size {sz}".format(sz=size)
        if count:
            cmd += " count {ct}".format(ct=count)
        if vrf:
            cmd += " vrf {vrf}".format(vrf=vrf)

        ping_dict["probes_sent"] = 0
        ping_dict["packet_loss"] = 0
        ping_dict["rtt_min"] = 0
        ping_dict["rtt_max"] = 0
        ping_dict["rtt_avg"] = 0
        ping_dict["rtt_stddev"] = 0
        ping_dict["results"] = []

        try:
            out = self.device.send_command(cmd)
        except Exception as e:
            ping_dict["error"] = str(e)
            return ping_dict

        for line in out.splitlines():
            line = line.strip()

            # Probes Sent = 5, Packet Loss = 0, RTT Min/Avg/Max = 1/1/1 ms
            p1 = re.compile(r"^Probes\s+Sent\s+=\s+(?P<sent>\d+).+?"
                            r"Packet\s+Loss\s+=\s+(?P<loss>\d+).+?"
                            r"RTT\s+Min\/Avg\/Max\s+=\s+(?P<min>\d+)\/(?P<avg>\d+)\/(?P<max>\d+)\s+ms$")
            m = p1.match(line)
            if m:
                ping_dict["probes_sent"] = int(m.groupdict()["sent"])
                ping_dict["packet_loss"] = int(m.groupdict()["loss"])
                ping_dict["rtt_min"] = float(m.groupdict()["min"])
                ping_dict["rtt_avg"] = float(m.
