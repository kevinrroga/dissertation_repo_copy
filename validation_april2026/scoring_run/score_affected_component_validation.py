import sys, os
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]  # repository root
sys.path.insert(0, str(ROOT / "scoring_for_affected_component"))
import score_affected_component as sac

sac.RESULTS_PATH = str(ROOT / "validation_april2026" / "merging_results_validation.json")
sac.OUT_DIR = str(ROOT / "validation_april2026" / "scoring_run" / "affected_component_outputs")
os.makedirs(sac.OUT_DIR, exist_ok=True)
sac.main()
