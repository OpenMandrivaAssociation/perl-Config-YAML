%define	upstream_name	 Config-YAML
%define upstream_version 1.42

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Generic Config perl module
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MD/MDXI/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(YAML)
BuildArch:	noarch

%description
This module opens a config file and parses it's contents for you. The
method new requires one parameter which needs to be a filename. The
method getall returns a hash which contains all options and it's
associated values of your config file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Config
%{_mandir}/man3/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.420.0-2mdv2011.0
+ Revision: 680845
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.420.0-1mdv2011.0
+ Revision: 403026
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.42-6mdv2009.0
+ Revision: 241191
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.42-4mdv2008.0
+ Revision: 86195
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.42-3mdv2007.0
- Rebuild

* Thu Dec 15 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.42-2mdk
- fix buildrequires

* Tue Nov 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.42-1mdk
- first mdk release

