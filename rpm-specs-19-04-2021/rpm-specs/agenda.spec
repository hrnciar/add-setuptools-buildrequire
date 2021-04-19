%global appname com.github.dahenson.agenda

Name:           agenda
Summary:        A simple, slick, speedy and no-nonsense task manager
Version:        1.1.0
Release:        8%{?dist}
# The entire source is GPLv3+, except data/Agenda.css which is GPLv2+,
# test/TestCase.vala which is LGPLv2+, and
# data/com.github.dahenson.agenda.appdata.xml.in which is CC0.
License:        GPLv3+ and GPLv2+ and LGPLv2+ and CC0

URL:            https://github.com/dahenson/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       hicolor-icon-theme

Summary(ca):    Un gestor de tasques fàcil d’utilitzar
Summary(de):    Ein einfacher, handlicher, schneller und nützlicher Aufgaben Verwalter
Summary(es):    Un administrador de tareas simple, pulido, rápido y sin complicaciones
Summary(fr):    Un gestionnaire de tâches simple, rapide et élégant
Summary(gl):    Un xestor de tarefas pulido, sinxelo, rápido e sen complicacións
Summary(it):    Un promemoria semplice, elegante, veloce e senza fronzoli
Summary(ja):    タスクを完了しましょう
Summary(ka):    მარტივი, მოხერხებული, სწრაფი დავალებების მმართველი ყოველგვარი უაზრობების გარეშე
Summary(ko):    간단하고 미려한 일정 관리자
Summary(lt):    Paprasta, vikri, greita, dalykiška užduočių tvarkytuvė
Summary(ms):    Pengurus tugas yang ringkas dan pantas
Summary(pl):    Prosty, gładki, szybki i niebezsensowny menedżer zadań
Summary(pt):    Um gestor de tarefas simples, liso, rápido e sem falhas
Summary(ru):    Простой и быстрый менеджер задач
Summary(sr):    Једноставан, гладак, брз и без којештарија управник задатака
Summary(tr):    Basit, şık, hızlı ve zırvalıksız görev yöneticisi
Summary(ur):    ﺎﯿﮐ ﺱﺍﺩہ، ہﻮﺸﯾﺍﺭ، ﻑﻭﺮﯾ ﺍﻭﺭ ﺲﯾﺩﺍہ ﺱﺍﺩہ ٹﺎﺴﮐ ﻢﯿﻨﯿﺟﺭ
Summary(zh_CN): 简单流畅、快速不脑残的任务规划管理器

%description
A task manager to help you keep track of the tasks that matter most.

Sometimes, you just need a task list to keep you motivated. Agenda provides a
way to write down your tasks and tick them off as you complete them. The list
is saved automatically, so you can close the list to get it out of the way
without losing your place.

Key Features:

  • Saves your task list automatically
  • See your completed tasks until you choose to delete them
  • Autocompletion for previously added tasks
  • Undo/Redo with Ctrl-Z and Ctrl-Y
  • Quit with the Esc key

%description -l ja
最も重要なタスクの記録に便利な、タスク管理アプリです。

モチベーションを維持するために、タスクリストが必要なときはありませんか。
Agenda を使えば、タスクを登録して、終わったらチェックマークをつけていくこと
ができます。リストは自動的に保存されるので、最新の状態を失うことなくリストを
閉じられます。

主な機能:

  • タスクリストを自動的に保存します
  • 完了したタスクは、削除しない限り確認できます
  • 以前に追加したタスクを自動補完します
  • Esc キーで終了できます


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license LICENSE

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Mon Mar 08 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1.0-8
- Localize summary and description where translations are available upstream

* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-7
- Rebuilt for granite 6 soname bump.

* Tue Feb 09 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1.0-6
- Add CC0 to License field for AppData file

* Tue Feb 09 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1.0-5
- Correct License from “GPLv3” to “GPLv3+ and GPLv2+ and LGPLv2+”

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 06 2020 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1
- Update to version 1.1.0.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 16 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.12-1
- Update to version 1.0.12.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.11-1
- Update to version 1.0.11.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jan 21 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.9-1
- Initial package.

