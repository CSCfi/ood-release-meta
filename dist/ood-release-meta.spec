%define config_path /etc/ood/config

Name:           ood-release-meta
Version:        7
Release:        1%{?dist}
Summary:        Open on Demand release meta package

BuildArch:      noarch

License:        MIT
Source:         %{name}-%{version}.tar.bz2

Requires:       ondemand

Requires:       ood-util = 7
Requires:       ood-initializers = 12

Requires:       ood-allas-conf = 1
Requires:       ood-base-jupyter = 7
Requires:       ood-cloud-storage-conf = 4
Requires:       ood-course-jupyter = 8
Requires:       ood-csc-status = 5
Requires:       ood-disk-quotas = 1
Requires:       ood-html = 8
Requires:       ood-julia-jupyter = 6
Requires:       ood-lumi-o-auth = 1
Requires:       ood-lumi-o-tools = 1
Requires:       ood-lustre-quota = 1
Requires:       ood-mlflow = 5
Requires:       ood-persistent-ssh = 5
Requires:       ood-quota-generator = 1
Requires:       ood-shell = 1
Requires:       ood-tensorboard = 6
Requires:       ood-vnc-util = 8
Requires:       ood-vscode = 7

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
* Mon Jun 10 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Update Visual Studio Code to 1.89.1.
- Make Jupyter app always install Jupyter kernels for virtual environments.
- Fix issues with some containerized applications in Desktop app.
- Clarify LUMI-O token lifetime and refreshing.
- Update csc-ui to 2.1.10.

* Fri May 24 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Improve Cloud Storage Configuration revokation message.

* Thu May 23 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Add LUMI-O to Cloud Storage Configuration tool.
- Clarify 502 error page links

* Mon Apr 8 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Improve accessibility.
- Improve error pages.
- Desktop app terminal now uses default $XDG_CONFIG_HOME, and squeue can now be used.

* Mon Feb 26 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Fix reset desktop icons not working.
- Make TensorBoard and MLflow use default module versions.

* Thu Feb 22 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Make OOD 3.1 work.
- Add GPU partitions (MIG) to apps.
- Desktop uses srun instead of SSH.
- Add desktop app categories.
- Update VSCode to 1.86.1.
- Reduce reservation buffer time 5 minutes.

* Tue Jan 9 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Fix form validation when no reservation exists.

* Tue Dec 12 2023 Robin Karlsson <robin.karlsson@csc.fi>
- Fix reservation handling in Jupyter for Courses form.

* Fri Dec 8 2023 Robin Karlsson <robin.karlsson@csc.fi>
- Allow any reservation on all apps.
- Limit job time to reservation length when using reservation.
- Improve caching of reservations.
- Show the status of reservations in apps.
- Add support for node-specific reservations.
- Make it possible to define reservation in course modules.
- Fix error with some types of partitions.
- Move remote validation to OOD RPMs.
- Improve errors for TensorBoard and Jupyter for Courses forms.

* Mon Oct 9 2023 Robin Karlsson <robin.karlsson@csc.fi>
- Add MLflow.
- Add Allas configuration tool.
- Desktop icons and configuration are now persistent.
- Update VSCode to 1.82.2.
- Fix Jupyter notebooks in VSCode.
- Usage metrics are 3d instead of 6h.
- Usage metrics now include a description.
- Clarify SMT behaviour/core amount in app forms.
- Invalid app form options are now highlighted (red text).
- Fix ood-csc-status error on project names with ";".

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
