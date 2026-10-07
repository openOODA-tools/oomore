Name:           oomore
Version:        0.1.0
Release:        1%{?dist}
Summary:        Minimal POSIX-compliant paging utility for single-screen scrolling on restricted TTYs.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oomore
Source0:        oomore-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oomore is a sovereign, capability-bounded BASIC PAGER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oomore
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oomore-uninstall

%files
/usr/bin/oomore
/usr/bin/oomore-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
