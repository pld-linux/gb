Summary:	GB - GNOME Basic
Summary(pl.UTF-8):	GB - GNOME Basic
Name:		gb
Version:	0.0.20
Release:	5
License:	LGPL v2 (gbrun), GPL v2 (gb)
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gb/0.0/%{name}-%{version}.tar.gz
# Source0-md5:	19e35bd7f24ad619250484a997c0e02d
Patch0:		%{name}-am_fixes.patch
Patch1:		%{name}-am15.patch
Patch2:		%{name}-gbrun.patch
Patch3:		%{name}-locale_names.patch
URL:		http://www.gnome.org/projects/gb/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	gettext-tools
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.28
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an embryonic attempt to provide VB compatible functionality
for the GNOME project, particularly with respect to office (VBA)
compatibility.

%description -l pl.UTF-8
Pakiet ten zawiera bibliotekę która udostępnia funkcje umożliwiające
realizację VB (Visual Basic) dla aplikacji GNOME.

%package devel
Summary:	Development resources for GNOME Basic
Summary(pl.UTF-8):	Zasoby potrzebne przy tworzeniu aplikacji używających GNOME Basic
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development resources for GNOME Basic.

%description devel -l pl.UTF-8
Zasoby potrzebne przy tworzeniu aplikacji używających gb.

%package static
Summary:	Static libraries for GNOME Basic
Summary(pl.UTF-8):	Biblioteki statyczne do GNOME Basic
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for GNOME Basic.

%description static -l pl.UTF-8
Biblioteki statyczne do GNOME Basic.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

mv -f po/{no,nb}.po

%build
rm -f missing
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gb
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO docs/*.txt
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
