Name:		texlive-adfsymbols
Version:	1.001
Release:	1
Summary:	SymbolsADF with TeX/LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/adfsymbols
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adfsymbols.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adfsymbols.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Requires(post):	texlive-tetex

%description
The package provides Arkandis foundry's ArrowsADF and
BulletsADF fonts in Adobe Type 1 format, together with
TeX/LaTeX support files. The fonts are licensed under GPL v2 or
later with font exception. (See NOTICE, COPYING, README.) The
TeX/LaTeX support is licensed under LPPL. (See README,
manifest.txt.).

%pre
    %_texmf_mktexlsr_pre

%post
sed -i	-e 's/^#! \(Map ArrowsADF.map\)/\1/'	\
	-e 's/^#! \(Map BulletsADF.map\)/\1/'	\
	%{_texmfdir}/web2c/updmap.cfg
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	if [ -f %{_texmfdir}/web2c/updmap.cfg ]; then
	    sed -i  -e 's/^\(Map ArrowsADF.map\)/#! \1/'	\
		    -e 's/^\(Map BulletsADF.map\)/#! \1/'	\
		%{_texmfdir}/web2c/updmap.cfg
	fi
	%_texmf_mltexlsr_post
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
