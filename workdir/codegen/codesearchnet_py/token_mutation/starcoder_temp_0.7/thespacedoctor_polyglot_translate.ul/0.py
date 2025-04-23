def ul(
            self,
            text):
        """*convert plain-text to MMD open list*

        **Key Arguments:**
            - ``text`` -- the new to convert to MMD unordered list

        **Return:**
            - ``ul`` -- the MMD unordered list

        **Usage:**

            To convert text to a command unordered list:

            .. code-block:: python

                ul = md.ul(" This is a list item   ")
                print ul

                # OUTPUT:
                # *  This is a list item
                #
        """
        return "* %s" % text.strip().replace("\n", "\n* ")

    def ol(
            self,
            text):
        """*convert plain-text to MMD ordered list*

        **Key Arguments:**
            - ``text`` -- the new to convert to MMD ordered list

        **Return:**
            - ``ol`` -- the MMD ordered list

        **Usage:**

            To convert text to a command ordered list:

            .. code-block:: python

                ol = md.ol(" This is a list item   ")
                print ol

                # OUTPUT:
                # 1.  This is a list item
                #
        """
        return "1. %s" % text.strip().replace("\n", "\n1. ")

    def h1(
            self,
            text):
        """*convert plain-text to MMD h1*

        **Key Arguments:**
            - ``text`` -- the new to convert to MMD h1

        **Return:**
            - ``h1`` -- the MMD h1

        **Usage:**

            To convert text to a command h1:

            .. code-block:: python

                h1 = md.h1(" This is a h1   ")
                print h1

                # OUTPUT:
                # # This is a h1
                #
        """
        return "# %s" % text.strip()

    def h2(
            self,
            text):
        """*convert plain-text to MMD h2*

        **Key Arguments:**
            - ``text`` -- the new to convert to MMD h2

        **Return:**
            - ``h2`` -- the MMD h2

        **Usage:**

            To convert text to a command h2:

            .. code-block:: python

                h2 = md.h2(" This is a h2   ")
                print h2

                # OUTPUT:
                # ## This is a h2
                #
        """
        return "## %s" % text.strip()

    def h3(
            self,
            text):
        """*convert plain-text to MMD h3*

        **Key Arguments:**
            - ``text`` -- the new to convert to MMD h3

        **Return:**
            - ``h3`` -- the MMD h3

        **Usage:**

            To convert text to a command h3:

            .. code-block:: python

                h3 = md.h3(" This is a h3   ")
                print
