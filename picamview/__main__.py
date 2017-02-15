import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from picamera import PiCamera
from os import path

class Controller:
	def __init__(self):
		here = path.abspath(path.dirname(__file__))
		self.builder = Gtk.Builder()
		self.builder.add_from_file(path.join(here, 'mainwindow.glade'))
		self.window = self.builder.get_object('mainWindow')
		self.img = self.builder.get_object('capImg')
		self.btn = self.builder.get_object('capBtn')
		self.cam = PiCamera(resolution=(1280,720))
		
		self.window.connect('delete-event', Gtk.main_quit)
		self.btn.connect('clicked', self.capture)
		self.window.show_all()


	def capture(self, arg=''):
		self.cam.capture('/tmp/picamview-capture.png', 'png')
		self.img.set_from_file('/tmp/picamview-capture.png')

if __name__ == '__main__':
	c = Controller()
	c.capture()
	Gtk.main()