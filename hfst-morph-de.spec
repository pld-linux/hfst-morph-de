Summary:	HFST morphological analysis transducer for German language
Summary(pl.UTF-8):	Automat HFST do analizy morfologicznej dla języka niemieckiego
Name:		hfst-morph-de
# or 20110316?
Version:	0
Release:	1
License:	GPL v2 (SMOR analyser), Morhisto License (http://code.google.com/p/morphisto/)
Group:		Applications/Text
# source is hfst-german.tar.gz, but it doesn't contain scripts
Source0:	http://downloads.sourceforge.net/hfst/hfst-german-installable.tar.gz
# Source0-md5:	e6e2bbc98ca68a63be6738a5f65c5343
Patch0:		%{name}-DESTDIR.patch
URL:		http://hfst.sourceforge.net/
Requires:	hfst
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a German morphological transducer for HFST. It's based on
SFST SMOR morphological analyser with Morphisto lexical extensions
(<http://code.google.com/p/morphisto/>).

%description -l pl.UTF-8
Ten pakiet zawiera automat dla HFST do analizy morfologicznej języka
niemieckiego. Jest oparty na analizatorze morfologicznym SFST SMOR
wraz z rozszerzeniami językowymi Morphisto
(<http://code.google.com/p/morphisto/>).

%prep
%setup -q -n hfst-german-installable
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/german-analyze.sh
%attr(755,root,root) %{_bindir}/german-generate.sh
%{_datadir}/hfst/de
