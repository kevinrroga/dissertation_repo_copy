import sys, os
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]  # repository root
sys.path.insert(0, str(ROOT / "scoring_for_CIA"))
import cia_scorer as cia

cia.RESULTS_PATH = str(ROOT / "validation_april2026" / "merging_results_validation.json")
cia.OUT_DIR = str(ROOT / "validation_april2026" / "scoring_run" / "cia_outputs")
os.makedirs(cia.OUT_DIR, exist_ok=True)
cia.main()
