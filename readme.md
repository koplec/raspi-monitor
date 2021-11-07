# systemd 

/etc/systemd/system以下にシンボリックリンクを張る

```
sudo systemctl stop monitor-raspi.timer
sudo systemctl disable monitor-raspi.timer

sudo ln -s /home/ubuntu/apps/monitor-raspi/systemd/monitor-raspi.service /etc/systemd/system/
sudo ln -s /home/ubuntu/apps/monitor-raspi/systemd/monitor-raspi.timer /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl enable monitor-raspi.timer
sudo systemctl start monitor-raspi.timer
```