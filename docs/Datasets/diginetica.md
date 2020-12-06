# Diginetica

[Diginetica dataset](https://competitions.codalab.org/competitions/11161#learn_the_details-data2) 
for session-based recommendations in an e-commerce website.


## Stats
- 1,235,380 views
- 18,025 purchases
- 232,816 users
- 184,047 items


## Example

```python
from rs_datasets import Diginetica
d = Diginetica()
d.info()
```
```text
items
   item_id  log2price                      name_tokens
0        1         10  4875,776,56689,18212,18212,4896
1    69585          6      7583,18117,41805,41805,2371
2    90939          6       604,18117,41805,41805,2371

categories
   item_id  category_id
0   139578         1096
1   417975         1096
2   291805         1096

purchases
   session_id  user_id   timeframe        date  order_id  item_id
0         150  18278.0    17100868  2016-05-06     16421    25911
1         151      NaN     6454547  2016-05-06     16290   175874
2         156      7.0  1721689387  2016-05-27     21173    35324

views
   session_id  user_id  item_id  timeframe        date
0           1      NaN    81766     526309  2016-05-09
1           1      NaN    31331    1031018  2016-05-09
2           1      NaN    32118     243569  2016-05-09

queries
   query_id  session_id  user_id  timeframe  duration        date                           tokens  category_id                                              items  is_test
0         1           1      NaN   16327074       311  2016-05-09  16655,244087,51531,529597,58153            0  7518,71,30311,7837,30792,8252,81766,9338,62220...    False
1         2           2      NaN     705527       314  2016-05-09                    528941,529116            0  70095,15964,8627,134850,32754,100747,74771,314...    False
2         3           3      NaN          0       502  2016-05-09              133713,16655,138389            0  59081,51125,9338,9550,32087,62793,2717,10403,3...     True
```
