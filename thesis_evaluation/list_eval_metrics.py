import os
import json
import glob
import pandas as pd

def check_all_eval():
    lightly_eval = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\evaluation_results'
    metric_files = glob.glob(os.path.join(lightly_eval, '*TEST_coco_metrics.json'))
    
    records = []
    for mf in metric_files:
        bn = os.path.basename(mf)
        with open(mf) as fp:
            d = json.load(fp)
            mets = d.get('metrics', {})
            records.append({
                'filename': bn,
                'run_name': d.get('run_name', ''),
                'model_variant': d.get('model_variant', ''),
                'AP': mets.get('AP'),
                'AP50': mets.get('AP50'),
                'AP75': mets.get('AP75'),
                'AR_max100': mets.get('AR_max100')
            })
    df = pd.DataFrame(records)
    print("Found eval metrics:", len(df))
    print(df.to_string())

if __name__ == '__main__':
    check_all_eval()
