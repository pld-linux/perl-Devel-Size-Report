#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Devel
%define		pnam	Size-Report
Summary:	Devel::Size::Report - generate a size report for all elements in a structure
Summary(pl):	Devel::Size::Report - generowanie raportów o rozmiarach elementów w strukturze
Name:		perl-Devel-Size-Report
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9ac6783d9b23abba849e4b6091d409b1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Devel-Size
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::Size can only report the size of a single element or the total
size of a structure (array, hash etc). This module enhances
Devel::Size by giving you the ability to generate a full size report
for each element in a structure.

%description -l pl
Devel::Size mo¿e raportowaæ tylko rozmiar pojedynczego elementu lub
ca³kowity rozmiar struktury (tablicy, hasza itp.). Ten modu³ rozszerza
Devel::Size daj±c mo¿liwo¶æ generowania pe³nych raportów o rozmiarze
ka¿dego elementu w strukturze.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES NEW README TODO
%dir %{perl_vendorlib}/Devel/Size
%{perl_vendorlib}/Devel/Size/Report.pm
%{_mandir}/man3/*
