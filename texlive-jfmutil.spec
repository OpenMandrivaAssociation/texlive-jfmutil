%global tl_name jfmutil
%global tl_revision 60987

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3.3
Release:	%{tl_revision}.1
Summary:	Utility to process pTeX-extended TFM and VF
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/utilities/jfmutil
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jfmutil.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jfmutil.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(jfmutil.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This program provides functionality to process data files (JFM and VF)
that form logical fonts used in (u)pTeX. The functions currently
available include: The mutual conversion between Japanese virtual fonts
(pairs of VF and JFM) and files in the "ZVP format", which is an
original text format representing data in virtual fonts. This function
can be seen as a counterpart to the vftovp/vptovf programs. The mutual
conversion between VF files alone and files in the "ZVP0 format", which
is a subset of the ZVP format.

