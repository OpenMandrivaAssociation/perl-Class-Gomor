%define upstream_name    Class-Gomor
%define upstream_version 1.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Class::Gomor - another class and object builder
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GO/GOMOR/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch
%rename	perl-Class-Gomor-Hash

%description
This module is yet another class builder. This one adds parameter checking in
new constructor, that is to check for attributes existence, and definedness.

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
%doc Changes LICENSE LICENSE.Artistic README
%dir %{perl_vendorlib}/Class/Gomor
%{perl_vendorlib}/Class/Gomor/*.pm
%{perl_vendorlib}/Class/Gomor.pm
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.20.0-2mdv2011.0
+ Revision: 680821
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2011.0
+ Revision: 403013
- rebuild using %%perl_convert_version

* Sun May 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2010.0
+ Revision: 379209
- update to new version 1.02

* Sun Feb 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.01-4mdv2009.1
+ Revision: 340475
- obsoleting perl-Class-Gomor-Hash

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.01-3mdv2009.0
+ Revision: 255959
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.01-1mdv2008.1
+ Revision: 136683
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.01-1mdv2008.0
+ Revision: 19799
- 1.01


* Sat Jul 29 2006 <oeriksson@mandriva.com> 1.00-1mdv2007.0
- initial Mandriva package

