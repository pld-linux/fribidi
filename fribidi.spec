Summary:	Library implementing the Unicode BiDi algorithm
Name:		fribidi
Version:	0.1.12
Release:	2
License:	LGPL
Group:		Libraries
Group(pl):	Biblioteki
Source0:	http://imagic.weizmann.ac.il/~dov/freesw/FriBidi/fribidi-%{version}.tar.gz

#Patch1:		fribidi-0.1.12-gtkbeta.patch

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL:		http://imagic.weizmann.ac.il/~dov/freesw/FriBidi
## this spec is prepared for glib,gtk 2.0
BuildRequires:	glib-devel >= 1.3.1

%description
A Free Implementation of the Unicode BiDi algorithm

%package devel
Summary:	Library implementing the Unicode BiDi algorithm
Group:		Development/Libraries
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
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static %{name} libraries.

%description -l pl static
Biblioteki statyczne %{name}.

%prep
%setup -q
#%patch1 -p1 -b .gtkbeta

# .gtkbeta patch changes Makefile.am
libtoolize --force --copy
autoconf
automake

%build
CFLAGS="$RPM_OPT_FLAGS"; export CFLAGS
GLIB_CONFIG="%{_bindir}/glib-config-2.0"; export GLIB_CONFIG
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/fribidi
%attr(755,root,root) %{_libdir}/libfribidi.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_includedir}/fribidi
%attr(755,root,root) %{_bindir}/fribidi-config

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
