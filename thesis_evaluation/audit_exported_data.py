
import os, glob, json
import pandas as pd
import numpy as np

master_csv = r'thesis_evaluation/master_runs_database.csv'
df_master = pd.read_csv(master_csv)
lightly_eval = r'C:/Users/emilb/My Drive/Model_Exports/_trainer_lightly/evaluation_results'
dino_eval = r'C:/Users/emilb/Documents/GitHub/_trainer_DINOV3-YOLOV12/export/evaluation_results'

print(f'Master database shape: {df_master.shape}')

opt_f1_path = os.path.join(lightly_eval, 'optimal_f1_test_evaluation_summary.json')
with open(opt_f1_path, 'r', encoding='utf-8') as f:
    opt_data = json.load(f)

# Inspect model entries in optimal_f1_test_evaluation_summary.json
print('\n=== AUDITING OPTIMAL F1 TEST EVALUATION SUMMARY (40 models) ===')
opt_models = opt_data['all_models']
print(f'Total models in summary: {len(opt_models)}')

report_rows = []
for m in opt_models:
    name = m.get('model_name')
    fam = m.get('model_family')
    arch = m.get('architecture')
    seed = m.get('seed')
    opt_conf = m.get('optimal_confidence')
    tm = m.get('test_metrics', {})
    
    # Ground truth test metrics
    std_ap50 = tm.get('mAP_50_standard')
    std_ap = tm.get('mAP_50_95_standard')
    opt_f1 = tm.get('test_f1')
    opt_p = tm.get('test_precision')
    opt_r = tm.get('test_recall')
    
    report_rows.append({
        'name': name,
        'family': fam,
        'seed': seed,
        'std_ap50': std_ap50,
        'std_ap': std_ap,
        'opt_conf': opt_conf,
        'opt_f1': opt_f1,
        'opt_p': opt_p,
        'opt_r': opt_r
    })

df_opt = pd.DataFrame(report_rows)
print(df_opt.to_string())

# Cross-reference with master_runs_database.csv
print('\n=== CROSS-REFERENCING WITH MASTER_RUNS_DATABASE.CSV ===')
discrepancies = []
for idx, r in df_opt.iterrows():
    name = r['name']
    seed = r['seed']
    std_ap50 = r['std_ap50']
    
    # Try finding in master database
    # Check matching by canonical_model or run_name or variant
    matches = df_master[(df_master['seed'] == seed) & (
        (df_master['run_name'].str.contains(name, case=False, na=False)) |
        (df_master['model_variant'].str.contains(name, case=False, na=False)) |
        (df_master['canonical_model'].str.contains(name, case=False, na=False))
    )]
    
    if matches.empty:
        # Try finding by architecture family + seed
        pass
    else:
        m_row = matches.iloc[0]
        db_ap50 = m_row['test_coco_AP50']
        if pd.notna(std_ap50) and pd.notna(db_ap50):
            diff = abs(std_ap50 - db_ap50)
            if diff > 1e-3:
                discrepancies.append({
                    'name': name,
                    'seed': seed,
                    'exported_AP50': std_ap50,
                    'db_AP50': db_ap50,
                    'diff': diff,
                    'db_canonical': m_row['canonical_model'],
                    'db_run_name': m_row['run_name']
                })

print(f'Total potential discrepancies found: {len(discrepancies)}')
for d in discrepancies:
    print(d)
