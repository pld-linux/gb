Summary:	GB - Gnome Basic
Summary(pl):	GB - Gnome Basic
Name:		gb
Version:	0.0.20
Release:	3
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/gb/%{name}-%{version}.tar.gz
Patch0:		%{name}-am_fixes.patch
Patch1:		%{name}-am15.patch
Patch2:		%{name}-%{name}run.patch
URL:		http://www.gnome.org/gb/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.28
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This is an embryonic attempt to provide VB compatible functionality
for the GNOME project, particularly with respect to office (VBA)
compatibility.

%description -l pl
Pakiet ten zawiera bibliotekê która udostêpnia funkcje umo¿liwiaj±ce
realizacjê VB (Visual Basic) dla aplikacji GNOME.

%package devel
Summary:	Development resources for Gnome Basic
Summary(pl):	Zasoby potrzebne przy tworzeniu aplikacji u¿ywaj±cych Gnome Basic
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development resources for Gnome Basic.

%description devel -l pl
Zasoby potrzebne przy tworzeniu alikacji u¿ywaj±cych gb.

%package static
Summary:	Static libraries for Gnome Basic
Summary(pl):	Biblioteki statyczne do Gnome Basic
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries for Gnome Basic.

%description static -l pl
Biblioteki statyczne do Gnome Basic.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
libtoolize --copy --force
aclocal -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog NEWS README TODO docs/*.txt

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
%doc *.gz docs/*.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
