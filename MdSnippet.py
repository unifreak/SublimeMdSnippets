import sublime, sublime_plugin
import re

debug = 1
def log(line):
    if debug:
        print(line)

log('----started mdsnippet----')

def inside_table_header(view):
    cursor = view.sel()[0].a
    cursor_row, _ = view.rowcol(cursor)
    next_line = view.substr(view.line(view.text_point(cursor_row + 1, 0)))
    return re.match(r'^\s*\|[-|]+\|+$', next_line)

def inside_table_body(view):
    cursor = view.sel()[0].a
    line = view.substr(view.line(cursor))
    return re.match(r'^\s*\|.+\|$', line)

def insert_snippet(view, snippet):
    view.run_command('clear_fields')
    return view.run_command('insert_snippet', {'contents': snippet})

class TabKeyHandler(sublime_plugin.EventListener):
    def on_query_context(self, view, key, op, operand, match_all):
        log('tab: %s' % key)
        cursor = view.sel()[0].a

        if (view.score_selector(cursor, 'markup.raw.block.fenced.markdown')
            or not view.score_selector(cursor, 'text.html.markdown')
            or not key.startswith('mdsnippet')):
            log('wrong scope %s' % view.scope_name(cursor))
            return None

        if key == 'mdsnippet.add_table_column' and not inside_table_header(view):
            log('not inside table header')
            return None

        return True

class EnterKeyHandler(sublime_plugin.EventListener):
    def on_query_context(self, view, key, op, operand, match_all):
        log('enter: %s' % key)
        cursor = view.sel()[0].a

        if (view.score_selector(cursor, 'markup.raw.block.fenced.markdown')
            or not view.score_selector(cursor, 'text.html.markdown')
            or not key.startswith('mdsnippet')):
            log('wrong scope %s' % view.scope_name(cursor))
            return None

        if key == 'mdsnippet.enter':
            return True

        return None

class ExpandMarkdownSnippetCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        expander = TabExpander()
        if not expander.expand(view, edit):
            if inside_table_body(view):
                view.run_command('next_field')
            else:
                user_settings = sublime.load_settings('Preferences.sublime-settings')
                view.run_command('insert_best_completion', {
                    'default': '\t',
                    'exact': user_settings.get('tab_completion', True)
                })

class TabExpander():
    def expand(self, view, edit):
        cursor = view.sel()[0].a
        trigger_region = view.word(cursor)
        trigger = view.substr(trigger_region).strip()
        trigger_line = view.substr(view.line(cursor)).strip()
        leading_region = sublime.Region(trigger_region.a - 5, trigger_region.a)
        log('trigger: %s' % trigger)
        log('trigger line: %s' % trigger_line)

        # see |||, expand table
        if re.match(r'^\s*\|\|\|$', trigger_line):
            view.erase(edit, trigger_region)
            snippet = '|${1:header}|${2:header}|\n|------|------|\n|${4:content}|${5:content}|\n'
            insert_snippet(view, snippet)
            return True

        # see something like ``js, expand code snippet
        if trigger_line.startswith('``'):
            settings = sublime.load_settings('MdSnippet.sublime-settings')
            lang = settings.get('lang_alias').get(trigger, trigger)
            if lang != '':
                view.erase(edit, trigger_region)

            snippet = '`%s\n${1:code}\n```\n' % lang
            insert_snippet(view, snippet)
            return True

        # see [[, expand url link
        if trigger.startswith('[['):
            view.erase(edit, trigger_region)
            snippet = '[${1:text}](${2:url} "${3:optional title}")'
            insert_snippet(view, snippet)
            return True

         # see ![, expand image link
        if trigger.startswith('!['):
            view.erase(edit, trigger_region)
            snippet = '![${1:alt text}](${2:img path} "${3:optional title}")'
            insert_snippet(view, snippet)
            return True

        return False

class AddTableColumnCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        log('--running add table column command:')
        view = self.view
        cursor = view.sel()[0].a
        cursor_row, _ = view.rowcol(cursor)

        for i in range(3):
            view.run_command('expand_selection', {'to': 'line'})

        old_regions = view.split_by_newlines(view.sel()[0])
        new_snippet = view.substr(old_regions[0]) + '${1:header}|\n'
        log('  old seperator:%s' % view.substr(old_regions[1]))
        new_snippet += view.substr(old_regions[1]).lstrip() + '------|\n'
        i = 2
        for item in view.substr(old_regions[2]).split('|'): # table body line
            if item == 'content':
                new_snippet += '|${%s:content}' % i
                i +=  1
        new_snippet += '|${%s:content}|\n' % i

        view.run_command('left_delete')
        view.run_command('insert_snippet', {'contents': new_snippet})

def add_table_row(view):
    log('--running add_table_row:')
    cursor = view.sel()[0].a
    line = view.substr(view.line(cursor))

    snippet = '\n'
    i = 1
    for item in line.split('|'):
        if len(item.strip()):
            log('  item:%s' % item)
            snippet += '|${%s:content}' % i
            i += 1
    snippet += '|\n'

    view.run_command('move', {'by': 'characters', 'forward': True})
    view.run_command('insert_snippet', {'contents': snippet})

class HandleEnterCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        if inside_table_header(view):
            return view.run_command("next_field")
        return add_table_row(view)
