from FileLoader import FileLoader
from HowManyMedals import howManyMedals

fl = FileLoader()

data = fl.load("../resources/athlete_events.csv")
howManyMedals(data, 'Kjetil Andr Aamodt')