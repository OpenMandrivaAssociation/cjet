Summary:	PCL emulation for Canon CaPSL printers
Name:		cjet
Version:	0.8.9
Release:	22
License:	GPLv2
Group:		System/Printing
Url:		ftp://metalab.unc.edu/pub/Linux/system/printing/
Source0:	http://www.ibiblio.org/pub/Linux/system/printing/cjet089.tar.bz2
Patch0:		cjet-0.8.9-flags.patch

%description
CJET filters printer data from stdin to stdout, converting HP PCL (Printer
Command Language) commands to their CaPSL equivalents.
CaPSL is short for `Canon Printing Systems Language'.
Whereas PCL is a de-facto world-wide standard as a laser and inkjet printer
control language, CaPSL is limited to Canon laser printers.

%prep
%setup -qn %{name}089
%patch0 -p1

%build
%setup_compile_flags
%make

%install
install -d %{buildroot}%{_bindir}
install -m0755 cjet %{buildroot}%{_bindir}

%files
%doc README COPYING TODO ChangeLog samples/
%{_bindir}/cjet

