# Snape

Snape is a minimalism snippets manager written in Python. You may add/search a snippet, all data is saved into a local json file, you can modify the json file at will and put that file with other dot files under version control.

Of course the name comes from Harry Potter, as mentioned by Harry potter:

> He was probably the bravest man I ever knew.

I think we all need a little bravery from time to time.


# Installation and usage

The installation is plain and simple, just use pip to install it.

```
pip install Snape
```

To add a snippet, run `Snape add [name of snippeet]`, for example:

```
{~}Snape add python post json
Enter/Paste your content. Ctrl-D to save it.
import requests, json
url = 'http://127.0.0.1:27182/api/account'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data = {'name': 1, 'param': 2}
response = requests.post(url, data=json.dumps(data), headers=headers}
```

Please note that after you have added all the data there, you need to add an `Enter` and a `Ctrl-D` to send an `EOL` to make the end of the input.

After that, the snippet would be added to `~/.snape.json`.

You can list all the snippets by running `Snape`. You can also search the snippets with `Snape search [query]` to look for the snippet you need.
