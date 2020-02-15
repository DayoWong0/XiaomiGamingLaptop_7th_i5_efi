sudo -i
zx19981219
diskutil list
umount /dev/disk1s1
mount_ntfs -o rw,nobrowse /dev/disk1s1 /Users/zx/Desktop/ntfs_d