import urllib.request
import os

# Free aesthetic dessert/coffee vertical videos
url1 = "https://player.vimeo.com/external/498764065.sd.mp4?s=d00bb61906a5b7d9c6d32839bdf11f2a33f44605&profile_id=165&oauth2_token_id=57447761"
url2 = "https://player.vimeo.com/external/459389137.sd.mp4?s=86eb29db809f6ab41e8c460cc512bc0b7316fc1f&profile_id=165&oauth2_token_id=57447761"

print("Downloading reel1.mp4...")
urllib.request.urlretrieve(url1, "reel1.mp4")

print("Downloading reel2.mp4...")
urllib.request.urlretrieve(url2, "reel2.mp4")

print("Done!")
