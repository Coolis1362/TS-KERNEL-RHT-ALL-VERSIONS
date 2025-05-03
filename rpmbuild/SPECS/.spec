Name: ts-kernel-rht
Version: 1.0.0
Release: 1%{?dist}
Summary: TS-KERNEL RHT - Adaptive Red Hat Kernel System
License: GPLv3+
URL: https://github.com/Coolis1362/TS-KERNEL-RHT-ALL-VERSIONS
Source0: /home/coolis1362/ts-kernle-rht-package/rpmbuild/SOURCES/ts-kernel-rht-1.0.0.tar.gz
ExclusiveArch: x86_64  # Ensures it only builds for AMD64

%description
TS-KERNEL RHT is an adaptive kernel designed for Red Hat-based environments.

%prep
%setup -q

%install
install -m 0755 %{_topdir}/tsbuild/SOURCES/ts-kernel-rht.py $RPM_BUILD_ROOT/usr/bin/ts-kernel-rht

%files
/usr/bin/root

%changelog
* Tue May 2 2025 Coolis1362 tadeotherocketbuilder@outlook.com - 1.0.0-1
  - Initial release of TS-KERNEL RHT 1.0.0
