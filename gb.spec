Summary:	GB - Gnome Basic
Summary:	GB - Gnome Basic
Name:		gb
Version:	0.0.17
Release:	1
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/gb/%{name}-%{version}.tar.gz
URL:		http://www.gnome.org/gb/
BuildRequires:	flex
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This is an embryonic attempt to provide VB compatible functionality
for the GNOME project, particularly with respect to office (VBA)
compatibility.

%description -l pl
Pakierte ten zawiera bibliotekê która udostêpnia funkcje umo¿liwiaj±ce
realizacjê VB (Visual Basic) dla aplikacji GNOME.

%package devel
Summary:	Development resources for Gnome Basic
Summary(pl):	Zasoby potrzebne przy tworzeniu alikacji u¿ywaj±cych Gnome Basic
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Development resources for Gnome Basic.

description -l pl devel
Zasoby potrzebne przy tworzeniu alikacji u¿ywaj±cych gb.

%package static
Summary:	Static libraries for Gnome Basic
Summary(pl):	Biblioteki statyczne do Gnome Basic
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries for Gnome Basic.

%description -l pl static
Biblioteki statyczne do Gnome Basic.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog NEWS README TODO docs/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
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
