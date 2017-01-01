import unittest

from pt import CustomElementTree


class Test(unittest.TestCase):

    def test_create_hakobus_tree_correctly(self):
        url = "http://h4k0bu5.hatu.ga/"
        root = CustomElementTree(url)
        root.generate()

        self.assertEqual(root.tree.name, "http://h4k0bu5.hatu.ga/")
        self.assertEqual(root.tree.children[0].name, 'http://h4k0bu5.hatu.ga/x-app.html')

        self.assertSetEqual({child.name for child in root.tree.children[0].children}, {
            'http://h4k0bu5.hatu.ga/bower_components/app-layout/app-header-layout/app-header-layout.html',
            'http://h4k0bu5.hatu.ga/bower_components/app-layout/app-header/app-header.html',
            'http://h4k0bu5.hatu.ga/bower_components/app-layout/app-scroll-effects/app-scroll-effects.html',
            'http://h4k0bu5.hatu.ga/bower_components/app-layout/app-toolbar/app-toolbar.html',
            'http://h4k0bu5.hatu.ga/bower_components/iron-ajax/iron-ajax.html',
            'http://h4k0bu5.hatu.ga/bower_components/iron-flex-layout/iron-flex-layout.html',
            'http://h4k0bu5.hatu.ga/bower_components/iron-icon/iron-icon.html',
            'http://h4k0bu5.hatu.ga/bower_components/iron-icons/iron-icons.html',
            'http://h4k0bu5.hatu.ga/bower_components/paper-spinner/paper-spinner.html',
            'http://h4k0bu5.hatu.ga/bower_components/polymer/polymer.html',
            'http://h4k0bu5.hatu.ga/bower_components/vaadin-combo-box/vaadin-combo-box.html'
        })
