#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	GNU FriBidi - library implementing the Unicode BiDi algorithm
Summary(pl.UTF-8):	GNU FriBidi - biblioteka implementująca algorytm Unicode BiDi
Name:		fribidi
Version:	1.0.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/fribidi/fribidi/releases
Source0:	https://github.com/fribidi/fribidi/releases/download/v%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	ad74503b4c88091544f19308f517d3fc
URL:		https://fribidi.org/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
Obsoletes:	libfribidi0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU FriBidi is a free Implementation of the Unicode BiDi algorithm.

%description -l pl.UTF-8
GNU FriBidi to wolnodostępna implementacja algorytmu Unicode BiDi.

%package devel
Summary:	Header files for FriBidi library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki FriBidi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libfribidi0-devel

%description devel
The fribidi-devel package includes header files for the fribidi
package.

%description devel -l pl.UTF-8
Pliki programistyczne pozwalające na wykorzystywanie biblioteki
fribidi w swoim oprogramowaniu.

%package static
Summary:	Static FriBidi library
Summary(pl.UTF-8):	Biblioteka statyczna FriBidi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static FriBidi library.

%description static -l pl.UTF-8
Biblioteka statyczna FriBidi.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}

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
%attr(755,root,root) %ghost %{_libdir}/libfribidi.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfribidi.so
%{_libdir}/libfribidi.la
%{_includedir}/fribidi
%{_pkgconfigdir}/fribidi.pc
%{_mandir}/man3/fribidi_*.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libfribidi.a
%endif
