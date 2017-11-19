import urllib.request
import os
videoArr = ['https://files3.lynda.com/secure/courses/604246/VBR_MP4h264_main_SD/604246_03_01_XR15_Creational_Design_patterns_The_Maze.mp4?PgAd7k-Y3YjpgJ5UUUstZyHqVHH80VRKmU0MYMim1lzaGlZ6ko9EJvS7IDZnYQQHOuv-UOHoqpgejSMzj86YxVuEKZigXRmHxXp6GKg4ehBL8KaqlSnVEN8LuwGzrSRKZeZtia8isxWCedZW9WrtVwxQdN-gI-UThZf6ArWNTJTwbiYNHdC9-xwfft_pLYDu3NrQ1cgKqiUNIpclfy6rDALu']
nameArr = ['Creational design patterns The maze labyrinth game']
for i in range(len(videoArr)):
    fullfilename = os.path.join('D:/python-video/Python Projects', nameArr[i])
    print(fullfilename)
    try:
        print("Downloading starts...\n")
        urllib.request.urlretrieve(videoArr[i], fullfilename)
        print("Download completed of "+nameArr[i]+" ..!!")
    except Exception as e:
        print(e)