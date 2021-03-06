#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x102C2C17498D6B9E (i.tkomiya@gmail.com)
#
Name     : pypi-sphinxcontrib_websupport
Version  : 1.2.4
Release  : 58
URL      : https://files.pythonhosted.org/packages/da/aa/b03a3f569a52b6f21a579d168083a27036c1f606269e34abdf5b70fe3a2c/sphinxcontrib-websupport-1.2.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/da/aa/b03a3f569a52b6f21a579d168083a27036c1f606269e34abdf5b70fe3a2c/sphinxcontrib-websupport-1.2.4.tar.gz
Source1  : https://files.pythonhosted.org/packages/da/aa/b03a3f569a52b6f21a579d168083a27036c1f606269e34abdf5b70fe3a2c/sphinxcontrib-websupport-1.2.4.tar.gz.asc
Summary  : Sphinx API for Web Apps
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-sphinxcontrib_websupport-license = %{version}-%{release}
Requires: pypi-sphinxcontrib_websupport-python = %{version}-%{release}
Requires: pypi-sphinxcontrib_websupport-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(sphinxcontrib_serializinghtml)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
sphinxcontrib-websupport provides a Python API to easily integrate Sphinx
        documentation into your Web application.

%package license
Summary: license components for the pypi-sphinxcontrib_websupport package.
Group: Default

%description license
license components for the pypi-sphinxcontrib_websupport package.


%package python
Summary: python components for the pypi-sphinxcontrib_websupport package.
Group: Default
Requires: pypi-sphinxcontrib_websupport-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinxcontrib_websupport package.


%package python3
Summary: python3 components for the pypi-sphinxcontrib_websupport package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_websupport)
Requires: pypi(sphinxcontrib_serializinghtml)

%description python3
python3 components for the pypi-sphinxcontrib_websupport package.


%prep
%setup -q -n sphinxcontrib-websupport-1.2.4
cd %{_builddir}/sphinxcontrib-websupport-1.2.4
pushd ..
cp -a sphinxcontrib-websupport-1.2.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656370503
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_websupport
cp %{_builddir}/sphinxcontrib-websupport-1.2.4/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_websupport/e5d1b0fd46b681f4be3ce69e064b9427372ea1f2
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinxcontrib_websupport/e5d1b0fd46b681f4be3ce69e064b9427372ea1f2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
