Name: ts-kernel-rht
Version: 1.0.0
Release: 1%{?dist}
Summary: TS-KERNEL RHT - Adaptive Red Hat Kernel System
License: GPLv3+
URL: https://github.com/Coolis1362/TS-KERNEL-RHT-ALL-VERSIONS
Source0: root/
ExclusiveArch: x86_64

%description
TS-KERNEL RHT is an adaptive kernel designed for Red Hat-based environments.

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
cp -r %{SOURCE0}/* $RPM_BUILD_ROOT/usr/bin/

%files
/usr/bin/*
