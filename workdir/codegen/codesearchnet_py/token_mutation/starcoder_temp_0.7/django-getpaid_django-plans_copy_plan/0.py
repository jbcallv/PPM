def copy_plan(modeladmin, request, queryset):
    """
    " prices for duplicating plans preserving strategies and pricings.
    """
    for plan in queryset:
        plan.id = None
        plan.save()


copy_plan.short_description = _('Duplicate plans')

