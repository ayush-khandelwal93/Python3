-Use absolute imports
-All imports path should be set from the path from which the module was run
-If run the module in the root folder, no problems as all the imports in the subfolder is configured from the path of the root folder only
>>>>python main.py

- If want to run some sub folder, cant be run after going to the subfolder as the path is set from the root folder. So run those subfolders as a package from the root folder only
>>>>python -m popularity.pop2
>>>>python -m popularity.pop1

