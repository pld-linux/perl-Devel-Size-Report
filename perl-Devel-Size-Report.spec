
# Conditional build:
%bcond_without	tests	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Size-Report
Summary:	Devel::Size::Report - generate a size report for all elements in a structure
Name:		perl-Devel-Size-Report
Version:	0.05
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	965632af6997e6bba60e0fcd27f9bf6a
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl(Devel::Size)
Requires:	perl(Devel::Size)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::Size can only report the size of a single element or the total size of a structure (array, hash etc). This module
enhances Devel::Size by giving you the ability to generate a full size report for each element in a structure.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:make test}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Devel/Size/Report.pm
#%attr(755,root,root) %{perl_vendorarch}/auto/Devel/Size/Size.so
%{_mandir}/man3/*
