# Stick with Markdown Snippets

我们都喜欢 markdown 简洁的语法, 不过的确有几个语法并非 "那么" 简洁, 比如表格, 代码块儿, 链接等...

这个扩展可以简化这些复杂语法

虽然已经有很多相关插件了, 但是我仍然写这个插件, 是因为想 **尽量以 markdown 风格的语法** 来简化

## 特性

- Markdown 风格语法的 snippets
- 简化表格, 代码块儿, url 及图片链接的生成
- 动态添加表格列和行
- 可配置的代码片段语言别名

## 安装

有两种方式可以安装, 第一种是通过 `Package Control`:

1. 确保装有 Package Control, 参见 <https://packagecontrol.io/installation>
2. 打开命令面板 (command pallete), 运行 `Package Control: Install Pacakge`
2. 搜索 `Stick With Markdown Snippets` 并安装

另一种方式是直接通过克隆源码安装:

1. 进入 sublime text 的包目录
2. 运行 `git clone https://github.com/UniFreak/SublimeMdSnippets.git`

## 用法

这个插件提供了四种快捷语法: 表格, 代码块儿, url 链接以及图片链接. 输入相应的触发文本, 然后按 <kbd>tab</kbd> 即可生成对应语法

### 表格

触发文本: `|||`

生成结果:

```
|header|header|
|------|------|
|content|content|
```

为了更方便使用, **你还可以动态的添加表格的列和行**:

- 当光标处于最后一个表头单元格时, 使用 <kbd>tab</kbd> 添加新列, 使用 <kbd>enter</kbd> 移到表格体
- 当光标处于最后一个表格体单元格时, 使用 <kbd>enter</kbd> 添加新行, 使用 <kbd>tab</kbd> 移出表格编辑

这个动图能讲的更明白:

![table gif](https://github.com/UniFreak/SublimeMdSnippets/blob/master/shot.gif)

### 代码块儿

触发文本: <code>``</code>.

生成结果:

<pre>
```
code
```
</pre>

你也可以 **指定语言别名** 如 <code>``js</code>, 则生成如下:

<pre>
```javascript
code
```
</pre>

通过编辑插件的配置, 你可可以自定义语言别名. 默认配置如下:

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

### 图片链接

触发文本: `![`

生成结果: `![alt text](img path "optional title")`

### Url 链接

触发文本: `[[`

生成结果: `[text](url "optional title")`

