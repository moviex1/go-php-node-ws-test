<h1>Requirements</h1>
<p>python3 </p>
<p>docker compose</p>

<h2>Set up python for tests</h2>
<pre>python3 -m venv <path_to_venv></pre>
<pre>source <path_to_venv></pre>
<pre>pip3 install -r requirements.txt</pre>

<h1>How to start servers</h1>
<pre>docker compose up --build</pre>

<h1>How to get performance test of server</h1>
<p>simply execute:</p>
<pre>python3 test_ws.py</pre>
