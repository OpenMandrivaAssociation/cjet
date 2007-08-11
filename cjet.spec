Summary:	Cjet PCL emulation for Canon CaPSL printers
Name:		cjet
Version:	0.8.9
Release:	%mkrel 1
License:	GPL
Group:		System/Configuration/Printing
URL:		ftp://metalab.unc.edu/pub/Linux/system/printing/
Source:		ftp://metalab.unc.edu/pub/Linux/system/printing/cjet089.tar.bz2
Conflicts:	printer-utils-2006 printer-utils-2007
Conflicts:	printer-filters-2006 printer-filters-2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
CJET filters printer data from stdin to stdout, converting HP PCL (Printer
Command Language) escape sequences and data structures, e.g. font headers, to
their CaPSL equivalents. CaPSL is short for `Canon Printing Systems Language'.
Whereas PCL is a de-facto world-wide standard as a laser and inkjet printer
control language (if you can call a bunch of escape sequences a `language'),
CaPSL is limited to Canon laser printers. Newer laser printers from Canon come
with PCL emulation, so CaPSL may well be facing extinction.

%prep

%setup -q -n %{name}089

%build
make OPT="%{optflags}"

%install
rm -rf %{buildroot}

install -d  %{buildroot}%{_bindir}
install -m0755 cjet %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README INSTALL COPYING TODO ChangeLog samples/ 
%attr(0755,root,root)%{_bindir}/cjet
