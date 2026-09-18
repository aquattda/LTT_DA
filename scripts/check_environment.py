"""Validate the notebook/dashboard interpreter and a real small ML fit."""
import sys
import traceback

print('Interpreter:', sys.executable, flush=True)
try:
    import numpy as np
    import pandas as pd
    import scipy.stats
    import sklearn
    import ipykernel
    import jupyterlab
    from sklearn.ensemble import GradientBoostingRegressor
    from jupyter_client.kernelspec import KernelSpecManager

    model = GradientBoostingRegressor(n_estimators=2, max_depth=2, random_state=42)
    model.fit(np.arange(20).reshape(-1, 1), np.arange(20))
    assert np.isfinite(model.predict([[5]])[0])
    kernel = KernelSpecManager().get_kernel_spec('walmart')
    print('Kernel:', kernel.argv[0])
    print('pandas:', pd.__version__, 'numpy:', np.__version__, 'sklearn:', sklearn.__version__)
    print('PASS: Jupyter dependencies, named kernel and real estimator fit/predict')
except Exception:
    traceback.print_exc()
    print('\nDependency check failed. If Windows Application Control blocked a DLL, the device policy must allow the official Python package before ML can run. This script does not change security policy.', file=sys.stderr)
    raise SystemExit(1)
