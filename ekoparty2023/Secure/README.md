# Secure (500 points)

We need to find critical secrets somewhere.

This problem is kinda very hard, doing some information gathering with trial and error. So scanning through the network go.ctf.site host is a must. 

From port of IRC server 16667, I found a footprint with the flag which is a critical secrets somewhere.

```
16697/tcp open  ssl/irc UnrealIRCd
| irc-info: 
|   users: 43
|   servers: 2
|   ops: 7
|   chans: 26
|   lusers: 36
|   lservers: 1
|_  server: go.ctf.site
| ssl-cert: Subject: commonName=go.ctf.site/organizationName=EKO{th3_f1rst_irc_fl4g}/stateOrProvinceName=Antioquia/countryName=CO
| Not valid before: 2023-10-22T03:44:22
|_Not valid after:  2033-10-19T03:44:22
```

**FLAG:** `EKO{th3_f1rst_irc_fl4g}`