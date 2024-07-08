### solders.pubkey.Pubkey.is_on_curve
判断公钥是否在椭圆曲线上，在椭圆曲线上的公钥都有其对应的私钥。

```python
from solders.pubkey import Pubkey
demo_pubkey = Pubkey.from_string("EBziZDuZwJNSMx57fZFqgzXVLssWZSLMQzweVkGzRdVv")
result = Pubkey.is_on_curve(demo_pubkey)
print(result)  # True
```
