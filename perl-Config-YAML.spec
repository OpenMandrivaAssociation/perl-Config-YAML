%define	module	Config-YAML
%define	name	perl-%{module}
%define version 1.42
%define	release	%mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Generic Config perl module
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MD/MDXI/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-YAML
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module opens a config file and parses it's contents for you. The
method new requires one parameter which needs to be a filename. The
method getall returns a hash which contains all options and it's
associated values of your config file.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Config
%{_mandir}/man3/*

