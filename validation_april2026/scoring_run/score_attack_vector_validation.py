import sys
sys.path.insert(0, r"<PROJECT_ROOT>\scoring_for_attack_vector")
import score_attack_vector as sav

sav.REPORT_TXT = r"<PROJECT_ROOT>\validation_april2026\scoring_run\score_attack_vector_validation_report.txt"
sav.REPORT_JSON = r"<PROJECT_ROOT>\validation_april2026\scoring_run\score_attack_vector_validation_results.json"

sys.argv = ["score_attack_vector.py", r"<PROJECT_ROOT>\validation_april2026\merging_results_validation.json"]
sav.main()
