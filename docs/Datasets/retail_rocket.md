# Retail Rocket

[Retail Rocket Dataset](https://www.kaggle.com/retailrocket/ecommerce-dataset). 

!!! note
    You have to [configure](https://github.com/Kaggle/kaggle-api#:~:text=API%20credentials,file%20containing%20your%20API%20credentials.) 
    kaggle api token for auto download.

## Stats
- 2,756,101 transactions
- 1,407,580 users
- 235,061 items

## Example

```python
from rs_datasets import RetailRocket
rr = RetailRocket()
rr.info()
```
```text
category_tree
   category_id  parent_id
0         1016      213.0
1          809      169.0
2          570        9.0

log
              ts  user_id event  item_id  transaction_id
0  1433221332117   257597  view   355908             NaN
1  1433224214164   992329  view   248676             NaN
2  1433221999827   111016  view   318965             NaN

items
              ts  item_id    property                            value
0  1435460400000   460429  categoryid                             1338
1  1441508400000   206783         888          1116713 960601 n277.200
2  1439089200000   395014         400  n552.000 639502 n720.000 424566
```
