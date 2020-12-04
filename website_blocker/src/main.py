from src.functions import WebsiteBlocker


def run():
    url = input("Enter url you want to block: ")
    print(WebsiteBlocker(url).blockWebsite())