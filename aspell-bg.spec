%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

# NOTE: the bulgarian.kbd file in the sources is not in utf-8;
# that is wrong and fixed in the spec file; the fix has to
# be removed once the kbd file shipped with the sources is fixed.

%define src_ver 4.0-0
%define fname aspell5-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Bulgarian
%define languagecode bg
%define lc_ctype bg_BG

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       4.0.0
Release:       %mkrel 3
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:           http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}


BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandrake Stuff
Requires:      locales-%{languagecode}
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


