# fem_mcip
FEM multiple calculation in pipeline (fem_mcip) using opensource tools / Wielokrotne analizy MES z użyciem narzędzi o otwartym źródle

by MJB
2026-03-21

Uwaga: Jeżeli jesteś zainteresowana/y wyłącznie uruchomieniem obliczeń fem_mcip, to przejdź do załącznika A.
Uwaga: ```bash ...``` oznacza by skorzystać z powłoki bash.
Uwaga: ```python ...``` oznacza część programy w języku Python.

### ### ### ### ###
1. Wyznaczenie zadania i celu
### ### ### ### ###

1.1. Wyznacz zadania i celu symulacji.
1.2. Wyznacz podstawy działań, w tym weryfikacji i walidacji wyników.
1.3. Przygotuj i przeanalizuj dane próbek.

### ### ### ### ###
2. Zasoby
### ### ### ### ###

Uwaga: Schemat tworzenia zasobów ukazano w modelling_process_diagram.pdf

2.1. Zainstaluj wymagany system operacyjny np. Kubuntu.
2.1.1. Kubuntu: https://cdimage.ubuntu.com/kubuntu/releases/24.04.4/release/

Uwaga: Użyto wersji: 24.04.4.

2.2. Zainstaluj środowisko Miniconda: https://repo.anaconda.com/miniconda/

Uwaga: Użyto wersji: py312_24.7.1-0.
Uwaga: Szczegółowy opis instalacji i konfiguracji środowiska Miniconda znajduje się w załączniku B.

2.3. Zainstaluj FreeCADa: https://www.freecad.org/downloads.php?lang=en

Uwaga: Użyto wersji: 1.0.
Uwaga: Zaleca się skorzystanie z wersji 1.1 w paczce AppImage: https://github.com/FreeCAD/FreeCAD/releases/tag/1.1.0
Uwaga: Zaleca się instalację paczki w katalogu np. home/user/apps/freecad_11 - zamiast ciągu "user" użyj Twoich danych np. "john_smith".

2.4. Zainstaluj Salome Platform: https://www.salome-platform.org/?page_id=2430

Uwaga: Użyto wersji: 9.14.0, Linux Universal.
Uwaga: Zaleca się instalację w katalogu np. home/user/apps/salome_914 - zamiast ciągu "user" użyj Twoich danych np. "john_smith".

2.5. Zainstaluj Gmsh: https://gmsh.info/bin/Linux/gmsh-4.13.1-Linux64.tgz

Uwaga: Użyto wersji: 4.13.1
Uwaga: Zaleca się instalację w katalogu np. home/user/apps/gmsh_4131 - zamiast ciągu "user" użyj Twoich danych np. "john_smith".
Uwaga: Do analizy wielokrotnej użyto biblioteki gmsh 4.13.1 z repozytorium pip, patrz załącznik B.

2.6. Zainstaluj Salome Meca: https://code-aster.org/spip.php?article303

Uwaga: Użyto wersji salome_meca-lgpl-2024.1.0-1-20240327.
Uwaga: Zaleca się instalację w katalogu np. home/user/apps/salome_meca_2k14 - zamiast ciągu "user" użyj Twoich danych np. "john_smith".
Uwaga: Do analizy wielokrotnej użyto biblioteki code_aster 17.0.1 z repozytorium conda-forge, patrz punkt załącznik B.

2.7. Zainstaluj ParaView: https://www.paraview.org/download/

Uwaga: Użyto wersji: 5.13.2.
Uwaga: Zaleca się instalację w katalogu np. home/user/apps/paraview_5132 - zamiast ciągu "user" użyj Twoich danych np. "john_smith".

2.8. Utwórz katalog główny np. fem_mcip dla potrzeb symulacji. Wymagana kontrola wolnej przestrzeni na dysku.

Uwaga: Zaleca się instalację w katalogu np. home/user/analyses/fem_mcip - zamiast ciągu "user" użyj Twoich danych np. "john_smith".

2.9. Zainstaluj gita. Została wybrana instalacja wersji systemu dostępnego bezpośrednio z zasobów gita.
2.9.1. Dodaj repozytorium gita:

```bash
sudo add-apt-repository ppa:git-core/ppa
```

2.9.2. Zaktualizuj repozytoria apt:

```bash
sudo apt update
```

