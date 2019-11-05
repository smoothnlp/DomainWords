# SmoothNLP在复旦新闻语料上的领域词发现


>本项目使用**SmoothNLP**中的`extract_phrase`函数，从不同领域的文本中抽取**领域专有词汇**，并进行结果展示。


## 复旦大学新闻语料库 - 数据介绍
本实验采用的数据来源于**复旦大学计算机信息与技术系国际数据库中心的复旦文本语料库**,包括`经济`、`计算机`、`环境`、`体育`、`艺术`、`农业`、`政治`、`历史`、`宇航`、`教育`、`法律`、`哲学`、`军事`、`文学`、`交通`、`医疗`、`矿业`、`能源`、`电子`、`通信`共20个领域的文本。  


* 经济领域文本示例：  
>【 标  题 】利息所得税：启动经济的新尝试  
【 作  者 】李奎  
【 正  文 】  
    经国务院批准，《对储蓄存款利息所得征收个人所得税的实施办法》于近日颁布，并将于1999年11月1日起实施，适用20%的比例税率。这表明，根据我国国民经济总量结构和国民收入结构的重大变化，1958年取消的《个人所得税法》免征的利息所得税即将重新征收。  
    征收利息所得税将有效刺激消费品需求的增加，扩大社会总需求，带动经济增长，并将转变居民的投资观念和消费观念。  
    第一，在扩大内需方面，征收利息所得税将比降息更加有效。储蓄存款利率下降与社会消费品增长有一定的相关关系：利率下降1个百分点，市场商品销售将增加1.8个百分点。但是1996年5月以来的7次降息实践表明，降息对扩大内需、增加社会投资的作用越来越弱。其主要原因在于：首先，目前不仅城乡居民的即期收入上不去，而且对未来的预期收入也不佳，同时政府机构精简、国有企业改革以及住房、养老、医疗、教育等各种制度的改革，使居民普遍感到预期支出的提高，我国又没有建立起完善的社会保障制度，从而增强了居民的储蓄动机，以增强安全感。其次，由于社会消费需求不足以及私人投资难以获得融资，降息并没有有效增加社会投资需求，但货币供给量增加，大量资金沉淀于银行，货币流通速度降低，造成货币政策作用不明显，一旦经济启动引起资金需求增加，货币流通速度加快，容易形成货币供应过多、经济过热的隐患。有可能隐入“启动—紧缩—再启动—再紧缩”的怪圈。    
    
* 计算机领域文本示例：  
>Domino环境中的数据加密技术  
李俊海　耿继秀　钱丽瑾　刘彦丽　张德壮  
　　摘　要　在企业网络实践的基础上，讨论了数据加密技术在企业网络中的应用。为了防止对非授权的数据库和文档的存取，可以对数据库进行选择算法的加密和使用私钥/公钥加密机制，对数据库文档的字段加密。  
　　关键词　数据库文档，数据加密，密钥，存取授权  
1　引言  
　　加密技术可以使我们在不安全的通道上建立安全的连接。在Domino环境中，为了防止对非授权的数据库、文档或者邮件的存取，除对数据库进行不同级别的授权外（七种级别），我们能够对数据库、对某个库中的一个文档、多个文档或者全部文档进行加密。通过加密的办法，使得系统中的各种数据的安全在三个面上得到保障。加密的办法有多种多样的，但是总离不开加密用的密钥。Domino提供了对称和非对称的两种加密机制。在对称的加密机制中，用户需要在阅读加密文档时具备密钥。我们着重讨论对数据库中的一般文档、对使用指定表单产生的所有文档、文档中的全部字段或部分字段使用指定密钥进行加密、对数据库进行选择算法的加密以及指定用户解密的方法和技术。     
  
## 领域词汇抽取教程

```
git clone https://github.com/smoothnlp/DomainWords.git
cd DomainWords
python getDomainWords.py
```

### SmoothNLP函数调用示例

这里的短语抽取过程，用到了[SmoothNLP](https://github.com/smoothnlp "smoothnlp")提供的`extract_phrase`函数，该函数使用词语本身及词语的上下文特征进行短语抽取。  

```python
from smoothnlp.algorithm.phrase import extract_phrase
extract_phrase(corpus,top_k,chunk_size,max_n,min_freq)
```
  
参数说明：
```text
corpus:     必需，file open()、database connection或list
top_k:      float or int,表示短语抽取的比例或个数
```
`extract_phrase`函数可以基于大量文本实现高效的短语抽取。不同领域文本的`短语抽取用时`统计如下：

|**数据领域**|**文件数**|**总字数**|**短语抽取用时**|
| :-:|:---:|:---:|:---:|
|Economy|3201|2083,5291|2min 1s|
|Computer|2714|1625,7862|1min 31s|
|Enviornment|2435|1294,4809|1min 11s|
|Sports|2507|1136,6098|1min 26s|
|Art|1482|1054,7150|1min 1s|
|Agriculture|2043|1027,1244|1min 1s|
|Politics|2050|994,2158|54s|
|History|934|774,8028|38s|
|Space|1282|500,0878|24s|
|Education|120|15,1783|51ms|
|Law|103|14,9372|48ms|
|Philosophy|89|14,4040|41ms|
|Military|150|11,0303|32ms|




## 领域词汇效果展示

经过我们的实验分析, 文本量较大(字符数量>10万)能有效抽取出领域词汇. 以下是多个领域的结果展示: 
  
### 经济  
![经济](https://github.com/smoothnlp/DomainWords/blob/master/img/%E7%BB%8F%E6%B5%8E.PNG?raw=true)  
  
### 计算机
![计算机](https://github.com/smoothnlp/DomainWords/blob/master/img/%E8%AE%A1%E7%AE%97%E6%9C%BA.PNG?raw=true)

### 环境
![](https://github.com/smoothnlp/DomainWords/blob/master/img/%E7%8E%AF%E5%A2%83.PNG?raw=true)

### 体育
![](https://github.com/smoothnlp/DomainWords/blob/master/img/%E4%BD%93%E8%82%B2.PNG?raw=true)

### 艺术  
![艺术](https://github.com/smoothnlp/DomainWords/blob/master/img/%E8%89%BA%E6%9C%AF.PNG?raw=true)


* 领域词汇获取方式：
`https://github.com/smoothnlp/DomainWords.git`
  

## 注：

* 本项目所用数据来自`复旦大学计算机信息与技术系国际数据库中心的复旦文本语料库`：[CSDN分享](https://download.csdn.net/download/ydf_micro/10770075)  [直接下载](https://github.com/smoothnlp/DomainWords/tree/master/data)
* 本项目中涉及的**领域词汇**结果, [直接下载](https://github.com/smoothnlp/DomainWords/tree/master/domainPhrase)
已上传到`data`文件夹下.
* 本项目所用代码已在SmoothNLP中开源：
https://github.com/smoothnlp/SmoothNLP.

  

### 看到这里,还有彩蛋0 :)
如果您对NLP感兴趣, SmoothNLP目前招收:
* (实习/全职) NLP算法工程师;
* (实习) 研究型NLP算法实习生 - 发paper的那种哈

cv投递**hr@smoothnlp.com**.