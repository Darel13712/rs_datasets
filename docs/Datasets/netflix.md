# Netflix

Classic dataset from the famous [Netflix Prize](https://www.kaggle.com/netflix-inc/netflix-prize-data) 
which took place 2006-2009. 

No ratings are available for testing data.


## Stats
- 480,189 users
- 17,770 movies
- 100m ratings on the scale from 1 to 5


## Example

```python
from rs_datasets import Netflix
netflix = Netflix()
netflix.info()
```
```text
movies
   item_id    year                       title
0        1  2003.0             Dinosaur Planet
1        2  2004.0  Isle of Man TT 2004 Review
2        3  1997.0                   Character

test
  item_id  user_id  timestamp
0       1  1046323 2005-12-19
1       1  1080030 2005-12-23
2       1  1830096 2005-03-14

train
   item_id  user_id  rating  timestamp
0      373   643460       4 2005-01-26
1      373   349399       5 2002-11-06
2      373  1315469       2 2005-08-15
```

!!! warning
    It is not recommended to read data without wrapper (`df = pd.read_parquet`)
    when using PyCharm scientific mode.
    PyCharm tries to load all 100m rows to show DataFrame info,
    which causes huge memory consumption and freezes.
    When loading with a wrapper (as in using this class) it doesn't 
    load that until you specifically try to show it.