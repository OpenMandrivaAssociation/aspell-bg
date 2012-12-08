%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

# NOTE: the bulgarian.kbd file in the sources is not in utf-8;
# that is wrong and fixed in the spec file; the fix has to
# be removed once the kbd file shipped with the sources is fixed.

%define src_ver 4.1-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Bulgarian
%define languagecode bg
%define lc_ctype bg_BG

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       4.1.0
Release:       %mkrel 7
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:           http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}


BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

# the kbd file is not in utf-8; that is wrong, fixing it
cat bulgarian.kbd | iconv -f cp1251 -t utf-8  > tmpfile
cat tmpfile > bulgarian.kbd

%build

# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

mv -f README README.%{languagecode}
chmod 644 Copyright README.%{languagecode} doc/*

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.%{languagecode} Copyright 
%doc doc/*
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 4.1.0-7mdv2011.0
+ Revision: 662798
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 4.1.0-6mdv2011.0
+ Revision: 603193
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 4.1.0-5mdv2010.1
+ Revision: 518907
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 4.1.0-4mdv2010.0
+ Revision: 413047
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 4.1.0-3mdv2009.1
+ Revision: 349998
- 2009.1 rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 4.1.0-2mdv2009.0
+ Revision: 264321
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Alexander Kurtakov <akurtakov@mandriva.org> 4.1.0-1mdv2009.0
+ Revision: 194985
- new version

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 4.0.0-5mdv2008.1
+ Revision: 182401
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 4.0.0-4mdv2008.1
+ Revision: 148738
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 4.0.0-3mdv2007.1
+ Revision: 123223
- Import aspell-bg

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 4.0.0-3mdv2007.1
- use the mkrel macro
- disable debug packages

* Sat Dec 04 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 4.0.0-2mdk
- fixed *.kbd file

* Fri Dec 03 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 4.0.0-1mdk
- new release

* Fri Dec 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.50.0-2mdk
- rebuild for new aspell

* Tue Jul 20 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.50.0-1mdk
- first version for mandrake

