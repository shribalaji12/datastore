Note: I have done this assignment with basic script with commandline arguments, as i'm not sure i could use webserver is expected.

**Specify file path**

`python3 server.py -f /home/balaji/freshworks/data/`

**Create Data**

` python3 server.py -f /home/balaji/freshworks/data/  -c '{"key":{"value":"hello"},"expiry":30}'`

**Read Data**

`python3 server.py -f /home/balaji/freshworks/data/ -r 'key'`

**Delete Data**

`python3 server.py -f /home/balaji/freshworks/data/ -d 'key'`