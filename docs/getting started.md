First, make sure you have [bat](https://github.com/sharkdp/bat) and [fzf](https://github.com/junegunn/fzf) installed. Lexy requires it for syntax highlighting and searching.

### Important for Linux users

When installing [bat](https://github.com/sharkdp/bat) via `apt`, the executable may be installed as `batcat` instead of `bat`. In this case, you should follow these [steps](https://github.com/sharkdp/bat?tab=readme-ov-file#on-ubuntu-using-apt) to create the necessary symlink to make `lexy` work properly. **Note**: creating an alias will not work, as aliases are not visible to subprocesses started by Python.

You can use the command `lexy --help` to see all available options.

```bash
lexy --help
Usage: lexy [OPTIONS] <LANGUAGE>

  Display <LANGUAGE> documentation using bat.

  <LANGUAGE> refers to the language name or the following options:

  - Use "list" to view all available languages.

  - Use "update" to force update Lexy.

  - Use "modified" to view the last modified date of Lexy.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.
```

Lexy keeps a local copy of the documentation in `$HOME/.config/lexy`, which is created automatically the first time you run Lexy, and it will be updated every 60 days. You can force an update using "update" as `<LANGUAGE>`.
