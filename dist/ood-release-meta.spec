%define config_path /etc/ood/config

Name:           ood-release-meta
Version:        1
Release:        5%{?dist}
Summary:        Open on Demand release meta package

BuildArch:      noarch

License:        MIT
Source:         %{name}-%{version}.tar.bz2

Requires:       ondemand

Requires:       ood-util = 2
Requires:       ood-initializers = 5

Requires:       ood-base-jupyter = 2
Requires:       ood-course-jupyter = 2
Requires:       ood-csc-status = 2
Requires:       ood-disk-quotas = 1
Requires:       ood-html = 3
Requires:       ood-julia-jupyter = 2
Requires:       ood-lustre-quota = 1
Requires:       ood-persistent-ssh = 1
Requires:       ood-quota-generator = 1
Requires:       ood-shell = 1
Requires:       ood-tensorboard = 2
Requires:       ood-vnc-util = 2
Requires:       ood-vscode = 2

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
* Fri Jun 9 2023 Robin Karlsson <robin.karlsson@csc.fi>
- Mask sensitive files app paths (remotes).
- Fix dashboard modal scrolling bug.

* Thu Jun 8 2023 Robin Karlsson <robin.karlsson@csc.fi>
- Add accessibility statement and cookie policy modals to dashboard.
- Initialize ood-csc-status nginx config during install.

* Thu Jun 1 2023 Robin Karlsson <robin.karlsson@csc.fi>
- Improve form validation.
- Remove develop dropdown.
- Adjust pinned apps.
- Add RPM versions page.
- Fix welcome page error pages.

* Fri May 26 2023 Robin Karlsson <robin.karlsson@csc.fi>
- Remove test partition from apps.
- Update code-server version.
- Add Julia extension to VSCode.
- Add Julia dashboard icon.
- Add negative BU warnings.
- Validate Rclone remotes.
- Improve welcome page.

* Tue May 16 2023 Robin Karlsson <robin.karlsson@csc.fi>
- Initial version
