Name:    embedlite-components-search-engines
Version: 0.0.6
Release: 1
Summary: EmbedLite Components Search Engines
License: MPLv2
URL:     https://github.com/sailfishos/embedlite-components-search-engines
BuildArch: noarch
Source0: %{name}-%{version}.tar.gz
BuildRequires: qt5-qmake

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build

%qmake5 -r VERSION=%{version} embedlite-components-search-engines.pro
%make_build

%install
%qmake5_install

%files
%{_libdir}/mozembedlite/chrome/embedlite/content/*
