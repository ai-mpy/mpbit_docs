# 在这里添加任何Sphinx扩展模块名，作为字符串。它们可以是
# 扩展自带Sphinx（命名为‘ Sphinx .ext.*’）或您的自定义
# 的。

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinxcontrib.jquery",
]

# 添加任何包含模板的路径，相对于这个目录。
templates_path = ['_templates']
exclude_patterns = []

# 源文件名的后缀。
source_suffix = ".rst"

# 主toctree文档。
master_doc = "index"

project = 'LGBIT'
copyright = 'LGY'
author = 'bright'
version = release = '1.0'

# 要使用的pyents（语法高亮）样式的名称。
pygments_style = "sphinx"

# 全局包含文件。Sphinx文档建议优先使用rst_epilog
# 的rst_prolog，所以我们遵循。下面的绝对路径表示 "from the base of the doctree"
rst_epilog = """
.. include:: /templates/replace.inc
"""

# 修改输出目录配置
html_theme = 'sphinx_rtd_theme'
html_theme_path = ["."]
html_favicon = "static/favicon.ico"
html_static_path = ['static']
html_css_files = ['custom.css']
html_last_updated_fmt = "%d %b %Y"

# 添加这一行，将输出直接放在 docs 根目录
html_baseurl = 'https://ai-mpy.github.io/mpbit_docs/'
html_extra_path = ['.nojekyll']  # 防止 GitHub Pages 忽略下划线文件

html_theme_options = {
    'titles_only': True,
    'navigation_depth': 4
}
# html_additional_pages = {"index": "topindex.html"}

latex_elements = {
    "preamble": r"\setcounter{tocdepth}{2}",
}

intersphinx_mapping = {"python": ("https://docs.python.org/3.5", None)}

# 多语言配置
locale_dirs = ['locale/']
gettext_compact = False
language = 'zh_CN'