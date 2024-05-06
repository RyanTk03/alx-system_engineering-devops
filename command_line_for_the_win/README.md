# Command line for the win project

## Steps to send the files from the local machine to the distant machine:
* Start an SFTP session:
```
sftp Username@Host
```

* Move into the local directory that contains the images:
```
lcd c:/users/ryan/Pictures/
```

* Transfer 6 files from the local machine to the remote machine:
```
put 0-first_9_tasks.jpg 0-first_9_tasks.png 1-next_9_tasks.jpg 1-next_9_tasks.png 2-next_9_tasks.jpg 2-next_9_tasks.png
```

* move them into the git repo
```
mv 0-first_9_tasks.jpg 0-first_9_tasks.png 1-next_9_tasks.jpg 1-next_9_tasks.png 2-next_9_tasks.jpg 2-next_9_tasks.png /root/alx-system_engineering-devops/command_line_for_the_win
```


* Once the transfers are complete, exit the SFTP session:
```
bye
```

