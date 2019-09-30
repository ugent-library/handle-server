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
%defattr(-,%{name},%{name},-)
/opt/%{name}/
/var/log/%{name}
%attr(755, root, root)/etc/init.d/%{name}

%doc

%pre
getent group %{name} > /dev/null || groupadd -r %{name}
getent passwd %{name} > /dev/null || useradd -r -g %{name} -G apache \
    -m -s /sbin/nologin -c "%{name} user" %{name}

has_service=$(chkconfig --list | grep %{name})
if [ "$has_service" != "" ];then
  chkconfig --del %{name} &> /dev/null
fi
exit 0

%post
(
chkconfig --add %{name} && chkconfig --level 345 %{name} on &&
echo "service %{name} installed!"
) || exit 1

%preun
chkconfig --del %{name} &> /dev/null
echo "service %{name} removed"
exit 0

%postun

%changelog
