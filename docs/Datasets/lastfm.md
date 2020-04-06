# Last.fm

[Last.fm-360k](http://ocelma.net/MusicRecommendationDataset/lastfm-360K.html) 
contains `(user, artist, play count)` triplets collected with Last.fm API,
using `user.getTopArtists()` method.

## Stats

- 359,347 unique users
- 186,642 artists with MBID
- 107,373 artists without MBDID
- 17,559,530 total rows

## Example
```python
from rs_datasets import Lastfm
lastfm = Lastfm()
lastfm.info()
```
```text
play_counts
                                    user_id                             artist_id        artist_name  play_count
0  00000c289a1829a808ac09c00daf10bc3c4e223b  3bd73256-3905-4f3a-97e2-8b341527f805    betty blowtorch        2137
1  00000c289a1829a808ac09c00daf10bc3c4e223b  f2fb0ff0-5679-42ec-a55c-15109ce6e320          die Ärzte        1099
2  00000c289a1829a808ac09c00daf10bc3c4e223b  b3ae82c2-e60b-4551-a76d-6620f1b456aa  melissa etheridge         897

users
                                    user_id gender   age  country  signup_date
0  00000c289a1829a808ac09c00daf10bc3c4e223b      f  22.0  Germany  Feb 1, 2007
1  00001411dc427966b17297bf4d69e7e193135d89      f   NaN   Canada  Dec 4, 2007
2  00004d2ac9316e22dc007ab2243d6fcb239e707d          NaN  Germany  Sep 1, 2006
```