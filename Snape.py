#!/usr/bin/env python3
import json
import os
import sys

try:
    from pygments import highlight
    from pygments.formatters import TerminalFormatter
    from pygments.lexers import find_lexer_class, guess_lexer

    HAS_PYGMENTS = True
except ImportError:
    HAS_PYGMENTS = False


USAGE = """
Usage:
    snape                       # list all snippet with descriptions.
    snape [Name of snippet]     # show a single snippet.
    snape add [Name of snippet] # add a snippet
    snape search [pattern]      # search for a pattern in the library.
"""


class SnippetFile:
    DBFILE = os.path.expanduser("~/.snape.json")

    def __init__(self):
        """Load the DB file."""
        if not os.path.isfile(self.DBFILE):
            self.snippets = {}
            return

        with open(self.DBFILE) as fobj:
            content = fobj.read()
            if not content.strip():
                content = "{}"

            self.snippets = {
                name: Snippet(name, data)
                for name, data in json.loads(content).items()
            }

    def save(self):
        with open(self.DBFILE, "w") as fobj:
            fobj.write(
                json.dumps(
                    self.snippets,
                    default=lambda s: s.__json__,
                    indent=2,
                    sort_keys=True,
                    separators=(",", ": "),
                )
            )

    def list(self):
        for snippet in self.snippets.values():
            snippet.show()

    def add(self, name):
        print("Enter/Paste your content. Ctrl-D to save it.")
        contents = []
        while True:
            try:
                line = input("")
            except EOFError:
                break
            except KeyboardInterrupt:
                print("\nUser cancelled, not saving.", file=sys.stderr)
                sys.exit(1)

            contents.append(line)

        text = "\n".join(contents)
        lang = guess_lexer(text).name if HAS_PYGMENTS else ""
        self.snippets[name] = Snippet(
            name, {"content": text, "lang": lang}
        )
        self.save()

    def search(self, query):
        query = query.lower()
        for key, snippet in self.snippets.items():
            if query in key.lower() or query in snippet.content.lower():
                snippet.show()

    def __contains__(self, name):
        return name in self.snippets


class Snippet:
    def __init__(self, name, data):
        self.name = name
        self.content = data["content"]
        self.lang = data["lang"]

    @property
    def __json__(self):
        return {'content': self.content, 'lang': self.lang}

    @property
    def text(self):
        if not HAS_PYGMENTS:
            return self.content

        if self.lang:
            lexer = find_lexer_class(self.lang)
        else:
            lexer = guess_lexer(self.content)

        return highlight(self.content, lexer(), TerminalFormatter()).strip()

    def show(self):
        print(f"\x1b[1;34m## {self.name}\x1b[0m\n")
        print("```")
        print(self.text)
        print("```")
        print("\n")


def main():
    snippet_file = SnippetFile()
    if len(sys.argv) == 1:
        snippet_file.list()
    else:
        args = " ".join(sys.argv[1:])
        first = sys.argv[1]
        if args in snippet_file:
            snippet_file.snippets[args].show()
        elif first == "add" and len(sys.argv) > 2:
            snippet_file.add(" ".join(sys.argv[2:]))
        elif first == "search" and len(sys.argv) > 2:
            snippet_file.search(" ".join(sys.argv[2:]))
        else:
            print(USAGE)
            sys.exit(1)


if __name__ == "__main__":
    main()
