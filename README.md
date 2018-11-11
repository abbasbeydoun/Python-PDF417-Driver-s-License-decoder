# Python-PDF417-Driver-s-License-decoder
This is a quick script to decode PDF417 driver's license data (The type of barcode used on most US and Canada Driver's licenses).

This assumes you already have a scanner connected to your computer that can scan PDF417 codes. Just create a txt file and name it
'dlstring.txt' in the same directory as the 'decoder.py' script. While the txt file is open, Scan the barcode. The encoded data should be pasted into the txt file.

now just run the script with the command "python decoder.py" and it will output the data to a file called 'dlstringdecoded.txt'
