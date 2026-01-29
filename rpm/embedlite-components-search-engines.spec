Name:    embedlite-components-search-engines
Version: 0.0.6
Release: 1
Summary: EmbedLite Components Search Engines
License: MPLv2
URL:     https://github.com/sailfishos/embedlite-components-search-engines
BuildArch: noarch
Source0: %{name}-%{version}.tar.gz

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%install
mkdir -p %{buildroot}%{_libdir}/mozembedlite/chrome/embedlite/content
install -m 644 -p -t %{buildroot}%{_libdir}/mozembedlite/chrome/embedlite/content *.xml

%files
%{_libdir}/mozembedlite/chrome/embedlite/content/*
