import numpy as np
import airsim
import os
import cv2


client = airsim.MultirotorClient()
client.confirmConnection()

#response = client.simGetImage('0', airsim.ImageType.Scene)
responses = client.simGetImages([airsim.ImageRequest('0', airsim.ImageType.Scene, False, False)])

if responses:
    response = responses[0]
    img_1D = np.frombuffer(response.image_data_uint8, dtype=np.uint8).reshape(response.height, response.width, 3)
    cv2.imwrite('image.png', img_1D)
    print('Image saved.')
else:
    print('No images found.')

# Set up the AirSim environment


# Connect to the AirSim simulator
