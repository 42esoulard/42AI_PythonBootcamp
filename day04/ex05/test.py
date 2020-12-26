from FileLoader import FileLoader
from HowManyMedalsByCountry import howManyMedalsByCountry as hm

fl = FileLoader()
data = fl.load("../resources/athlete_events.csv")
hm(data, 'France')