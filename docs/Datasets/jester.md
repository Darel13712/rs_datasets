# Jester

[Jokes dataset](http://eigentaste.berkeley.edu/dataset/) 
consists of several datasets which contain joke ratings in
real values ranging from -10.00 to +10.00.

Texts of jokes are available too.

## Stats
### Dataset 1

- 73,421 users
- 100 jokes
- collected between April 1999 - May 2003

### Dataset 3

- 54,905 users
- 150 jokes( 50 not in Dataset 1)
- collected from November 2006 - Mar 2015
- 22 jokes have few ratings as they were removed as of May 2009
    deemed to be out of date (eg, Bill Clinton jokes;)
    their ids are: {1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 14, 20,
    27, 31, 43, 51, 52, 61, 73, 80, 100, 116}.
- As of May 2009, the jokes {7, 8, 13, 15, 16, 17, 18, 19} are the "gauge set"
    (as discussed in the Eigentaste paper)
    and the jokes {1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 14, 20, 27, 31, 43,
    51, 52, 61, 73, 80, 100, 116} were removed
    (i.e. they are never displayed or rated).

### Dataset 4

- 7699 users
- 158 jokes
- 22 of the jokes don't have ratings, their ids are:
    {1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 14, 20, 27, 31,
    43, 51, 52, 61, 73, 80, 100, 116}.
- The jokes {1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 14, 20,
    27, 31, 43, 51, 52, 61, 73, 80, 100, 116} have been removed
    (i.e. they are never displayed or rated).
    
## Extra parameters

- `dataset=1` 
    
    one of 1, 3, 4 to choose corresponding version.

## Structure

Dataset 1 consists of 3 matrices as provided, they are not merged together.

Ratings are in a form of matrix with columns representing jokes. 
In original data 99 meant "no rating" it is replaced to `NaN` here.

```text
data
    1     2     3   ...
0 -7.82  8.79 -9.66 ...
1  4.08 -0.29  6.36 ...
2   NaN   NaN   NaN ...
... ...   ...   ... ...
```

Joke texts are available as `Pandas.Series`

```text
jokes
1    A man visits the doctor. The doctor says "I ha...
2    This couple had an excellent relationship goin...
3    Q. What's 200 feet long and has 4 teeth?   A. ...
```