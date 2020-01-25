#
# Conditional build:
%bcond_without	tests		# perform "make test"
#
%define	pdir	MozRepl
%define	pnam	RemoteObject
Summary:	MozRepl::RemoteObject - MozRepl client, treat Javascript objects as Perl objects
Summary(pl.UTF-8):	MozRepl::RemoteObject - klient MozRepl, traktuje obiekty Javascriptowe jak Perlowe
Name:		perl-MozRepl-RemoteObject
Version:	0.39
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/C/CO/CORION/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	767c69482363f2596213b9ff4aafd2c6
URL:		http://search.cpan.org/dist/MozRepl-RemoteObject/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:  perl(MozRepl)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MozRepl client. Treat Javascript objects as Perl objects.

%description -l pl.UTF-8
Klient MozRepl. Traktuje obiekty Javascriptowe jak Perlowe.

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
%doc Changes
%{perl_vendorlib}/MozRepl/AnyEvent.pm
%{perl_vendorlib}/MozRepl/RemoteObject.pm
%{perl_vendorlib}/MozRepl/Plugin
%{perl_vendorlib}/MozRepl/RemoteObject
%{_mandir}/man?/*
