import os
import json
import glob

def check_baseline():
    base_sub = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\evaluation_results\baseline'
    eval_sum_json = os.path.join(base_sub, 'evaluation_summary.json')
    if os.path.exists(eval_sum_json):
        with open(eval_sum_json) as f:
            d = json.load(f)
            print("baseline evaluation_summary.json keys/len:", len(d) if isinstance(d, list) else list(d.keys()))
            if isinstance(d, list):
                for row in d[:10]:
                    print(" ", row)
            elif isinstance(d, dict):
                for k in list(d.keys())[:5]:
                    print(f"  {k}:", d[k])

    eval_sum_md = os.path.join(base_sub, 'evaluation_summary.md')
    if os.path.exists(eval_sum_md):
        with open(eval_sum_md) as f:
            lines = f.readlines()
            print("\nbaseline evaluation_summary.md first 30 lines:")
            for l in lines[:30]:
                print(l.strip())

if __name__ == '__main__':
    check_baseline()
