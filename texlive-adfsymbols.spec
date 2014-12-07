# revision 19766
# category Package
# catalog-ctan /fonts/adfsymbols
# catalog-date 2010-09-13 13:22:42 +0200
# catalog-license lppl
# catalog-version 1.001
Name:		texlive-adfsymbols
Version:	1.001
Release:	9
Summary:	SymbolsADF with TeX/LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/adfsymbols
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adfsymbols.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adfsymbols.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex

%description
The package provides Arkandis foundry's ArrowsADF and
BulletsADF fonts in Adobe Type 1 format, together with
TeX/LaTeX support files. The fonts are licensed under GPL v2 or
later with font exception. (See NOTICE, COPYING, README.) The
TeX/LaTeX support is licensed under LPPL. (See README,
manifest.txt.).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/arkandis/adfsymbols/ArrowsADF.afm
%{_texmfdistdir}/fonts/afm/arkandis/adfsymbols/BulletsADF.afm
%{_texmfdistdir}/fonts/enc/dvips/adfsymbols/SymbolsADF.enc
%{_texmfdistdir}/fonts/map/dvips/adfsymbols/ArrowsADF.map
%{_texmfdistdir}/fonts/map/dvips/adfsymbols/BulletsADF.map
%{_texmfdistdir}/fonts/tfm/arkandis/adfsymbols/ArrowsADF.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/adfsymbols/BulletsADF.tfm
%{_texmfdistdir}/fonts/type1/arkandis/adfsymbols/ArrowsADF.pfb
%{_texmfdistdir}/fonts/type1/arkandis/adfsymbols/BulletsADF.pfb
%{_texmfdistdir}/tex/latex/adfsymbols/adfarrows.sty
%{_texmfdistdir}/tex/latex/adfsymbols/adfbullets.sty
%{_texmfdistdir}/tex/latex/adfsymbols/uarrowsadf.fd
%{_texmfdistdir}/tex/latex/adfsymbols/ubulletsadf.fd
%_texmf_updmap_d/adfsymbols
%doc %{_texmfdistdir}/doc/fonts/adfsymbols/COPYING
%doc %{_texmfdistdir}/doc/fonts/adfsymbols/NOTICE
%doc %{_texmfdistdir}/doc/fonts/adfsymbols/README
%doc %{_texmfdistdir}/doc/fonts/adfsymbols/adfsymbols.pdf
%doc %{_texmfdistdir}/doc/fonts/adfsymbols/adfsymbols.tex
%doc %{_texmfdistdir}/doc/fonts/adfsymbols/manifest.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/adfsymbols <<EOF
Map ArrowsADF.map
Map BulletsADF.map
EOF


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.001-2
+ Revision: 749086
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.001-1
+ Revision: 717794
- texlive-adfsymbols
- texlive-adfsymbols
- texlive-adfsymbols
- texlive-adfsymbols
- texlive-adfsymbols

