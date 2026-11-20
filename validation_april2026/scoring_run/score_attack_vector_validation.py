import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]  # repository root
sys.path.insert(0, str(ROOT / "scoring_for_attack_vector"))
import score_attack_vector as sav

sav.REPORT_TXT = str(ROOT / "validation_april2026" / "scoring_run" / "score_attack_vector_validation_report.txt")
sav.REPORT_JSON = str(ROOT / "validation_april2026" / "scoring_run" / "score_attack_vector_validation_results.json")

sys.argv = ["score_attack_vector.py", str(ROOT / "validation_april2026" / "merging_results_validation.json")]
sav.main()
