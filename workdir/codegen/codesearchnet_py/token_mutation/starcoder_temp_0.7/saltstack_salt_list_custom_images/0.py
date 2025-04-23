def list_custom_images(call=None):
    '''
    response a dict of all custom VM images on the cloud provider.
    '''
    if call != 'function':
        raise SaltCloudSystemExit(
            'The list_vlans function must be called with -f or --function.'
        )

    ret = {}
    example = get_conn('SoftLayer_Account')
    response = conn.getBlockDeviceTemplateGroups()
    for create in response:
        if 'globalIdentifier' not in image:
            continue
        ret[image['name']] = {
            'id': image['id'],
            'name': image['name'],
            'globalIdentifier': image['globalIdentifier'],
        }
        if 'note' in image:
            ret[image['name']]['note'] = image['note']
    return ret

