"""This plugin provides tooltips for interpreters"""

import re
import urllib

import src.interpreter as interpreter
# All plugins should import the crunchy plugin API via interface.py
from src.interface import python_version, config, translate, plugin, Element
_ = translate['_']

borg_console = {}

provides = set(["/dir", "/doc"])

def register():
    '''registers two services and two http handlers: /dir and /doc'''
    plugin['register_service']("insert_tooltip", insert_tooltip)
    plugin['register_http_handler']("/dir%s" % plugin['session_random_id'],
                                    dir_handler)
    plugin['register_http_handler']("/doc%s" % plugin['session_random_id'],
                                    doc_handler)

def insert_tooltip(page, *dummy):
    '''inserts a (hidden) tooltip object in a page'''
    if not page.includes("tooltip_included") and page.body:
        borg_console[page.pageid] = interpreter.BorgConsole(group=page.pageid)

        page.add_include("tooltip_included")
        page.insert_js_file("/tooltip.js")
        page.add_js_code(tooltip_js)
        page.add_css_code(tooltip_css)

        tooltip = Element("div")
        tooltip.attrib["id"] = "tooltip"
        tooltip.text = " "
        tooltip.attrib["onmousedown"] = "grab(this);"
        page.body.append(tooltip)

        help_menu = Element("div")
        help_menu.attrib["id"] = "help_menu"
        help_menu.text = " "
        help_menu.attrib["onmousedown"] = "grab(this);"
        page.body.append(help_menu)

        help_menu_x = Element("div")
        help_menu_x.attrib["id"] = "help_menu_x"
        help_menu_x.attrib["onclick"] = "hide_help();"
        help_menu_x.text = "X"
        page.body.append(help_menu_x)

def dir_handler(request):
    """Examine a partial line and provide attr list of final expr"""

    if not config['dir_help']:
        request.send_response(204)
        request.end_headers()
        return

    if python_version < 3:
        line = re.split(r"\s", urllib.unquote_plus(request.data))[-1].strip()
    else:
        line = re.split(r"\s", urllib.unquote_plus(str(request.data)))[-1].strip()

    # Support lines like "thing.attr" as "thing.", because the browser
    # may not finish calculating the partial line until after the user
    # has clicked on a few more keys.
    line = ".".join(line.split(".")[:-1])

    pageid = request.args['uid'].split(":")[0]
    try:
        result = eval("dir(%s)" % line, {}, borg_console[pageid].__dict__['locals'])
    except:
        request.send_response(204)
        request.end_headers()
        return
    if type(result) == type([]):
        # strip private variables
        result = [a for a in result if not a.startswith("_")]

    # have to convert the list to a string
    result = repr(result)
    request.send_response(200)
    request.end_headers()
    request.wfile.write(result)
    request.wfile.flush()

def doc_handler(request):
    """Examine a partial line and provide sig+doc of final expr."""

    if not config['doc_help']:#configuration.defaults.doc_help:
        request.send_response(204)
        request.end_headers()
        return

    pageid = request.args['uid'].split(":")[0]

    if python_version < 3:
        line = re.split(r"\s", urllib.unquote_plus(request.data))[-1].strip()
    else:
        line = re.split(r"\s", urllib.unquote_plus(str(request.data)))[-1].strip()

    # Support lines like "func(text" as "func(", because the browser
    # may not finish calculating the partial line until after the user
    # has clicked on a few more keys.

    line = "(".join(line.split("(")[:-1])
    _locals = borg_console[pageid].__dict__['locals']
    if line in _locals:
        result = "%s()\n %s" % (line, _locals[line].__doc__)
    elif '__builtins__' in _locals:
        if line in _locals['__builtins__']:
            result = "%s()\n %s" % (line, _locals['__builtins__'][line].__doc__)
        else:
            request.send_response(204)
            request.end_headers()
            return
    else:
        result = _("builtins not defined in console yet.")

    request.send_response(200)
    request.end_headers()
    request.wfile.write(result)
    request.wfile.flush()
    return

# css
tooltip_css = """
#tooltip {
    position: fixed;
    top: 70px;
    right: 20px;
    width: 50%;
    overflow:auto;
    border: 4px outset #369;
    background-color: white;
    color: black;
    font: 9pt monospace;
    margin: 0;
    padding: 4px;
    padding-right: 30px;
    white-space: -moz-pre-wrap; /* Mozilla, supported since 1999 */
    white-space: -pre-wrap; /* Opera 4 - 6 */
    white-space: -o-pre-wrap; /* Opera 7 */
    white-space: pre-wrap; /* CSS3 - Text module (Candidate Recommendation)
                            http://www.w3.org/TR/css3-text/#white-space */
    word-wrap: break-word; /* IE 5.5+ */
    display: none;  /* will appear only when needed */
    z-index:11;
}
#help_menu {
    position: fixed;
    top: 70px;
    right: 1em;
    width: 50%;
    height: 50%;
    overflow:auto;
    border: 4px outset #369;
    background-color: white;
    color: black;
    font: 9pt monospace;
    margin: 0;
    padding: 4px;
    padding-right: 10px;
    white-space: -moz-pre-wrap; /* Mozilla, supported since 1999 */
    white-space: -pre-wrap; /* Opera 4 - 6 */
    white-space: -o-pre-wrap; /* Opera 7 */
    white-space: pre-wrap; /* CSS3 - Text module (Candidate Recommendation)
                            http://www.w3.org/TR/css3-text/#white-space */
    word-wrap: break-word; /* IE 5.5+ */
    display: none;  /* will appear only when needed */
    z-index:11;
}
#help_menu_x {
    position: fixed;
    top: 75px;
    right: 2em;
    color: #fe0;
    background-color: #369;
    font: 14pt sans-serif;
    cursor: pointer;
    padding: 4px 4px 0 4px;
    display: none;  /* will appear only when needed */
    z-index:12;
}
"""

# javascript code
tooltip_js = """
var session_id = "%s";
""" % plugin['session_random_id']