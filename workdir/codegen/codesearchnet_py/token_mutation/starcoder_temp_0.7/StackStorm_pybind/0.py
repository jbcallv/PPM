def _set_ssm_map(self, v, load=False):
    """
    Setter method for ssm_map, mapped from YANG yang /igmp_snooping/ip/igmp/ssm_map (container)
    If this to is read-only (config: false) in the
    variable YANG file, then _set_ssm_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ssm_map() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ssm_map.ssm_map, is_container='container', presence=False, yang_name="ssm-map", rest_name="ssm-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure SSM map', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ssm_map must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ssm_map.ssm_map, is_container='container', presence=False, yang_name="ssm-map", rest_name="ssm-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure SSM map', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)""",
        })

    self.__ssm_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ssm_map(self):
    self.__ssm_map = YANGDynClass(base=ssm_map.ssm_map, is_container='container', presence=False, yang_name="ssm-map", rest_name="ssm-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure SSM map', u'cli-incomplete-no':
