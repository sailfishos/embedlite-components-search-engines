TEMPLATE = aux
include(common.pri)

search-engines.path = $$[QT_HOST_LIBS]/$$SEARCH_ENGINE_PATH
search-engines.files = bing.xml \
                    google.xml \
                    yahoo.xml \
                    yandex.xml

INSTALLS += search-engines
