TEMPLATE = aux
SEARCH_ENGINE_PATH = mozembedlite/chrome/embedlite/content

search-engines.path = $$[QT_HOST_LIBS]/$$SEARCH_ENGINE_PATH
search-engines.files = bing.xml \
                    google.xml \
                    yahoo.xml \
                    yandex.xml

INSTALLS += search-engines
