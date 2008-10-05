"""  power_browser.py plugin.

Allow the user to always insert a file/url browser at the top of a page.
Also includes a link to the browsers page in the menu.
"""

# All plugins should import the crunchy plugin API via interface.py
from src.interface import plugin, config, Element, SubElement, translate, \
   additional_menu_items
_ = translate['_']

def register(): # tested
    """The register() function is required for all plugins.
       """
    plugin['register_end_pagehandler'](insert_browser)
    plugin['register_begin_pagehandler'](add_browsing_to_menu)

def add_browsing_to_menu(dummy):
    '''adds a menu item allowing the user to go the the browsers page'''
    menu_item = Element("li")
    link = SubElement(menu_item, 'a', href="/docs/basic_tutorial/browsing.html")
    link.text = _("Browsing")
    additional_menu_items['browsing'] = menu_item

def insert_browser(page, *dummy): # tested
    '''Inserts a default file/url browser at the top of a page'''
    div = Element("div")
    div.text = ' '

    if config[page.username]['power_browser'] is None:
        return
    else:
        try:
            plugin[config[page.username]['power_browser']](page, div, 'dummy')
            page.body.insert(0, div)
        except: # unrecognized value, just ignore... (see below)
            return

# Why ignoring the exception?  Perhaps the browser requested is not available.
# For example, suppose the user upgrades to a new Python version but do not
# install docutils. As a result, she will not be able to process rst files.
# However, she could have set the configuration to include an rst browser
# while using a previous version of Python ...