def get_queryset(self, request):
        """Limit to TenantGroups that this group can access."""
        return TenantGroup.objects.filter(
            pk__in=request.user.get_permitted_objects(TenantGroup)
        )

