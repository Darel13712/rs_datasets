# Welcome to rs_datasets

This tool allows you download, unpack and read 
recommender systems datasets into `pandas.DataFrame` as easy as `data = Dataset()`.

## Installation
```
pip install rs_datasets
```

## Available datasets

The following datasets are available for automatic download and 
can be retrieved with this package.

!!! note 
    Check dataset license to know available usecases. 
    Authors of this package are not affiliated with dataset contents in any way.

|                  Dataset                   | Users | Items | Interactions |
| :----------------------------------------: | :---: | :---: | :----------: |
|     [Movielens](Datasets/movielens.md)     | 162k  |  62k  |  up to 25m   |
|  [Million Song Dataset](Datasets/msd.md)   |  1m   | 385k  |     48m      |
|       [Netflix](Datasets/netflix.md)         | 480k  | 17.7k |     100m     |
|     [Goodreads](Datasets/goodreads.md)     | 800k  | 1.5m  |     225m     |
|       [Last.fm](Datasets/lastfm.md)        | 360k  | 290k  |    17.5m     |
|      [Epinions](Datasets/epinions.md)      |  49k  | 140k  |     660k     |
|     [Book Crossing](Datasets/bookx.md)     | 279k  | 271k  |     1.1m     |
|        [Jester](Datasets/jester.md)        |  73k  |  100  |     4.1m     |
|        [Amazon](Datasets/amazon.md)        | ?[^*] | ?[^*] |  up to 32m   |
|        [Rekko](Datasets/rekko.md)          | 100k, 500k |  8k   |  500k, 9.6m  |
|        [Steam](Datasets/steam.md)          |    12k     |  5k   |     200k     |
|        [Anime](Datasets/anime.md)          |    73k     |  11k  |     7.8m     |
| [Retail Rocket](Datasets/retail_rocket.md) |    1.4m    | 235k  |     2.7m     |
|     [YooChoose](Datasets/yoochoose.md)     |     9m     |  52k  |   33m, 1m    |
|    [Diginetica](Datasets/diginetica.md)    |    232k    | 184k  |  1.2m, 18k   | 




[^*]: Their download speed is extremely slow and I wasn't patient enough to download the biggest one to check this.


    


## Example of use

```python
from rs_datasets import MovieLens
ml = MovieLens()
ml.info()
```
```text
ratings
   user_id  item_id  rating  timestamp
0        1        1     4.0  964982703
1        1        3     4.0  964981247
2        1        6     4.0  964982224
items
   item_id  ...                                       genres
0        1  ...  Adventure|Animation|Children|Comedy|Fantasy
1        2  ...                   Adventure|Children|Fantasy
2        3  ...                               Comedy|Romance
[3 rows x 3 columns]
tags
   user_id  item_id              tag   timestamp
0        2    60756            funny  1445714994
1        2    60756  Highly quotable  1445714996
2        2    60756     will ferrell  1445714992
links
   item_id  imdb_id  tmdb_id
0        1   114709    862.0
1        2   113497   8844.0
2        3   113228  15602.0
```
Loaded DataFrames are available as class attributes.
