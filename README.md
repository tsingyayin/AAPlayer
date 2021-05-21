# Yayin Story Player

从Interpreter_Ver0.4.0开始为了节省版本号，引入pre后缀与pub后缀。pre后缀是浏览版，pub是公开版。

从Ver0.4.0.0_Pre9开始，因为各个部件不像以前那么孤立，所以版本名称从原来的三段命名改为了一段。

关于release包的pre与否的问题，我当然知道它本来的用途，但是在我这里，凡是挂pre的就是没有编译的代码包，没挂pre的就是编译过的程序包。

我当然知道在创建一个release的时候会自动截取现有代码生成源码包，但问题在于我不能保证我的github更新与本地修改是完全同步的——很有可能在大部分是当前版本的文件中会混入一个上一版的文件。所以为了避免这个问题，我会上传直接由本地文件压缩形成的包。

编译过的包可以直接运行，不需要安装任何东西。
# V0.4.0.0_Pre10:

音乐控制器现在能够使用，具有基本的功能

# Ver0.4.0.0_Pre9.1

重新进行了英文翻译

修复了line命令下的内核版本错误

修复了0.4.1内核line模式下自由文本控制器输出不正确的bug

# Ver0.4.0.0_Pre9(已编译)

修改内容：

修改了顶层的显示逻辑与屏幕内容更新逻辑

修改了启动按钮的图标

新增内容：

新增了自动播放与手动播放的切换功能。剧情默认采用自动播放，可以自己切换。但是请注意，手动播放仅支持在当前页流程结束后手动翻页，暂不支持明日方舟原版播放时的文字跳跃和直接翻页。

新增了程序退出按钮

现已支持通过双击剧情文件打开剧情播放器，您只需要在默认程序选择的时候选择为程序文件夹下的click_run.exe即可。click_run.exe仅用来通过click_run.bat传递参数，本身不含任何剧情播放功能。

修复内容：

修复了剧情分支与对话分支部分偶尔不能使用的bug

修复了连续打开文件的过程中，UI可能出现的bug

修复了剧情最后一个控制器不是背景控制器时，无法正确回到初始页面的bug

修复了剧情最后一个讲述控制器不是空场控制器时，最后一个对话会在剧情播放完毕后、在回到初始页面的过渡动画中一直存在于的bug

修复了其他偶现的解释器线程意外停止的bug

修复了在某些情况下，背景切换时可能闪屏的bug

修复了使用about命令后显示的错误文本

# Interpreter_Ver0.4.0_Pre7;SPOL_0.4.1;UI0_0.2.0（已编译）

最新内核升级到0.4.1版本

新增了游戏内的按钮，能够进行剧情分支和对话分支的选择

新增了标题与副标题的显示，并且由于需要显示背景和Logo而修改了SPOL标题控制器的语法。

修复了连续打开文件过程中，第二个剧情在播放时会出现各种各样问题的bug

# Interpreter_Ver0.4.0_Pre6;SPOL_0.4.0&SPOL_0.3.5;UI0_0.1.0

修复了0.3.5内核无法正确显示特效的翻译的问题

新增了0.4.0内核，支持还原游戏内的按钮分支对话（仍在测试，估计Bug很多）

0.4.0_U内核虽然也已经可以正常识别，但是对应UI还没有做。

# Interpreter_Ver0.4.0_Pre5;SPOL_0.3.5;UI0_0.1.0（已编译）

新增了文件选择功能，现在可以自由选择剧情文件

改变了文件相互调用逻辑。上一个版本中，aaspcommand里面的spawn函数被改做QThread对象的run函数，这就导致无法使用spawn命令正常进入命令行的解释模式。现在这个部分已经独立成文件UICoreLauncher了，原来的spawn函数已经恢复。

*如果不想看范例文件N2U.spol，您大可自己编写，但是别忘了在Visual/source文件夹下面的对应位置添加对应素材。

*目前所有图形处理特效只有翻转立绘已经实现了，其他滤镜和变换仍然在寻找更快的处理方法。

# Interpreter_Ver0.4.0_Pre4;SPOL_0.3.5;UI0_0.1.0

从这个版本开始可以使用UI

使用UI命令启动UI

由于现在还在做对接拼合工作，spawn命令改之后还没来得及修复，暂时不要使用spawn

还没有加选择文件的UI，现在固定测试N2U.spol这个文件

从这个版本开始，必须使用PyQt5这个库才能够启动程序

本版大部分时间都在解决UI问题，老bug没有修，甚至新增了Bug。目前分辨率是固定分辨率1920x1080，后期会改成适配分辨率，不过需要指出的是，程序到最后一定是全屏，打死我都不做窗口化。

# Interpreter_Ver0.4.0_Pre3;SPOL0.3.5

优化了多分支情况下的内存占用。现在最大占用取决于读取过程中遇到的最大的那个文件。

*开玩笑，怎么可能支持0.3？这个不测也应该知道。启动0.3内核需要的参数是files和timestart，启动0.3.5内核需要的参数是files和storyname，而aaspcommand的结构是顺着0.3.5来的，根本没法在启动的时候传入timestart参数，这个启动参数在0.3.5被改作内核自己负责了，aaspcommand根本没有这个参数！（再次犯傻.jpg）
# Interpreter_Ver0.4.0_Pre2;SPOL0.3.5&！0.3

修复了会一股脑把所有剧情控制器均当成参数错误的控制器的bug

修复了Second字段没有被正确翻译的问题

修复了若干可能引起解释器崩溃的bug

修复了在spawn层下，程序提示可以用exit退出的地方无法用exit退出该层的bug

优化了时序，现在计时timestart会在循环读取开始前的最后一个步骤进行，以避免数毫秒的语言文本加载占用导致计时延迟

！本版支持0.3是因为没有删除0.3相关文件。我们并未对0.3兼容与否展开任何测试。

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
