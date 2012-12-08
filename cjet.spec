Summary:	Cjet PCL emulation for Canon CaPSL printers
Name:		cjet
Version:	0.8.9
Release:	%mkrel 12
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


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.9-11mdv2011.0
+ Revision: 663377
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.9-10mdv2011.0
+ Revision: 603832
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.9-9mdv2010.1
+ Revision: 522360
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.8.9-8mdv2010.0
+ Revision: 413237
- rebuild

* Thu Dec 25 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.9-7mdv2009.1
+ Revision: 318469
- use %%ldflags

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.8.9-6mdv2009.0
+ Revision: 220501
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.8.9-5mdv2008.1
+ Revision: 149081
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.9-4mdv2008.0
+ Revision: 75322
- fix deps (pixel)

* Wed Aug 22 2007 Thierry Vignaud <tv@mandriva.org> 0.8.9-3mdv2008.0
+ Revision: 69008
- fix description

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.9-2mdv2008.0
+ Revision: 64143
- use the new System/Printing RPM GROUP

* Sat Aug 11 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.9-1mdv2008.0
+ Revision: 62053
- Import cjet



* Sat Aug 11 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.9-1mdv2008.0
- initial Mandriva package

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 17:25:42 (7481)
- Copying release 0.8.9-1cl to releases/ directory.

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 17:25:41 (7480)
- Copying release 0.8.9-1cl to pristine/ directory.

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 17:25:38 (7479)
- Imported package from 8.0.

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 17:25:35 (7478)
- Created package directory
