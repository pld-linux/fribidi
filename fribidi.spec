Summary:	Library implementing the Unicode BiDi algorithm
Name:		fribidi
Version:	0.1.14
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://imagic.weizmann.ac.il/~dov/freesw/FriBidi/%{name}-%{version}.tar.gz
Patch0:		%{name}-0.1.12-glib2.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	glib-devel >= 1.3.1
URL:		http://imagic.weizmann.ac.il/~dov/freesw/FriBidi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Free Implementation of the Unicode BiDi algorithm.

%package devel
Summary:	Library implementing the Unicode BiDi algorithm
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The fribidi-devel package includes the static libraries and header
files for the fribidi package.

Install fribidi-devel if you want to develop programs which will use
fribidi.

%package static
Summary:	Static %{name} libraries
Summary(pl):	Biblioteki statyczne %{name}
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static %{name} libraries.

%description -l pl static
Biblioteki statyczne %{name}.

%prep
%setup -q
%patch -p1

libtoolize --force --copy
autoconf
automake

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fribidi
%attr(755,root,root) %{_libdir}/libfribidi.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/fribidi-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/fribidi

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
