Summary:	This client for pbbuttonsd displays small GTK popup windows
Summary(pl):	Klient dla pbbuttonsd wyswietlaj±cy ma³e okienka z u¿yciem GTK
Name:		gtkpbbuttons
Version:	0.4.6
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.cymes.de/members/joker/projects/pbbuttons/tar/%{name}-%{version}.tar.gz
URL:		http://www.cymes.de/members/joker/projects/pbbuttons/gtkpbbuttons.html
Requires:	pbbuttonsd
BuildRequires:	autoconf
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/pbbuttons
%define		_bindir		%{_sbindir}

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
Ten klient pbbuttonsd wy¶wietla z u¿yciem GTK ma³e okienka po ka¿dym
komunikacie od demona pbbuttonsd. Okienka te mog± zawieraæ:
- aktualny poziom jasno¶ci
- aktualn± g³o¶no¶æ
- informacjê, czy d¼wiêk jest aktualnie wyciszony
- ostrze¿enie o zbli¿aj±cym siê wyczerpaniu baterii
- informacjê o aktualnym trybie trackpada
- ostrze¿enie o wchodzeniu komputera w stan u¶pienia - pozwalaj±ce
  zapobiec u¶pieniu przez naci¶niêcie klawisza lub poruszenie myszy.

%prep
%setup -q

%build
autoconf
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/{rc.d/init.d,sysconfig},%{_mandir}/man8}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

#gzip -9nf NEWS TODO 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc conf/*.gz *.gz
%attr(750,root,root) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(640,root,root) %config %verify(not size md5 mtime) /etc/sysconfig/*
%{_mandir}/man8/*
