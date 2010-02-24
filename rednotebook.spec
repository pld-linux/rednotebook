Summary:	A Desktop Diary
Summary(pl.UTF-8):	Dziennik na biurko
Name:		rednotebook
Version:	0.9.3
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/rednotebook/%{name}-%{version}.tar.gz
# Source0-md5:	3a070d49e458c7c0945fcf993bab6bfa
Patch0:		%{name}-desktop.patch
URL:		http://digitaldump.wordpress.com/projects/rednotebook/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	gtk+2 >= 2:2.18
Requires:	python-PyYAML
Requires:	python-gnome-extras-gtkhtml
Requires:	python-gnome-extras-mozilla
Requires:	python-pygtk-glade >= 2:2.14
BuildArch:	noarch
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
%doc CHANGELOG PKG-INFO README
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/48x48/apps/rednotebook.png
%{_pixmapsdir}/%{name}.png
%{py_sitescriptdir}/%{name}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/rednotebook-*.egg-info
%endif
