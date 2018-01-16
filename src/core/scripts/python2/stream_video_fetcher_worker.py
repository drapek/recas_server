import socket
import string

import cv2
import pickle
import struct

import numpy as np
import time
import sys
import random
import subprocess

PYTHON3_PROJECT_INTERPRETER = "/home/drapek/HDD/projects/python/recas/recas_server/env/bin/python"


class VideoStreamFetcher:
    """
    This class will work only on python2.7 because of modules it is using.
    """
    FETCH_FRAME_MAX_TIRES = 500
    FRAME_WIDTH = 640
    FRAME_HEIGHT = 480

    def __init__(self, verbose=False, port=8089, camera_name='', online_tmp_jpg_localization='',  video_folder=''):
        self.port = port
        self.video_folder = video_folder
        self.camera_name = camera_name
        self.online_preview_jpg_localization = online_tmp_jpg_localization
        self.verbose = verbose
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('0.0.0.0', self.port))
        self.payload_size = struct.calcsize("q")

    def run(self):
        while True:
            now = time.time() + 3600  # add one hour because it is returning UTC time.
            random_characters = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
            # mp4 because it is converted later on this format
            video_name = "{}_{}.mp4".format(int(now), random_characters)
            tmp_video_avi_name = "{}_tmp.avi".format(int(now))
            video_writer = cv2.VideoWriter("{}/{}".format(self.video_folder, tmp_video_avi_name),
                                           cv2.VideoWriter_fourcc(*'MJPG'), 9.0,
                                           (self.FRAME_WIDTH, self.FRAME_HEIGHT))
            self.socket.listen(10)
            conn, addr = self.socket.accept()
            if self.verbose:
                print('Connection established. Socket is now listening on {}:{}'.format('0.0.0.0', self.port))

            data = b''
            while True:

                tries = 0
                video_stream_ended = False
                while len(data) < self.payload_size:
                    if tries > self.FETCH_FRAME_MAX_TIRES:
                        video_stream_ended = True
                        break
                    if self.verbose:
                        print("Tries: {}".format(tries))
                    tries += 1
                    data += conn.recv(1024)

                if video_stream_ended:
                    if self.verbose:
                        print("Stream ended")
                    break

                packed_msg_size = data[:self.payload_size]
                data = data[self.payload_size:]
                msg_size = struct.unpack("q", packed_msg_size)[0]

                tries = 0
                video_stream_ended = False
                while len(data) < msg_size:
                    if tries > self.FETCH_FRAME_MAX_TIRES:
                        video_stream_ended = True
                        break
                    if self.verbose:
                        print("Tries: {}".format(tries))
                    tries += 1
                    data += conn.recv(1024)

                if video_stream_ended:
                    if self.verbose:
                        print("Stream ended")
                    break

                frame_data = data[:msg_size]
                data = data[msg_size:]
                if self.verbose:
                    print("[LOG] Frame received")
                frame = np.fromstring(pickle.loads(frame_data), np.uint8)
                img_np = cv2.imdecode(frame, cv2.IMREAD_COLOR)
                cv2.imwrite(self.online_preview_jpg_localization, img_np)
                video_writer.write(img_np)

            video_writer.release()
            # This should be python3 - the same as django server is running
            subprocess.call(["core/scripts/convert_to_mp4.sh", self.video_folder, tmp_video_avi_name, video_name])
            subprocess.call([PYTHON3_PROJECT_INTERPRETER, "core/scripts/python3/add_video_to_system.py",
                             self.camera_name, video_name, str(int(now))])
            if self.verbose:
                print("Video {} saved".format(video_name))
            cv2.destroyAllWindows()


if __name__ == '__main__':
    # get the args
    print("Starting ReCaS server in development mode")
    VideoStreamFetcher(verbose=False, camera_name=sys.argv[1], port=int(sys.argv[2]),
                       online_tmp_jpg_localization=sys.argv[3],
                       video_folder=sys.argv[4]).run()