2.9.3. Zainstaluj gita poleceniem:

```bash
sudo apt install git
```

2.9.4. Pobieranie zasobów z GitHub.

```bash
git clone https://github.com/ennamepro/fem_mcip.git
```

2.10. Jeżeli nie chcesz korzystać z Git, możesz ręcznie przygotować wszystkie wymagane katalogi np. poleceniem `md base-stage1s`.
2.10.1. base-stage1s
2.10.2. exports
2.10.3. round_specimen_a1_salome_breps
2.10.4. round_specimen_a1_salome_comms
2.10.5. round_specimen_a1_salome_geoms
2.10.6. round_specimen_a1_salome_meds
2.10.7. round_specimen_a1_salome_pngs
2.10.8. round_specimen_a1_salome_pviews
2.10.9. round_specimen_a1_salome_rmeds
2.10.10. round_specimen_a1_salome_txts

Uwaga: Przykład struktury katalogu głównego zawarto w powyższym repozytorium GitHub.
Uwaga: Pamiętaj by skopiować wszystkie pliki z repozytorium do katalogu na Twoim komputerze.

### ### ### ### ###
3. Przygotowania
### ### ### ### ###

Uwaga: Punkt ten zawiera opis czynności wykonywanych podczas przygotowywania symulacji. Jeżeli chcesz skorzystać wyłącznie z pobranych zasobów, to przejdź do punktu 3.9.

3.1. Modeluj w 3D zmienności próbki w FreeCAD. Zapisz pliki próbek w katalogu: fcstds.
3.1.1. Jako zmienne w modelu próbki okrągłej z karbem półokrągłym wybrano `bar_radius` i `undercut_radius`.

Uwaga: Przykładowe widoki próbek pokazano w round_specimen_a1_salome_all.pdf

3.2. Modeluj próbkę w Salome Platform moduł Geometry. Można skorzystać z wielu materiałów treningowych np. https://docs.salome-platform.org/latest/main/index.html
3.2.1. Pamiętaj o utworzeniu grup (physical groups), jak we wzorcu round_specimen_a1_salome_geom_pattern.py.
3.2.2. Zapisz model w formacie *.brep w katalogu round_specimen_a1_salome_breps.
3.2.3. Zapisz model jako Dump Study pod wybraną nazwą round_specimen_a1_salome_geom_pattern.py w katalogu głównym elasf_fc.

3.3. Otwórz plik round_specimen_a1_salome_geom_pattern.py w edytorze np. Kate.
3.3.1. W pliku przygotuj zmienne parametrów aktualnych, patrz plik round_specimen_a1_salome_geom_pattern.py:
3.3.1.1. `X_length = X_length_pattern` (niewymagane)
3.3.1.2. `bar_radius = bar_radius_pattern`
3.3.1.3. `undercut_radius = undercut_radius_pattern`
3.3.2. Zamień zmienne aktualne np. "15" jako bar radius na `bar_radius`. W pliku round_specimen_a1_salome_geom_pattern.py w miejscach poza definicjami wszystkie parametry aktualne już zamieniono np. na `bar_radius`.
3.3.4. Zapisz plik round_specimen_a1_salome_geom_pattern.py w katalogu głównym.

3.4. Wygeneruj siatkę korzystając z Gmsh. Możesz skorzystać z wielu materiałów treningowych np. https://gmsh.info/#Documentation
3.4.1. Pamiętaj o zdefiniowaniu Physical Groups. W pliku round_specimen_a1_stress_concentrator_all.py physical groups są zdefiniowane w funkcji `gmsh_mesher`.
3.4.2. Zapisz model w formacie *.geo w katalogu głównym. Umożliwi to zdefiniowanie sposobu nakładania siatki w funkcji `gmsh_mesher`. Wykorzystaj do tego metody (parametry podano jako przykładowe):
`gmsh.model.addPhysicalGroup(2, [3, 18], tag=103)`,
`gmsh.model.setPhysicalName(2, 103, "Z_0")`.

