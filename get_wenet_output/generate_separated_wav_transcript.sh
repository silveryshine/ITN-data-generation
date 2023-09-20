#!/bin/bash
# shellcheck disable=SC1012
python ./generate_separated_wav_transcript.py \
  -i "D:\study\singaporeMasters\master_project\term2\data\youtube_crawler\Chris@HoneyMoneySG\wav" \
  -t "D:\study\singaporeMasters\master_project\term2\data\youtube_crawler\Chris@HoneyMoneySG\segmented_text_with_times" \
  -o "D:\study\singaporeMasters\master_project\term2\data\youtube_crawler\Chris@HoneyMoneySG\segmented_wav"

sleep 20