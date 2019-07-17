#
# openSUSE RPM spec for tcl-duktype
#

%define pkgname duktype

Name:           tcl-duktape
Version:        0.7.0
Summary:        Tcl bindings for Duktape
Release:        0
License:        MIT
Group:          Development/Libraries/Tcl
Url:            https://github.com/dbohdan/tcl-duktape.git
BuildRequires:  tcl >= 8.5
BuildRequires:  tcl-devel >= 8.5
BuildRequires:  make
BuildRequires:  gcc
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This Tcl extension provides bindings for Duktape,
a JavaScript interpreter library.

%prep
%setup -q -n %{name}-%{version}

%build
./configure
make

%install
mkdir -p %{buildroot}%{tcl_archdir}/%{pkgname}%{version}
cp libtclduktape.so %{buildroot}%{tcl_archdir}/%{pkgname}%{version}
cp pkgIndex.tcl %{buildroot}%{tcl_archdir}/%{pkgname}%{version}
cp ./lib/oo.tcl %{buildroot}%{tcl_archdir}/%{pkgname}%{version}
cp ./lib/utils.tcl %{buildroot}%{tcl_archdir}/%{pkgname}%{version}

%files
%doc README.md LICENSE
%{tcl_archdir}/%{pkgname}%{version}

%changelog

