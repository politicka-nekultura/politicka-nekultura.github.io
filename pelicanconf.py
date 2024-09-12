import os

FILES_CATEGORY = list(f"category/{file}" for file in os.listdir("docs/category"))

FILES_TAG = list(f"tag/{file}" for file in os.listdir("docs/tag"))

AUTHOR = "politicka-nekultura"
SITENAME = "/* Politička nekultura */"
SITEURL = "https://politicka-nekultura.github.io"

PATH = "content"

TIMEZONE = "Europe/Zagreb"

DEFAULT_DATE = "fs"

DEFAULT_LANG = "hr"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

# Social widget

DEFAULT_PAGINATION = 10

OUTPUT_PATH = "docs"

THEME = "themes/politicka-nekultura"

# chunk theme settings
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

SITESUBTITLE = "Blog o političkoj kulturi i srodnim temama."

SINGLE_AUTHOR = True

FOOTER_TEXT = """
<a href="github.com/politicka-nekultura">GitHub</a><br>
Powered by Python and pelican.
"""

DISPLAY_CATEGORIES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
