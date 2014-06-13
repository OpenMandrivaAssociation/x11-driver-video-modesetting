# X.org modules reference symbols provided by the X server
%global _disable_ld_no_undefined 1

Name:		x11-driver-video-modesetting
Version:	0.8.1
Release:	3
Epoch:		1
Summary:	Generic X.org driver
Group:		System/X11
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-modesetting-%{version}.tar.bz2
License:	MIT
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1

Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)
Requires:	udev

%description
x11-driver-video-modesetting is a generic X.org driver for hardware.

It managed by KMS (Kernel Mode Setting), eg: ATI/AMD, Intel&Nvidia.

%prep
%setup -q -n xf86-video-modesetting-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/*
%{_mandir}/man4/modesetting.*

