# pytex

![license](https://img.shields.io/github/license/mashape/apistatus.svg)

将python当成你的文本编辑器，直接将内容输出为pdf文档。
无需转换格式，**直接**将你的文字以pdf的格式呈现。
## Usage
```python
from pytex import pdfwriter

writer = pdfwriter(file_name='demo.pdf')

writer.h1('一级标题')
writer.h2('二级标题')
writer.h3('三级标题')
writer.h4('四级标题')

writer.p('正文文本')
writer.pic('figure/图片.jpg')
writer.save()
```

## Example
以[TensorFlow中文文档](https://github.com/jikexueyuanwiki/tensorflow-zh)的介绍内容为例。

```python
from pytex import pdfwriter

writer = pdfwriter(file_name='demo.pdf')
writer.h1('TensorFlow 官方文档中文版')
writer.pic('figure/TensorFlow.jpg', place=1)
writer.p('你正在阅读的项目可能会比 Android 系统更加深远地影响着世界！', fontsize=12, first_indent=False)
writer.h2('缘起')
writer.p('2015年11月9日，Google发布人工智能系统TensorFlow并宣布开源，同日，极客学院组织在线TensorFlow中文文档翻译。')
writer.p('机器学习作为人工智能的一种类型，可以让软件根据大量的数据来对未来的情况进行阐述或预判。如今，领先的科技巨头无'
         '不在机器学习下予以极大投入。Facebook、苹果、微软，甚至国内的百度。Google 自然也在其中。「TensorFlow」是 '
         'Google 多年以来内部的机器学习系统。如今，Google 正在将此系统成为开源系统，并将此系统的参数公布给业界工程师'
         '、学者和拥有大量编程能力的技术人员，这意味着什么呢？', line_dist=5)
writer.p('打个不太恰当的比喻，如今 Google 对待 TensorFlow 系统，有点类似于该公司对待旗下移动操作系统 Android。如'
         '果更多的数据科学家开始使用 Google 的系统来从事机器学习方面的研究，那么这将有利于 Google 对日益发展的机器学'
         '习行业拥有更多的主导权。', line_dist=5)
writer.p('为了让国内的技术人员在最短的时间内迅速掌握这一世界领先的 AI 系统，极客学院 Wiki 团队发起对 TensorFlow 官'
         '方文档的中文协同翻译，一周之内，全部翻译认领完成，一个月后，全部30章节翻译校对完成，上线极客学院Wiki平台并'
         '提供下载。', line_dist=5)
writer.p('Google TensorFlow项目负责人Jeff Dean为该中文翻译项目回信称："看到能够将TensorFlow翻译成中文我非常激动'
         '，我们将TensorFlow开源的主要原因之一是为了让全世界的人们能够从机器学习与人工智能中获益，类似这样的协作翻译'
         '能够让更多的人更容易地接触到TensorFlow项目，很期待接下来该项目在全球范围内的应用!"', line_dist=5)
writer.p('Jeff回信原文：', line_dist=5)
writer.pic('figure/jeff.png', width=350, place=0)
writer.p('再次衷心感谢每一位为该翻译项目做出贡献的同学，我们会持续关注TensorFlow、AI领域以及其它最新技术的发展、持'
         '续维护该协作翻译、持续提供更多更优质的内容，为广大IT学习者们服务！', line_dist=5)
writer.pic('figure/tf.png', width=150, place=0)
writer.pic('figure/tf.png', width=150, place=1)
writer.pic('figure/tf.png', width=150, place=2)
writer.newline(line_dist=50)
writer.p('Zhanpw97',fontsize=15,char_dist_bias=6)

writer.save()
```
将会输出demo.pdf，如下所示：
![](https://ws4.sinaimg.cn/large/006tNc79ly1fpssgz5il0j30u62mokhd.jpg)

## To Do
More features are on the way
* [ ] 行尾标点优化
* [ ] 下划线
* [ ] 删除线
* [ ] 字体颜色
* [ ] 背景颜色

## License
MIT

