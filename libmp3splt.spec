#global __arch_install_post   /usr/lib/rpm/check-rpaths   /usr/lib/rpm/check-buildroot
%global soname 0
%bcond_with ltdl

Summary:       Libraries for the mp3Splt project
Name:          libmp3splt
Version:       0.9.2
Release:       19%{?dist}
License:       GPLv2
Group:         Development/Libraries
Source:        http://downloads.sourceforge.net/mp3splt/%{name}-%{version}.tar.gz
URL:           http://mp3splt.sourceforge.net/
Patch0:        v0.9.2..385d2001_2020-11-10.patch
Patch1:        fix_snprintf-overflow.patch

BuildRequires: gettext
BuildRequires: libid3tag-devel
BuildRequires: libmad-devel
BuildRequires: libtool-ltdl-devel
BuildRequires: libvorbis-devel
BuildRequires: pcre-devel
BuildRequires: doxygen, graphviz
BuildRequires: pkgconfig
BuildRequires: flac-devel
BuildRequires: autoconf automake libtool gettext-devel

%description
The mp3Splt project provides utilities to split mp3 and ogg files,
by selecting a begin and an end time position, without decoding.
It is very useful to split large mp3/ogg into smaller files,
or to split entire albums to obtain original tracks.
To split an album, the split points and filenames can be selected
manually or automatically from CDDB (internet or a local file),
or from .cue files.

It supports automatic silence detection, which can be used
to adjust cddb/cue split points. It is also possible to extract
tracks from Mp3Wrap or AlbumWrap files in a few seconds.

The mp3splt project is divided in 3 parts:
libmp3splt, mp3splt and mp3splt-gtk.

%package devel
Summary: Files for the development of applications which will use %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains development files for the mp3splt project.

%prep
%setup -q
%patch -P0 -p2
%patch -P1 -p1

%build
autoreconf -fiv
# Avoid standard rpaths on lib64 archs:
sed -i -e 's|"/lib /usr/lib\b|"/%{_lib} %{_libdir}|' configure
%configure --disable-static \
%if %{with ltdl}
           --with-ltdl-lib=%{_libdir} \
           --with-ltdl-include=%{_includedir}
%endif

%make_build

%install
%make_install

# Remove libtool la files:
find %{buildroot}%{_libdir} -name '*.la' -exec rm -f {} ';'

%find_lang %{name}%{soname}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}%{soname}.lang
%doc AUTHORS NEWS README ChangeLog
%license COPYING
%{_libdir}/%{name}.so.*
%{_libdir}/%{name}%{soname}/libsplt_mp3.so.*
%{_libdir}/%{name}%{soname}/libsplt_ogg.so.*
%{_libdir}/%{name}%{soname}/libsplt_flac.so.*
%exclude %{_docdir}/%{name}/doxygen

%files devel
%{_includedir}/%{name}/*.h
%{_libdir}/%{name}.so
%{_libdir}/%{name}%{soname}/libsplt_mp3.so
%{_libdir}/%{name}%{soname}/libsplt_ogg.so
%{_libdir}/%{name}%{soname}/libsplt_flac.so
%{_libdir}/pkgconfig/%{name}.pc
%{_docdir}/%{name}/doxygen

%changelog
* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.9.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.9.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.9.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 Sérgio Basto <sergio@serjux.com> - 0.9.2-16
- fix snprintf overflow on F38+

* Sun Mar 05 2023 Sérgio Basto <sergio@serjux.com> - 0.9.2-15
- Update to last git snapshot from https://github.com/mp3splt/mp3splt

* Wed Feb 08 2023 Leigh Scott <leigh123linux@gmail.com> - 0.9.2-14
- Rebuild for new flac

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.9.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.9.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 01 2015 Sérgio Basto <sergio@serjux.com> - 0.9.2-1
- Update to 0.9.2 .

* Fri Aug 30 2013 Paulo Roma <roma@lcg.ufrj.br> 0.9.0-13
- Updated to 0.9.0
- Added BR flac-devel.

* Sun Mar 31 2013 Paulo Roma <roma@lcg.ufrj.br> 0.8.2-12
- Updated to 0.8.2
- Changed libmp3splt for libmp3splt%%{soname}.

* Fri Sep 07 2012 Paulo Roma <roma@lcg.ufrj.br> 0.7.3-11
- Updated to 0.7.3

* Wed Jun 06 2012 Paulo Roma <roma@lcg.ufrj.br> 0.7.2-10
- Updated to 0.7.2

* Wed Jan 04 2012 Paulo Roma <roma@lcg.ufrj.br> 0.7.1-9
- Updated to 0.7.1
- Added BR doxygen.
- Added doxygen files.

* Sat Sep 03 2011 Paulo Roma <roma@lcg.ufrj.br> 0.7-9
- Updated to 0.7

* Sun Mar 13 2011 Paulo Roma <roma@lcg.ufrj.br> 0.6.1a-8
- Updated to 0.6.1a

* Mon Sep 27 2010 Paulo Roma <roma@lcg.ufrj.br> 0.6-6
- Updated to 0.6

* Wed Feb 17 2010 Paulo Roma <roma@lcg.ufrj.br> 0.5.9-6
- Updated to 0.5.9

* Wed Nov 04 2009 Paulo Roma <roma@lcg.ufrj.br> 0.5.8a-6
- Updated to 0.5.8a
- Using %%bcond_with ltdl.

* Sat Oct 31 2009 Paulo Roma <roma@lcg.ufrj.br> 0.5.8-5
- Updated to 0.5.8
- Removed "sed echo" from build section.

* Thu Jul 30 2009 Paulo Roma <roma@lcg.ufrj.br> 0.5.7a-4
- Bugfix release: 0.5.7a

* Mon Jul 27 2009 Paulo Roma <roma@lcg.ufrj.br> 0.5.7-4
- Updated to 0.5.7
- Moved libsplt_mp3.so and libsplt_ogg.so back to devel.
- Using find_lang.

* Tue Jun 23 2009 Paulo Roma <roma@lcg.ufrj.br> 0.5.6-3
- Fixed #476061 - libsplt_mp3.so and libsplt_ogg.so
  moved from devel to the main package.

* Sat May 16 2009 Paulo Roma <roma@lcg.ufrj.br> 0.5.6-2
- Updated to 0.5.6

* Sat May 09 2009 Paulo Roma <roma@lcg.ufrj.br> 0.5.5-2
- Updated to 0.5.5
- Added BR libid3tag-devel and libtool-ltdl.
- Fixed configure for finding libtool-ltdl.

* Sun Aug 26 2007 Paulo Roma <roma@lcg.ufrj.br> 0.3.1-1
- Initial spec file.

