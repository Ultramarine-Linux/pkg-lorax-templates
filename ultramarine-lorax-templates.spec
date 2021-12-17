%undefine _disable_source_fetch

Name:           ultramarine-lorax-templates
Version:        0.1
Release:        1%{?dist}
Summary:        Lorax Templates for Ultramarine

License:        MIT
Source0:        https://gitlab.ultramarine-linux.org/release-engineering/lorax-templates/-/archive/%{version}/lorax-templates-%{version}.tar.gz

Requires:       lorax
BuildArch:      noarch

%description


%prep
%autosetup -n lorax-templates-%{version}


%install
rm -rf $RPM_BUILD_ROOT
install -d %{buildroot}/usr/share/lorax/templates.d/60-ultramarine-linux

cp -rv * %{buildroot}/usr/share/lorax/templates.d/60-ultramarine-linux/

%files
/usr/share/lorax/templates.d/60-ultramarine-linux/



%changelog
* Fri Dec 17 2021 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Release
