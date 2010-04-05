Summary:	A directory artist/song provider plugin for gmpc
Name:		gmpc-mdcover
Version:	0.20.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl//gmpc-plugins-mdcover
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	libmpd-devel >= 0.15.98
BuildRequires:	libxml2-devel
BuildRequires:	gtk+2-devel >= 2.8
BuildRequires:	gmpc-devel >= 0.15.98
BuildRequires:	intltool
Requires:	gmpc
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This gmpc plugin fetches cover art, artist art,album and 
artist information from the file system. 

%prep
%setup -q

%build
%configure2_5x
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

%find_lang %name

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%{_libdir}/gmpc/plugins/mdcaplugin.la
%{_libdir}/gmpc/plugins/mdcaplugin.so
