import pelican, re

def init(pelican_object):
    global fa_prog, fa_replace
    # Search for :fa<type>-<icon>:, such as :fas-paw: or :fab-twitter:
    pattern = r':fa(?P<type>[bsr])-(?P<icon>[a-z0-9_]+):'
    fa_prog = re.compile(pattern)
    fa_replace = "<i class=\"fa\g<type> fa-\g<icon>\"></i>"

def replace(content):
    fileext = str(content).split('.')[-1].lower()
    if fileext in ['md','html','rst','txt']:
        try:
            content._content = fa_prog.sub(fa_replace, content._content)
        except:
            print("Something went wrong editing {} for simple-fa, sorry".format(str(content)))

def register():
    pelican.signals.initialized.connect(init)
    pelican.signals.content_object_init.connect(replace)