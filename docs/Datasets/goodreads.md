# Goodreads

This dataset is [user-book interactions](https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/shelves)
from Goodreads dataset.

You can find text reviews and additional data on dataset site.

## Stats 

- 876,145 users
- 2,360,650 books
- 228,648,342 interactions

## Extra parameters

- `read_maps=False`

    ids in interactions are encoded to save memory.
    You can read mappings, but there's no point
    if you don't use the rest of the dataset, which is not included here.

## Example

```python
from rs_datasets import Goodreads
goodreads = Goodreads(read_maps=True)
goodreads.info()
```
```text
ratings
   user_id  item_id  is_read  rating  is_reviewed
0        0      948     True       5        False
1        0      947     True       5         True
2        0      946     True       5        False

books
   book_id_csv   book_id
0            0  34684622
1            1  34536488
2            2  34017076

users
   user_id_csv                           user_id
0            0  8842281e1d1347389f2ab93d60773d4d
1            1  72fb0d0087d28c832f15776b0d936598
2            2  ab2923b738ea3082f5f3efcbbfacb218
```