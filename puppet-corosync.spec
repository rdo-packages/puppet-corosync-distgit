%{!?upstream_version: %global upstream_version %{commit}}
%global commit f438aa583b59fe312347ff080a7ca99ba058c7e9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-corosync
Version:        5.0.0
Release:        3%{?alphatag}%{?dist}
Summary:        This module is a set of manifests and types/providers for quickly setting up highly available clusters using Corosync
License:        ASL 2.0

URL:            https://github.com/puppet-community/puppet-corosync

Source0:        https://github.com/puppet-community/%{name}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
This module is a set of manifests and types/providers for quickly setting up highly available clusters using Corosync

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/corosync/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/corosync/



%files
%{_datadir}/openstack-puppet/modules/corosync/


%changelog
* Thu Feb 09 2017 Alfredo Moralejo <amoralej@redhat.com> 5.0.0-3.f438aa5git
- Ocata update 5.0.0 (f438aa583b59fe312347ff080a7ca99ba058c7e9)

