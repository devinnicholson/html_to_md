# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from markdownify import markdownify as md
from bs4 import BeautifulSoup
import sys

def markdown_html(html_file):
    read_file = open(html_file, "r")
    html_file = html_file.strip(".htm")
    md_file = open(html_file + ".md", "w")

    lines = read_file.read()
    read_file.close()
    md_file.write( md(lines) )

    return md_file

if __name__ == "__main__":
    markdown_html(sys.argv[1])
