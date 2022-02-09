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
mkdir -p %{buildroot}/etc/systemd/system/
mkdir -p %{buildroot}/var/log/%{name}

cp -r $RPM_BUILD_DIR/%{name}/* %{buildroot}/opt/%{name}/
cp $RPM_BUILD_DIR/%{name}/systemd/%{name}.service %{buildroot}/etc/systemd/system/

echo "Complete!"

%clean
rm -rf %{buildroot}

%files
%defattr(-,%{name},%{name},-)
/opt/%{name}/
/var/log/%{name}
%attr(755,root,root) /etc/systemd/system

%doc

%pre
getent group %{name} > /dev/null || groupadd -r %{name}
getent passwd %{name} > /dev/null || useradd -r -g %{name} -G apache \
    -m -s /sbin/nologin -c "%{name} user" %{name}

exit 0

%post
systemctl daemon-reload &&
systemctl enable %{name} &&
systemctl restart %{name}
exit 0

%preun
if [ "$1" = 0 ] ; then
  systemctl stop %{name}
  systemctl disable %{name}
fi
exit 0

%changelog
