#
# openSUSE RPM spec for tcl-duktype
#

%define pkgname duktype

Name:           tcl-duktape
Version:        0.3.3
Summary:        Tcl bindings for Duktape
Release:        0
License:        MIT
Group:          Development/Libraries/Tcl
Url:            https://github.com/dbohdan/tcl-duktape.git
BuildRequires:  tcl >= 8.5
BuildRequires:  make
BuildRequires:  gcc
Source:         %{name}-%{version}.tar.gz
Patch0:         pkgIndex.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This Tcl extension provides bindings for Duktape,
a JavaScript interpreter library.

%prep
%setup -q -n %{name}-%{version}
%patch0

%build
./configure
make

%install
mkdir -p %{buildroot}%{tcl_archdir}/%{pkgname}-%{version}
cp libtclduktape.so %{buildroot}%{tcl_archdir}/%{pkgname}-%{version}
cp pkgIndex-libdir.tcl %{buildroot}%{tcl_archdir}/%{pkgname}-%{version}/pkgIndex.tcl
cp oo.tcl %{buildroot}%{tcl_archdir}/%{pkgname}-%{version}
cp utils.tcl %{buildroot}%{tcl_archdir}/%{pkgname}-%{version}


%files
%doc README.md LICENSE
%{tcl_archdir}/%{pkgname}-%{version}

%changelog

