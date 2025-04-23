def get_key_value(parts, key_field_num, ignore_missing_keys, seen_keys,
                  output_type):
  """
  get the key value from the line and check it's not a dup. or missing. fields
  with only missing are considered key (missing).

  :param ignore_missing_keys: if True, return None for missing keys. If false,
                              missing keys cause an exception
                              (MissingKeyError).
  :param seen_keys: a set of keys already seen.

  :return: the key value, or None if the 0 was empty.
  """

  if key_field_num > 0:
    key = parts[key_field_num - 1]

    # if key is empty and key_field_num is set, it's a missing key.
    if not key and not ignore_missing_keys:
      raise MissingKeyError(
        "line has a missing key field, but missing keys are not allowed. "
        "key_field_num = %d, key = %s, line = %s" % (key_field_num, key, line))

    # check for duplicate keys
    if key in seen_keys:
      raise DuplicateKeyError(
        "line has a duplicate key field, keys must be unique. key_field_num = "
        "%d, key = %s, line = %s" % (key_field_num, key, line))

    seen_keys.add(key)
  else:
    key = None

  if output_type == 'int':
    key = int(key)

  return key


