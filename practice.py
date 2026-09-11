Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\KiTE> wsl --status
Default Distribution: docker-desktop
Default Version: 2
PS C:\Users\KiTE> wsl --list --verbose
  NAME              STATE           VERSION
* docker-desktop    Stopped         2
  Ubuntu            Stopped         2
PS C:\Users\KiTE> wsl -d Ubuntu
root@E042502088:/mnt/c/Users/KiTE# pwd
/mnt/c/Users/KiTE
root@E042502088:/mnt/c/Users/KiTE# ls
 -1.14-windows.xml                                                                              OneDrive
 AppData                                                                                        PY26062
'Application Data'                                                                              Pictures
 Contacts                                                                                       Postman
 Cookies                                                                                        PrintHood
 Desktop                                                                                        Recent
 Documents                                                                                     'Saved Games'
 Downloads                                                                                      Searches
 Favorites                                                                                      SendTo
 Links                                                                                         'Start Menu'
'Local Settings'                                                                                Templates
 Music                                                                                          Videos
'My Documents'                                                                                  mlflow.db
 NTUSER.DAT                                                                                     models
 NTUSER.DAT{c68735b4-2dd2-11f0-9fdb-cd0a2c180d3c}.TM.blf                                        ntuser.dat.LOG1
 NTUSER.DAT{c68735b4-2dd2-11f0-9fdb-cd0a2c180d3c}.TMContainer00000000000000000001.regtrans-ms   ntuser.dat.LOG2
 NTUSER.DAT{c68735b4-2dd2-11f0-9fdb-cd0a2c180d3c}.TMContainer00000000000000000002.regtrans-ms   ntuser.ini
 NetHood                                                                                        venv
root@E042502088:/mnt/c/Users/KiTE# cd ~
root@E042502088:~# pwd
/root
root@E042502088:~# mkdir
mkdir: missing operand
Try 'mkdir --help' for more information.
root@E042502088:~# cd mkdir
-bash: cd: mkdir: No such file or directory
root@E042502088:~# ls
ansible.cfg  hello_wsl.txt  hosts  install.yml  main.tf  snap  terraform.tfstate  y
root@E042502088:~# mkdir mlops-job-practice
root@E042502088:~# ls
ansible.cfg  hello_wsl.txt  hosts  install.yml  main.tf  mlops-job-practice  snap  terraform.tfstate  y
root@E042502088:~# cd mlops-job-practice
root@E042502088:~/mlops-job-practice# ls
root@E042502088:~/mlops-job-practice# pwd
/root/mlops-job-practice
root@E042502088:~/mlops-job-practice# mkdir app
root@E042502088:~/mlops-job-practice# mkdir models
root@E042502088:~/mlops-job-practice# mkdir logs
root@E042502088:~/mlops-job-practice# touch requirements.txt
root@E042502088:~/mlops-job-practice# ls
app  logs  models  requirements.txt
root@E042502088:~/mlops-job-practice# cd app
root@E042502088:~/mlops-job-practice/app# touch main.py
root@E042502088:~/mlops-job-practice/app# ls
main.py
root@E042502088:~/mlops-job-practice/app# cd main.py
-bash: cd: main.py: Not a directory
root@E042502088:~/mlops-job-practice/app# nano main.py
root@E042502088:~/mlops-job-practice/app# cat main.py
print("ML Service started")

root@E042502088:~/mlops-job-practice/app# python3 main.py
ML Service started
root@E042502088:~/mlops-job-practice/app# ls
main.py
root@E042502088:~/mlops-job-practice/app# cp main.py
cp: missing destination file operand after 'main.py'
Try 'cp --help' for more information.
root@E042502088:~/mlops-job-practice/app# touch main_backup.py
root@E042502088:~/mlops-job-practice/app# ls
main.py  main_backup.py
root@E042502088:~/mlops-job-practice/app# cp main.py main_backup.py
root@E042502088:~/mlops-job-practice/app# cat main_backup.py
print("ML Service started")

root@E042502088:~/mlops-job-practice/app# mv main_backup.py main_old.py
root@E042502088:~/mlops-job-practice/app# ls
main.py  main_old.py
root@E042502088:~/mlops-job-practice/app# cd ..
root@E042502088:~/mlops-job-practice# cd logs
root@E042502088:~/mlops-job-practice/logs# nano app.log
root@E042502088:~/mlops-job-practice/logs# cat app.log
INFO Model service started
INFO Model loaded successfully
ERROR Failed to connect to database
INFO Request received
ERROR Prediction failed

root@E042502088:~/mlops-job-practice/logs# grep app.log
^C
root@E042502088:~/mlops-job-practice/logs# grep "ERROR" app.log
ERROR Failed to connect to database
ERROR Prediction failed
root@E042502088:~/mlops-job-practice/logs# nano app.log
root@E042502088:~/mlops-job-practice/logs# grep "WARNING" app.log
WARNING Model response time is high
root@E042502088:~/mlops-job-practice/logs# tail app.log
INFO Model service started
INFO Model loaded successfully
ERROR Failed to connect to database
INFO Request received
ERROR Prediction failed
WARNING Model response time is high

root@E042502088:~/mlops-job-practice/logs# tail -n 3 app.log
ERROR Prediction failed
WARNING Model response time is high

root@E042502088:~/mlops-job-practice/logs# tail -n 3 app.log | grep "ERROR"
ERROR Prediction failed
root@E042502088:~/mlops-job-practice/logs# tail -n 5 app.log | grep "ERROR"
ERROR Failed to connect to database
ERROR Prediction failed
root@E042502088:~/mlops-job-practice/logs# ps
    PID TTY          TIME CMD
    424 pts/0    00:00:00 bash
    917 pts/0    00:00:00 ps
