#Run pip freeze for the system interpreter. Take the contents and create a similar viru]tualenv.

PS C:\Users\gauta\OneDrive\Desktop\chapter13ps> pip freeze > requirements.txt
PS C:\Users\gauta\OneDrive\Desktop\chapter13ps> virtualenv rakhienv
created virtual environment CPython3.14.3.final.0-64-x86_64 in 14483ms
  creator CPython3Windows(dest=C:\Users\gauta\OneDrive\Desktop\chapter13ps\rakhienv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, via=copy, app_data_dir=C:\Users\gauta\AppData\Local\pypa\virtualenv\Cache)
    added seed packages: pip==26.0.1
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
PS C:\Users\gauta\OneDrive\Desktop\chapter13ps>
PS C:\Users\gauta\OneDrive\Desktop\chapter13ps>
PS C:\Users\gauta\OneDrive\Desktop\chapter13ps>
PS C:\Users\gauta\OneDrive\Desktop\chapter13ps> .\rakhienv\Scripts\activate.ps1
(rakhienv) PS C:\Users\gauta\OneDrive\Desktop\chapter13ps> pip install -r.\requirements.txt
Collecting distlib==0.4.0 (from -r .\requirements.txt (line 1))
  Using cached distlib-0.4.0-py2.py3-none-any.whl.metadata (5.2 kB)
Collecting filelock==3.25.2 (from -r .\requirements.txt (line 2))
  Using cached filelock-3.25.2-py3-none-any.whl.metadata (2.0 kB)
Collecting numpy==2.4.3 (from -r .\requirements.txt (line 3))
  Using cached numpy-2.4.3-cp314-cp314-win_amd64.whl.metadata (6.6 kB)
Collecting pandas==3.0.1 (from -r .\requirements.txt (line 4))
  Using cached pandas-3.0.1-cp314-cp314-win_amd64.whl.metadata (19 kB)
Collecting platformdirs==4.9.4 (from -r .\requirements.txt (line 5))
  Using cached platformdirs-4.9.4-py3-none-any.whl.metadata (4.7 kB)
Collecting python-dateutil==2.9.0.post0 (from -r .\requirements.txt (line 6))
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting python-discovery==1.1.3 (from -r .\requirements.txt (line 7))
  Using cached python_discovery-1.1.3-py3-none-any.whl.metadata (5.4 kB)
Collecting six==1.17.0 (from -r .\requirements.txt (line 8))
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting tzdata==2025.3 (from -r .\requirements.txt (line 9))
  Using cached tzdata-2025.3-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting virtualenv==21.2.0 (from -r .\requirements.txt (line 10))
  Using cached virtualenv-21.2.0-py3-none-any.whl.metadata (3.5 kB)
Using cached distlib-0.4.0-py2.py3-none-any.whl (469 kB)
Using cached filelock-3.25.2-py3-none-any.whl (26 kB)
Using cached numpy-2.4.3-cp314-cp314-win_amd64.whl (12.4 MB)
Using cached pandas-3.0.1-cp314-cp314-win_amd64.whl (9.9 MB)
Using cached platformdirs-4.9.4-py3-none-any.whl (21 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached python_discovery-1.1.3-py3-none-any.whl (31 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached tzdata-2025.3-py2.py3-none-any.whl (348 kB)
Using cached virtualenv-21.2.0-py3-none-any.whl (5.8 MB)
Installing collected packages: distlib, tzdata, six, platformdirs, numpy, filelock, python-discovery, python-dateutil, virtualenv, pandas
Successfully installed distlib-0.4.0 filelock-3.25.2 numpy-2.4.3 pandas-3.0.1 platformdirs-4.9.4 python-dateutil-2.9.0.post0 python-discovery-1.1.3 six-1.17.0 tzdata-2025.3 virtualenv-21.2.0
(rakhienv) PS C:\Users\gauta\OneDrive\Desktop\chapter13ps>
(rakhienv) PS C:\Users\gauta\OneDrive\Desktop\chapter13ps>
#pip freeze > requirements.txt
# virtualenv rakhienv 