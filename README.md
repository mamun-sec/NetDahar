<code>![](https://komarev.com/ghpvc/?username=mamun-sec&color=blue&label=Total+Views+This+Month)</code> <code>![status](https://img.shields.io/badge/status-up-brightgreen)</code> <code><b><a href="https://www.linkedin.com/in/mamun-infosec/">Linkedin</a></code> <code><a href="https://www.facebook.com/Mamun.Masak/">Facebook</a></code> <code><a href="https://intarna.com/blog/">Blog</a></code> <code><a href="mailto:ceo@intarna.com">Email</a></b></code>
<br>
<h1>:white_square_button: NetDahar</h1>
<br>
<b>NetDahar logs network activities of each process with the following data:</b>
<br><br>
<ul>
  <li><code>Process Name</code></li>
  <li><code>Process PID</code></li>
  <li><code>Source File of The Process</code></li>
  <li><code>Opened Files by The Process</code></li>
  <li><code>Commandline of The Process</code></li>
  <li><code>Username of The Process</code></li>
  <li><code>Source IP</code></li>
  <li><code>Source Port</code></li>
  <li><code>Remote IP</code></li>
  <li><code>Remote Port</code></li>
  <li><code>CPU Percentage</code></li>
  <li><code>Log Time</code></li>
</ul>
Hopefully, if multiple processes with the same name are found, but they have different source IP or, source port or, remote IP or, remote port then NetDahar will log each of those processes individually by adding an unique numerical value with each process name so that, you can differentiate between them.
<br><br><br>
<h2>:notebook: Required Python3 Modules:</h2>
Install these modules using <code>pip3</code> as root/administrator if not installed:<br>
<ul>
  <li><code>psutil</code></li>
  <li><code>threading</code></li>
  <li><code>json</code></li>
  <li><code>collections</code></li>
</ul>
<br>
<h2>:beginner: How to Use (Linux):</h2>
<b>1.</b> After cloning NetDahar, go to its directory using <code>cd NetDahar</code> command.<br>
<b>2.</b> Now run the netdahar.py script using <code>sudo python3 netdahar.py</code> command. Logging will be started at this point.<br><br>
<b>Note:</b> If you want to continuously store logs then, add the netdahar.py script to crontab for running it on startup automatically (<a href="https://stackoverflow.com/a/39225774/17874021">details</a>).
<br><br><br>
<h2>:beginner: How to Use (Windows):</h2>
(NetDahar is created for Linux but also works in Windows)<br><br>
<b>1.</b> After cloning NetDahar, open an Administrator command prompt and go to its directory using <code>cd NetDahar</code> command.<br>
<b>2.</b> Now run the netdahar.py script using <code>python netdahar.py</code> command. Logging will be started at this point.<br><br>
<b>Note:</b> If you want to continuously store logs then, add the netdahar.py script to autorun registry key to run it on each reboot automatically (<a href="https://www.geeksforgeeks.org/autorun-a-python-script-on-windows-startup/">details</a>).
<br><br><br>
<h2>:clipboard: View The Logs</h2>
NetDahar will store logs by creating a file with today's date in the './NetDahar/Report' directory. And if you add NetDahar to startup then it'll store each day's logs by creating file with that day's date. And logs are written to the log file after every 20 seconds.
<br>
