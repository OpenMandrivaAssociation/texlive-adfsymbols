%global tl_name adfsymbols
%global tl_revision 78315

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	SymbolsADF with TeX/LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/adfsymbols
License:	lppl1.3c gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adfsymbols.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adfsymbols.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adfsymbols.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides Arkandis foundry's ArrowsADF and BulletsADF fonts
in Adobe Type 1 format, together with TeX/LaTeX support files.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/source/fonts
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/adfsymbols
%dir %{_datadir}/texmf-dist/fonts/afm/arkandis
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/tfm/arkandis
%dir %{_datadir}/texmf-dist/fonts/type1/arkandis
%dir %{_datadir}/texmf-dist/source/fonts/adfsymbols
%dir %{_datadir}/texmf-dist/tex/latex/adfsymbols
%dir %{_datadir}/texmf-dist/fonts/afm/arkandis/adfsymbols
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/adfsymbols
%dir %{_datadir}/texmf-dist/fonts/map/dvips/adfsymbols
%dir %{_datadir}/texmf-dist/fonts/tfm/arkandis/adfsymbols
%dir %{_datadir}/texmf-dist/fonts/type1/arkandis/adfsymbols
%doc %{_datadir}/texmf-dist/doc/fonts/adfsymbols/COPYING
%doc %{_datadir}/texmf-dist/doc/fonts/adfsymbols/NOTICE
%doc %{_datadir}/texmf-dist/doc/fonts/adfsymbols/README.md
%doc %{_datadir}/texmf-dist/doc/fonts/adfsymbols/adfsymbols.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/adfsymbols/manifest.txt
%{_datadir}/texmf-dist/fonts/afm/arkandis/adfsymbols/ArrowsADF.afm
%{_datadir}/texmf-dist/fonts/afm/arkandis/adfsymbols/BulletsADF.afm
%{_datadir}/texmf-dist/fonts/enc/dvips/adfsymbols/SymbolsADF.enc
%{_datadir}/texmf-dist/fonts/map/dvips/adfsymbols/adfsymbols.map
%{_datadir}/texmf-dist/fonts/tfm/arkandis/adfsymbols/ArrowsADF.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/adfsymbols/BulletsADF.tfm
%{_datadir}/texmf-dist/fonts/type1/arkandis/adfsymbols/ArrowsADF.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/adfsymbols/BulletsADF.pfb
%doc %{_datadir}/texmf-dist/source/fonts/adfsymbols/adfarrows.dtx
%doc %{_datadir}/texmf-dist/source/fonts/adfsymbols/adfbullets.dtx
%doc %{_datadir}/texmf-dist/source/fonts/adfsymbols/adfsymbols.dtx
%doc %{_datadir}/texmf-dist/source/fonts/adfsymbols/adfsymbols.ins
%{_datadir}/texmf-dist/tex/latex/adfsymbols/adfarrows.sty
%{_datadir}/texmf-dist/tex/latex/adfsymbols/adfbullets.sty
%{_datadir}/texmf-dist/tex/latex/adfsymbols/adfsymbols-uni.tex
%{_datadir}/texmf-dist/tex/latex/adfsymbols/uarrowsadf.fd
%{_datadir}/texmf-dist/tex/latex/adfsymbols/ubulletsadf.fd
