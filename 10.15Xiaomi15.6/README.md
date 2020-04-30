# 安装最新版mac 10.15.3?在小米游戏本15.6 i5 7300hq+1060(独显没用)-2020/4/30
## 1.下载mac系统
https://blog.daliansky.net/macOS-Catalina-10.15.4-19E266-Release-version-with-Clover-5107-original-image-Double-EFI-Version-UEFI-and-MBR.html

## 2.参考的安装步骤
https://zxacn.com/articles/2019/08/02/1564717450462.html#b3_solo_h2_5
- win用到的软件
[TransMac]()
[DiskGenius]()

## 3.安装盘制作
参考步骤2的网站

## 不能进入安装界面 卡苹果
Dayo Wong 2020/4/30 3:47:41
用了黑果小兵的配置文件。把conflig改了,boot.efi复制了改了

Dayo Wong 2020/4/30 3:47:52
驱动kext忘了

efi分区没搞好

efi分区新建方法(Mac OSX 抹盘发生错误:Mediakit 报告设备上空间不足以执行此操作的解决办法

):https://blog.zzzmode.com/2016/05/02/osx-mediakit-reports-partition-map-too-small/

用了黑果小兵的配置文件。把config改了,Boot目录下 boot.efi复制了改了
boot.efi不改的话,clover界面显示不正确

Dayo Wong 2020/4/30 4:14:56
安装系统的副本已经损坏

Dayo Wong 2020/4/30 4:15:18
终端输入:date 10251020

Dayo Wong 2020/4/30 4:15:35
Dayo Wong  
终端输入:date 10251020
10.15系统

Dayo Wong 2020/4/30 4:26:04
关键:黑果小兵的kext和clover版本 小米游戏本用来安装过mac13.6的配置文件(这个可能不是关键,下次试试)

Dayo Wong 2020/4/30 4:26:24
Dayo Wong  
关键:黑果小兵的kext和clover版本 小米游戏本用来安装过mac13.6的配置文件(这个可能不是关键,下次试试)
efi分区要搞对

Dayo Wong 2020/4/30 4:26:37
Dayo Wong  
efi分区新建方法(Mac OSX 抹盘发生错误:Mediakit 报告设备上空间不足以执行此操作的解决办法

):https://blog.zzzmode.com/2016/05/02/osx-mediakit-reports-partition-map-too-small/
efi分区看这个

Dayo Wong 2020/4/30 4:28:05
机械硬盘安装系统是真的慢,启动也慢得一批

Dayo Wong 2020/4/30 4:28:54
Mac系统ghost备份和恢复的方法？

Dayo Wong  17:01:49
https://www.sqlsec.com/2019/12/macos.html

总结:   
config改为了以前成功安装10.13.6系统的那个(可能不是因为改了这个才成功的,推测,没验证)  
efi分区下的 boot/boot.efi对应的改了  
Boot目录下 boot.efi复制了改了  
boot.efi不改的话,clover界面显示不正确(可能主要原因是这个,推测,没验证)  

现在驱动没安装正确,10.13.6里面能好好用的驱动升级了部分没用了  

# 总结一下安装过程
### 分区(efi分区不能忘记)--安装盘制作--clover进入--进入mac安装系统界面(我尝试着替换了efi引导文件(将clover下面的CLOVERX64.efi复制到了Boot下并改名为BOOTX64.efi(这两个文件本来就是一样的,但是用黑果小兵的文件,不这样操作,进入clover显示有问题,可能不能进入安装系统界面,这也是用来升级clover的方法),和修改了config文件(用的10.13.6成功的文件).还改了Lilu_Debug_v1.4.3.kext,WhateverGreen_v1.3.8.kext,这里就是mac风格了,这一个步骤算是我每次都遇到的问题,详情在下面)--安装好系统配置驱动(10.13用的一个热心网友的clover文件,驱动全部正常--10.15靠自己了--目前正在学)----关键点 config文件和驱动,这是核心技术,只要我掌握了,就能随心所欲黑苹果,同时也是最难的 
1.下载系统,去黑果小兵下载,集成了efi 大部分机器能正常进入安装界面,操作比自己找efi方便,如果不能进入安装界面(我是卡苹果),  
试着修改config文件(找别人成功安装的文件,或者自己配置(难度大))  
2.安装过程遇到问题 谷歌.  
我遇到的:  
不能格式化硬盘 报错:...报告,..空间不足-----efi分区没搞,需要此分区大于200m,我一般设置300m   
提示安装程序副本已经损坏----终端命令修改时间---10.13.6 修改时间大约2016年,10.15我修改的2020年  
从u盘写好文件到系统盘之后,还会重启几次..需要正确进入mac安装系统----建议设置u盘为第一启动项(10.13.6遇到的问题,10.15有经验了,但还是自己手动选的)
安装系统重启了,又卡苹果了,苹果图标成了红色(10.15遇到,后来强制关机,再进入安装就成功了)
3.成功进入系统了,驱动没搞好.---目前为止(考虑参考10.13的clover驱动,升级一下,再自己根据硬件配置)




