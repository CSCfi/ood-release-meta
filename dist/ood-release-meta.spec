%define config_path /etc/ood/config

Name:           ood-release-meta
Version:        1
Release:        5%{?dist}
Summary:        Open on Demand release meta package

BuildArch:      noarch

License:        MIT
Source:         %{name}-%{version}.tar.bz2

Requires:       ondemand

Requires:       ood-util
Requires:       ood-initializers

Requires:       ood-base-jupyter
Requires:       ood-csc-projects-lumi
Requires:       ood-cloud-storage-conf
Requires:       ood-course-jupyter
Requires:       ood-html
Requires:       ood-julia-jupyter
Requires:       ood-lumi-o-auth
Requires:       ood-lustre-quota
Requires:       ood-matlab-html
Requires:       ood-mlflow
Requires:       ood-openfoam
Requires:       ood-persistent-ssh
Requires:       ood-shell
Requires:       ood-tensorboard
Requires:       ood-vnc-util
Requires:       ood-vscode
Requires:       ood-csc-status

# Disable debuginfo
%global debug_package %{nil}

%description
Open on Demand release meta package

%prep
%setup -q

%build

%install

%__install -m 0755 -d %{buildroot}%{config_path}
echo "%{version} (develop)" > %{buildroot}%{config_path}/CSC_OOD_RELEASE

%files

%{config_path}

%changelog
* Tue May 16 2023 Robin Karlsson <robin.karlsson@csc.fi>
- Initial version
