Summary:	This client for pbbuttonsd displays small GTK+ popup windows
Summary(pl.UTF-8):	Klient dla pbbuttonsd wyświetlający małe okienka z użyciem GTK+
Name:		gtkpbbuttons
Version:	0.6.8
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/pbbuttons/%{name}-%{version}.tgz
# Source0-md5:	59ae81ec9eefe905e24cabde123ac496
URL:		http://pbbuttons.sourceforge.net/projects/gtkpbbuttons/
BuildRequires:	autoconf
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel
BuildRequires:	pbbuttonsd-lib
BuildRequires:	pkgconfig
Requires:	pbbuttonsd
ExclusiveArch:	%{ix86} ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This client for pbbuttonsd displays small GTK+ popup windows each time
a message from the daemon pbbuttonsd appeares. The following windows
could pop up:
- brightness level
  The current display brightness level would be displayed.
- volume level
  The current volume level would be displayed
- mute
  The window shows if the speakers were muted.
- battery warning
  This window shows that battery is running low and how long it would
  last until shutdown.
- trackpad mode
  This window shows the current trackpad mode.
- sleep warning
  This window shows that the machine is going to enter sleep mode.
  Usually at that time you could press any key or move the mouse to
  prevent sleep mode.

%description -l pl.UTF-8
Ten klient pbbuttonsd wyświetla z użyciem GTK+ małe okienka po każdym
komunikacie od demona pbbuttonsd. Okienka te mogą zawierać:
- aktualny poziom jasności
- aktualną głośność
- informację, czy dźwięk jest aktualnie wyciszony
- ostrzeżenie o zbliżającym się wyczerpaniu baterii
- informację o aktualnym trybie trackpada
- ostrzeżenie o wchodzeniu komputera w stan uśpienia - pozwalające
  zapobiec uśpieniu przez naciśnięcie klawisza lub poruszenie myszy.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_datadir}/%{name}
