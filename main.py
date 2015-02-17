from kivy.app import App
from kivy.core.audio import SoundLoader

class HelloWorldApp (App):
	stopped = True
	def play_music(self):
		if HelloWorldApp.stopped is True:
			self.sound = SoundLoader.load('Jesse_Cook-Dance_of_Spring.ogg')
			self.sound.play()
			HelloWorldApp.stopped = False
	
	def stop_music(self):
		self.sound.stop()
		HelloWorldApp.stopped = True
	
	def volume_change(self, volume):
		if self.sound.state is 'play' or self.sound.state is 'stop':
			self.sound.volume = volume

if __name__ == "__main__":
	HelloWorldApp().run()