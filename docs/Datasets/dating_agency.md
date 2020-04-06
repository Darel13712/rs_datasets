# Dating Agency

[Dating Agency dataset](http://www.occamslab.com/petricek/data/) contains 1-10 ratings 
of profiles on a dating site.

- user_id is user who provided rating
- profile_id is user who has been rated
- not every profile has been rated
- ratings are on a 1-10 scale where 10 is best (integer ratings only)
- only users who provided at least 20 ratings were included
- users who provided constant ratings were excluded
- gender is denoted by a "M" for male and "F" for female and "U" for unknown

## Stats

- 135,359 users
- 168,791 profiles rated
- 17,359,346 ratings



## Example

```python
from rs_datasets import DatingAgency
da = DatingAgency()
da.info()
```
```text
ratings
   user_id  profile_id  rating
0        1         133       8
1        1         720       6
2        1         971      10

users
   user_id gender
0        1      F
1        2      F
2        3      U
```
