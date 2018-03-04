* New in HAProxy 1.8: https://www.haproxy.com/blog/whats-new-haproxy-1-8
* Download: http://www.haproxy.org/download/1.8/src/haproxy-1.8.4.tar.gz

* Compiling ...

```
cd ~/Downloads
tar xvf haproxy-1.8.4.tar.gz
cd haproxy-1.8.4
make TARGET=generic
```

Verify:
```
[jd@jdpc haproxy-1.8.4]$ file haproxy 
haproxy: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=989e4eb352472aba4432b2617a6d3c0699029095, with debug_info, not stripped
```

Make a link:
```
sudo ln -s /home/jd/Downloads/haproxy-1.8.4/haproxy /usr/local/bin/haproxy -f
```

Verify link and path exists:
```
# Link valid?
[jd@jdpc haproxy-1.8.4]$ ls -ltr /usr/local/bin/haproxy
lrwxrwxrwx. 1 root root 40 Mar  4 13:51 /usr/local/bin/haproxy -> /home/jd/Downloads/haproxy-1.8.4/haproxy
# link works?
[jd@jdpc haproxy-1.8.4]$ which haproxy 
/usr/local/bin/haproxy
# Binary works?
[jd@jdpc haproxy-1.8.4]$ haproxy --help
HA-Proxy version 1.8.4-1deb90d 2018/02/08
Copyright 2000-2018 Willy Tarreau <willy@haproxy.org>
Usage : haproxy [-f <cfgfile|cfgdir>]* [ -vdVD ] [ -n <maxconn> ] [ -N <maxpco
...
...
```