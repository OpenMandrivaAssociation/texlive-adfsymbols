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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides Arkandis foundry's ArrowsADF and BulletsADF fonts
in Adobe Type 1 format, together with TeX/LaTeX support files.

