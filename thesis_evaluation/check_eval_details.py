import os
import json
import glob
import pandas as pd

def check_eval():
    lightly_eval = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\evaluation_results'
    bench_file = os.path.join(lightly_eval, 'benchmark_statistical_report.json')
    with open(bench_file) as f:
        bench = json.load(f)
    print("=== Benchmark statistical report summary table ===")
    for row in bench.get('summary_table', []):
        print(f"{row.get('family'):18} | {row.get('variant'):22} | params={row.get('params_m'):4.1f}M | mAP50={row.get('mean_mAP50'):.4f}±{row.get('std_mAP50'):.4f} | mAP={row.get('mean_mAP'):.4f} | latency={row.get('latency_ms')}ms")

    # Now check individual metric files for distillation models
    print("\n=== Individual TEST_coco_metrics.json sample ===")
    files = sorted(glob.glob(os.path.join(lightly_eval, '*TEST_coco_metrics.json')))
    results = []
    for f in files:
        b = os.path.basename(f)
        try:
            with open(f) as fp:
                data = json.load(fp)
                # Some files have 'mAP50' or 'mAP_50' or 'coco_metrics'
                results.append({'file': b, 'keys': list(data.keys())[:8], 'data': {k: data[k] for k in list(data.keys())[:5]}})
        except Exception as e:
            results.append({'file': b, 'error': str(e)})

    for r in results[:10]:
        print(r['file'], "->", r.get('data') if 'data' in r else r.get('error'))

if __name__ == '__main__':
    check_eval()
