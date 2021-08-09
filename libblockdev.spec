#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libblockdev
Version  : 2.26
Release  : 51
URL      : file:///aot/build/clearlinux/packages/libblockdev/libblockdev-v2.26.tar.gz
Source0  : file:///aot/build/clearlinux/packages/libblockdev/libblockdev-v2.26.tar.gz
Summary  : A library with utility functions used by the libblockdev library
Group    : Development/Tools
License  : LGPL-2.1
Requires: libblockdev-bin = %{version}-%{release}
Requires: libblockdev-data = %{version}-%{release}
Requires: libblockdev-lib = %{version}-%{release}
Requires: libblockdev-python = %{version}-%{release}
Requires: libblockdev-python3 = %{version}-%{release}
BuildRequires : autoconf
BuildRequires : autoconf-archive
BuildRequires : autoconf-archive-dev
BuildRequires : autogen
BuildRequires : autogen-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : buildreq-configure
BuildRequires : docbook-xml
BuildRequires : glib-dev
BuildRequires : glibc-bin
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : nss-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(bytesize)
BuildRequires : pkgconfig(devmapper)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(libcryptsetup)
BuildRequires : pkgconfig(libkmod)
BuildRequires : pkgconfig(libndctl)
BuildRequires : pkgconfig(libparted)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(mount)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(yaml-0.1)
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : volume_key-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
### CI status
<img alt="CI status" src="https://fedorapeople.org/groups/storage_apis/statuses/libblockdev-2.x.svg" width="100%" height="300ex" />

%package bin
Summary: bin components for the libblockdev package.
Group: Binaries
Requires: libblockdev-data = %{version}-%{release}

%description bin
bin components for the libblockdev package.


%package data
Summary: data components for the libblockdev package.
Group: Data

%description data
data components for the libblockdev package.


%package dev
Summary: dev components for the libblockdev package.
Group: Development
Requires: libblockdev-lib = %{version}-%{release}
Requires: libblockdev-bin = %{version}-%{release}
Requires: libblockdev-data = %{version}-%{release}
Provides: libblockdev-devel = %{version}-%{release}
Requires: libblockdev = %{version}-%{release}

%description dev
dev components for the libblockdev package.


%package lib
Summary: lib components for the libblockdev package.
Group: Libraries
Requires: libblockdev-data = %{version}-%{release}

%description lib
lib components for the libblockdev package.


%package python
Summary: python components for the libblockdev package.
Group: Default
Requires: libblockdev-python3 = %{version}-%{release}

%description python
python components for the libblockdev package.


%package python3
Summary: python3 components for the libblockdev package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libblockdev package.


%package staticdev
Summary: staticdev components for the libblockdev package.
Group: Default
Requires: libblockdev-dev = %{version}-%{release}

%description staticdev
staticdev components for the libblockdev package.


%prep
%setup -q -n libblockdev
cd %{_builddir}/libblockdev

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1628541641
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
## -fno-tree-vectorize: disable -ftree-vectorize thus disable -ftree-loop-vectorize and -ftree-slp-vectorize
## -Ofast -ffast-math
## -funroll-loops maybe dangerous
## -Wl,-z,max-page-size=0x1000
## -pthread -lpthread
## -Wl,-Bsymbolic-functions
export CXXFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export FCFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export FFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export CFFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export LDFLAGS="-g3 -ggdb -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=0
export __GL_SYNC_DISPLAY_DEVICE=DFP-1
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=DFP-1
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
## altflags1 end
sd -r '\s--dirty\s' ' ' .
sd -r 'git describe' 'git describe --abbrev=0' .
%autogen  --enable-shared \
--enable-static \
--with-python3=yes \
--with-dmraid=no \
--with-gtk-doc=no
make  %{?_smp_mflags}    V=1 VERBOSE=1


