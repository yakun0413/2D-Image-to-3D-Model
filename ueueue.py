import ids
cam = ids.Camera()
cam.color_mode = ids.ids_core.COLOR_RGB8    # Get images in RGB format
cam.exposure = 5                            # Set initial exposure to 5ms
cam.auto_exposure = True
cam.continuous_capture = True               # Start image capture

img, meta = cam.next()                      # Get image as a Numpy array

from PIL import Image
pil_img = Image.fromarray(img)
pil_img.save("pil.jpg", quality=95)
