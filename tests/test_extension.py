"""
Markdown extension for modifying local links to Django static links
Author: Melvin Koh

"""

import markdown
import unittest


class DjangoStaticImageTest(unittest.TestCase):
    """ Test if extension works as expected """
    def test_img_tag_without_src(self):
        """ This test tests if the extension parses image without source as expected """
        md = "![profile_pic]()"

    def test_img_tag_with_local_source(self):
        """ This test tests if the extension parses local source as expected """
        md = "![profile_pic](images/profile_pic.png)"

    def test_img_tag_with_external_source(self):
        """ This test tests if the extension ignores image with external source """
        md = "![profile_pic](https://melvinkoh.herokuapp.com/static/images/profile_pic.png)"

    def test_extension_config(self):
        """ This test tests if Prefix configuration works as expected """
        pass