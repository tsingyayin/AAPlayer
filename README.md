# AAPlayer
仿明日方舟剧情播放风格的剧情生成器，鉴于我目前还不会写UI，所以目前先搞好底层的剧情键入语法（称之为鹰语）和基本的内容识别。

从Interpreter_Ver0.4.0开始为了节省版本号，引入pre后缀与pub后缀。pre后缀是浏览版，pub是公开版。pre版一定是源码版本，pub版可能是编译版本，也可能是源码版本。

实时更新的代码一定是当前最新版。

# Interpreter_Ver0.4.0_Pre1;SPOL0.3.5&！0.3

重构了整个解释器的文件结构，现在支持使用后缀为splang的文本文档进行多语言支持。目前除简体中文外支持一个因为本人水平不够而导致翻译的烂到家的英文

重构了解释器部分块之间的逻辑

重构了解释器的部分参数的使用逻辑

！本版支持0.3是因为没有删除0.3相关文件。我们并未对0.3兼容与否展开任何测试。

spawn mode:

支持设置剧情分支选项

修复了若干可能引起解释器崩溃的bug

*由于剧情分支是新增的复杂系统之一，所以会有很多可能引起崩溃的bug，会陆续修复。

# Interpreter_Ver0.3.1;SPOL0.3
spawn mode:

修复了文本行进驻留控制器遇到不合法数值会引起解释器崩溃的bug

修复了文本行进驻留控制器能够接受不合法数值的bug

line mode：

修复了文本行进驻留控制器遇到不合法数值会引起解释器崩溃的bug

修复了文本行进驻留控制器能够接受不合法数值的bug

# Interpreter_Ver0.3.0;SPOL0.3
spawn mode：

修复了背景控制器遇到不合法数值会引起解释器崩溃的bug

修复了音乐控制器遇到不合法数值会引起解释器崩溃的bug

修复了讲述控制器遇到不合法数值会引起解释器崩溃的bug

修复了背景控制器能够接受不合法数值的bug

修复了音乐控制器能够接受不合法数值的bug

修复了讲述控制器能够接受不合法数值的bug

新增自由文本控制器（仍在测试）

新增不合法数值设定汇报

line mode：

修复了讲述控制器遇到不合法数值会引起解释器崩溃的bug

修复了讲述控制器能够接受不合法数值的bug

新增自由文本控制器

新增line模式下允许指定解释器版本的功能（如果可以选择的话）


# Interpreter_Ver0.2.0;SPOL0.2.5
改变了内在的相关逻辑，引入了一个伪命令提示符的机制。现在headana不再负责直接调用core，而是识别用户键入命令从而调用aaspcommand，由aaspcommand决定是否调用以及如何调用core

现在可以在line命令下单独测试某一行的解释结果

或者是使用spawn命令解释整个文件

新增了文本控制器和末尾回车的格式问题警告

# Interpreter_Ver0.1.6;SPOL0.2.5&0.2
加入了未能识别文本的警告汇报功能

加入了音频控制器

音频控制器用背景控制器直接魔改而来，所以可能会有变量名称冲突。若有BUG后续会修复。

# Interpreter_Ver0.1.5;SPOL0.2.1&0.2&0.1
把语言的前缀名称从AASP（AASD）换成了SPOL

这项更改是因为需要名称标准化

本体功能未变更

# Interpreter_Ver0.1.5;AASP0.2.1&0.2&0.1
增加了时间输出，现在每输出一个场景就输出距离开始播放过去的秒数（精确到小数点后两位）

增加了跨行注释功能

# Interpreter_Ver0.1.4;AASP0.2&0.1
优化了识别版本的意义不明的算法（我当初是怎么写出这种脑残代码的？）

现在正文识别已经被迁移到其他文件上（core.py），需要一起下载。这么迁移一是为了让主体好看一些，第二是争取让AASP0.1还能再多存活几天（所谓眼不见心不烦）

# Interpreter_Ver0.1.3;AASP0.2&0.1
取消了场景淡出参数，请已经开始尝试编写的人员尽快将场景控制器的这一参数删除。

这一版本的解释器暂时保留对于0.1方案的支持，但不再更新该方案。

# Interpreter_Ver0.1.2;AASP0.1
重写了用于将用户输入（指背景控制器和讲述控制器）正确填充入对应列表的部分代码

# Interpreter_Ver0.1.1;AASP0.1
修复了背景控制器在某些缩写情况下未能正确传入程序的bug

修复了讲述控制器在某些缩写情况下未能正确传入程序的bug

为了方便后期与UI上的流程匹配，现在决定在下一个版本：

取消场景的淡出参数，只保留淡入参数

体现出立绘淡出的处理顺序，而不是单纯标出参数

*在明日方舟原版之中，还有一些文本特效，这些特效处理留到以后UI写好再进行，文本控制器会留出第三个参数甚至第四个参数

# Interpreter_Ver0.1;AASP0.1
这个版本实现了基本的内容识别
