def rename_fields(layer, fields_to_copy):
    """Rename fields inside an input table.

    Only since QGIS 2.16.

    :param layer: The vector layer.
    :type layer: QgsVectorLayer

    :param fields_to_copy: type of fields to copy.
    :type fields_to_copy: dict
    """

    if int(QGIS_VERSION[:2]) >= 216:
        QgsVectorFileWriter.renameAttributes(layer, fields_to_copy)

