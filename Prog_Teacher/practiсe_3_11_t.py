import airsim

import os
import cv2
import numpy as np

client = airsim.MultirotorClient()
client.confirmConnection()

# response = client.simGetImage("0", airsim.ImageType.Scene)
responses = client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.Scene, False, False)])

if responses:
    response = responses[0]

    img_1D = np.frombuffer(response.image_data_uint8, dtype=np.uint8)
    img_rgb = img_1D.reshape(response.height, response.width, 3)

    cv2.imwrite('test.jpg', img_rgb)
    print("Image saved")
else:
    print("No images found")
