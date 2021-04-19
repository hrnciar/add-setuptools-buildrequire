%global dia_datadir %{_datadir}/dia
%global shapes electronic

Name:           dia-%{shapes}
Version:        0.1
Release:        18%{?dist}
Summary:        Dia Digital IC logic shapes

License:        GPLv2+
URL:            http://dia-installer.de/shapes/electronic/index_en.html
Source0:        http://dia-installer.de/shapes/electronic/electronic.zip

Requires:       dia
BuildArch:      noarch

%description
The following shapes are included in the package:
 * Antenna
 * Bell
 * Button
 * Capacitor
 * Electrolytic capacitor
 * Crystal
 * Di-Gate
 * Diac
 * Engine
 * Headphone
 * Inverse diode
 * Schottky diode
 * Tunnel diode
 * Zenner diode
 * Inductor
 * LED display
 * Microphone
 * Photo-emiting part
 * Photosensitive part
 * Potenciometer
 * Ground
 * Contact
 * Contact Pair
 * IN Port
 * OUT Port
 * IN/OUT Port
 * Voltmeter
 * Ampermeter
 * Source or Meter
 * Current source
 * Substitute linearised source
 * Voltage source
 * Alternating voltage source
 * Direct voltage source
 * Bipolar transistor NPN
 * Bipolar transistor NPN
 * Bipolar transistor PNP
 * Bipolar transistor PNP
 * JFE transitor - N
 * JFE transistor - P
 * MISFE conducting transistor - N
 * MISFE conducting transistor - P
 * MISFE inducting transistor - N
 * MISFE inducting transistor - P
 * Single ..... transistor
 * Triac
 * Diode tyristor, blocking
 * Triode tyristor, blocking
 * Vacuum diode
 * Vacuum pentode
 * Vacuum triode
 * Linear variable part
 * Nonlinear variable part
 * Varicap

%prep
%setup -q -c


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{dia_datadir}/sheets
cp -p sheets/%{shapes}.sheet %{buildroot}%{dia_datadir}/sheets
cp -pr shapes %{buildroot}%{dia_datadir}



%files
%doc COPYING
%{dia_datadir}/sheets/%{shapes}.sheet
%{dia_datadir}/shapes/%{shapes}/

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 15 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 0.1-1
- init fedora package