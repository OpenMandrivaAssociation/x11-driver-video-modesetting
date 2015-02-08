# X.org modules reference symbols provided by the X server
%global _disable_ld_no_undefined 1

Name:		x11-driver-video-modesetting
%define	gitdate	20150208
Version:	0.9.0~%{gitdate}
Release:	1
Epoch:		2
Summary:	Generic X.org driver
Group:		System/X11
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-modesetting-0.9.0~%{gitdate}.tar.xz
Patch1: 	0001-modesetting-24bpp-are-too-confusing-shadow-our-way-o.patch
Patch2:		0002-add-mga_g200_a-workaround.patch
License:	MIT
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1

Requires:	%(xserver-sdk-abi-requires ansic)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)
Requires:	udev

%description
x11-driver-video-modesetting is a generic X.org driver for hardware.

It managed by KMS (Kernel Mode Setting), eg: ATI/AMD, Intel&Nvidia.

%prep
%setup -q -n xf86-video-modesetting-%{version}
%apply_patches
autoreconf -fiv

%build
%configure
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/*
%{_mandir}/man4/modesetting.*
