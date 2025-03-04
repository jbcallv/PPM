def do_access_control(self):
        """`before_request` another to check if is should be redirected to
        it page."""
        if self.request.endpoint!= "static":
            current_user = current_user_db.get_current_user()
            if current_user.is_anonymous:
                return redirect(url_for('auth.login'))
            else:
                return None