root@E042502088:~/mlops-job-practice/logs# ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.1  22084 12636 ?        Ss   05:35   0:01 /sbin/init
root           2  0.0  0.0   3120  1920 ?        Sl   05:35   0:00 /init
root           7  0.0  0.0   3136  1796 ?        Sl   05:35   0:00 plan9 --control-socket 7 --log-level 4 --server-fd 8
root          53  0.0  0.1  33964 12160 ?        S<s  05:35   0:00 /usr/lib/systemd/systemd-journald
root         102  0.0  0.0  25528  6272 ?        Ss   05:35   0:00 /usr/lib/systemd/systemd-udevd
root         113  0.0  0.1 526756 12188 ?        Ssl  05:35   0:02 snapfuse /var/lib/snapd/snaps/snapd_26865.snap /snap/
root         114  0.0  0.0 153068  1284 ?        Ssl  05:35   0:00 snapfuse /var/lib/snapd/snaps/terraform_859.snap /sna
root         118  0.0  0.0 153068  1412 ?        Ssl  05:35   0:00 snapfuse /var/lib/snapd/snaps/core24_1587.snap /snap/
systemd+     135  0.0  0.1  21452 12032 ?        Ss   05:35   0:00 /usr/lib/systemd/systemd-resolved
systemd+     136  0.0  0.1  91020  7424 ?        Ssl  05:35   0:00 /usr/lib/systemd/systemd-timesyncd
root         208  0.0  0.0   4236  2432 ?        Ss   05:35   0:00 /usr/sbin/cron -f -P
message+     209  0.0  0.0   9592  4864 ?        Ss   05:35   0:00 @dbus-daemon --system --address=systemd: --nofork --n
root         221  0.1  0.5 2368304 38992 ?       Ssl  05:35   0:02 /usr/lib/snapd/snapd
root         226  0.0  0.1  17956  8320 ?        Ss   05:35   0:00 /usr/lib/systemd/systemd-logind
root         234  0.0  0.1 1830084 12416 ?       Ssl  05:35   0:00 /usr/libexec/wsl-pro-service -vv
root         258  0.0  0.0   3160  1920 hvc0     Ss+  05:35   0:00 /sbin/agetty -o -p -- \u --noclear --keep-baud - 1152
syslog       265  0.0  0.0 222508  5632 ?        Ssl  05:35   0:00 /usr/sbin/rsyslogd -n -iNONE
root         273  0.0  0.0   3116  1792 tty1     Ss+  05:35   0:00 /sbin/agetty -o -p -- \u --noclear - linux
root         293  0.0  0.3 107012 22272 ?        Ssl  05:35   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unatt
root         422  0.0  0.0   3124   896 ?        Ss   05:35   0:00 /init
root         423  0.0  0.0   3140  1156 ?        S    05:35   0:00 /init
root         424  0.0  0.0   6072  5248 pts/0    Ss   05:35   0:00 -bash
root         425  0.0  0.0   6668  3968 pts/1    Ss   05:35   0:00 /bin/login -f
root         471  0.0  0.1  20360 11264 ?        Ss   05:35   0:00 /usr/lib/systemd/systemd --user
root         473  0.0  0.0  21156  3304 ?        S    05:35   0:00 (sd-pam)
root         495  0.0  0.0   6072  4864 pts/1    S+   05:35   0:00 -bash
root         779  0.0  0.0 153068  1284 ?        Ssl  05:36   0:00 snapfuse /var/lib/snapd/snaps/terraform_928.snap /sna
root         918  0.0  0.0   8280  4096 pts/0    R+   06:20   0:00 ps aux
root@E042502088:~/mlops-job-practice/logs# ps aux | grep python
root         293  0.0  0.3 107012 22272 ?        Ssl  05:35   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
root         923  0.0  0.0   4088  1920 pts/0    S+   06:22   0:00 grep --color=auto python
root@E042502088:~/mlops-job-practice/logs# cd ~/mlops-job-practice/app
root@E042502088:~/mlops-job-practice/app# nano server.py
root@E042502088:~/mlops-job-practice/app# python3 server.py
ML service started
Terminated
root@E042502088:~/mlops-job-practice/app# export MODEL_NAME="churn-model"
root@E042502088:~/mlops-job-practice/app# echo $MODEL_NAME
churn-model
root@E042502088:~/mlops-job-practice/app# printenv MODEL_NAME
churn-model
root@E042502088:~/mlops-job-practice/app# churn-model
churn-model: command not found
root@E042502088:~/mlops-job-practice/app# env | grep MODEL_NAME
MODEL_NAME=churn-model
root@E042502088:~/mlops-job-practice/app# nano env_test.py
root@E042502088:~/mlops-job-practice/app# python3 env_test.py
Model: churn-model
root@E042502088:~/mlops-job-practice/app# export MODEL_NAME="fraud-model"
root@E042502088:~/mlops-job-practice/app# python3 env_test.py
Model: fraud-model
root@E042502088:~/mlops-job-practice/app# nano web_server.py
root@E042502088:~/mlops-job-practice/app# python3 web_server.py
Server running on port 8000
127.0.0.1 - - [11/Sep/2026 06:54:34] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [11/Sep/2026 06:55:50] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [11/Sep/2026 06:57:04] "GET /predict HTTP/1.1" 200 -
 