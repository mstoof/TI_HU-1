from apa102_pi.driver import apa102

strip = apa102.APA102(num_led=150, order='rgb')

strip.clear_strip()
strip.set_pixel_rgb(1, 0xFF0000) #Red
strip.set_pixel_rgb(2, 0x00FF00) #Green
strip.set_pixel_rgb(3, 0x00FF00) #Green
strip.set_pixel_rgb(4, 0x0000FF) #Blue
strip.set_pixel_rgb(5, 0x0000FF) #Blue
strip.set_pixel_rgb(6, 0x0000FF) #Blue

strip.show()
strip.cleanup()

