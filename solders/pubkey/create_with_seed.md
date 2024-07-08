### solders.pubkey.Pubkey.create_with_seed
使用一个公钥，种子再加上程序公钥(program id)派生出一个公钥

```python
from solders.pubkey import Pubkey

demo_pubkey = Pubkey.from_string("EBziZDuZwJNSMx57fZFqgzXVLssWZSLMQzweVkGzRdVv")
print(demo_pubkey)  # EBziZDuZwJNSMx57fZFqgzXVLssWZSLMQzweVkGzRdVv type: Pubkey 
derived_pubkey = Pubkey.create_with_seed(demo_pubkey, "this is seed", Pubkey.from_string("1"*32))
print(derived_pubkey)  # 4XSrYFQG3BMVGqpWUuSmD4eQwmSCQ1ZwZpGQs3wWqNPo
```
