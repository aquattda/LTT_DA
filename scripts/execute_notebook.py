"""Execute the original notebook, save fresh outputs separately, fail on cell errors."""
from datetime import datetime
from pathlib import Path
import os
import sys
import traceback

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'Do_An/walmart_eda_model/3122410447_LTT.ipynb'
OUTPUT = ROOT / 'artifacts/notebook' / datetime.now().strftime('%Y%m%d-%H%M%S-%f')
OUTPUT.mkdir(parents=True, exist_ok=True)
os.environ['WALMART_PROJECT_ROOT'] = str(ROOT)
os.environ['WALMART_OUTPUT_DIR'] = str(OUTPUT)
nb = nbformat.read(SOURCE, as_version=4)
for cell in nb.cells:
    if cell.cell_type == 'code':
        cell.outputs = []
        cell.execution_count = None


def report_cell(cell, cell_index, **kwargs):
    if cell.cell_type == 'code' and cell.source.strip():
        print(f'Executing cell {cell_index + 1}/{len(nb.cells)}', flush=True)


client = NotebookClient(nb, timeout=1800, kernel_name='walmart', allow_errors=False,
                        resources={'metadata': {'path': str(ROOT)}}, on_cell_start=report_cell)
result = 0
try:
    client.execute()
    print('PASS: notebook executed without cell errors', flush=True)
except Exception:
    traceback.print_exc()
    result = 1
finally:
    target = OUTPUT / (SOURCE.stem + ('.executed.ipynb' if result == 0 else '.failed.ipynb'))
    nbformat.write(nb, target)
    print('Notebook output:', target, flush=True)
raise SystemExit(result)
