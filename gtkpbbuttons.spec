Summary:	This client for pbbuttonsd displays small GTK popup windows
Summary(pl):	Klient dla pbbuttonsd wy�wietlaj�cy ma�e okienka z u�yciem GTK
Name:		gtkpbbuttons
Version:	0.6.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/pbbuttons/%{name}-%{version}.tar.gz
# Source0-md5:	26001c1d3d6ee22ea57a4f50a747051e
URL:		http://pbbuttons.sourceforge.net/projects/gtkpbbuttons/
BuildRequires:	autoconf
BuildRequires:	gtk+2-devel
BuildRequires:	pbbuttonsd-lib
Requires:	pbbuttonsd
ExclusiveArch:	ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This client for pbbuttonsd displays small GTK popup windows each time
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

%description -l pl
Ten klient pbbuttonsd wy�wietla z u�yciem GTK ma�e okienka po ka�dym
komunikacie od demona pbbuttonsd. Okienka te mog� zawiera�:
- aktualny poziom jasno�ci
- aktualn� g�o�no��
- informacj�, czy d�wi�k jest aktualnie wyciszony
- ostrze�enie o zbli�aj�cym si� wyczerpaniu baterii
- informacj� o aktualnym trybie trackpada
- ostrze�enie o wchodzeniu komputera w stan u�pienia - pozwalaj�ce
  zapobiec u�pieniu przez naci�ni�cie klawisza lub poruszenie myszy.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
