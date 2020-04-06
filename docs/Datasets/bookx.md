# Book-Crossing

[Book-crossing dataset](http://www2.informatik.uni-freiburg.de/~cziegler/BX/) 
contains user ratings of books on a scale from 1 to 10.
Books have extra information and links to covers.
Users have age and location features. item_ids are actual book ISBNs.

## Stats

- 278,858 users
- 271,379 items
- 1,149,780 ratings

## Example

```python
from rs_datasets import BookCrossing
bx = BookCrossing()
bx.info()
```
```text
ratings
   user_id     item_id  rating
0   276725  034545104X       0
1   276726  0155061224       5
2   276727  0446520802       0

items
      item_id                 title                author  year                publisher       img_s       img_m       img_l
0  0195153448   Classical Mythology    Mark P. O. Morford  2002  Oxford University Press  http://...  http://...  http://...
1  0002005018          Clara Callan  Richard Bruce Wright  2001    HarperFlamingo Canada  http://...  http://...  http://...
2  0060973129  Decision in Normandy          Carlo D'Este  1991          HarperPerennial  http://...  http://...  http://...

users
   user_id                         location   age
0        1               nyc, new york, usa   NaN
1        2        stockton, california, usa  18.0
2        3  moscow, yukon territory, russia   NaN
```

