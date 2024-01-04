%define config_path /etc/ood/config

Name:           ood-release-meta
Version:        2
Release:        2%{?dist}
Summary:        Open on Demand release meta package

BuildArch:      noarch

License:        MIT
Source:         %{name}-%{version}.tar.bz2

Requires:       ondemand

Requires:       ood-util = 4
Requires:       ood-initializers = 5

Requires:       ood-base-jupyter = 5
Requires:       ood-course-jupyter = 3
Requires:       ood-html = 7
Requires:       ood-julia-jupyter = 3
Requires:       ood-lustre-quota = 1
Requires:       ood-persistent-ssh = 4
Requires:       ood-shell = 1
Requires:       ood-tensorboard = 5
Requires:       ood-vnc-util = 4
Requires:       ood-vscode = 4

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
* Thu Jan 4 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Make TensorBoard use default module version.

* Wed Jan 3 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Add ParaView 5.11.
- Use default pytorch module version in Jupyter.
- Allow any reservation on all apps.
- Limit job time to reservation length when using reservation.
- Improve caching of reservations.
- Show the status of reservations in apps.
- Add support for node-specific reservations.
- Make it possible to define reservation in course modules.
- Improve errors for TensorBoard and Jupyter for Courses forms.

* Wed Nov 8 2023 Robin Karlsson <robin.karlsson@csc.fi>
- Remove LUMI-D NVME option.
- Remove VNC form settings header.

* Mon Nov 6 2023 Robin Karlsson <robin.karlsson@csc.fi>
- Add OIDC error page redirect

* Mon Nov 6 2023 Robin Karlsson <robin.karlsson@csc.fi>
- Initial release build.
- Fix docs links.
- Add Julia-Jupyter and Active Jobs to pinned apps.
- Fix dashboard title.
- Remove classic Jupyter notebook.
- Remove customer portal link.
- Update VSCode to 1.83.1.
- Fix Jupyter notebooks in VSCode.
- Remove email on started options.
- Add cray-python 3.10.10.

* Fri Oct 20 2023 Robin Karlsson <robin.karlsson@csc.fi>
- Add Matomo IDs
- Fix SlurmLimits error
- Fix app card caching

* Thu Oct 12 2023 Robin Karlsson <robin.karlsson@csc.fi>
- Jupyter has been improved.
- Login page improvements.

* Thu Oct 5 2023 Robin Karlsson <robin.karlsson@csc.fi>
- Add welcome page logos

* Thu Oct 5 2023 Robin Karlsson <robin.karlsson@csc.fi>
- Fixed compute node shell

* Tue Sep 26 2023 Robin Karlsson <robin.karlsson@csc.fi>
- Initial release version

* Tue May 16 2023 Robin Karlsson <robin.karlsson@csc.fi>
- Initial version
