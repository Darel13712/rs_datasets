# Anime

[Anime Recommendations Database](https://www.kaggle.com/CooperUnion/anime-recommendations-database). 

!!! note
    You have to [configure](https://github.com/Kaggle/kaggle-api#:~:text=API%20credentials,file%20containing%20your%20API%20credentials.) 
    kaggle api token for auto download.

## Stats
- 7,813,737 ratings
- 73,515 users
- 11,200 anime titles

## Example

```python
from rs_datasets import Anime
anime = Anime()
anime.info()
```
```text
ratings
   user_id  item_id  rating
0        1       20      -1
1        1       24      -1
2        1       79      -1

titles
   item_id                              name                                              genre   type  episodes  rating  members
0    32281                    Kimi no Na wa.               Drama, Romance, School, Supernatural  Movie         1    9.37   200630
1     5114  Fullmetal Alchemist: Brotherhood  Action, Adventure, Drama, Fantasy, Magic, Mili...     TV        64    9.26   793665
2    28977                          Gintama°  Action, Comedy, Historical, Parody, Samurai, S...     TV        51    9.25   114262

```
