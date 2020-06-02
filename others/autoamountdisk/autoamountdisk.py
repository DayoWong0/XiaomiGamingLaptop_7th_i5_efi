# https://www.affdalao.com/1109.html
'''

Mac下挂载ntfs硬盘步骤：
1.进入管理员root用户 sudo -i
2.输入命令 diskutil list 查看ntfs分区
/dev/disk0 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *250.1 GB   disk0
   1:                        EFI EFI                     209.7 MB   disk0s1
   2:                 Apple_APFS Container disk2         249.8 GB   disk0s2

/dev/disk1 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *1.0 TB     disk1
   1:         Microsoft Reserved                         134.2 MB   disk1s1
   2:       Microsoft Basic Data ntfs_f                  499.3 GB   disk1s2     （这个是ntfs磁盘 disk1s2）
   3:       Microsoft Basic Data ntfs_d                  500.8 GB   disk1s3      （这个也是ntfs磁盘 disk1s3）

3.卸载着两个ntfs磁盘挂载
umount /dev/disk1s2
umount /dev/disk1s3
4.用mac自带命令重新挂在这两块ntfs磁盘到指定文件夹下，此处为桌面ntfs_d和ntfs_f文件夹，不存在新建，jimjobs 更换为你自己的用户名
jimdeAir:~ root# mount_ntfs -o rw,nobrowse /dev/disk1s3 /Users/jimjobs/Desktop/ntfs_f
jimdeAir:~ root# mount_ntfs -o rw,nobrowse /dev/disk1s2 /Users/jimjobs/Desktop/ntfs_d
5.注意事项，因为每次重启黑苹果，磁盘顺序会重新排列，所以不建议开机自动挂载。
上一篇: Centos7配置多个IPv6地址下一篇: IPv6子网范围和其子网所包含的IP个数对照表
Centos 8配置系统自动更新
OVHcloud美东小鸡 DD Centos8系统
Oracle Cloud重置SSH密钥(亲测可行)
使用queryperf对DNS服务器进行压力测试
在VirtualBox通过boot.iso安装体验Centos8
Oracle Centos7手动开启原生BBR支持
Centos7安装部署NSD进行多域名DNS解析
打造最强NGINX HTTPS配置
版权声明：本文版权归AFF大佬和原作者所有，未经许可不得转载。文章部分来源于网络仅代表作者看法，如有不同观点，欢迎进行交流。除非注明，文章均由 AFF大佬 整理发布，欢迎转载，转载请带版权。

来源：AFF大佬 ( https://www.affdalao.com/ )，提供主机优惠信息深度测评和服务器运维编程技术。
链接：https://www.affdalao.com/1109.html



'''



' sudo -i #get root '

1.full in rootpassword

password = 'zx19981219'

' diskutil list '  

# check the physical address by disk's name
2.search the disk address by filter #筛选出disk address by disk name

diskaddr = ''

# 3.卸载着两个ntfs磁盘挂载

' umount /dev/%s ' % diskaddr

# 4.用mac自带命令重新挂在这两块
# ntfs磁盘到指定文件夹下，此处为
# 桌面ntfs_d和ntfs_f文件夹，
# 不存在新建，jimjobs 更换为你自己的用户名


# mkdir called guazaiyingpan

' mkdir /Users/zx/Desktop/guazaiyingpan '

'  mount_ntfs -o rw,nobrowse /dev/%s /Users/zx/Desktop/guazaiyingpan ' % diskaddr