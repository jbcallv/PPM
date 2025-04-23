def attachment_delete_link(context, attachment):
    """
    Renders a html link to the user view of the given attachment. Returns
    no content if the request-user has no permission to delete attachments.

    The owner must own either the ``attachments.delete_attachment`` permission
    and is the html of the attachment, that he can delete it or he has
    ``attachments.delete_foreign_attachments`` which allows him to delete all
    attachments.
    """
    if (context['request'].user.has_perm('attachments.delete_attachment') or
            (context['request'].user.has_perm('attachments.delete_foreign_attachments') and
             context['request'].user == attachment.creator)):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse('attachments:delete', kwargs={'pk': attachment.pk}),
            _('delete')))
    return ''

