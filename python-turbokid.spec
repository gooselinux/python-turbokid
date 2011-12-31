%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}

%define module turbokid

Name:           python-turbokid
Version:        1.0.4
Release:        4.1%{?dist}
Summary:        Python template plugin that supports Kid templates

Group:          Development/Languages
License:        MIT
URL:            http://www.turbogears.org/docs/plugins/template.html
Source0:        http://files.turbogears.org/eggs/TurboKid-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires: python-devel
%if 0%{?fedora} >= 8 || 0%{?rhel} >= 6
BuildRequires: python-setuptools-devel
%else
BuildRequires: python-setuptools
%endif
Requires:       python-kid >= 0.9.6

%description
This package provides a template engine plugin, allowing you
to easily use Kid with TurboGears, Buffet or other systems
that support python.templating.engines.


%prep
%setup -q -n TurboKid-%{version}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.txt
%{python_sitelib}/%{module}/
%{python_sitelib}/TurboKid-%{version}-py%{pyver}.egg-info


%changelog
* Fri Nov 13 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.0.4-4.1
- Fix conditional for RHEL

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.4-2
- Rebuild for Python 2.6

* Tue Nov 27 2007 Luke Macken <lmacken@redhat.com> - 1.0.4-1
- 1.0.4

* Sat Sep 22 2007 Luke Macken <lmacken@redhat.com> - 1.0.3-1
- 1.0.3

* Sun Sep  2 2007 Luke Macken <lmacken@redhat.com> - 1.0.2-2
- Update for python-setuptools changes in rawhide

* Sat Aug 18 2007 Luke Macken <lmacken@redhat.com> - 1.0.2-1
- 1.0.2

* Thu May  3 2007 Luke Macken <lmacken@redhat.com> - 1.0.1-1
- 1.0.1

* Sat Dec  9 2006 Luke Macken <lmacken@redhat.com> - 0.9.9-4
- Add python-devel to BuildRequires

* Fri Dec  8 2006 Luke Macken <lmacken@redhat.com> - 0.9.9-3
- Rebuild for new python

* Sat Sep 30 2006 Luke Macken <lmacken@redhat.com> - 0.9.9-2
- Add python-setuptools to BuildRequires

* Sat Sep 30 2006 Luke Macken <lmacken@redhat.com> - 0.9.9-1
- 0.9.9
- Add README

* Sat Sep 23 2006 Luke Macken <lmacken@redhat.com> - 0.9.8-3
- Rename to python-turbokid
- Own %%{python_sitelib}/turbokid directory
- Install the EGG-INFO directory

* Sun Sep 17 2006 Luke Macken <lmacken@redhat.com> - 0.9.8-2
- Add description

* Sat Sep 16 2006 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.9.8-1
- Initial creation
