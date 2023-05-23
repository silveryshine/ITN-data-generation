#!/bin/bash

# This script contains usage for customise search terms and transcription languages

stage=$1

# -------------------------------------------------------------------------------------------------------- #
#
# Here is the main use case:

if [ $stage -eq 1 ]; then
	
	echo Searching videos, filter by duration, then fetch audio and english transcription
 
	python youtube_crawler.py --search-terms singapore_covid19 cna_covid19 sg_cna_covid \
				--language en \
				--wav-dir covid_english/wav \
				--mp4-dir covid_english/mp4 \
				--transcripts-dir covid_english/transcripts \
				--min-duration 6000 \
				--num-pages 100 \
				--verbose \
				--to-wav
fi

# The above command will search youtube for the following:
#
# 		'singapore covid19', 'cna covid19' and 'sg cna covid'
# 
# Then it will pick videos with length greater than 6000s (1.4 hrs) in the first 100 pages of search results 
# The language id is set to 'en', i.e. english, so it will only check for presence of english transcriptions
# Then it will grab the transcripts+audio from youtube, save to the transcripts-dir and mp4-dir respectively
# Since 'to-wav' is set to true, the mp4 files will be converted to wav files
# Verbosity level is set to the highest
#
# -------------------------------------------------------------------------------------------------------- #



# -------------------------------------------------------------------------------------------------------- #
#
# Another example. Search indonesian news, filter duration of > 20mins, using first 5 pages of results, 
# fetch indonesian transcripts, but save as mp4 file, i.e. no conversion to wav

if [ ${stage} -eq 2 ]; then
	
	echo Searching indonesian news channels, then fetch audio and indoneisan transcription
 
	python youtube_crawler.py --search-terms tribunnews metrotvnews KOMPASTV detikcom \
				--language id \
				--mp4-dir news_indon/mp4 \
				--transcripts-dir news_indon/transcripts \
				--min-duration 1200 \
				--num-pages 5 \
				--verbose 
fi

# The default indonesian language id is 'id'. Since --to-wav is not set, no mp4 will be converted.
#
# -------------------------------------------------------------------------------------------------------- #



# -------------------------------------------------------------------------------------------------------- #
# 
# Another example, search by individual channels, use the --channel-only option. This will filter the results
# by channel first. The top 10 singaporean channels are avalaible in the file "sing_top10.txt"

if [ ${stage} -eq 3 ]; then 
	
	echo Searching individual channels, then fetch audio and transcription
 
	sg_youtubers=`less sing_top10.txt`
	for youtuber in ${sg_youtubers};
	do
		python youtube_crawler.py --search-terms ${youtuber} \
					--language en \
					--mp4-dir sg_top10/${youtuber}/mp4 \
					--wav-dir sg_top10/${youtuber}/wav \
					--transcripts-dir sg_top10/${youtuber}/transcripts \
					--min-duration 1200 \
					--num-pages 3 \
					--verbose \
					--to-wav \
					--channel-only
		
	done
fi

# The DISAVANTAGE of this option is that we require the EXACT matching string to search, otherwise the filter
# will fail to detect any video from the channel (Try WahBanana instead of Wah!Banana)
#
# -------------------------------------------------------------------------------------------------------- #



# -------------------------------------------------------------------------------------------------------- #
#
# Another example, crawl single chanel 'Eatbook' for MANUAL transcriptions. Use the --use-manual option to 
# specify the choice. In the example below, we search the first 10 results pages from the youtube channel
# 'Eatbook', filter videos greater than 2 mins and fetch the MANUALLY transcribed english text.

if [ ${stage} -eq 4 ]; then
	
	echo Crawling for MANUALLY transcribed wav files
# Dr wealth    chicken genius    jentan
  myYoutubers=("WhatTheFlak?!")  #"Jen Tan Property" "Chris @HoneyMoneySG" "Dr Wealth" "Chicken Genius Singapore" "Bluebird Bros" "WhatTheFlak?!"
  for myYoutuber in "${myYoutubers[@]}";
  do
     # YT-Transcripts\\crawler_youtube\\youtube_crawler.py --search-terms "$myYoutuber" \
    python youtube_crawler.py --search-terms "$myYoutuber" \
          --language en \
          --transcripts-dir "manual/transcripts/WhatTheFlak" \
          --mp4-dir "manual/mp4/WhatTheFlak" \
          --wav-dir "manual/wav/WhatTheFlak" \
          --min-duration 120 \
          --num-pages 10 \
          --to-wav \
          --verbose \
          --channel-only \
          --use-manual
#          --transcripts-dir "manual/transcripts/""$myYoutuber" \
#          --mp4-dir "manual/mp4/""$myYoutuber" \
#          --wav-dir "manual/wav/""$myYoutuber" \
  done
fi

sleep 10000



# -------------------------------------------------------------------------------------------------------- #



# -------------------------------------------------------------------------------------------------------- #
#
# Crawl radio data. Set the --sample-rate to 8000, default is at 16kHz. The youtube
# channel 'pdgls' is where the owner scans American skies for short wave radio chatter. For this example, 
# use the --audio-only option to crawl for ONLY AUDIO data, regardless the presence of transcripts

if [ ${stage} -eq 5 ]; then
	
	echo Crawling for RADIO wav files, without transcription
 
	python youtube_crawler.py --search-terms pdgls \
				--mp4-dir radio_8kHz/mp4 \
				--wav-dir radio_8kHz/wav \
				--min-duration 1200 \
				--num-pages 1 \
				--to-wav \
				--verbose \
				--sample-rate 8000 \
				--channel-only \
				--audio-only
fi

# -------------------------------------------------------------------------------------------------------- #
# Final Example, getting video ids only 
# use the --id-only option to crawl for ONLY video ids, regardless the presence of transcripts

if [ ${stage} -eq 6 ]; then
	
	echo Crawling for video ids, without transcription
 
	python youtube_crawler.py --search-terms 'Singapore covid news' \
				--language en \
				--ids-dir video_ids \
				--min-duration 120 \
				--num-pages 100 \
				--verbose \
				--id-only
fi

# -------------------------------------------------------------------------------------------------------- #

