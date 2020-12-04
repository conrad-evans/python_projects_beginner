import re


class EmailSlicer:
    EMAIL_RE = R"((\w+)@(\w+)(\W+))"

    def __init__(self, email):
        """
        email slicer class

        Args:
            param(str): email
        """
        self.email = email

    def _isEmail(self):
        """
        validates if string is email
        
        Returns:
            bool: True if string is email else False
        """
        if re.search(self.EMAIL_RE, self.email):
            return True
        return False

    def sliceEmail(self):
        """
        gets username from email

        Returns:
            str: greets user with username or returns invalid email message
        """
        if self._isEmail():
            user_name = self.email[: self.email.index("@")]
            return "Hello, your username is " + user_name
        return "Invalid email"
