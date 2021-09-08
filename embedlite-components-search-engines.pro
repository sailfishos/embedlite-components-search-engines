TEMPLATE = aux
include(common.pri)

search-engines.path = $$[QT_HOST_LIBS]/$$SEARCH_ENGINE_PATH
search-engines.files = list.json \
    google

INSTALLS += search-engines

OTHER_FILES += rpm/embedlite-components-search-engines.spec
