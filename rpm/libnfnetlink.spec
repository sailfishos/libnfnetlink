Name:           libnfnetlink
Version:        1.0.2
Release:        1
Summary:        Netfilter netlink userspace library
License:        GPLv2
URL:            https://github.com/sailfishos/libnfnetlink
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:	kernel-headers
BuildRequires:  automake autoconf libtool pkgconfig
BuildRequires:  make

%description
libnfnetlink is a userspace library that provides some low-level
nfnetlink handling functions.  It is used as a foundation for other, netfilter
subsystem specific libraries such as libnfnetlink_conntrack, libnfnetlink_log
and libnfnetlink_queue.

%package        devel
Summary:        Netfilter netlink userspace library
Requires:       %{name} = %{version}-%{release}
Requires:       kernel-headers

%description    devel
libnfnetlink is a userspace library that provides some low-level
nfnetlink handling functions.  It is used as a foundation for other, netfilter
subsystem specific libraries such as libnfnetlink_conntrack, libnfnetlink_log
and libnfnetlink_queue.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%autogen
%configure --disable-static
%make_build %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/libnfnetlink
%{_includedir}/libnfnetlink/*.h

