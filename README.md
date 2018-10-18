# Snape

Snape is a minimalistic snippets manager written in Python.

You may add snippets, list all snippets, search for a specific snippet using a keyword, and that's it.
All data are saved into a local json file(`~/.snape.json`), you can modify the json file at will and optionally put that file with other dot files under version control.

Snape strive to provide a simple solution for a simple task.


Of course the name comes from Harry Potter, as mentioned by Harry potter:

> He was probably the bravest man I ever knew.

I think we all need a little courage from time to time.


# Installation and usage

The installation is plain and simple, just use pip:.

```
pip install Snape
```

To show the help message, use:

```
Snape --help
```

which will display:

```
Usage:
    snape                       # list all snippet with descriptions.
    snape [Name of snippet]     # show a single snippet.
    snape add [Name of snippet] # add a snippet
    snape search [pattern]      # search for a pattern in the library.
```

As an example, suppose we use requests to post a json to an API, and we want to have that code snippet saved in Snape, we run the following command in the commnadline:

```
[user@host ~]Snape add python post json
```

Here, `python post json` will be the name of the snippet. Snape will now prompt you to enter your snippet, after you've dumped your snippets there, you need to add a new line and a `Ctrl-D` so as to save the snippet to `~/.snape.json`.

My personal snippets can be found here: https://github.com/xiaket/etc/blob/master/snape.json

The search feature will list all snippets which 

There's no intention to add the ability to modify or remove a snippet, since you can easily do that with any editor you like.
