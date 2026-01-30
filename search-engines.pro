TEMPLATE = aux
include(common.pri)

search-engines.path = $$[QT_HOST_LIBS]/$$SEARCH_ENGINE_PATH
search-engines.files = bing.xml \
                    ecosia.xml \
                    google.xml \
                    qwant.xml \
                    yahoo.xml \
                    yandex.xml

INSTALLS += search-engines
