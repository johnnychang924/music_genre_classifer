# Music genre classifier
## Description
This is a tool for recognizing music genres, which can help users filter the songs they like or dislike.
## How to use
1. Use playList_downloader.py to collect music as training data and place each music file in its corresponding genre folder.
2. Use mp4_To_mp3.py to transfer the video into mp3 file.
3. Use data_transfer.py to calculate the mfcc of the training data.
4. Use KNN_music_classifier.py to predict the song you want to filter.