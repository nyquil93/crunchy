""" configuration.py:
    Keeps track of user based settings, some automatically set
    by Crunchy, others ajustable by the user.
"""

### Important:
#
# In order to reduce the list of variables displayed in the popup
# "tooltip" when the user enters "crunchy.", some methods have been
# prefixed by a leading underscore; Crunchy (in tooltip.py) filters
# out such methods from the display.

import os
from urlparse import urlsplit
import cPickle

from src.interface import config, u_print, translate, additional_vlam

ANY = '*'

_ = translate['_']
translate['init_translation']()

# Existing translations for Crunchy messages
trans_path = os.path.join(config['crunchy_base_dir'], "translations")
trans_path2 = os.path.join(config['crunchy_base_dir'], "server_root",
                                                          "edit_area", "langs")
options = {
    'power_browser': ['None'],
    'security': [ 'trusted', 'display trusted',
                  'normal', 'display normal',
                  'strict', 'display strict'],
    'no_markup': ["none"],
    'override_default_interpreter' : ['default'],
    # allow languages values like "en" or "en_GB"
    'languages': [f for f in os.listdir(trans_path)
                             if (len(f)==2 or (len(f) == 5 and f[2] == '_'))
                                    and not f.startswith('.')],
    # language file names end in ".js"
    'editarea_languages': [f[0:-3] for f in os.listdir(trans_path2)
                             if (len(f)==5 or (len(f) == 8 and f[2] == '_'))
                                    and not f.startswith('.')]
}

def make_property(name, allowed, default=None):
    '''creates properties within allowed values (if so specified)
       with some defaults, and enables automatic saving of new values'''
    if default is None:
        default = allowed[0]

    def fget(obj):
        '''simply returns the attribute for the requested object'''
        return getattr(obj, "_"+name)

    def _set_and_save(obj, _name, value, initial=False):
        '''sets the value and make the required call to save the new status'''
        setattr(obj, "_" + _name, value)
        getattr(obj, '_save_settings')(_name, value, initial)
        return

    def _only_set_and_save_if_new(obj, name, val):
        '''sets the value (and save the new status) only if there is
           a change from the current value; this is to prevent
           needlessly writing to files'''
        try:  # don't save needlessly if there is no change
            current = getattr(obj, "_"+name)
            if val == current:
                return
            else:
                _set_and_save(obj, name, val)
        except:
            _set_and_save(obj, name, val)
        return

    def fset(obj, val):
        '''assigns a value within an allowed set (if defined),
           and saves the result'''
        prefs = getattr(obj, "_preferences")
        # some properties are designed to allow any value to be set to them
        if ANY in allowed and val != ANY:
            allowed.append(val)

        if val not in allowed:
            try:
                current = getattr(obj, "_"+name) # can raise AttributeError
                                                   # if not (yet) defined...
                u_print(_("%s is an invalid choice for %s.%s") % (val,
                                                        prefs['_prefix'], name))
                u_print(_("The valid choices are: "), allowed)
                u_print(_("The current value is: "), current)
            except AttributeError: # first time; set to default!
                _set_and_save(obj, name, default, initial=True)
        else:
            if val == ANY:
                try:
                    current = getattr(obj, "_"+name)
                except:
                    current = default
                val = current
            _only_set_and_save_if_new(obj, name, val)
        return
    return property(fget, fset)

class Base(object):
    '''Base class for all objects that keeps track of
       configuration values in properties.  On its own, it does nothing;
       see test_configuration.rst for sample uses.'''

    def _init_properties(self, cls):
        '''automatically assigns all known properties.'''
        # Note: properties are class variables which is why we need
        # to pass the class name as a parameter.
        for key in cls.__dict__:
            val = cls.__dict__[key]
            if isinstance(val, property):
                val.fset(self, ANY)
        return

    def _save_settings(self, name, value, initial=False):
        '''dummy function; needs to be defined by subclass'''
        raise NotImplementedError


