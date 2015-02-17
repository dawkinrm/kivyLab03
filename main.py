from kivy.app import App
from kivy.core.audio import SoundLoader

class HelloWorldApp (App):
	def play_music(self):
		self.sound = SoundLoader.load('Jesse_Cook-Dance_of_Spring.ogg')
		self.sound.play()

if __name__ == "__main__":
	HelloWorldApp().run()