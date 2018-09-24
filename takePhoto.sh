#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 1280x720 photos/$DATE.jpg

scp photos/$DATE.jpg takagisr@takagisr-debian1.wlan.rose-hulman.edu:/home/takagisr/dc2018/photos