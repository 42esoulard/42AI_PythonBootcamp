from FileLoader import FileLoader
from YoungestFellah import youngestFellah as yf

fl = FileLoader()

data = fl.load("../resources/athlete_events.csv")
yf(data, 2004)