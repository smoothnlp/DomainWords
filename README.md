# 领域文本的短语抽取


本实验采用**复旦大学计算机信息与技术系国际数据库中心自然语言处理小组提供的复旦文本语料库**,包括`经济`、`计算机`、`环境`、`体育`、`艺术`等20个领域的文本。领域文本包含的文档数和总字数统计如下：

|**数据领域**|**文件数**|**总字数**|
| :-:|:---:|:---:|
|Economy|3201|2083,5291|
|Computer|2714|1625,7862|
|Enviornment|2435|1294,4809|
|Sports|2507|1136,6098|
|Art|1482|1054,7150|
|Agriculture|2043|1027,1244|
|Politics|2050|994,2158|
|History|934|774,8028|
|Space|1282|500,0878|
|Education|120|15,1783|
|Law|103|14,9372|
|Philosophy|89|14,4040|
|Military|150|11,0303|
|Literature|67|9,1466|
|Transport|116|7,5620|
|Medical|104|6,5853|
|Mine|67|5,6017|
|Energy|65|4,6160|
|Electronics|55|3,8597|
|Communication|52|2,9893|

经过对短语抽取结果的分析，我们认为该短语抽取方法适用于不同领域，且文本量大的时候会有更好的效果。


  

### 不同领域效果展示

我们选择文本量较大的经济,计算机,艺术领域数据进行展示：

![经济](https://raw.githubusercontent.com/smoothnlp/DomainWords/master/img/经济.png)

![计算机](img/计算机.png)

![艺术](https://raw.githubusercontent.com/smoothnlp/DomainWords/master/img/艺术.png)

  

## 注：

* 本项目所用数据来自`复旦大学计算机信息与技术系国际数据库中心自然语言处理小组提供的复旦文本语料库`,已上传到data文件夹下.

* 本项目所用代码已在SmoothNLP中开源：
https://github.com/smoothnlp/SmoothNLP.

  

## 没想到吧,还有彩蛋 
如果您对NLP感兴趣,欢迎加入我们的团队,我们招收全职/实习nlp算法工程师.  

cv投递**hr@smoothnlp.com**.




