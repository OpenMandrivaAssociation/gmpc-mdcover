Summary:	A directory artist/song provider plugin for gmpc
Name:		gmpc-mdcover
Version:	0.20.0
Release:	%mkrel 2
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl//gmpc-plugins-mdcover
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	libmpd-devel >= 0.15.98
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.8
BuildRequires:	gmpc-devel >= 0.15.98
BuildRequires:	intltool
Requires:	gmpc

%description
This gmpc plugin fetches cover art, artist art,album and 
artist information from the file system. 

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%{_libdir}/gmpc/plugins/mdcaplugin.so
