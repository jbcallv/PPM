def _build_con_add_cmd(ssid: str, security_type: SECURITY_TYPES,
                       psk: Optional[str], hidden: bool,
                       eap_args: Optional[Dict[str, Any]]) -> List[str]:
    """ . the nmcli - add command to configure the new network.

    The parameters are the same as configure but without the defaults; this
    should be called only by configure.
    """
    args = ['con', 'add','ssid', ssid]
    if security_type == SECURITY_TYPES.WPA2_ENTERPRISE:
        args.extend(['psk', psk])
    elif security_type == SECURITY_TYPES.WPA2_PERSONAL:
        args.extend(['psk-file', psk])
    elif security_type == SECURITY_TYPES.OPEN:
        pass
    else:
        raise Exception(f"Unsupported security type {security_type}")
    if hidden:
        args.append('hidden')
    if eap_args:
        args.extend(['eap', ','.join(eap_args)])

    return args

