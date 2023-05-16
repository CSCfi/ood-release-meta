%define config_path /etc/ood/config

Name:           ood-release-meta
Version:        1
Release:        1%{?dist}
Summary:        Open on Demand release meta package

BuildArch:      noarch

License:        MIT
Source:         %{name}-%{version}.tar.bz2

Requires:       ondemand

Requires:       ood-util = 1
Requires:       ood-initializers = 1

Requires:       ood-base-jupyter = 1
Requires:       ood-course-jupyter = 1
Requires:       ood-csc-status = 1
Requires:       ood-disk-quotas = 1
Requires:       ood-html = 1
Requires:       ood-lustre-quota = 1
Requires:       ood-persistent-ssh = 1
Requires:       ood-quota-generator = 1
Requires:       ood-shell = 1
Requires:       ood-tensorboard = 1
Requires:       ood-vnc-util = 1
Requires:       ood-vscode = 1

# Disable debuginfo
%global debug_package %{nil}

%description
Open on Demand release meta package

%prep
%setup -q

%build

%install

%__install -m 0755 -d %{buildroot}%{config_path}
echo "%{version}" > %{buildroot}%{config_path}/CSC_OOD_RELEASE

%files

%{config_path}

%changelog
* Tue May 16 2023 Robin Karlsson <robin.karlsson@csc.fi>
- Initial version
