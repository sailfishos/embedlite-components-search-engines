Name:    embedlite-components-search-engines
Version: 0.0.1
Release: 1
Summary: EmbedLite Components Search Engines
Group:   Applications/Internet
License: MPLv2
URL:     https://git.merproject.org/mer-core/embedlite-components-search-engines
BuildArch: noarch
Source0: %{name}-%{version}.tar.gz
BuildRequires: qt5-qmake

%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build

%qtc_qmake5 -r VERSION=%{version} embedlite-components-search-engines.pro
%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
%qmake5_install

%files
%defattr(-,root,root,-)
%{_libdir}/mozembedlite/chrome/embedlite/content/*
