from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from rlottie_python import LottieAnimation

class LottieAnimationApp(App):
    def build(self):
        # Load the Lottie animation from a JSON file
        self.animation = LottieAnimation.from_file('account.json')

        # Get the total number of frames in the animation
        self.total_frames = self.animation.lottie_animation_get_totalframe()

        # Set the initial frame number
        self.frame_num = 0

        # Create an Image widget to display the animation frames
        self.image = Image()

        # Schedule the update function to be called every frame
        Clock.schedule_interval(self.update, 1.0 / self.animation.lottie_animation_get_framerate())

        return self.image

    def update(self, dt):
        # Render the current frame of the animation
        frame_buffer = self.animation.lottie_animation_render(frame_num=self.frame_num)

        # Flip the frame vertically
        flipped_frame_buffer = self._flip_vertical(frame_buffer)

        # Convert the frame buffer to an image and set it in the Image widget
        self.image.texture = self._buffer_to_texture(flipped_frame_buffer)

        # Increment the frame number for the next update
        self.frame_num += 1
        if self.frame_num >= self.total_frames:
            self.frame_num = 0

    def _flip_vertical(self, buffer):
        # Flip the buffer vertically
        width, height = self.animation.lottie_animation_get_size()
        flipped_buffer = bytearray()

        for y in range(height - 1, -1, -1):
            row = buffer[y * width * 4 : (y + 1) * width * 4]
            flipped_buffer.extend(row)

        return flipped_buffer

    def _buffer_to_texture(self, buffer):
        # Convert the frame buffer to a Kivy texture
        from kivy.graphics.texture import Texture
        texture = Texture.create(size=(self.animation.lottie_animation_get_size()), colorfmt='rgba')
        texture.blit_buffer(buffer, colorfmt='bgra', bufferfmt='ubyte')

        return texture

if __name__ == '__main__':
    LottieAnimationApp().run()