%install
export SOURCE_DATE_EPOCH=1628541641
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lvm-cache-stats

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/BlockDev-2.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/blockdev/blockdev.h
/usr/include/blockdev/btrfs.h
/usr/include/blockdev/crypto.h
/usr/include/blockdev/dbus.h
/usr/include/blockdev/dev_utils.h
/usr/include/blockdev/dm.h
/usr/include/blockdev/exec.h
/usr/include/blockdev/extra_arg.h
/usr/include/blockdev/fs.h
/usr/include/blockdev/fs/ext.h
/usr/include/blockdev/fs/generic.h
/usr/include/blockdev/fs/mount.h
/usr/include/blockdev/fs/ntfs.h
/usr/include/blockdev/fs/vfat.h
/usr/include/blockdev/fs/xfs.h
/usr/include/blockdev/kbd.h
/usr/include/blockdev/loop.h
/usr/include/blockdev/lvm.h
/usr/include/blockdev/mdraid.h
/usr/include/blockdev/module.h
/usr/include/blockdev/mpath.h
/usr/include/blockdev/nvdimm.h
/usr/include/blockdev/part.h
/usr/include/blockdev/plugins.h
/usr/include/blockdev/sizes.h
/usr/include/blockdev/swap.h
/usr/include/blockdev/utils.h
/usr/include/blockdev/vdo.h
/usr/lib64/libbd_btrfs.so
/usr/lib64/libbd_crypto.so
/usr/lib64/libbd_dm.so
/usr/lib64/libbd_fs.so
/usr/lib64/libbd_kbd.so
/usr/lib64/libbd_loop.so
/usr/lib64/libbd_lvm-dbus.so
/usr/lib64/libbd_lvm.so
/usr/lib64/libbd_mdraid.so
/usr/lib64/libbd_mpath.so
/usr/lib64/libbd_nvdimm.so
/usr/lib64/libbd_part.so
/usr/lib64/libbd_part_err.so
/usr/lib64/libbd_swap.so
/usr/lib64/libbd_utils.so
/usr/lib64/libbd_vdo.so
/usr/lib64/libblockdev.so
/usr/lib64/pkgconfig/blockdev-utils.pc
/usr/lib64/pkgconfig/blockdev.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbd_btrfs.so.2
/usr/lib64/libbd_btrfs.so.2.0.0
/usr/lib64/libbd_crypto.so.2
/usr/lib64/libbd_crypto.so.2.0.0
/usr/lib64/libbd_dm.so.2
/usr/lib64/libbd_dm.so.2.0.0
/usr/lib64/libbd_fs.so.2
/usr/lib64/libbd_fs.so.2.0.0
/usr/lib64/libbd_kbd.so.2
/usr/lib64/libbd_kbd.so.2.0.0
/usr/lib64/libbd_loop.so.2
/usr/lib64/libbd_loop.so.2.0.0
/usr/lib64/libbd_lvm-dbus.so.2
/usr/lib64/libbd_lvm-dbus.so.2.0.0
/usr/lib64/libbd_lvm.so.2
/usr/lib64/libbd_lvm.so.2.0.0
/usr/lib64/libbd_mdraid.so.2
/usr/lib64/libbd_mdraid.so.2.0.0
/usr/lib64/libbd_mpath.so.2
/usr/lib64/libbd_mpath.so.2.0.0
/usr/lib64/libbd_nvdimm.so.2
/usr/lib64/libbd_nvdimm.so.2.0.0
/usr/lib64/libbd_part.so.2
/usr/lib64/libbd_part.so.2.0.0
/usr/lib64/libbd_part_err.so.2
/usr/lib64/libbd_part_err.so.2.0.0
/usr/lib64/libbd_swap.so.2
/usr/lib64/libbd_swap.so.2.0.0
/usr/lib64/libbd_utils.so.2
/usr/lib64/libbd_utils.so.2.1.0
/usr/lib64/libbd_vdo.so.2
/usr/lib64/libbd_vdo.so.2.0.0
/usr/lib64/libblockdev.so.2
/usr/lib64/libblockdev.so.2.0.0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libbd_btrfs.a
/usr/lib64/libbd_crypto.a
/usr/lib64/libbd_dm.a
/usr/lib64/libbd_fs.a
/usr/lib64/libbd_kbd.a
/usr/lib64/libbd_loop.a
/usr/lib64/libbd_lvm-dbus.a
/usr/lib64/libbd_lvm.a
/usr/lib64/libbd_mdraid.a
/usr/lib64/libbd_mpath.a
/usr/lib64/libbd_nvdimm.a
/usr/lib64/libbd_part.a
/usr/lib64/libbd_part_err.a
/usr/lib64/libbd_swap.a
/usr/lib64/libbd_utils.a
/usr/lib64/libbd_vdo.a
/usr/lib64/libblockdev.a
