#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : snappy
Version  : 1.1.10
Release  : 38
URL      : https://github.com/google/snappy/archive/1.1.10/snappy-1.1.10.tar.gz
Source0  : https://github.com/google/snappy/archive/1.1.10/snappy-1.1.10.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Clear
Requires: snappy-lib = %{version}-%{release}
Requires: snappy-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : gflags-dev
BuildRequires : googletest-dev
BuildRequires : lzo-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0002-add-option-to-enable-rtti-set-default-to-current-beh.patch

%description
Snappy, a fast compressor/decompressor.
[![Build Status](https://github.com/google/snappy/actions/workflows/build.yml/badge.svg)](https://github.com/google/snappy/actions/workflows/build.yml)

%package dev
Summary: dev components for the snappy package.
Group: Development
Requires: snappy-lib = %{version}-%{release}
Provides: snappy-devel = %{version}-%{release}
Requires: snappy = %{version}-%{release}

%description dev
dev components for the snappy package.


%package lib
Summary: lib components for the snappy package.
Group: Libraries
Requires: snappy-license = %{version}-%{release}

%description lib
lib components for the snappy package.


%package license
Summary: license components for the snappy package.
Group: Default

%description license
license components for the snappy package.


%prep
%setup -q -n snappy-1.1.10
cd %{_builddir}/snappy-1.1.10
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678728357
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
export CXXFLAGS=$CFLAGS
export FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
export FCFLAGS=$FFLAGS
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake .. -DCMAKE_INSTALL_LIBDIR=/usr/lib64 \
-DBUILD_SHARED_LIBS=yes \
-DSNAPPY_REQUIRE_AVX2=yes \
-DSNAPPY_BUILD_TESTS=no \
-DSNAPPY_BUILD_BENCHMARKS=no \
-DSNAPPY_ENABLE_RTTI=ON
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
export CXXFLAGS=$CFLAGS
export FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
export FCFLAGS=$FFLAGS
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -DCMAKE_INSTALL_LIBDIR=/usr/lib64 \
-DBUILD_SHARED_LIBS=yes \
-DSNAPPY_REQUIRE_AVX2=yes \
-DSNAPPY_BUILD_TESTS=no \
-DSNAPPY_BUILD_BENCHMARKS=no \
-DSNAPPY_ENABLE_RTTI=ON
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1678728357
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/snappy
cp %{_builddir}/snappy-%{version}/COPYING %{buildroot}/usr/share/package-licenses/snappy/c3af063092a3cd8c31335607ba466fe91898bd4e || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/snappy-c.h
/usr/include/snappy-sinksource.h
/usr/include/snappy-stubs-public.h
/usr/include/snappy.h
/usr/lib64/cmake/Snappy/SnappyConfig.cmake
/usr/lib64/cmake/Snappy/SnappyConfigVersion.cmake
/usr/lib64/cmake/Snappy/SnappyTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Snappy/SnappyTargets.cmake
/usr/lib64/glibc-hwcaps/x86-64-v3/libsnappy.so
/usr/lib64/libsnappy.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libsnappy.so.1
/usr/lib64/glibc-hwcaps/x86-64-v3/libsnappy.so.1.1.10
/usr/lib64/libsnappy.so.1
/usr/lib64/libsnappy.so.1.1.10

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/snappy/c3af063092a3cd8c31335607ba466fe91898bd4e
