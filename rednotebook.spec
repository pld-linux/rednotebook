Summary:	A Desktop Diary
Summary(pl.UTF-8):	Dziennik na biurko
Name:		rednotebook
Version:	0.4.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rednotebook/%{name}-%{version}.tar.gz
# Source0-md5:	06e0192bf12a71ea853f27b1cd9a389c
Patch0:		%{name}-desktop.patch
URL:		http://digitaldump.wordpress.com/projects/rednotebook/
BuildRequires:	python-devel >= 2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-PyYAML
Requires:	python-wxPython
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RedNotebook is a Desktop Diary that makes it very easy for you to keep
track of the stuff you do and the thoughts you have.

%description -l pl.UTF-8
RedNotebook jest biurkowym dziennikiem, który w bardzo łatwy sposób
pozwala na zapisywanie rzeczy do zrobienia oraz myśli, które
przychodzą do głowy.

%prep
%setup -q
%patch0 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt PKG-INFO README.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/*.egg-info
