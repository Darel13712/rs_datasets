# Welcome to rs_datasets

![](https://img.shields.io/pypi/v/rs_datasets?color=%2300ccff)
![](https://img.shields.io/badge/datasets-16-00ccff)

This tool allows you download, unpack and read 
recommender systems datasets into `pandas.DataFrame` as easy as `data = Dataset()`.

## Installation

```
pip install rs_datasets
```

## Documentation
Please see [documentation](https://darel13712.github.io/rs_datasets/) to this project to 
see available datasets and examples of use.

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
