Summary:	Cjet PCL emulation for Canon CaPSL printers
Name:		cjet
Version:	0.8.9
Release:	%mkrel 8
License:	GPL
Group:		System/Printing
URL:		ftp://metalab.unc.edu/pub/Linux/system/printing/
Source:		ftp://metalab.unc.edu/pub/Linux/system/printing/cjet089.tar.bz2
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
CJET filters printer data from stdin to stdout, converting HP PCL (Printer
Command Language) commands to their CaPSL equivalents.
CaPSL is short for `Canon Printing Systems Language'.
Whereas PCL is a de-facto world-wide standard as a laser and inkjet printer
control language, CaPSL is limited to Canon laser printers.

%prep

%setup -q -n %{name}089

%build
make OPT="%{optflags}" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}

install -d  %{buildroot}%{_bindir}
install -m0755 cjet %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README INSTALL COPYING TODO ChangeLog samples/ 
%attr(0755,root,root) %{_bindir}/cjet
