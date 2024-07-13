### solana.rpc.api.Client.get_identity
# 获取当前节点的公钥信息，与上面的get_genesis_hash方法类似，也可以在运行本地节点的终端界面上看到。


from solana.rpc.api import Client

client = Client("http://localhost:8899")
identity = client.get_identity()
print(identity)
# GetIdentityResp(RpcIdentity(RpcIdentity { identity: "CnMdLhM1hH6nT8ekAQsLgZ9vigphriWiLbyHTkXnMc8B" }))
print(identity.value.identity)
# CnMdLhM1hH6nT8ekAQsLgZ9vigphriWiLbyHTkXnMc8B

