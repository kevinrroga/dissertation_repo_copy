import sys, os
sys.path.insert(0, r"<PROJECT_ROOT>\scoring_for_CIA")
import cia_scorer as cia

cia.RESULTS_PATH = r"<PROJECT_ROOT>\validation_april2026\merging_results_validation.json"
cia.OUT_DIR = r"<PROJECT_ROOT>\validation_april2026\scoring_run\cia_outputs"
os.makedirs(cia.OUT_DIR, exist_ok=True)
cia.main()
