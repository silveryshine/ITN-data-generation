# ITN-data-generation

[//]: # (generate ITN dataset)

This is the repo for ""

To run the project, first go into directory crawl_youtube and run youtube_crawler.sh with option 7. Note to change the saving directory and youtuber's name.

Second, go to get_wenet_output to and run gen_transcript_analyse_save.sh. The descriptions are in the execution file.

Last, go to use utils.py to generate paired training data and train Cross-Align. Also use utils.py to transform Cross-align's output.