# mkdocs-bibtex

A [MkDocs](https://www.mkdocs.org/) plugin for citation management using bibtex, with Pandoc backend.

This plugin uses Pandoc, and processes not only the bibliography, but everything else 
that Pandoc can handle. It outputs Pandoc's "strict markdown", converting any 
tags/extensions that Pandoc can recognize into plain markdown.

## Setup

Install the plugin using pip:

```
git clone https://github.com/alexvoronov/mkdocs-bibtex.git
cd mkdocs-bibtex
pip install -e .
```

This version relies on Pandoc through [pypandoc](https://pypi.org/project/pypandoc/). 
Pypandoc provides Pandoc on many systems, otherwise, you have to install Pandoc manually, 
see pypandoc documentation for more details.

Next, add the following lines to your `mkdocs.yml`:

```yml
plugins:
  - search
  - bibtex-pandoc:
      bib_file: "refs.bib"
```

> If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set.

## Options

* `bib_file` - Name of your bibtex file. Either the absolute path or the path relative to `mkdocs.yml`.
* `csl_file` - Name of your [CSL](https://citationstyles.org/) file. Either the absolute path or the path relative to `mkdocs.yml`.
* `pandoc_output_format` - `markdown_strict` (default), `gfm` (github-flavored-markdown), `markdown-citation`, or any other [Pandoc output format (`--to` option)](https://pandoc.org/MANUAL.html#option--to) compatible with MkDocs.

## Usage

In your markdown files, add your citations as you would normally using ["pandoc"](https://pandoc.org/MANUAL.html#citations) style. 
Citations go inside square brackets and are separated by semicolons. 
Each citation must have a key, composed of ‘@’ + the citation identifier from the database.

If the style calls for a list of works cited, it will be placed in a div with id `refs`, if one exists:
```markdown
::: {#refs}
:::
```
Otherwise, it will be placed at the end of the document.
