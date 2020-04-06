# Million Song Dataset

[Million Song Dataset](http://millionsongdataset.com/tasteprofile/) 
also known as Echo Nest Taste Profile Subset is a part of MSD, 
which contains play history of songs. 
Other datasets, such as preprocessed song features can be found at dataset site.

## Stats

- 1,019,318 unique users
- 384,546 unique songs
- 48,373,586 user-song-play count triplets

## Extra parameters

- `merge_kaggle_splits=True`

    In MSD Challenge on [Kaggle](https://www.kaggle.com/c/msdchallenge) there were 
    public and private parts. By default they are merged together.

- `drop_mismatches=True`

    There is a [matching error](http://millionsongdataset.com/blog/12-2-12-fixing-matching-errors/) 
    between track ids and song ids in MSD. It shouldn't matter if you don't use audio features, but 
    by default these items are removed.


!!! warning
    Dataset is quite big and loads for about 5 minutes first time,
    taking about 1.2GB RAM.
    If you use default recommended parameters, 
    processed data is saved to disk so that consequent loads take about 30 seconds.


## Example

```python
from rs_datasets import MillionSongDataset
msd = MillionSongDataset()
msd.info()
```
```text
train
                                    user_id             item_id  play_count
0  b80344d063b5ccb3212f76538f3d9e43d87dca9e  SOAKIMP12A8C130995           1
1  b80344d063b5ccb3212f76538f3d9e43d87dca9e  SOAPDEY12A81C210A9           1
2  b80344d063b5ccb3212f76538f3d9e43d87dca9e  SOBBMDR12A8C13253B           2

val
                                    user_id             item_id  play_count
0  0007140a3796e901f3190f12e9de6d7548d4ac4a  SONVMBN12AC9075271           1
1  0007140a3796e901f3190f12e9de6d7548d4ac4a  SOVIGZG12A6D4FB188           1
2  0007140a3796e901f3190f12e9de6d7548d4ac4a  SOZGXYF12AB0185579           2

test
                                    user_id             item_id  play_count
0  00007a02388c208ea7176479f6ae06f8224355b3  SOAITVD12A6D4F824B           3
1  00007a02388c208ea7176479f6ae06f8224355b3  SONZGLW12A6D4FBBC1           1
2  00007a02388c208ea7176479f6ae06f8224355b3  SOXNWYP12A6D4FBDC4           1
```