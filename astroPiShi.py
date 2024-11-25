#Opdracht 1 van regel 1-32
from orbit import ISS
#from picamera import PiCamera
from exif import Image
from datetime import datetime

#Set up camera
#cam = PiCamera()
#cam.resolution = (4056, 3040)

image_01 = 'photo_0674.jpg'
image_02 = 'photo_0675.jpg'
image_03 = 'photo_0676.jpg'

def getTime(image):
    with open(image, 'rb') as image_file:
        Img = Image(image_file)
        time_str = Img.get('datetime_original')
        time = datetime.strptime(time_str, '%Y:%m:%d %H:%M:%S')
    return time

def getLocation(image):
    with open(image, 'rb') as image_file:
        Img = Image(image_file)
        latitude = Img.get('gps_latitude')
        longitude = Img.get('gps_longitude')
    return latitude, longitude

time_01 = getTime(image_01)
time_02 = getTime(image_02)

#Opdracht 2 van regel 32-39 vvv (time wordt van getTime() functie gebruikt)
def timeDiff(time1, time2):
    totalTimeDiff = (time2 - time1).total_seconds()
    return "Time diff in secs:", totalTimeDiff



#Geen opdracht 3 want foto's worden niet gevisualiseerd
#Opdracht 4 van regel 40-46 (locatie wordt van getLocation() functie gebruikt, niet 100% correct)
def conversionPixelsToKm(meanDistancePixels, GSD):
    distanceInMetres = meanDistancePixels * GSD
    distanceInKilometres = distanceInMetres / 1000
    return distanceInKilometres

#Opdracht 5 van regel 46-51 (snelheid kan je correct uitrekenen als locatie een offset heeft)
def calculateSpeedInKmph(distanceInKilometers, timeDifference):
    return distanceInKilometers / timeDifference
    
print(getLocation(image_01))
print(timeDiff(time_01, time_02))