# 获取文件列表，写入html
import os
import HtmlBuilder

root_path = os.path.curdir
html_builder = HtmlBuilder.HtmlBuilder('dir.html')


def generate_html(path):

    os.chdir(path)
    for file in os.listdir(os.curdir):
        # file = os.path.join(path, file)
        if os.path.isdir(file):
            html_builder.build_tab(0)
            html_builder.build_path(file)
            generate_html(os.path.abspath(file))
            os.chdir(os.pardir)
        elif os.path.isfile(file):
            html_builder.build_tab(1)
            html_builder.build_file(file)

html_builder.build_h1('Directory')
generate_html(root_path)

html_builder.finish()
