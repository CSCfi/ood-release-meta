%define config_path /etc/ood/config

Name:           ood-release-meta
Version:        13
Release:        1%{?dist}
Summary:        Open on Demand release meta package

BuildArch:      noarch

License:        MIT
Source:         %{name}-%{version}.tar.bz2

Requires:       ondemand

Requires:       ood-util = 11
Requires:       ood-initializers = 15

Requires:       ood-base-jupyter = 15
Requires:       ood-cloud-storage-conf = 10
Requires:       ood-course-jupyter = 11
Requires:       ood-csc-projects-lumi = 3
Requires:       ood-csc-status = 7
Requires:       ood-html = 13
Requires:       ood-julia-jupyter = 7
Requires:       ood-lumi-o-auth = 4
Requires:       ood-lumi-o-tools = 1
Requires:       ood-lustre-quota = 2
Requires:       ood-matlab-html = 6
Requires:       ood-mlflow = 6
Requires:       ood-openfoam = 1
Requires:       ood-persistent-ssh = 10
Requires:       ood-shell = 1
Requires:       ood-tensorboard = 10
Requires:       ood-vnc-util = 11
Requires:       ood-vscode = 11

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
* Fri May 22 2026 Robin Karlsson <robin.karlsson@csc.fi>
- Add module version selection for Jupyter and MATLAB.
- Add LAIF lumi-multitorch to Jupyter.
- Add option to resume last VSCode session.
- Add option to reset Jupyter for Courses course material.
- Fix reset cache button missing in 4.1.

* Fri Apr 17 2026 Robin Karlsson <robin.karlsson@csc.fi>
- Load wget module for Jupyter for Courses.

* Fri Apr 17 2026 Robin Karlsson <robin.karlsson@csc.fi>
- Use MLflow 3.11.1 and 2.22.0 from /appl/local/ood.
- Update VSCode to 1.115.0.
- Add frontpage links to LUMI-K and LUMI-O.
- Fix app forms styling for 4.1.

* Fri Feb 27 2026 Robin Karlsson <robin.karlsson@csc.fi>
- Fix Compute node shell persistency.
- Update VSCode 1.109.2.
- Support newer MLflow versions.
- Add configurable expiration date for LUMI-O tokens.
- Fix sensitive URLs and titles being logged to Matomo.
- Fetch Swift storage URL from Allas dynamically.
- Increase CPU limit to 12 for Compute node shell.
- Update cray-python versions in Jupyter.

* Fri Oct 31 2025 Robin Karlsson <robin.karlsson@csc.fi>
- Add bring-your-own-license to MATLAB.
- Add small partition to MATLAB.
- Increase default memory to MATLAB.

* Fri Aug 29 2025 Robin Karlsson <robin.karlsson@csc.fi>
- Add support for Jupyter for Courses modules under /appl/local/csc/modulefiles/www_lumi_modules.
- Set Rclone default time to unix time 0.
- Wait until TensorBoard fully launches before allowing connections.
- Remove %post RPM section from Passenger apps.
- Fix a bug with Jupyter advanced settings and custom module.
- Use an unique name for Jupyter kernels.
- Force global SSH config to be used for shell apps.
- Use module reset instead of restore in Desktop.
- Launch Desktop terminal tabs outside of container.

* Thu Apr 17 2025 Robin Karlsson <robin.karlsson@csc.fi>
- Fix Jupyter script not working.

* Wed Apr 16 2025 Robin Karlsson <robin.karlsson@csc.fi>
- Update VSCode to 1.99.2.
- Add better support for containers in Jupyter.
- Add ability to use $PROJECT in Jupyter form.
- Add cray-python 3.11.5 to Jupyter.
- Add Blender 4.3.
- Enable saved settings for interactive apps.
- Ignore reservations with -no-ood in name.
- Support OOD 4.0.

* Mon Jan 13 2025 Robin Karlsson <robin.karlsson@csc.fi>
- Update accessibility statement contact info.
- Add geoconda to Jupyter.
- Disable password auth for shell, add retries.
- Add GIS applications to VNC.
- Fix lumi-o-auth excessive logging.

* Fri Nov 1 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Fix bugs with GPU field in Jupyter for Courses.

* Mon Oct 14 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Fix Allas Swift token creation not working.

* Fri Oct 11 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Show all partitions on VNC apps.
- Fix cache reset button on VNC apps.

* Fri Oct 11 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Fix help bar missing.

* Fri Oct 11 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Fix industry dashboard always being enabled.

* Fri Oct 11 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Add MLflow interactive app.
- Add industry dashboard for some projects.
- Add OpenFOAM "interactive" app (industry dashboard only).
- Add shortcuts to Desktop apps (industry dashboard only).
- Update Visual Studio Code to 1.92.2.
- Add project names to app forms.
- Support multiple compute node shells on the same node.
- Add terminal titles to compute node shells.
- Add disk quota and project viewer.
- Add option for using multiple GPUs in interactive apps.
- Set --propagate=NONE for all interactive apps.
- Make Desktop environment more robust. Only export some specific env vars.
- Make Desktop apps possible to run on CPU nodes.
- Use new Matomo URLs.

* Wed Jul 17 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Add env var for enabling/disabling flash.

* Fri Jun 14 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Update Visual Studio Code to 1.89.1.
- Add q_industry partition.
- Make Jupyter app always install Jupyter kernels for virtual environments.
- Clarify LUMI-O token lifetime and refreshing.

* Fri May 24 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Improve Cloud Storage Configuration revokation message.

* Thu May 23 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Add Cloud Storage Configuration tool with LUMI-O and Allas integration
- Add MATLAB and Cloud Storage Configuration to pinned apps
- Clarify 502 error page links

* Tue Apr 9 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Add MATLAB HTML and Desktop version.
- Add VisIt.
- Strip SLURM env vars in Desktop terminal.
- Keep Desktop terminal open on errors.
- Enable remote files again.
- Fix accessibility issues.
- Update accessibility statement.
- Add OIDC error pages.
- Fix GPU reservations in apps.

* Fri Jan 5 2024 Robin Karlsson <robin.karlsson@csc.fi>
- Fix form validation with missing reservations.

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
