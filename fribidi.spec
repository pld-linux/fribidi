%define	snap	20011029
Summary:	Library implementing the Unicode BiDi algorithm
Summary(pl.UTF-8):	Biblioteka implementująca algorytm Unicode BiDi
Name:		fribidi
Version:	0.10.4
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/fribidi/%{name}-%{version}.tar.bz2
# Source0-md5:	0f6e7ecca08e6e108dc06337f5b5cabf
URL:		http://fribi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Obsoletes:	libfribidi0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Free Implementation of the Unicode BiDi algorithm.

%description -l pl.UTF-8
Implementacja algorytmu Unicode BiDi.

%package devel
Summary:	Library implementing the Unicode BiDi algorithm
Summary(pl.UTF-8):	Implementacja algorytmu Unicode BiDi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libfribidi0-devel

%description devel
The fribidi-devel package includes header files for the fribidi
package.

Install fribidi-devel if you want to develop programs which will use
fribidi.

%description devel -l pl.UTF-8
Pliki developerskie pozwalające na wykorzystywanie biblioteki fribidi
w swoim oprogramowaniu.

%package static
Summary:	Static %{name} libraries
Summary(pl.UTF-8):	Biblioteki statyczne %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} libraries.

%description static -l pl.UTF-8
Biblioteki statyczne %{name}.

%prep
%setup -q

%build
rm -f missing acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/fribidi
%attr(755,root,root) %{_libdir}/libfribidi.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fribidi-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/fribidi
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
