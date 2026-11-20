import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]  # repository root
sys.path.insert(0, str(ROOT / "scoring_for_vuln_type"))
import score_pillar as sp

sp.RESULTS_FILE = Path(str(ROOT / "validation_april2026" / "merging_results_validation.json"))
sp.ALIASES_FILE = Path(str(ROOT / "scoring_for_vuln_type" / "cwe_aliases_v3_strict_reviewed.json"))
sp.VOCAB_FILE = Path(str(ROOT / "scoring_for_vuln_type" / "cwe_master_vocabulary_pillar_grouped.json"))
sp.DETAILS_OUTPUT = Path(str(ROOT / "validation_april2026" / "scoring_run" / "vulnerability_type_pillar_scored_details_validation.json"))
sp.SUMMARY_OUTPUT = Path(str(ROOT / "validation_april2026" / "scoring_run" / "vulnerability_type_pillar_summary_validation.json"))
sp.CSV_OUTPUT = Path(str(ROOT / "validation_april2026" / "scoring_run" / "vulnerability_type_pillar_summary_validation.csv"))
sp.main()
