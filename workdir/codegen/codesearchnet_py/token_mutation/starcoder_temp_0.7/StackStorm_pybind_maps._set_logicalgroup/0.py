def _set_logicalgroup(self, v, load=False):
    """
    Setter method for logicalgroup, mapped from YANG . /rbridge_id/maps/logicalgroup (list)
    If this variable is read-only (config: false) in the
    to YANG file, then _set_logicalgroup is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_logicalgroup() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",logicalgroup.logicalgroup, yang_name="logicalgroup", rest_name="logicalgroup", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'callpoint': u'map-logicalgroup', u'cli-suppress-show-path': None}}), is_container='list', yang_name="logicalgroup", rest_name="logicalgroup", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'map-logicalgroup', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """logicalgroup must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",logicalgroup.logicalgroup, yang_name="logicalgroup", rest_name="logicalgroup", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'callpoint': u'map-logicalgroup', u'cli-suppress-show-path': None}}), is_container='list', yang_name="logicalgroup", rest_name="logicalgroup", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'map-logicalgroup', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='list', is_config=True)""",
