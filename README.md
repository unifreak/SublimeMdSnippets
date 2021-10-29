# Stick with Markdown Snippets

_中文请见 [这里](https://github.com/UniFreak/SublimeMdSnippets/blob/master/README.cn.md "中文 README")_

We love the simplicity of markdown syntax, but there are a few that are actually complex, like table, code block, and links...

This plugin come to rescue

Though obviously there are other markdown snippets plugins out there, but this plugin **try to stick with markdown flavour syntax**

## Feature

- Stick with markdown syntax snippets
- Simplify table, code block, url and image link creation
- Dynamically add table column and row
- Configurable code block language alias

## Installation

There are two ways to install, the first and recommended way is via `Package Control`:

1. Make sure you have `Package Control` installed, see <https://packagecontrol.io/installation>
2. Open Command Pallete, and run `Package Control: Install Package`
2. Search for `Stick With Markdown Snippets` and install

Another way is to clone source from github:

1. Browse into your sublime text's package folder
2. Run `git clone https://github.com/UniFreak/SublimeMdSnippets.git`

## Usage

This plugin provide four snippet: table, code block, url link and image link. Just type in trigger then press <kbd>tab</kbd> to generate

**NOTE**: After updating of `Markdown Editing`, I found that snippet trigger \`\`
doesn't work anymore. To fix this, you can open its user's key binding setting and
find these lines and comment out them:

```
{ "keys": ["`"], "command": "run_macro_file", "args": {"file": "Packages/MarkdownEditing/macros/Skip Closing Character.sublime-macro"}, "context":
 [
     { "key": "selection_empty", "operator": "equal", "operand": true, "match_all": true },
     { "key": "following_text", "operator": "regex_contains", "operand": "^`", "match_all": true },
     { "key": "selector", "operator": "equal", "operand": "text.html.markdown", "match_all": true }
 ]
},
```

### Table

Trigger by: `|||`

Result in:

```
|header|header|
|------|------|
|content|content|
```

More conveniently, **you can add table column and table row dynamically**:

- when cursor in last header cell, use <kbd>tab</kbd> to add column, use <kbd>enter</kbd> to move to table body
- when cursor in last table body cell, use <kbd>enter</kbd> to add row, use <kbd>tab</kbd> to tab out the table snippet

This gif will make things clear

![table gif](https://raw.githubusercontent.com/UniFreak/SublimeMdSnippets/master/shot.gif)

### Code Block

Trigger by: <code>``</code>.

Result in:

<pre>
```
code
```
</pre>

You can also **specify language alias** like <code>``js</code>, then it will be expand to

<pre>
```javascript
code
```
</pre>

You can specify language alias in setting file. Default setting is like this:

```
{
    "lang_alias": {
        "js": "javascript",
        "py": "python",
        "md": "markdown",
        "rb": "ruby"
    }
}
```

### Image Link

Trigger by: `![`

Result in: `![alt text](img path "optional title")`

### Url Link

Trigger by: `[[`

Result in: `[text](url "optional title")`

