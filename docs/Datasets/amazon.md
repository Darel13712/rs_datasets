# Amazon

This is ratings by category for [Amazon Review Data (2018)](https://nijianmo.github.io/amazon/index.html). 
You can download 5-core reviews from dataset site. Full reviews and metadata are available per request as well.

## Stats

Use `category` parameter to specify which category to download.

| Key                 | Ratings    |
| ------------------- | ---------- |
| fashion             | 883,636    |
| beauty              | 371,345    |
| appliances          | 602,777    |
| arts                | 2,875,917  |
| automotive          | 7,990,166  |
| books               | 51,311,621 |
| cds                 | 4,543,369  |
| phones              | 10,063,255 |
| clothing            | 32,292,099 |
| music               | 1,584,082  |
| electronics         | 20,994,353 |
| cards               | 147,194    |
| grocery             | 5,074,160  |
| kitchen             | 21,928,568 |
| scientific          | 1,758,333  |
| kindle              | 5,722,988  |
| luxury              | 574,628    |
| subscriptions       | 89,689     |
| movies              | 8,765,568  |
| musical instruments | 1,512,530  |
| office              | 5,581,313  |
| garden              | 5,236,058  |
| pet                 | 6,542,483  |
| pantry              | 471,614    |
| software            | 459,436    |
| sports              | 12,980,837 |
| tools               | 9,015,203  |
| toys                | 8,201,231  |
| game                | 2,565,349  |



## Example

```python
from rs_datasets import Amazon
amazon = Amazon('cards')
amazon.info()
```
```text
ratings
      user_id         item_id  rating
0  B001GXRQW0   APV13CM0919JD     1.0
1  B001GXRQW0  A3G8U1G1V082SN     5.0
2  B001GXRQW0   A11T2Q0EVTUWP     5.0
```