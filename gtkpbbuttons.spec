Summary:	This client for pbbuttonsd displays small GTK popup windows each time a message from the daemon pbbuttonsd appeares.
Summary(pl):	Klient dla pbbuttonsd wyswietlaj±cy ma³e okienko wskazuj±ce zmiany ustawieñ kontrolowanych przez pbbuttonsd. 
Name:		gtkpbbuttons
Version:	0.4.6
Release:	1
License:	GPL
Group:		X11
Source0:	http://www.cymes.de/members/joker/projects/pbbuttons/tar/%{name}-%{version}.tar.gz
URL:		http://www.cymes.de/members/joker/projects/pbbuttons/gtkpbbuttons.html
Requires:	pbbuttonsd
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/pbbuttons
%define		_bindir		%{_sbindir}

%description
This client for pbbuttonsd displays small GTK popup windows each time a message from the daemon pbbuttonsd appeares. The following 
windows could pop up:

- brightness level
  The current display brightness level would be displayed. 
- volume level
  The current volume level would be displayed 
- mute
  The window shows if the speakers were muted. 
- battery warning
  This window shows that battery is running low and how long it would last until shutdown. 
- trackpad mode
  This window shows the current trackpad mode. 
- sleep warning
  This window shows that the machine is going to enter sleep mode. Usually at that time you could
  press any key or move the mouse to prevent sleep mode. 

%description -l pl

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

%post
/sbin/chkconfig --add pbbuttonsd
if [ -f /var/lock/subsys/pbbuttonsd ]; then
	/etc/rc.d/init.d/pbbuttonsd restart >&2
else
	echo "Run \"/etc/rc.d/init.d/pbbuttonsd start\" to start ntp daemon."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/pbbuttonsd ]; then
		/etc/rc.d/init.d/pbbuttonsd stop >&2
	fi
	/sbin/chkconfig --del pbbuttonsd
fi

%files
%defattr(644,root,root,755)
%doc conf/*.gz *.gz
%attr(750,root,root) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(754,root,root) /etc/rc.d/init.d/ntp
%attr(640,root,root) %config %verify(not size md5 mtime) /etc/sysconfig/*
%{_mandir}/man8/*
