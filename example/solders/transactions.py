### 转账
# 发送方使用密钥对，接收方使用地址，转账的单位是lamport，1 SOL = 10^9 lamport。
# 最后返回的hash值可以在solana的区块浏览器(https://solscan.io/?cluster=custom&customUrl=http://127.0.0.1:8899)上查看交易的详情。


from solders.system_program import TransferParams, transfer
from solana.transaction import Transaction
from solana.rpc.api import Client
from solders.pubkey import Pubkey
from solders.keypair import Keypair
from pybip39 import Mnemonic


client = Client("http://localhost:8899")
amount = 88  # 单位为SOL
lamports = int(amount * 10 ** 9)  # 转账的单位是lamport
mnemonic = Mnemonic().phrase
# 发送方需要授权，所以发送方需要通过助记词生成密钥对
sender_keypair = Keypair.from_seed_phrase_and_passphrase(mnemonic, "")
# 接收方的话就只需要一个地址就好了，这和我们在转账是一样的
receiver_pubkey = Pubkey.from_string("EhvvSB8xy44SmE3LE5Y1Jv3W98GQ8JFJfYv1ZUinzULQ")
transfer_params = TransferParams(
    from_pubkey=sender_keypair.pubkey(),
    to_pubkey=receiver_pubkey,
    lamports=lamports
)
txn = Transaction().add(transfer(transfer_params))
trans_hash = client.send_transaction(txn, sender_keypair).value
print(trans_hash)  # 交易的hash值，可以在solana的区块浏览器上查看交易的详情


### 生成包含特定字符串的地址
# 其实原理就是不断生成助记词，然后获取地址，直到地址的某一部分是你想要的字符串为止。生成难度根据字符串的长度而定。


from pybip39 import Mnemonic
from solders.keypair import Keypair

mnemonic = Mnemonic().phrase
pubkey = Keypair.from_seed_phrase_and_passphrase(mnemonic, "").pubkey()
while str(pubkey)[:3] != "sol":
    mnemonic = Mnemonic().phrase
    pubkey = Keypair.from_seed_phrase_and_passphrase(mnemonic, "").pubkey()
print(mnemonic)
print(pubkey)


