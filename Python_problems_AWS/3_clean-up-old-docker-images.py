"""
We will clean up old docker images on a server to free up space using python
We will use Docker SDK for python (import docker) to manage docker and containers

docker.from_env() - creates a docker client instace using default docker env settings
(local docker daemon)

client.images.list(filters={'dangling': True}) - list docker images with dangling filter. 
This will list docker images which are unused. 

client.images.remove(image.id) - removes each docker image identified by image ID. 
"""

import docker 

client = docker.from_env() # Create docker client instance

def remove_image():
    images = client.images.list(filters={'dangling': True})
    for images in images:
        client.images.remove(image.id) # Remove docker image
        print (f"Removed image: {image.id}")
    
remove_image()