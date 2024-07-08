## 安装

首先我们在本地开发，所以我们需要先安装solana节点。
```shell
sh -c "$(curl -sSfL https://release.solana.com/stable/install)"
```
安装完成后，我们可以通过 `solana --version` 查看是否安装成功。

```shell
solana --version
```

使用下面的命令启动一个本地的solana节点。如未能启动成功， 
请参考更多安装内容[官方文档](https://solana.com/developers/guides/getstarted/setup-local-development)。

```shell
solana-test-validator
```

接下来我们需要安装python的solana库，我们可以通过下面的命令安装。
```shell
pip install solana
pip install solders
pip install pybip39
```

## 概念

我们需要先清楚上面的 solana 库和 solders 库之间的关系和各自的职能，更有利于我们的学习和使用。

solana库可以理解为是对Solana区块链的***钱包应用***，它负责链上状态的查询和交易，如账户之间的转账交易，账户信息，余额，区块状态，交易费用等链上数据的查询。

而solders库可以理解为是***用户应用***。它主要负责用户对自己账户的管理，包括公钥(Pubkey)和密钥对(Keypair)的管理。如使用公钥生成其他账户，
例如 PDA, BPF 账户等，在 Solana 链上，可以直接把平时使用的地址当作公钥(在EVM上，其实还需要公钥通过 KECCAK-256 算法才得到地址)，在solders 库中的
Pubkey类其实就是对地址的封装。

为了更好地理解密钥对和公钥各自的职能和定位，我们需要知道钱包地址是怎么来的，钱包地址的生成过程如下：
1. 随机生成种子
2. 通过种子在二进制和BIP39助记词汇表的映射中转换成助记词
3. 助记词通过 HMAC-SHA256 算法生成私钥
4. 私钥通过椭圆曲线算法生成公钥

Solana的账户是将代码和数据分别存储在不同账户上的，所以分了多个账户：
- 数据账户，即管理你钱包资产的地址，主要用于存储程序的***状态***，不可执行，存储可变的数据，有对应的私钥。
- 程序账户，用于***存储程序***的账户，可执行，存储不可变的数据，有对应的私钥。我们只能通过这个执行程序账户的代码来查询或修改数据账户的数据。
- 程序派生账户(PDA)，即程序执行过程中存储的数据，这个账户由程序的program_id 和 seed 再加上一个数字(bump)派生而来，bump值由255依次递减，直到找到一个bump值派生出来的地址***不在椭圆曲线上***时，这个地址就是程序派生账户。
- 其他账户，如质押，投票等账户。

安装好上述库以及了解了账户概念后，我们就可以开始使用solana库和solders库来进行开发了。


