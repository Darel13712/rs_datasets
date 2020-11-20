# Steam

[Steam Video Games dataset](https://www.kaggle.com/tamber/steam-video-games/data). 

!!! note
    You have to [configure](https://github.com/Kaggle/kaggle-api#:~:text=API%20credentials,file%20containing%20your%20API%20credentials.) 
    kaggle api token for auto download.

## Stats
- 200,000 transactions
- 12,393 users
- 5155 games

## Example

```python
from rs_datasets import Steam
steam = Steam()
steam.info()
```
```text
data
     user_id                        game  behavior  value
0  151603712  The Elder Scrolls V Skyrim  purchase    1.0
1  151603712  The Elder Scrolls V Skyrim      play  273.0
2  151603712                   Fallout 4  purchase    1.0
```