3.5. Przygotuj analizę w Salome_Meca korzystając z siatki wcześniej przygotowanej. Możesz zastosować materiały treningowe np. https://code-aster.org/spip.php?rubrique68
3.5.1. Do przygotowania analizy może posłużyć plik round_specimen_a1_salome_pattern.comm.
3.5.2. Po weryfikacji analizy zastosuj plik export do przygotowania szablonu, pliku export_pattern. Plik export winien być w katalogu przygotowanym przez Salome Meca - `nazwa_projektu_Files/RunCase_1/Result-Stage_1`.
3.5.3. Używany plik export_pattern znajduje się katalogu głównym. Można go wykorzystać do porównania z otrzymanym plikiem export w wyniku analizy FEM. W pliku export_pattern należy zmienić ścieżki dostępu - są one podane w pliku export. Pliki oraz ich parametry muszą pozostać, jak niżej:
3.5.3.1. `F comm /home/user/data/analyses/fem_mcip/round_specimen_a1_salome/round_specimen_a1_salome_comms/round_specimen_a1_salome_pattern.comm D  1`
3.5.3.2. `F libr /home/user/data/analyses/fem_mcip/round_specimen_a1_salome/round_specimen_a1_salome_meds/round_specimen_a1_salome_pattern_gmsh.med D  20`
3.5.3.3. `F libr /home/user/data/analyses/fem_mcip/round_specimen_a1_salome/round_specimen_a1_salome_rmeds/round_specimen_a1_salome_pattern.rmed R  80`
3.5.3.4. `F libr /home/user/data/analyses/fem_mcip/round_specimen_a1_salome/round_specimen_a1_salome_txts/round_specimen_a1_salome_pattern.txt R  8`
3.5.3.5. `F mess /home/user/data/analyses/fem_mcip/round_specimen_a1_salome/messages/message_pattern R  6`
3.5.3.6. `R base /home/user/data/analyses/fem_mcip/round_specimen_a1_salome/base-stage1s/base-stage1_pattern R  0`

Uwaga: zamiast ciągu "user" użyj Twoich danych np. "john_smith".

3.6. Przygotuj plik comm na podstawie którego Code_Aster wykona analizy FEM. Można skorzystać z wzorca - round_specimen_a1_salome_pattern.comm. Przygotowano w nim ciąg znaków `PRES=-X.XX`, który będzie zmieniany w wartość liczbową ciśnienia stanowiącego siłę rozciągającą pręt. Pozostałe parametry Twojej symulacji znajdują się w pliku comm w katalogu `nazwa_projektu_Files/RunCase_1/Result-Stage_1`.

Uwaga: Przykładowy widok warunków brzegowych pokazano w round_specimen_a1_salome_bc.pdf

3.6.1. Należy zwrócić uwagę, że w analizie stosowano naprężenia zredukowane HMH (Huber, Mises, Hencky), naprężenia główne 1,2,3 oraz trójosiowość stanu naprężenia. Zatem w wynikach zaznaczono: `NOM_CMP=('VMIS', 'PRIN_1', 'PRIN_2', 'PRIN_3', 'TRIAX')`. W innych pracach można zmieniać zapisywane wielkości.

3.7. Korzystając z ParaView można przygotować wizualizację wyników obliczeń. Należy do tego celu wykorzystać plik rmed z obliczeń FEM.
3.7.1. W ParaView wywołaj komendę: Tools/Start Trace
3.7.2. W ParaView wczytaj plik rmed. Pamiętaj by w opcjach: Tools/Manage Plugins, wybrać MEDReader wraz z Auto Load. W tym wypadku translator plików rmed będzie uruchamiany w trakcie startu ParaView.
3.7.3. Ustaw wszystkie parametry widoku, wyświetlane pola np. HMH, etc. Pamiętaj, że w trakcie wykonywania ciągu obliczeń próbki będą różniły się wielkością. Należy to przewidzieć.
3.7.4. Po przygotowaniu w ParaView oczekiwanej wizualizacji korzystaj z komendy: Tools/Stop Trace. Pojawi się okno ze skryptem Python. Pamiętaj by dodać do niego:

```python
LoadPlugin('MEDReader', remote=False, ns=globals())
```

spowoduje to dodanie translatora plików w formacie MED. Jest to wymagane, gdyż komenda Tools/Stop Trace generuje skrypt Pythona, ale nie dodaje wymogu ładowania wtyczki MEDReader.

3.7.5. Wizualizacja wyników z ParaView wymaga przygotowania stosownego szablonu. Można do tego celu zastosować plik round_specimen_a1_salome_pview_pattern.py.

3.8. Aktywuj środowisko conda np. py311.

