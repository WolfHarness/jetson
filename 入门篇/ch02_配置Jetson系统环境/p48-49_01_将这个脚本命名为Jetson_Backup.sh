# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第2章 配置Jetson系统环境 · 印刷第48-49页 (PDF第58页, PDF第59页)
# 上下文: 图2-41 使用lsblk 命令查看存储设备信息

#
# 入参1：Jetson设备地址，如/dev/sdb
####################################

# 检查是否提供了设备地址参数
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <Jetson Nano device address>"
    exit 1
fi

FILE_NAME=Jetson_Backup_$(date +%Y%m%d).img
FILE_PATH=~/${FILE_NAME}

# 镜像备份
# if=$1为入参，可以使用lsblk查到的磁盘设备号，如/dev/sdb
# of=${FILE_PATH}为备份文件名，如Jetson_Backup_20240401.img
# bs=4M表示块大小为4MB，可以提高烧录速度
sudo dd if=$1 of=${FILE_PATH} bs=4M status=progress

# 校验和信息
echo "Calculating SHA1 checksum for the backup file..."

# 使用sha1sum命令计算文件的SHA1校验和
# -c选项可以检查SHA1校验和，这里我们使用echo生成预期的校验和字符串
CHECKSUM=$(sha1sum "${FILE_PATH}" | awk '{print $1}')

# 输出SHA1校验码
echo "SHA1 checksum: ${CHECKSUM}"

# 可选：将校验码追加到备份文件名中，以便于识别
# 例如：Jetson_Backup_20240401-4a2e82c95b9c9a8f8f1b4f0c416a1c1c.sha1
FINAL_FILE_PATH="${FILE_PATH}-${CHECKSUM}.sha1"
mv "${FILE_PATH}" "${FINAL_FILE_PATH}"

# 输出最终文件的路径
echo "Backup file with checksum: ${FINAL_FILE_PATH}"
