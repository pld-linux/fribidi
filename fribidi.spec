%define	snap	20011029
Summary:	Library implementing the Unicode BiDi algorithm
Summary(pl):	Biblioteka implementuj╠ca algorytm Unicode BiDi
Name:		fribidi
Version:	0.10.0
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Source0:	http://telia.dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}.pc
Patch0:		%{name}-am_ac.patch
URL:		http://fribi.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	glib2-devel >= 1.3.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libfribidi0

%description
A Free Implementation of the Unicode BiDi algorithm.

%description -l pl
Implementacja algorytmu Unicde BiDi.

%package devel
Summary:	Library implementing the Unicode BiDi algorithm
Summary(pl):	Implementacja algorytmu Unicode BiDi
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}
Requires:	glib2-devel
Obsoletes:	libfribidi0-devel

%description devel
The fribidi-devel package includes header files for the fribidi
package.

Install fribidi-devel if you want to develop programs which will use
fribidi.

%description -l pl devel
Pliki developerskie pozwalaj╠ce na wykorzystywanie biblioteki fribidi
w swoim oprogramowaniu.

%package static
Summary:	Static %{name} libraries
Summary(pl):	Biblioteki statyczne %{name}
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
Static %{name} libraries.

%description -l pl static
Biblioteki statyczne %{name}.

%prep
%setup -q
%patch0 -p1

%build
rm -f acinclude.m4
libtoolize --force --copy
aclocal
autoheader
autoconf
automake -a -c
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pkgconfigdir}

install %{SOURCE1}	$RPM_BUILD_ROOT%{_pkgconfigdir}/%{name}.pc

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README THANKS TODO

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
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/fribidi
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
