#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : snappy
Version  : 1.1.3
Release  : 8
URL      : https://github.com/google/snappy/archive/1.1.3.tar.gz
Source0  : https://github.com/google/snappy/archive/1.1.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Clear
Requires: snappy-lib
Requires: snappy-doc
BuildRequires : gtest-dev
BuildRequires : lzo-dev
BuildRequires : zlib-dev

%description
Snappy, a fast compressor/decompressor.
Introduction
============
Snappy is a compression/decompression library. It does not aim for maximum
compression, or compatibility with any other compression library; instead,
it aims for very high speeds and reasonable compression. For instance,
compared to the fastest mode of zlib, Snappy is an order of magnitude faster
for most inputs, but the resulting compressed files are anywhere from 20% to
100% bigger. (For more information, see "Performance", below.)

%package dev
Summary: dev components for the snappy package.
Group: Development
Requires: snappy-lib
Provides: snappy-devel

%description dev
dev components for the snappy package.


%package doc
Summary: doc components for the snappy package.
Group: Documentation

%description doc
doc components for the snappy package.


%package lib
Summary: lib components for the snappy package.
Group: Libraries

%description lib
lib components for the snappy package.


%prep
%setup -q -n snappy-1.1.3

%build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -falign-functions=32 -fno-semantic-interposition -flto -O3 "
export FCFLAGS="$CFLAGS -falign-functions=32 -fno-semantic-interposition -flto -O3 "
export FFLAGS="$CFLAGS -falign-functions=32 -fno-semantic-interposition -flto -O3 "
export CXXFLAGS="$CXXFLAGS -falign-functions=32 -fno-semantic-interposition -flto -O3 "
%autogen --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/snappy/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
