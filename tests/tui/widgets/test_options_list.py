from papis.tui.widgets.list import *


def test_basic():
    ol = OptionsList(['hello', 'world', 'bye'])
    assert(ol.get_selection() == 'hello')
    assert(len(ol.marks) == 0)
    assert(len(ol.indices) == 3)
    ol.move_down()
    assert(ol.get_selection() == 'world')
    ol.move_up()
    assert(ol.get_selection() == 'hello')
    ol.mark_current_selection()
    assert(ol.marks == [0])
    ol.move_down()
    ol.move_down()
    ol.mark_current_selection()
    assert(ol.marks == [0, 2])
    ol.toggle_mark_current_selection()
    assert(ol.marks == [0])
    assert(ol.get_tokens() == [('', 'hello\n'), ('', 'world\n'), ('', 'bye\n')])
    assert(
        ol.get_line_prefix(2, None) ==
        [('class:options_list.selected_margin', '>')]
    )
    assert(
        ol.get_line_prefix(1, None) ==
        [('class:options_list.unselected_margin', ' ')]
    )
    assert(
        ol.get_line_prefix(0, None) ==
        [('class:options_list.marked_margin', '#')]
    )

    assert(ol.search_regex == re.compile('.*', re.I))
    ol.search_buffer.text = 'l'
    assert(ol.search_regex == re.compile('.*l', re.I))
    assert(ol.indices == [0, 1])
    ol.search_buffer.text = 'l  '
    assert(ol.search_regex == re.compile('.*l.*', re.I))
    assert(ol.indices == [0, 1])


    ol.options = [str(i) for i in range(1000)]
    assert(len(ol.marks) == 0)
    assert(len(ol.indices) == 1000)
    ol.go_bottom()
    assert(ol.get_selection() == '999')
    ol.go_top()
    assert(ol.get_selection() == '0')

    del ol