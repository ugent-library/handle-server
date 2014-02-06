Name: handle-server
Summary: Handle server
License: Handle System Public License Agreement
Version: 0.1
Release: X
BuildArch: noarch
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires: jre
Source: %{name}.tar.gz

%description
Handle server

%prep
%setup -q -n %{name}

%build
echo "nothing to build"

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/opt/%{name}
mkdir -p %{buildroot}/etc/init.d
mkdir -p %{buildroot}/var/log/%{name}

cp -r $RPM_BUILD_DIR/%{name}/* %{buildroot}/opt/%{name}/
cp $RPM_BUILD_DIR/%{name}/init.d/%{name} %{buildroot}/etc/init.d/%{name}

echo "Complete!"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/opt/%{name}/
%attr(755, -, -) /etc/init.d/%{name}
/var/log/%{name}

%doc

%pre
#in case of an upgrade (first installs new version, then deletes old version)
service %{name} stop &> /dev/null
chkconfig --del %{name} &> /dev/null
exit 0

%post
(
chkconfig --add %{name} && chkconfig --level 345 %{name} on && service %{name} start &&
echo "service %{name} installed!"
) || exit 1

%preun
service %{name} stop &> /dev/null
chkconfig --del %{name} &> /dev/null
echo "service %{name} removed"
exit 0

%postun
service %{name} restart &> /dev/null
exit 0

%changelog
