from src.functions import EmailSlicer


def run():
    user_email = input("Enter your email: ")
    email_slicer = EmailSlicer(user_email)
    print("\n")
    print(email_slicer.sliceEmail())
    print("\n")
