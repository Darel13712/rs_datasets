# Rekko

Movie data from [Rekko Challenge](https://boosters.pro/championship/rekko_challenge/data). 

No ratings available for test data.

## Stats
- 9,643,012 transactions
- 438,790 ratings 0 to 10
- 499,663 users with transactions
- 104,563 users with ratings
- 8296 movies

## Example

```python
from rs_datasets import Rekko
rekko = Rekko()
rekko.info()
```
```text
transactions
   item_id  user_id consumption_mode            ts  watched_time  device_type  device_manufacturer
0     3336     5177                S  4.430518e+07          4282            0                   50
1      481   593316                S  4.430518e+07          2989            0                   11
2     4128   262355                S  4.430518e+07           833            0                   50

ratings
   user_id  item_id  rating            ts
0   571252     1364      10  4.430517e+07
1    63140     3037      10  4.430514e+07
2   443817     4363       8  4.430514e+07

bookmarks
   user_id  item_id            ts
0   301135     7185  4.430516e+07
1   301135     4083  4.430516e+07
2   301135    10158  4.430516e+07
```
Additional info available in `json` catalogue:
```python
rekko.catalogue['8432']
```
```json
{'type': 'movie',
 'availability': ['purchase', 'rent', 'subscription'],
 'duration': 100,
 'feature_1': 9059050.751458582,
 'feature_2': 0.7044612684,
 'feature_3': 7,
 'feature_4': 1.1212215513,
 'feature_5': 0.5927161087,
 'attributes': [14658,
  27695,
  27696,
  3713,
  2025,
  7,
  13953,
  10,
  42,
  14,
  15,
  239,
  20,
  21,
  13954,
  197]}
```