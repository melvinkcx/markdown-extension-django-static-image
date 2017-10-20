"""
Markdown extension for modifying local links to Django static links
Author: Melvin Koh

"""

import markdown
import unittest

from django_static_image import *


class DjangoStaticImageTest(unittest.TestCase):
    """ Test if extension works as expected """
    def test_img_tag_without_src(self):
        """ This test tests if the extension parses image without source as expected """
        text = """![profile_pic]()"""
        expected_html = """<p><img alt="profile_pic" src="" /></p>"""

        md = markdown.Markdown(extensions=[DjangoStaticImageExtension()])
        html = md.convert(text)
        self.assertEqual(html, expected_html)

    def test_img_tag_with_local_source(self):
        """ This test tests if the extension parses local source as expected """
        text = """![profile_pic](images/profile_pic.png)"""
        expected_html = """<p><img alt="profile_pic" src="{% static 'images/profile_pic.png' %}" /></p>"""

        md = markdown.Markdown(extensions=[DjangoStaticImageExtension()])
        html = md.convert(text)
        self.assertEqual(html, expected_html)

    def test_img_tag_with_external_source(self):
        """ This test tests if the extension ignores image with external source """
        text = """![profile_pic](https://melvinkoh.herokuapp.com/static/images/profile_pic.png)"""

        expected_html = """<p><img alt="profile_pic" src="https://melvinkoh.herokuapp.com/static/images/profile_pic.png" /></p>"""

        md = markdown.Markdown(extensions=[DjangoStaticImageExtension()])
        html = md.convert(text)
        self.assertEqual(html, expected_html)

    def test_extension_config(self):
        """ This test tests if Prefix configuration works as expected """
        pass

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(DjangoStaticImageTest)
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_suite)
