# mac


这些好到爆炸的网站:
https://www.kancloud.cn/q952008898/hei_ping_guo/1053738
https://blog.daliansky.net/



黑苹果系列 遇到的问题和办法
全篇参考文章(参考这个基本没问题):http://zxacn.com/articles/2019/08/02/1564717450462.html#b3_solo_h2_5

其他参考文章
https://zhuanlan.zhihu.com/p/84327935
https://www.codetd.com/article/1805647

安装:

资源文件:

资源工具
mac os镜像、windows下的工具以及配置文件

关注公众号raiseProductivity回复黑苹果获取下载地址

百度云账号用户名叫 爱0000k 下
小米游戏本黑苹果资源

注:clover要用

CLOVER的副本.zip 这个才支持我这本子


问题:c盘有54gb剩余 但是分区空间很小,怎么回事.

所以只能mac装在机械硬盘上,

就成了 双硬盘装双系统


分区:

苹果要apfs格式 需要用 DiskGenius.exe 将整个机械硬盘 

由MRB格式转换为GPT格式 右键点击硬盘 选择 转换分区表类型为GUID格式

从d盘分:

1.macos系统盘 我分的一百多g(右键 此电脑-->管理-->磁盘管理)

右键单击这个maoos分区，在弹出菜单中选择 New Volume 创建新卷
http://zxacn.com/articles/2019/08/02/1564717450462.html#b3_solo_h2_5

9到15步

2.一个mac系统专门用来存文件的盘(可以不选择这个 因为那样只能mac独用)

可以将win下使用的硬盘分区 和mac共用 需要在mac系统下进行卸载 再挂载nftp格式硬盘
https://www.affdalao.com/1109.html

此项目下的文件里有(脚本还在完善中): mac/autoamountdisk/

2.1:上面2的操作不用了.
新建一个exFAT格式的盘 win mac系统都能自由读写

https://www.kancloud.cn/q952008898/hei_ping_guo/1053738

3.一个efi分区 200mb以上 我选择的300m

Windows下使用diskpart建立EFI分区及挂载EFI分区
https://blog.daliansky.net/Under-Windows-using-DISKPART-to-create-EFI-points.html

4.刷系统 

先修改系统时间-->抹掉磁盘HFS+格式-->安装系统-->期间会重启系统,重启第一次开始选择从刚才抹掉的那个磁盘启动(重启过程必须连续,
不能再安装期间进入win10系统)-->安装完成


修改时间:

黑苹果 安装系统出现"安装 macOS xxx"应用程序副本已损坏，不能用来安装macOS解决方法
https://blog.csdn.net/qq_41855420/article/details/102762647

5.安装
mac/software-mac/
目录下的软件:

HoRNDIS-9.2.pkg --安卓手机共享usb网络上网(macos不能用wifi的)---安装后重启系统

Scroll Reverser鼠标方向矫正.zip

其他的科学上网软件

6.安装显卡驱动:

1.安装clover

黑苹果使用clover configurator修改config.plist配置文件
https://blog.csdn.net/blackei/article/details/88216473

clover Mac下的管理软件 百度网盘里/本仓库mac/software-mac/下面

黑苹果10.13.6安装WebDriver驱动nvidia独立显卡，以及修改机型
https://blog.csdn.net/blackei/article/details/88216169

驱动下载网址:
https://www.tonymacx86.com/nvidia-drivers/









进入macOS后：

sudo spctl --master-disable

在终端输入这个 打开任何来源


备份：

# https://www.bilibili.com/video/av39026334/

# https://www.kancloud.cn/q952008898/hei_ping_guo/1108249(好文章 参考这个)

# 黑苹果在win10下备份 推荐经常备份

# 备份软件:Paragon HFS+ for Windows v10.5 百度网盘里有


上面是参考的:

我最想要的是:win10下直接备份还原,简单好操作 = 淘宝店家选用的方法.(不用准备单独的苹果格式的硬盘来备份)
只用一个软件---Paragon Hard Disk Manger
https://www.bilibili.com/video/av75454979/



疑问:备份mac系统是不是只需要备份 mac下的 efi分区+mac系统盘?



其他:
1.隐藏系统盘

https://iknow.lenovo.com.cn/detail/dc_151394.html

2.hackingtools使用方法:
https://blog.daliansky.net/Intel-FB-Patcher-tutorial-and-insertion-pose.html