```bash
conda activate py311
```

3.9. Uruchom aplikację Spyder z załadowaniem pliku round_specimen_a1_stress_concentrator.py

```bash
spyder round_specimen_a1_stress_concentrator.py
```

3.9.1. Przygotuj liczniki będące promieniami karbu i próbki oraz skoki iteracji np.:

```python
undercut_radius_min = 1.5
undercut_radius_max = 1.5 # max 12.0
undercut_radius_step = 0.5

bar_radius_min = 15.0
bar_radius_max = 15.0 # max 26.5
bar_radius_step = 0.5
```

3.9.2. Ze względu na mogące wystąpić błędy, w licznikach:

```python
undercut_radius_max = 1.5 # max 12.0
bar_radius_max = 15.0 # max 26.5
```

przyjęto wartości, które spowodują wykonanie wyłącznie jednej iteracji.

3.9.3. Przygotowane liczniki umieść w pliku uruchomieniowym round_specimen_a1_stress_concentrator.py

3.10. Wywołaj komendę Run (F5)
3.10.1. Jeżeli nie pojawią się błędy, zmień parametry liczników, na:

```python
undercut_radius_max = 12.0
bar_radius_max = 26.5
```

3.11. Wywołaj komendę Run (F5), czekaj na wykonanie programu - może to potrwać kilka godzin.

### ### ### ### ###
4. Działanie programu
### ### ### ### ###

Uwaga: Schemat wykonywania obliczeń process_calculation_diagram.pdf

4.1. Przygotowanie instrukcji do działania w pętli.
4.2. Zastosowanie pętli while w programie od wartości min do wartości max.
4.3. Wykonanie obliczeń siły rozciągającej próbki. W programie rozłożono siłę na powierzchni bocznej próbki.
4.4. Przygotowanie pliku export wg wzorca export_pattern dla kolejnej próbki.
4.5. Przygotowanie pliku comm wg wzorca round_specimen_a1_salome_pattern.comm dla kolejnej próbki.
4.6. Przygotowanie pliku geometry do Salome Platfrom wg wzorca round_specimen_a1_salome_geom_pattern.py dla kolejnej próbki.
4.7. Przygotowanie pliku pview do ParaView wg wzorca round_specimen_a1_salome_pview_pattern.py dla kolejnej próbki.
4.8. Wywołanie aplikacji Salome Platform z parametrem będącym nazwą skryptu tworzącego geometrię próbki.
4.8.1. Można skorzystać z polecenia (nazwa parametru jest przykładowa):

```python
geom = subprocess.run(["../../../apps/salome_914/salome", "-t", "-w1", "round_specimen_a1_salome_geoms/probka_okragla_a1_salome_geom_15_0_1_5.py"])
```

Uwaga: zamiast ciągu "user" użyj Twoich danych np. "john_smith".

4.9. Wywołanie funkcji `gmsh_mesher` podając paramtery: X_length, bar_radius, undercut_radius.
4.10. Uruchomienie analizy FEM z użyciem Code_Aster z parametrem będącym nazwą skryptu export.
4.10.1. Można skorzystać z polecenia (nazwa parametru jest przykładowa):

```python
code_aster = subprocess.run(["as_run", "exports/export_15_0_1_5"])
```

4.11. Wywołanie aplikacji ParaView z parametrem będącym nazwą skryptu tworzącego wizualizację próbki.
4.11.1. Można skorzystać z polecenia (nazwa parametru jest przykładowa):

```python
paraview = subprocess.run(["../../../apps/paraview_5132/bin/pvpython", "round_specimen_a1_salome_pviews/round_specimen_a1_salome_pview_15_0_1_5.py"])
```

Uwaga: zamiast ciągu "user" użyj Twoich danych np. "john_smith".

4.12. Ustawienie nowych wartości liczników i powrót na początek pętli.

### ### ### ### ###
5. Zakończenie działania programu
### ### ### ### ###

