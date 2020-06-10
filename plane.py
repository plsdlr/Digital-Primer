#import Fibel.drivers.drivers_base as drivers_base
import Fibel.drivers.it8951 as driver_it8951
from Fibel.input.gesture import gesture
from Fibel.input.fibelaudio import fibelaudio

# a minimal class initalising all drivers with parameters and providing a continuous interface
# at one point this might need to become a factory class  -> https://en.wikipedia.org/wiki/Factory_method_pattern

class plane:

    def __init__(self,busno_gesture,screen):
         self.screen_init = False
         self.gesture_init = False
         self.audio_init = False
         self.screen = screen
         self.busno_gesture = busno_gesture
         self.audiodriver = None
         self.screendriver = driver_it8951.IT8951()
         self.gesturedriver = None

    def initscreen(self):
        self.screendriver.init(screen=self.screen)
        self.screen_init = True

    def initaudio(self):
        self.audiodriver = fibelaudio()
        self.audio_init = True

    def initgesture(self):
        self.gesturedriver = gesturedriver(busno=busno,caseflag=1)
        self.gesture_init = True

    ##helperfunctions to return the class methods of the specifc drivers, these could be usefull for prototyping

    def returnmethods_audio(self):
        print(dir(self.audiodriver))

    def returnmethods_screen(self):
        print(dir(self.screendriver))

    def returnmethods_gesture(self):
        print(dir(self.gesturedriver))

if __name__ == "__main__":
    a = plane(3,"back")
    a.initscreen()
    a.initaudio()
    a.returnmethods_audio()
    a.audiodriver.run()
