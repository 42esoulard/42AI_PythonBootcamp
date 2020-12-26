from FileLoader import FileLoader
from ProportionBySport import proportionBySport as pbs

fl = FileLoader()

data = fl.load("../resources/athlete_events.csv")
pbs(data, 2004, 'Tennis', 'F')