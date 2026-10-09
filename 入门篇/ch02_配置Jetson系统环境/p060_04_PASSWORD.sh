# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第2章 配置Jetson系统环境 · 印刷第060页 (PDF第70页)
# 上下文: ####################################图2-59 Ubuntu 20.04 远程桌面配置 ／ 便于构建无人值守的批量操作脚本。

PASSWORD=$(whiptail --title "VINO Password Setting" --passwordbox "Enter your password and choose Ok to continue." 10 60 3>&1 1>&2 2>&3)
exitstatus=$?

if [ -n "$PASSWORD" ]; then
    gsettings set org.gnome.Vino authentication-methods "['vnc']"
    gsettings set org.gnome.Vino vnc-password $(echo -n $PASSWORD|base64)
    echo "Your VINO password is:" $PASSWORD
else
    echo "You did not enter a password."
fi
