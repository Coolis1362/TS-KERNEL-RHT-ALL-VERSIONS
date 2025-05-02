Name: ts-kernel-rht
Version: 1.0.0
Release: 1%{?dist}
Summary: TS-KERNEL RHT - Adaptive Red Hat Kernel System
License: GPLv3+
URL: https://github.com/Coolis1362/TS-KERNEL-RHT
Source0: ts-kernel-rht-1.0.0.tar.gz

%description
TS-KERNEL RHT is an adaptive kernel designed for Red Hat-based environments.

%prep
%setup -q

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/lib/ts-kernel-rht
mkdir -p $RPM_BUILD_ROOT/etc
mkdir -p $RPM_BUILD_ROOT/var/log/ts-kernel-rht
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/ts-kernel-rht

install -m 0755 ts-kernel-rht $RPM_BUILD_ROOT/usr/bin/
install -m 0644 ts-kernel-rht.conf $RPM_BUILD_ROOT/etc/

%files
/usr/bin/ts-kernel-rht
/usr/lib/ts-kernel-rht/
/etc/ts-kernel-rht.conf
/var/log/ts-kernel-rht/
/usr/share/doc/ts-kernel-rht/

%changelog
* Tue May 2 2025 Coolis1362 - Initial release of TS-KERNEL RHT 1.0.0
