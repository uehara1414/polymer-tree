from urllib.parse import urljoin, urlparse
import sys

from anytree import Node, RenderTree
import requests
from bs4 import BeautifulSoup


class CustomElementTree:

    def __init__(self, url):
        self.tree = Node(url)

    def generate(self):
        self.dfs(self.tree)

    def to_abs_path(self, base, link):
        if link.startswith("http"):
            return link

        if link.startswith("//"):
            if "https://" in base:
                return "https:" + link
            else:
                return "http:" + link

        return urljoin(base, link)

    def get_imported_custom_element_path(self, node):
        html = requests.get(node.name).text
        soup = BeautifulSoup(html, "html.parser")
        for element in soup.find_all("link", rel="import"):
            url = self.to_abs_path(node.name, element.get("href"))
            yield url

    def dfs(self, parent: Node):
        for url in self.get_imported_custom_element_path(parent):
            node = Node(url, parent=parent)
            if "bower_components" not in node.name:
                self.dfs(node)

    def visualize(self):
        for pre, fill, node in RenderTree(self.tree):
            print("%s%s" % (pre, node.name))


def main():
    url = sys.argv[1]
    tree = CustomElementTree(url)
    tree.generate()
    tree.visualize()

if __name__ == '__main__':
    main()