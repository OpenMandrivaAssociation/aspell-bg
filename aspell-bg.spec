%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

# NOTE:	the bulgarian.kbd file in the sources is not in utf-8;
# that is wrong and fixed in the spec file; the fix has to
# be removed once the kbd file shipped with the sources is fixed.

%define src_ver 4.1-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Bulgarian
%define languagecode bg
%define lc_ctype bg_BG

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	4.1.0
Release:	13
Group:		System/Internationalization
License:	GPLv2
Url:		http://aspell.net/
Source0:	http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
BuildRequires:	aspell >= %{aspell_ver}
BuildRequires:	make
Requires:	aspell >= %{aspell_ver}
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	spell-%{languagecode}
Provides:	aspell-%{lc_ctype}
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{fname}-%{src_ver}

# the kbd file is not in utf-8; that is wrong, fixing it
cat bulgarian.kbd | iconv -f cp1251 -t utf-8  > tmpfile
cat tmpfile > bulgarian.kbd

%build

# don't use configure macro
./configure

%make

%install
%makeinstall_std

mv -f README README.%{languagecode}
chmod 644 Copyright README.%{languagecode} doc/*

%files
%doc README.%{languagecode} Copyright 
%doc doc/*
%{_libdir}/aspell-%{aspell_ver}/*

