# Epinions

[Epinions dataset](http://www.trustlet.org/downloaded_epinions.html) 
contains item ratings and trust statements between users.

There are no distrust statements in the dataset (block list)
but only trust statements (web of trust),
because the block list is kept private and not shown on the site.

## Stats

- 49,290 users who rated a total of
- 139,738 different items at least once, writing
- 664,824 reviews and
- 487,181 issued trust statements.

## Example

```python
from rs_datasets import Epinions
epinions = Epinions()
epinions.info()
```
```text
ratings
   user_id  item_id  rating
0        1      100       4
1        1      101       5
2        1      102       3

trust
   source_user_id  target_user_id  trust_value
0           22605           42915         True
1           22605            5052         True
2           22605           42913         True
```

