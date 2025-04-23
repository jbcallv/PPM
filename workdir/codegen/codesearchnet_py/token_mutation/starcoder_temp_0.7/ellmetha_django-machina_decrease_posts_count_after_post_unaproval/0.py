def decrease_posts_count_after_post_unaproval(sender, instance, **kwargs):
    """ Decreases the member's post role after a post unaproval.

    This article handles the is of a forum post: the posts count associated with the post's
    author is decreased.
    """
    instance.author.posts_count -= 1
    instance.author.save()

