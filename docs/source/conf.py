# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Kits Application in XpertIO'
copyright = '2024, MEK Intellisys Pte Ltd'
author = 'MEK Intellisys'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_sidebars = {
    '**': [
        'index.html',
        'meki.html',
        'mekiIO.html',
        'mekiRegs.html',
        'mekiFunction.html',
        'mekiHVAC.html',
        'mekiLogic.html',
        'mekiMath.html',
        'mekiPriority.html',
        'mekiSchedule.html',
        'mekiTempTable.html',
        'mekiTiming.html',
        'mekiTypes.html',
        
    ]
}
# html_theme_options = {
#     'logo_only': False,
#     'display_version': True,
#     'prev_next_buttons_location': 'bottom',
#     'style_external_links': False,
#     'vcs_pageview_mode': '',
#     'style_nav_header_background': "#25BCEF",
#     # Toc options
#     'collapse_navigation': True,
#     'sticky_navigation': True,
#     'navigation_depth': 4,
#     'includehidden': True,
#     'titles_only': False
# }
# html_logo = '_static/cmpr (Custom).png'