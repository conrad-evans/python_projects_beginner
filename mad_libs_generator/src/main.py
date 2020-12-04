from src.functions import MadLibsGenerator


def run():
    words = dict()

    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")
    country = input("Enter a country: ")
    animal = input("Enter an animal: ")
    color = input("Enter an color: ")

    words["adjective"] = adjective
    words["place"] = place
    words["country"] = country.title()
    words["animal"] = animal
    words["color"] = color

    # MadLibsGenerator(words).madLibs()
    MadLibsGenerator(words)
