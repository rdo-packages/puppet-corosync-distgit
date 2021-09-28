%global milestone .0rc0
%{!?upstream_version: %global upstream_version %{commit}}
%global commit cd23c0ad7f3f18d981e33a936cc271dc11169684
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-corosync
Version:        8.2.1
Release:        0.1%{?milestone}%{?alphatag}%{?dist}
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
* Tue Sep 28 2021 RDO <dev@lists.rdoproject.org> 8.2.1-0.1.0rc0.cd23c0agit
- Update to post 8.2.1 (cd23c0ad7f3f18d981e33a936cc271dc11169684)



