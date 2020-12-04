from src import functions


class Test_EmailSlicer:
    email_one = "someone@example.com"
    email_two = "someone@example.co.sa"
    email_three = "@example"
    email_four = "someone@examplecom"
    email_five = "someoneexample.com"
    email_six = "someone@"
    email_seven = "someone"
    email_eight = "someoneelse@example.co.sa"

    def test_isEmail(self):
        assert functions.EmailSlicer(self.email_one)._isEmail()
        assert functions.EmailSlicer(self.email_two)._isEmail()

    def test_isEmail_fail(self):
        assert not functions.EmailSlicer(self.email_three)._isEmail()
        assert not functions.EmailSlicer(self.email_four)._isEmail()
        assert not functions.EmailSlicer(self.email_five)._isEmail()
        assert not functions.EmailSlicer(self.email_six)._isEmail()
        assert not functions.EmailSlicer(self.email_seven)._isEmail()

    def test_sliceEmail(self):
        user_name_one = functions.EmailSlicer(self.email_one).sliceEmail()
        user_name_two = functions.EmailSlicer(self.email_eight).sliceEmail()

        greeting = "Hello, your username is "

        assert user_name_one == greeting + "someone"
        assert user_name_two == greeting + "someoneelse"

    def test_sliceEmail_fail(self):
        user_name_one = functions.EmailSlicer(self.email_four).sliceEmail()
        user_name_two = functions.EmailSlicer(self.email_five).sliceEmail()

        invalid_email = "Invalid email"

        assert user_name_one == invalid_email
        assert user_name_two == invalid_email