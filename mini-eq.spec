%global uuid mini-eq@bhack.github.io
%global rdn_name io.github.bhack.mini-eq
%global pypi_name mini_eq
%global shell_ver 50

Name:           mini-eq
Version:        0.8.7
Release:        1
Summary:        Small parametric equalizer for PipeWire desktops

License:        GPL-3.0
URL:            https://github.com/bhack/mini-eq
Source0:        https://github.com/bhack/mini-eq/archive/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-build
BuildRequires:  python-installer
BuildRequires:  python-setuptools
BuildRequires:  python-wheel
BuildRequires:  python-pip

BuildRequires:  desktop-file-utils
BuildRequires:  appstream

BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(libebur128)
BuildRequires:  python-numpy
BuildRequires:  python-cairo
BuildRequires:	pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(gtk4)

Requires: pipewire
Requires: %{_lib}pipewire-gobject
Requires: wireplumber
Requires: %{_lib}ebur128_1
Requires: gtk4
Requires: python-gobject3
Requires: python-numpy
Requires: typelib(Adw)
Requires: typelib(Pwg)

%description
Mini EQ is a small system-wide parametric equalizer for PipeWire desktops.
It uses GTK/Libadwaita for the UI, pipewire-gobject for app-facing PipeWire
routing, metadata, and monitor streams.

%package -n gnome-shell-extension-%{name}
Summary:        GNOME Shell extension for Mini EQ
Requires:       gnome-shell >= %{shell_ver}
Requires:       %{name} = %{EVRD}

BuildArch:      noarch

%description -n gnome-shell-extension-%{name}
GNOME Shell extension for Mini EQ.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%py_build

%install
%py_install

mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/metainfo
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

cp -a data/%{rdn_name}.desktop \
    %{buildroot}%{_datadir}/applications/

cp -ar src/%{pypi_name}/assets/icons/* \
    %{buildroot}%{_datadir}/icons/

cp -a data/%{rdn_name}.metainfo.xml \
    %{buildroot}%{_datadir}/metainfo/

cp -a extensions/gnome-shell/%{uuid}/* \
    %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

%files
%{_bindir}/mini-eq
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.dist-info/
%{_datadir}/applications/%{rdn_name}.desktop
%{_datadir}/icons/scalable/apps/io.github.bhack.mini-eq.svg
%{_datadir}/icons/symbolic/apps/io.github.bhack.mini-eq-symbolic.svg
%{_datadir}/metainfo/%{rdn_name}.metainfo.xml
%doc README*

%files -n gnome-shell-extension-%{name}
%{_datadir}/gnome-shell/extensions/%{uuid}/
%doc extensions/gnome-shell/README*
