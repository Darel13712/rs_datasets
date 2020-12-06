# YooChoose

[YooChoose dataset](https://2015.recsyschallenge.com/challenge.html). 


## Stats
- 33,003,944 clicks
- 9,249,729 sessions
- 1,150,753 purchases
- 52,739 items


## Example

```python
from rs_datasets import YooChoose
yc = YooChoose()
yc.info()
```
```text
log
   session_id                        ts    item_id category
0           1  2014-04-07T10:51:09.277Z  214536502    False
1           1  2014-04-07T10:54:09.868Z  214536500    False
2           1  2014-04-07T10:54:46.998Z  214536506    False

purchases
   session_id                        ts    item_id  price  quantity
0      420374  2014-04-06T18:44:58.314Z  214537888  12462         1
1      420374  2014-04-06T18:44:58.325Z  214537850  10471         1
2      281626  2014-04-06T09:40:13.032Z  214535653   1883         1

test
   session_id                        ts    item_id category
0           5  2014-04-07T17:13:46.713Z  214530776    False
1           5  2014-04-07T17:20:56.973Z  214530776    False
2           5  2014-04-07T17:21:19.602Z  214530776    False
```