5.1. Zakończenie działania programu po osiągnięciu przez liczniki wartości max.
5.2. Podanie czasu działania programu.
5.3. W poniższych katalogach można znaleźć odpowiednie wyniki obliczeń:
5.3.1. round_specimen_a1_salome_breps - pliki graficzne próbek.
5.3.2. round_specimen_a1_salome_comms - pliki comm do Code_Aster.
5.3.3. round_specimen_a1_salome_geoms - pliki geomterii do Salome Platform.
5.3.4. round_specimen_a1_salome_meds - pliki z siatkami do Code_Aster.
5.3.5. round_specimen_a1_salome_pngs - pliki graficzne zawierające wyniki obliczeń - pola skalarne trójosiowości stanu naprężenia.
5.3.6. round_specimen_a1_salome_pviews - pliki wsadowe do ParaView.
5.3.7. round_specimen_a1_salome_rmeds - pliki wyników obliczeń z Code_Aster.
5.3.8. round_specimen_a1_salome_txts - pliki tekstowe obliczeń z Code_Aster. Są one używane do dalszych analiz z użyciem ML - patrz repozytorium elasf_fc na GitHubie.

### ### ### ### ###
Załącznik A. Obliczenia fem_mcip
### ### ### ### ###

A.1. Jeżeli chcesz uruchomić przygotowane obliczenia, to przygotuj system do pracy.
A.1.1. Zainstaluj Gita zgodnie z punktem 2.9.
A.1.2. Utwórz katalog np. analyses. Przejdź do tego katalogu.
A.1.3. Wykonaj polecenie:

```bash
git clone https://github.com/ennamepro/fem_mcip.git
```

A.1.4. Zainstaluj i skonfiguruj Miniconda wg punktu 2.2. i załącznika B. Pamiętaj o zainstalowaniu pakietu code_aster 17.0.1 z repozytorium conda-forge.
A.1.5. Zainstaluj i skonfiguruj Salome Platform wg 2.4.
A.1.6. Zainstaluj i skonfiguruj Gmsh wg punktu 2.5.
A.1.7. Zainstaluj i skonfiguruj ParaView wg 2.7.

A.2. Aktywuj środowisko conda np. py311.

```bash
conda activate py311
```

A.3. Uruchom aplikację Spyder z załadowaniem pliku round_specimen_a1_stress_concentrator.py

```bash
spyder round_specimen_a1_stress_concentrator.py
```

Uwaga: Pamiętaj o ścieżkach dostępu do aplikacji i plików. W programie round_specimen_a1_stress_concentrator.py zaznaczono wszystkie wymagania.

A.3.1. Wywołaj komendę Run (F5)
A.3.1.1. Ze względu na mogące wystąpić błędy, w licznikach:

```python
undercut_radius_max = 1.5 # max 12.0
bar_radius_max = 15.0 # max 26.5
```

przyjęto wartości, które spowodują wykonanie wyłącznie jednej iteracji.

A.3.1.2. Jeżeli nie pojawią się błędy, zmień parametry liczników, na:

```python
undercut_radius_max = 12.0
bar_radius_max = 26.5
```

A.3.1.3. Wywołaj komendę Run (F5), czekaj na wykonanie programu - może to potrwać kilka godzin.

A.4. Wyniki analiz znajdują się w odpowiednich katalogach podanych z punkcie 5.

### ### ### ### ###
Załącznik B. Instalacja i konfiguracja środowiska Miniconda
### ### ### ### ###

B.1. Pełny opis dostępu do zasobów, ich instalacji i konfiguracji znajduje się tutaj:

https://www.anaconda.com/docs/getting-started/miniconda/install/linux-install#wget

B.2. Po pobraniu pakietu np. Miniconda3-py312_24.7.1-0-Linux-x86_64.sh nadaj mu atrybut execute np. `chmod a+x Miniconda3-py312_24.7.1-0-Linux-x86_64.sh`.

B.3. Uruchom plik Miniconda3-py312_24.7.1-0-Linux-x86_64.sh i wykonaj wszystkie kroki sugerowane przez instalator.

B.3. Utwórz wymagane środowisko z interpreterem Python 3.11.

```bash
conda create -n py311 python=3.11
```

Uwaga: Środowisko Miniconda 26.1.1-1 z dnia 2026-03-04 zawiera następujące interpretery Pythona: 3.13.12, 3.12.12, 3.11.14, 3.10.19

B.4. Aktywuj utworzone środowisko:

```bash
conda activate py311
```

B.5. Zainstaluj wymagane pakiety:

```bash
conda install conda-forge::code-aster=17.0.1
conda install spyder=6.0.7
pip install gmsh==4.13.1
```
