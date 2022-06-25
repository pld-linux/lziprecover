Summary:	Data recovery tool and decompressor for lzip files
Summary(pl.UTF-8):	Narzędzie do odzyskiwania danych i dekompresor dla plików lzip
Name:		lziprecover
Version:	1.23
Release:	1
License:	GPL v3+
Group:		Applications/Archiving
Source0:	http://download.savannah.gnu.org/releases/lzip/lziprecover/%{name}-%{version}.tar.lz
# Source0-md5:	f970adb845f7166002f9fc03d3f631d5
Patch0:		%{name}-info.patch
URL:		http://savannah.nongnu.org/projects/lzip/
BuildRequires:	libstdc++-devel
BuildRequires:	lzip
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lziprecover is a data recovery tool and decompressor for files in the
lzip compressed data format (.lz), able to repair slightly damaged
files, recover badly damaged files from two or more copies, extract
data from damaged files, decompress files and test integrity of files.

%description -l pl.UTF-8
Lziprecover to narzędzie do odzyskiwania danych i dekompresor dla
plików w formacie skompresowanym lzip (.lz), potrafiący naprawić
nieznacznie uszkodzone pliki, odtworzyć bardziej uszkodzone pliki z
dwóch lub większej liczby kopii, wydobyć dane z uszkodzonych plików,
dekompresować pliki oraz testować integralność plików.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make} all info

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/lziprecover
%{_mandir}/man1/lziprecover.1*
%{_infodir}/lziprecover.info*
