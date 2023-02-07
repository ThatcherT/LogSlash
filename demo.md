# demo

0. Go to `~/projects/work/arctype/Logslash`
1. `sudo rm /var/log/slash/test-slashed.log` (if needed)
2. `vector -c ./Vector/logslash-zeek_files.toml`
2.5. wait a bit (60s?)
3. `python send_log.py`
