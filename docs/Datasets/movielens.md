# MovieLens

[MovieLens](https://grouplens.org/datasets/movielens/) is 
probably the most popular rs dataset out there.
Contains movie ratings from grouplens site.

Some versions provide addational information such as user info or tags.

## Versions

Following stable versions are available:

| Version | Size  | Ratings | Users | Movies | Tags |
| ------- | ----- | ------- | ----- | ------ | ---- |
| 25m     | 250MB | 25m     | 162k  | 62k    | 1m   |
| 20m     | 190MB | 20m     | 138k  | 27k    | 456k |
| 10m     | 63MB  | 10m     | 72k   | 10k    | 100k |
| 1m      | 6MB   | 1m      | 6k    | 4k     | —    |
| 100k    | 5MB   | 100k    | 1k    | 1.7k   | —    |

There are also 2 versions that change as time goes and are not recommended for research.
That is `latest` version which contains all the data they have for the moment (bigger than `25m`) and 
`small` which is just a subset of the `latest` version. `small` is loaded by default if you don't 
specify version.

## Extra parameters

- `version='small'`

    One of `{'100k', '1m', '10m', '20m', '25m', 'small', 'latest'}`
    
- `read_genome=False`

    whether to read genome tag dataset or not
    (available from version 20m and up).
    Are not loaded by default to save memory.

## Example 
```python
from rs_datasets import MovieLens
ml = MovieLens('10m')
ml.info()
```
```text
ratings
   user_id  item_id     rating  timestamp
0        1      122        5.0  838985046
1        1      185        5.0  838983525
2        1      231        5.0  838983392

items
   item_id                    title                                       genres
0        1         Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy
1        2           Jumanji (1995)                   Adventure|Children|Fantasy
2        3  Grumpier Old Men (1995)                               Comedy|Romance

tags
   user_id  item_id         tag   timestamp
0       15     4973  excellent!  1215184630
1       20     1747    politics  1188263867
2       20     1747      satire  1188263867
```