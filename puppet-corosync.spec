%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-corosync
%global commit f3ada2529dfbd7202a94e9c151e916dca32d8f4a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-corosync
Version:        5.0.0
Release:        1%{?alphatag}%{?dist}
Summary:        This module is a set of manifests and types/providers for quickly setting up highly available clusters using Corosync
License:        Apache License, Version 2.0

URL:            https://github.com/puppet-community/puppet-corosync

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

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
* Wed Sep 21 2016 Haikel Guemar <hguemar@fedoraproject.org> - 5.0.0-1.f3ada25.git
- Newton update 5.0.0 (f3ada2529dfbd7202a94e9c151e916dca32d8f4a)


# REMOVEME: error caused by commit https://github.com/puppetlabs/puppetlabs-corosync/commit/a8202cefd1de60f9cafcfd870a819985914be565
