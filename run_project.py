"""Project-local environment and launch commands (no shell activation required)."""
import argparse
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
ENV = ROOT / '.venv'
PYTHON = ENV / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
APP = ROOT / 'Do_An/walmart_eda_model'
NOTEBOOK = APP / '3122410447_LTT.ipynb'


def run(*args):
    env = os.environ.copy()
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    env['PYTHONIOENCODING'] = 'utf-8'
    env['WALMART_PROJECT_ROOT'] = str(ROOT)
    for key, name in {'JUPYTER_RUNTIME_DIR': 'jupyter', 'JUPYTER_CONFIG_DIR': 'config',
                      'IPYTHONDIR': 'ipython', 'MPLCONFIGDIR': 'matplotlib'}.items():
        directory = ENV / 'runtime' / name
        directory.mkdir(parents=True, exist_ok=True)
        env[key] = str(directory)
    return subprocess.call([str(arg) for arg in args], cwd=ROOT, env=env)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['setup', 'doctor', 'dashboard', 'notebook', 'execute'])
    args = parser.parse_args()
    if args.command == 'setup':
        if not PYTHON.exists():
            result = run(sys.executable, '-m', 'venv', ENV)
            if result:
                return result
        result = run(PYTHON, '-m', 'pip', 'install', '-r', APP / 'requirements-notebook.txt')
        if result:
            return result
        result = run(PYTHON, '-m', 'ipykernel', 'install', '--sys-prefix', '--name', 'walmart',
                     '--display-name', 'Python (Walmart)')
        if result:
            return result
        print('\nEnvironment and Jupyter kernel configured. Running dependency check...', flush=True)
        return run(PYTHON, ROOT / 'scripts/check_environment.py')
    if not PYTHON.exists():
        print('Project environment is missing. Run: python run_project.py setup', file=sys.stderr)
        return 1
    if args.command == 'doctor':
        return run(PYTHON, ROOT / 'scripts/check_environment.py')
    if args.command == 'dashboard':
        return run(PYTHON, '-m', 'streamlit', 'run', APP / 'streamlit_dashboard.py',
                   '--server.address', '127.0.0.1', '--server.headless', 'true')
    if args.command == 'notebook':
        return run(PYTHON, '-m', 'jupyterlab', NOTEBOOK, '--ServerApp.root_dir=' + str(ROOT),
                   '--ServerApp.ip=127.0.0.1', '--no-browser')
    if args.command == 'execute':
        return run(PYTHON, ROOT / 'scripts/execute_notebook.py')
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