class Defaults(Base):
    """
    class containing various default values:
        dir_help: interactive help for Borg consoles
        doc_help: interactive help for Borg consoles
        forward_accept_language: respecting user's webbrowser's language option
                                 settings
        friendly: traceback settings
        user_dir: home user directory
        temp_dir: temporary (working) directory
        nm: no_markup option, i.e. default mode to use when the user has
            not specied a vlam keyword
        language: language to use for feedback to user - and anything
            else that might have been translated.
        editarea_language: language used for ui of editarea

        security: level of filtering of web pages

        my_style: enables preferred styling of Python code, etc.
        alternate_python_version: path of an alternate Python interpreter

    This class is instantiated [instance name: defaults] within this module.
    """
    def __init__(self, prefs):
        self._preferences = prefs
        self._preferences.update({'_prefix': 'crunchy',
                            'page_security_level': self.page_security_level,
                            '_set_site_security': self._set_site_security})
        self._not_saved = self._preferences.keys()
        self._not_saved.extend(['user_dir', 'temp_dir', 'log', 'logging_uids',
                                'symbols', 'get_current_page_security_level'])

        self.site_security = {}
        self.styles = {}
        self._preferences.update({'site_security': self.site_security,
                            'styles': self.styles})

        self._set_dirs()
        # self.logging_uids is needed by comitIO.py:87
        self.logging_uids = {}  # {uid : (name, type)}
                               # name is defined by tutorial writer
                               # type is one of 'interpreter', 'editor',...
        # the following two variables will be replaced by Tao's improved logging
        self.log_filename = os.path.join(os.path.expanduser("~"),
                                          "crunchy_log.html")
        self.log = {}
        # Make sure to initialize properties so that they exist before
        # retrieving saved values
        self._not_loaded = True
        self._init_properties(Defaults)
        self._load_settings()

    dir_help = make_property('dir_help', [True, False])
    doc_help = make_property('doc_help', [True, False])
    forward_accept_language = make_property('forward_accept_language',
                                            [True, False])
    friendly = make_property('friendly', [True, False])
    _trans_path = os.path.join(config['crunchy_base_dir'], "translations")
    override_default_interpreter = make_property('override_default_interpreter',
                                    options['override_default_interpreter'])
    language = make_property('language', options['languages'], default='en')
    editarea_language = make_property('editarea_language',
                                    options['editarea_languages'], default='en')
    local_security = make_property('local_security', options['security'])
    no_markup = make_property('no_markup', options['no_markup'],
                              default='python_tutorial')
    power_browser = make_property('power_browser', options['power_browser'])
    my_style = make_property('my_style', [False, True])
    alternate_python_version = make_property('alternate_python_version', [ANY],
                                             default="python")
    user_dir = make_property('user_dir', [ANY])
    temp_dir = make_property('temp_dir', [ANY])

    def _set_dirs(self): # "tested"; i.e. called in unit tests.
        '''sets the user directory, creating it if needed.
           Creates also a temporary directory'''
        home = os.path.expanduser("~")
        self._user_dir = os.path.join(home, ".crunchy")
        self._temp_dir = os.path.join(home, ".crunchy", "temp")

        # hack to make it work for now.
        self.user_dir = self._user_dir
        self.temp_dir = self._temp_dir

        if not os.path.exists(self._user_dir):  # first time ever
            try:
                os.makedirs(self._user_dir)
                if not os.path.exists(self._temp_dir):
                    try:
                        os.makedirs(self._temp_dir)
                    except:
                        # Note: we do not translate diagnostic messages
                        # sent to the terminal
                        u_print("Created successfully home directory.")
                        u_print("Could not create temporary directory.")
                        self._temp_dir = self._user_dir
                    return
            except:
                u_print("Could not create the user directory.")
                self._user_dir = os.getcwd()  # use crunchy's as a default.
                self._temp_dir = os.path.join(self._user_dir, "temp")
                if not os.path.exists(self._temp_dir):
                    try:
                        os.makedirs(self._temp_dir)
                    except:
                        u_print("Could not create temporary directory.")
                        self._temp_dir = self._user_dir
                    return
                return
        # we may encounter a situation where a ".crunchy" directory
        # had been created by an old version without a temporary directory
        if not os.path.exists(self._temp_dir):
            try:
                os.makedirs(self._temp_dir)
            except:
                u_print("home directory '.crunchy' exists; however, ")
                u_print("could not create temporary directory.")
                self._temp_dir = self._user_dir
            return
        return

    def _load_settings(self):
        '''
        loads the user settings from a configuration file; uses default
        values if file specific settings is not found.
        '''
        success = False
        pickled_path = os.path.join(self._user_dir, "settings.pkl")
        try:
            pickled = open(pickled_path, 'rb')
            success = True
        except:
            u_print("No configuration file found.")
            print "user_dir = ", self._user_dir
        if success:
            try:
                saved = cPickle.load(pickled)
                pickled.close()
            except EOFError:
                self._not_loaded = False
                self._save_settings()
                return
        else:
            # save the file with the default value
            self._not_loaded = False
            self._save_settings()
            return

        for key in saved:
            try:
                val = Defaults.__dict__[key]
                if isinstance(val, property):
                    val.fset(self, saved[key])
                else:
                    print "*"*50
                    print "Unless Crunchy has just been updated,"
                    print "this should not happen."
                    print "saved variable: %s is not a property", key
            except:
                try:
                    val = getattr(self, key)
                    setattr(self, key, saved[key])
                    self._preferences[key] = saved[key]
                except:
                    print "*"*50
                    print "Unless Crunchy has just been updated,"
                    print "this should not happen."
                    print "saved variable: %s is not recognized" % key
        self._not_loaded = False
        return

    def _save_settings(self, name=None, value=None, initial=False):
        '''Update user settings and save results to a configuration file'''
        if name is not None: # otherwise, we need to save all...
            self._preferences[name] = value
            if initial:
                return
            if self._not_loaded:  # saved configuration not retrieved; do not overwrite
                return

        # update values of non-properties
        self._preferences['site_security'] = self.site_security
        self._preferences['styles'] = self.styles
        saved = {}
        for name in self._preferences:
            if name not in self._not_saved:
                saved[name] = self._preferences[name]
        pickled_path = os.path.join(self._user_dir, "settings.pkl")
        try:
            pickled = open(pickled_path, 'wb')
        except:
            u_print("Could not open file in configuration._save_settings().")
            return
        cPickle.dump(saved, pickled)
        pickled.close()
        return

    def page_security_level(self, url):
        info = urlsplit(url)
        # info.netloc == info[1] is not Python 2.4 compatible; we "fake it"
        info_netloc = info[1]
        if info_netloc == '':
            level = self.local_security
        else:
            level = self._get_site_security(info_netloc)
        self.current_page_security_level = level
        return level

    def get_current_page_security_level(self):
        return self.current_page_security_level

    def _get_site_security(self, site):
        if site in self.site_security:
            return self.site_security[site]
        else:
            return 'display trusted'

    def _set_site_security(self, site, choice):
        if choice in options['security']:
            self.site_security[site] = choice
            self._save_settings('site_security', choice)
            u_print(_("site security set to: ") , choice)
        else:
            u_print((_("Invalid choice for %s.site_security") %
                                                         self._preferences['_prefix']))
            u_print(_("The valid choices are: "), str(security_allowed))

    def add_site(self):
        '''interactive function to facilitate adding new site to
           the secured list'''
        site = raw_input(_("Enter site url (for example, docs.python.org) "))
        level = raw_input(_("Enter security level (for example: normal) "))
        self._set_site_security(site, level)

    #==============

def init():
    for key in additional_vlam:
        options[key].extend(additional_vlam[key])
    defaults = Defaults(config)

    config['log'] = defaults.log
    config['logging_uids'] = defaults.logging_uids
    config['symbols'] = {config['_prefix']:defaults, 'temp_dir': defaults.temp_dir}
    config['get_current_page_security_level'] = defaults.get_current_page_security_level

    #import pprint
    #pprint.pprint(config)

    # the following may be set as an option when starting Crunchy
    if 'initial_security_set' not in config:
        config['initial_security_set'] = False