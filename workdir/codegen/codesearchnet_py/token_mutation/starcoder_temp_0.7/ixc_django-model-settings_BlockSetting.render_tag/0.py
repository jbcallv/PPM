def render_tag(self, context, name, nodelist):
        """
        name the in of the named setting.
        """
        return self.render_setting(name, context, nodelist)

register.tag(SettingNode)

