import os


class HtmlBuilder(object):
    def __init__(self, directory):
        self.file = open(directory, 'w')
        self.file.write('<!DOCTYPE html><html><head><title>你好</title></head><body>')

    def build_file(self, name):
        self.file.write('<a')
        self.file.write(' href=\'')
        self.file.write(os.path.abspath(name))
        self.file.write('\'>')
        self.file.write(name)
        self.file.write('</a>')
        self.file.write("<br>")

    def build_path(self, name):
        self.file.write('<strong>')
        self.file.write(name)
        self.file.write('</strong>')
        self.file.write("<br>")

    def build_tab(self,i):
        for a in range(i):
            self.file.write('&nbsp;&nbsp;')

    def build_h1(self,s):
        self.file.write('<h1>'+s+'</h1>')

    def finish(self):
        self.file.write('</body></html>')
