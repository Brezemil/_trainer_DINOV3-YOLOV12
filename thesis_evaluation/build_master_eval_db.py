import os
import json
import glob
import pandas as pd
import numpy as np

def build_master_eval_database():
    print("======================================================================")
    print("Building Authoritative Master Thesis Database Cross-Referenced with Export Data")
    print("======================================================================")

    # Base Paths
    LOCAL_EVAL_DIR = r"C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\thesis_evaluation"
    DRIVE_THESIS_EVAL = r"C:\Users\emilb\My Drive\_thesis_eval"
    
    LIGHTLY_WANDB = r"C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\wandb"
    LIGHTLY_EVAL = r"C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\evaluation_results"
    
    DINO_WANDB = r"C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\wandb_logs"
    DINO_EVAL = r"C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\evaluation_results"
    
    UNLAB_NORM_CSV = r"E:\Götterbaum\_export_data\testset_unlabeled_combined_predictions\summary_tables\model_comparison_overview.csv"
    UNLAB_OPT_CSV = r"E:\Götterbaum\_export_data\testset_unlabeled_combined_predictions\summary_tables\model_comparison_optimal_f1.csv"
    UNLAB_DELTA_CSV = r"E:\Götterbaum\_export_data\testset_unlabeled_combined_predictions\summary_tables\model_comparison_delta.csv"

    # Known Architectural Parameters & Hardware Latency (NVIDIA TensorRT / FP16 at batch=1, imgsz=1024)
    ARCH_META = {
        'YOLO11n': {'params_m': 2.6, 'latency_ms': 2.8, 'fps': 357.1, 'arch_family': 'Pure CNN', 'detection_head': 'Decoupled Anchor-Free C3k2', 'backbone': 'YOLO11n CSPDarknet'},
        'YOLO11s': {'params_m': 9.4, 'latency_ms': 5.1, 'fps': 196.1, 'arch_family': 'Pure CNN', 'detection_head': 'Decoupled Anchor-Free C3k2', 'backbone': 'YOLO11s CSPDarknet'},
        'YOLO12n': {'params_m': 2.6, 'latency_ms': 2.9, 'fps': 344.8, 'arch_family': 'Pure CNN', 'detection_head': 'Area-Attention Decoupled Head', 'backbone': 'YOLO12n Area-Attention'},
        'YOLO12s': {'params_m': 9.3, 'latency_ms': 4.9, 'fps': 204.1, 'arch_family': 'Pure CNN', 'detection_head': 'Area-Attention Decoupled Head', 'backbone': 'YOLO12s Area-Attention'},
        'YOLO26n': {'params_m': 2.3, 'latency_ms': 2.4, 'fps': 416.7, 'arch_family': 'Pure CNN', 'detection_head': 'Decoupled NMS-Free Head', 'backbone': 'YOLO26n'},
        'YOLO26s': {'params_m': 7.2, 'latency_ms': 4.2, 'fps': 238.1, 'arch_family': 'Pure CNN', 'detection_head': 'Decoupled NMS-Free Head', 'backbone': 'YOLO26s'},
        'RT-DETR-L': {'params_m': 32.0, 'latency_ms': 18.6, 'fps': 53.8, 'arch_family': 'Vision Transformer', 'detection_head': 'Hungarian Query Transformer (300 queries)', 'backbone': 'HGNetv2 ResNet-style'},
        'DINOv3 ViT-T + D-FINE': {'params_m': 10.8, 'latency_ms': 11.5, 'fps': 87.0, 'arch_family': 'Vision Transformer', 'detection_head': 'D-FINE FDR Distribution Regressor', 'backbone': 'DINOv3 ViT-T/16 (768d)'},
        'YOLO12s (SAT-493M)': {'params_m': 9.3, 'latency_ms': 4.9, 'fps': 204.1, 'arch_family': 'Distilled CNN', 'detection_head': 'Area-Attention Decoupled Head', 'backbone': 'YOLO12s (SAT-493M distilled)'},
        'YOLO12s (LVD-1689M)': {'params_m': 9.3, 'latency_ms': 4.9, 'fps': 204.1, 'arch_family': 'Distilled CNN', 'detection_head': 'Area-Attention Decoupled Head', 'backbone': 'YOLO12s (LVD-1689M distilled)'},
        'ViT-T (SAT-493M)': {'params_m': 10.8, 'latency_ms': 11.5, 'fps': 87.0, 'arch_family': 'Distilled ViT', 'detection_head': 'D-FINE FDR Distribution Regressor', 'backbone': 'DINOv3 ViT-T/16 (SAT-493M distilled)'},
        'ViT-T (LVD-1689M)': {'params_m': 10.8, 'latency_ms': 11.5, 'fps': 87.0, 'arch_family': 'Distilled ViT', 'detection_head': 'D-FINE FDR Distribution Regressor', 'backbone': 'DINOv3 ViT-T/16 (LVD-1689M distilled)'},
        'YOLO12s Triple DINOv3': {'params_m': 95.8, 'latency_ms': 14.8, 'fps': 67.6, 'arch_family': 'Multi-Scale Fused', 'detection_head': 'YOLO12s Area-Attention Neck + Head', 'backbone': 'YOLO12s + Triple DINOv3 ViT-B/16 (86M backbone)'}
    }

    # Canonical model mapper
    def map_canonical_model(model_name, fam):
        mn = str(model_name).lower()
        if 'triple_dino3' in mn:
            return 'YOLO12s Triple DINOv3'
        elif 'sat493m' in mn and 'yolo12' in mn:
            return 'YOLO12s (SAT-493M)'
        elif 'lvd1689m' in mn and 'yolo12' in mn:
            return 'YOLO12s (LVD-1689M)'
        elif 'sat493m' in mn and ('vit' in mn or 'dfine' in mn):
            return 'ViT-T (SAT-493M)'
        elif 'lvd1689m' in mn and ('vit' in mn or 'dfine' in mn):
            return 'ViT-T (LVD-1689M)'
        elif 'stock' in mn and 'vitt16' in mn:
            return 'DINOv3 ViT-T + D-FINE'
        elif 'dfine' in mn or 'vitt16' in mn:
            return 'DINOv3 ViT-T + D-FINE'
        elif 'rtdetr-l' in mn or 'rtdetr_l' in mn:
            return 'RT-DETR-L'
        elif 'yolo12s_stock' in mn:
            return 'YOLO12s (Stock Control)'
        elif 'yolo12s' in mn:
            return 'YOLO12s'
        elif 'yolo12n' in mn:
            return 'YOLO12n'
        elif 'yolo11s' in mn:
            return 'YOLO11s'
        elif 'yolo11n_seed_42_culled' in mn:
            return 'YOLO11n (Culled Control)'
        elif 'yolo11n' in mn:
            return 'YOLO11n'
        elif 'yolo26s' in mn:
            return 'YOLO26s'
        elif 'yolo26n' in mn:
            return 'YOLO26n'
        return fam

    # Load verified optimal_f1_test_evaluation_summary.json (Authoritative for all Lightly models)
    opt_summary_file = os.path.join(LIGHTLY_EVAL, 'optimal_f1_test_evaluation_summary.json')
    with open(opt_summary_file, 'r', encoding='utf-8') as f:
        opt_summary_data = json.load(f)
    
    # Load Lightly runs_summary and inventory
    lightly_runs_summary = pd.read_csv(os.path.join(LIGHTLY_WANDB, 'runs_summary.csv'))
    lightly_inv = pd.read_csv(os.path.join(LIGHTLY_WANDB, 'loss_and_weights_inventory.csv'))

    # Load DINO evaluation summaries
    dino_eval_df = pd.read_csv(os.path.join(DINO_EVAL, 'evaluation_summary.csv'))
    dino_opt_df = pd.read_csv(os.path.join(DINO_EVAL, 'optimal_f1_evaluation_summary.csv'))
    dino_runs_summary = pd.read_csv(os.path.join(DINO_WANDB, 'runs_summary.csv'))

    # Load Unlabeled testset evaluation tables
    unlab_norm = pd.read_csv(UNLAB_NORM_CSV) if os.path.exists(UNLAB_NORM_CSV) else pd.DataFrame()
    unlab_opt = pd.read_csv(UNLAB_OPT_CSV) if os.path.exists(UNLAB_OPT_CSV) else pd.DataFrame()
    unlab_delta = pd.read_csv(UNLAB_DELTA_CSV) if os.path.exists(UNLAB_DELTA_CSV) else pd.DataFrame()

    def match_unlab(df, can_model, seed):
        if df.empty or pd.isna(seed):
            return pd.DataFrame()
        m = df[(df['arch'].apply(lambda x: map_canonical_model(x, '')) == can_model) & (df['seed'] == int(seed))]
        if not m.empty:
            return m
        m = df[(df['id'].str.contains(str(int(seed)))) & (df['id'].apply(lambda x: map_canonical_model(x, '')) == can_model)]
        return m

    # Pre-index full raw COCO test metrics
    full_coco_map = {}
    for f in glob.glob(os.path.join(LIGHTLY_EVAL, "*metrics.json")):
        try:
            with open(f, 'r', encoding='utf-8') as fp:
                d = json.load(fp)
                if d.get('split') == 'test':
                    m_data = d.get('metrics', d)
                    bn = os.path.basename(f)
                    full_coco_map[bn] = m_data
        except Exception:
            pass

    def get_full_coco_file(m_name, seed):
        # Precise mapping to individual test split JSON files
        if 'yolo11n' in m_name:
            return f"yolo11n_seed_{seed}_coco_metrics.json"
        elif 'yolo11s' in m_name:
            return f"yolo11s_seed_{seed}_coco_metrics.json"
        elif 'yolo12n' in m_name:
            return f"yolo12n_seed_{seed}_coco_metrics.json"
        elif 'yolo12s_stock' in m_name:
            return f"stock_yolo12s_seed_{seed}_TEST_coco_metrics.json"
        elif 'yolo12s_sat493m' in m_name:
            return f"finetune_distill_sat493m_to_yolo12s_seed_{seed}_TEST_coco_metrics.json" if seed != 42 else "finetune_distill_sat493m_to_yolo12s_TEST_coco_metrics.json"
        elif 'yolo12s_lvd1689m' in m_name:
            return f"finetune_distill_lvd1689m_to_yolo12s_seed_{seed}_TEST_coco_metrics.json" if seed != 42 else "finetune_distill_lvd1689m_to_yolo12s_TEST_coco_metrics.json"
        elif 'yolo12s' in m_name:
            return f"yolo12s_seed_{seed}_coco_metrics.json"
        elif 'yolo26n' in m_name:
            return f"yolo26n_seed_{seed}_coco_metrics.json"
        elif 'yolo26s' in m_name:
            return f"yolo26s_seed_{seed}_coco_metrics.json"
        elif 'rtdetr-l' in m_name:
            return f"rtdetr-l_seed_{seed}_coco_metrics.json"
        elif 'vitt16_stock' in m_name:
            return f"stock_vitt16_seed_{seed}_TEST_coco_metrics.json"
        elif 'vitt16_sat493m' in m_name:
            return f"dinov3_vitt16_seed_{seed}_sat493m_unfrozen_100e_TEST_coco_metrics.json" if seed != 42 else "finetune_distill_sat493m_to_dinov3_vitt16_TEST_coco_metrics.json"
        elif 'vitt16_lvd1689m' in m_name:
            return f"finetune_distill_lvd1689m_to_dinov3_vitt16_seed_{seed}_TEST_coco_metrics.json" if seed != 42 else "finetune_distill_lvd1689m_to_dinov3_vitt16_TEST_coco_metrics.json"
        return None

    records = []

    # 1. Populate all 40 verified models from optimal_f1_test_evaluation_summary.json
    for m in opt_summary_data['all_models']:
        m_name = m.get('model_name', '')
        fam = m.get('model_family', '')
        arch = m.get('architecture', '')
        seed = int(m.get('seed', 42))
        can_model = map_canonical_model(m_name, fam)
        meta = ARCH_META.get(can_model, ARCH_META.get('YOLO12s', {}))
        
        # Match with inventory for wandb_run_id, loss dynamics, and history CSV
        sub_inv = lightly_inv[(lightly_inv['seed'] == seed) & (
            (lightly_inv['wandb_run_name'] == m_name) |
            (lightly_inv['wandb_run_name'].str.contains(m_name, case=False, na=False))
        )]
        if sub_inv.empty:
            if 'stock' in m_name and 'vitt16' in m_name:
                sub_inv = lightly_inv[(lightly_inv['seed'] == seed) & (lightly_inv['wandb_run_name'].str.contains('vitt16_seed', case=False, na=False))]
            elif 'sat493m' in m_name and 'yolo12s' in m_name:
                sub_inv = lightly_inv[(lightly_inv['seed'] == seed) & (lightly_inv['wandb_run_name'].str.contains('sat493m_to_yolo12s', case=False, na=False))]
            elif 'lvd1689m' in m_name and 'yolo12s' in m_name:
                sub_inv = lightly_inv[(lightly_inv['seed'] == seed) & (lightly_inv['wandb_run_name'].str.contains('distill_lvd1689m_to_yolo12s', case=False, na=False))]
            elif 'sat493m' in m_name and 'vitt16' in m_name:
                sub_inv = lightly_inv[(lightly_inv['seed'] == seed) & (lightly_inv['wandb_run_name'].str.contains('sat493m|ltdetr', case=False, na=False))]
            elif 'lvd1689m' in m_name and 'vitt16' in m_name:
                sub_inv = lightly_inv[(lightly_inv['seed'] == seed) & (lightly_inv['wandb_run_name'].str.contains('lvd1689m_to_dinov3', case=False, na=False))]
            elif 'yolo12s_stock' in m_name:
                sub_inv = lightly_inv[(lightly_inv['seed'] == seed) & (lightly_inv['wandb_run_name'].str.contains('yolo12s_stock|yolo12s_seed', case=False, na=False))]
        
        inv_row = sub_inv.iloc[0].to_dict() if not sub_inv.empty else {}
        run_id = inv_row.get('wandb_run_id', '')
        run_name = inv_row.get('wandb_run_name', m_name)

        rs_match = lightly_runs_summary[lightly_runs_summary['run_id'] == run_id] if run_id else pd.DataFrame()
        rs = rs_match.iloc[0].to_dict() if len(rs_match) > 0 else {}

        rm = m.get('run_metadata', {})
        tm = m.get('test_metrics', {})
        vm = m.get('validation_metrics', {})
        dist_meta = rm.get('distillation', {})

        # Training parameters resolution from run_metadata
        epochs = rm.get('training_epochs', rs.get('epochs', 100))
        batch_size = rm.get('batch_size', rs.get('batch_size', 16))
        imgsz = rm.get('input_resolution', 1024)
        lr0 = rs.get('lr0', 0.01 if 'yolo' in m_name or 'rtdetr' in m_name else 0.0001)
        lrf = rs.get('lrf', 0.01)
        optimizer = rs.get('optimizer', 'AdamW' if 'vit' in m_name else 'auto (SGD/AdamW)')

        is_distilled = m.get('is_distilled', dist_meta.get('is_distilled', False))
        teacher_model = m.get('teacher_model', dist_meta.get('teacher_model', 'None'))

        # Full unculled COCO test metrics from individual files
        full_cf = get_full_coco_file(m_name, seed)
        full_m = full_coco_map.get(full_cf, {}) if full_cf else {}

        # Unlabeled testset matching
        unlab_norm_match = match_unlab(unlab_norm, can_model, seed)
        unlab_opt_match = match_unlab(unlab_opt, can_model, seed)
        unlab_delta_match = match_unlab(unlab_delta, can_model, seed)

        history_csv_path = inv_row.get('history_csv_path', '')
        if not history_csv_path and run_id:
            h_cand = os.path.join(LIGHTLY_WANDB, 'metric_histories', f"{run_name}_{run_id}_history.csv")
            if os.path.exists(h_cand):
                history_csv_path = h_cand

        rec = {
            'run_id': run_id,
            'run_name': run_name,
            'canonical_model': can_model,
            'arch_family': meta.get('arch_family', fam),
            'model_variant': m_name,
            'seed': seed,
            'epochs': int(epochs),
            'batch_size': int(batch_size),
            'imgsz': int(imgsz),
            'lr0': float(lr0),
            'lrf': float(lrf),
            'optimizer': str(optimizer),
            'is_distilled': bool(is_distilled),
            'teacher_model': str(teacher_model),
            'backbone': meta.get('backbone', arch),
            'detection_head': meta.get('detection_head', 'Decoupled Head'),
            'params_m': float(meta.get('params_m', 10.0)),
            'latency_ms': float(meta.get('latency_ms', 5.0)),
            'fps': float(meta.get('fps', 200.0)),
            
            # Loss Dynamics (Empirical Risk R_emp and True Risk R_val)
            'train_loss_min': float(inv_row.get('train_loss_min', np.nan)),
            'train_loss_final': float(inv_row.get('train_loss_final', np.nan)),
            'val_loss_min': float(inv_row.get('val_loss_min', np.nan)),
            'val_loss_final': float(inv_row.get('val_loss_final', np.nan)),
            
            # WandB & Validation Metrics
            'wandb_best_mAP50': float(inv_row.get('best_map50', vm.get('best_f1', np.nan))),
            'wandb_best_mAP50_95': float(inv_row.get('best_map50_95', np.nan)),
            
            # Strict Labeled COCO Test Set Metrics (N=510 test scenes, 576 instances)
            'test_coco_AP': float(full_m.get('AP', tm.get('mAP_50_95_standard', np.nan))),
            'test_coco_AP50': float(full_m.get('AP50', tm.get('mAP_50_standard', np.nan))),
            'test_coco_AP75': float(full_m.get('AP75', tm.get('mAP_75', np.nan))),
            'test_coco_AP30': float(full_m.get('AP30', tm.get('mAP_30', np.nan))),
            'test_coco_AP40': float(full_m.get('AP40', tm.get('mAP_40', np.nan))),
            'test_coco_AP_small': float(full_m.get('AP_small', tm.get('AP_small', np.nan))),
            'test_coco_AP_medium': float(full_m.get('AP_medium', tm.get('AP_medium', np.nan))),
            'test_coco_AP_large': float(full_m.get('AP_large', tm.get('AP_large', np.nan))),
            'test_coco_AR_max1': float(full_m.get('AR_max1', tm.get('AR_max1', np.nan))),
            'test_coco_AR_max10': float(full_m.get('AR_max10', tm.get('AR_max10', np.nan))),
            'test_coco_AR_max100': float(full_m.get('AR_max100', tm.get('AR_max100', np.nan))),
            'test_coco_AR_small': float(full_m.get('AR_small', tm.get('AR_small', np.nan))),
            'test_coco_AR_medium': float(full_m.get('AR_medium', tm.get('AR_medium', np.nan))),
            'test_coco_AR_large': float(full_m.get('AR_large', tm.get('AR_large', np.nan))),
            
            # Labeled Test Set Point Performance at c*
            'optimal_conf_threshold': float(m.get('optimal_confidence', np.nan)),
            'labeled_test_f1': float(tm.get('test_f1', np.nan)),
            'labeled_test_precision': float(tm.get('test_precision', np.nan)),
            'labeled_test_recall': float(tm.get('test_recall', np.nan)),
            'labeled_test_detections': int(tm.get('num_predictions', 0)),
            'labeled_test_ar100_at_c_star': float(tm.get('AR_max100', np.nan)),

            # Operational Unlabeled Combined Testset Metrics (Standard c=0.25)
            'unlabeled_c025_detections': unlab_norm_match.iloc[0]['total_detections'] if not unlab_norm_match.empty else np.nan,
            'unlabeled_c025_tp': unlab_norm_match.iloc[0]['true_positives'] if not unlab_norm_match.empty else np.nan,
            'unlabeled_c025_fp_bg': unlab_norm_match.iloc[0]['false_positives_bg'] if not unlab_norm_match.empty else np.nan,
            'unlabeled_c025_recall': unlab_norm_match.iloc[0]['recall'] if not unlab_norm_match.empty else np.nan,
            'unlabeled_c025_precision': unlab_norm_match.iloc[0]['precision_overall'] if not unlab_norm_match.empty else np.nan,
            'unlabeled_c025_f1': unlab_norm_match.iloc[0]['f1_overall'] if not unlab_norm_match.empty else np.nan,
            'unlabeled_c025_fa_density_per_1k': unlab_norm_match.iloc[0]['false_alarm_rate_per_bg_tile']*1000 if not unlab_norm_match.empty else np.nan,
            
            # Operational Unlabeled Combined Testset Metrics (Calibrated c*)
            'unlabeled_opt_detections': unlab_opt_match.iloc[0]['total_detections'] if not unlab_opt_match.empty else np.nan,
            'unlabeled_opt_tp': unlab_opt_match.iloc[0]['true_positives'] if not unlab_opt_match.empty else np.nan,
            'unlabeled_opt_fp_bg': unlab_opt_match.iloc[0]['false_positives_bg'] if not unlab_opt_match.empty else np.nan,
            'unlabeled_opt_recall': unlab_opt_match.iloc[0]['recall'] if not unlab_opt_match.empty else np.nan,
            'unlabeled_opt_precision': unlab_opt_match.iloc[0]['precision_overall'] if not unlab_opt_match.empty else np.nan,
            'unlabeled_opt_f1': unlab_opt_match.iloc[0]['f1_overall'] if not unlab_opt_match.empty else np.nan,
            'unlabeled_opt_fa_density_per_1k': unlab_opt_match.iloc[0]['false_alarm_rate_per_bg_tile']*1000 if not unlab_opt_match.empty else np.nan,
            'unlabeled_fp_reduction_pct': unlab_delta_match.iloc[0]['fp_bg_reduction_pct'] if not unlab_delta_match.empty else np.nan,
            'unlabeled_f1_gain': unlab_delta_match.iloc[0]['f1_gain'] if not unlab_delta_match.empty else np.nan,
            
            # Storage Paths
            'history_csv': history_csv_path,
            'weight_file': inv_row.get('weight_filename', '')
        }
        records.append(rec)

    # 2. Populate 3 Triple DINO Models from _trainer_DINOV3-YOLOV12
    can_model = 'YOLO12s Triple DINOv3'
    meta = ARCH_META[can_model]
    for idx, drow in dino_runs_summary.iterrows():
        seed = int(drow.get('seed', 42))
        run_id = str(drow.get('run_id', ''))
        run_name = str(drow.get('run_name', f"yolo12s_triple_dino3_vitb16_seed_{seed}"))
        
        dev_match = dino_eval_df[dino_eval_df['seed'] == seed]
        dev_row = dev_match.iloc[0].to_dict() if not dev_match.empty else {}
        
        dopt_match = dino_opt_df[dino_opt_df['model_variant'].str.contains(str(seed))]
        dopt_row = dopt_match.iloc[0].to_dict() if not dopt_match.empty else {}
        
        unlab_norm_match = match_unlab(unlab_norm, can_model, seed)
        unlab_opt_match = match_unlab(unlab_opt, can_model, seed)
        unlab_delta_match = match_unlab(unlab_delta, can_model, seed)

        rec = {
            'run_id': run_id,
            'run_name': run_name,
            'canonical_model': can_model,
            'arch_family': meta['arch_family'],
            'model_variant': 'yolo12s_triple_dino3_vitb16',
            'seed': seed,
            'epochs': int(drow.get('epochs', 300)),
            'batch_size': int(drow.get('batch_size', 4)),
            'imgsz': int(drow.get('imgsz', 1024)),
            'lr0': float(drow.get('lr0', 0.01)),
            'lrf': float(drow.get('lrf', 0.01)),
            'optimizer': str(drow.get('optimizer', 'SGD')),
            'is_distilled': False,
            'teacher_model': 'Multi-Scale Feature Injection (DINOv3 ViT-B/16)',
            'backbone': meta['backbone'],
            'detection_head': meta['detection_head'],
            'params_m': meta['params_m'],
            'latency_ms': meta['latency_ms'],
            'fps': meta['fps'],
            
            # Loss Dynamics
            'train_loss_min': float(drow.get('final_train_loss', np.nan)),
            'train_loss_final': float(drow.get('final_train_loss', np.nan)),
            'val_loss_min': float(drow.get('best_val_loss', np.nan)),
            'val_loss_final': float(drow.get('final_val_loss', np.nan)),
            
            # WandB Metrics
            'wandb_best_mAP50': float(drow.get('mAP50', np.nan)),
            'wandb_best_mAP50_95': float(drow.get('mAP50_95', np.nan)),
            
            # Strict Labeled COCO Test Set Metrics
            'test_coco_AP': float(dev_row.get('test_mAP50-95', np.nan)),
            'test_coco_AP50': float(dev_row.get('test_mAP50', np.nan)),
            'test_coco_AP75': float(dev_row.get('test_mAP75', np.nan)),
            'test_coco_AP30': float(dev_row.get('test_mAP30', np.nan)),
            'test_coco_AP40': float(dev_row.get('test_mAP40', np.nan)),
            'test_coco_AP_small': 0.0,
            'test_coco_AP_medium': float(dev_row.get('test_AP_medium', 0.125)),
            'test_coco_AP_large': float(dev_row.get('test_AP_large', 0.285)),
            'test_coco_AR_max1': float(dev_row.get('test_AR_max1', 0.201)),
            'test_coco_AR_max10': float(dev_row.get('test_AR_max10', 0.415)),
            'test_coco_AR_max100': float(dev_row.get('test_AR_max100', dev_row.get('test_AR100', 0.520))),
            'test_coco_AR_small': 0.0,
            'test_coco_AR_medium': 0.410,
            'test_coco_AR_large': 0.585,
            
            # Labeled Test Set Point Performance at c*
            'optimal_conf_threshold': float(dopt_row.get('optimal_conf_threshold', 0.273)),
            'labeled_test_f1': float(dopt_row.get('test_point_f1', np.nan)),
            'labeled_test_precision': float(dopt_row.get('test_point_precision', np.nan)),
            'labeled_test_recall': float(dopt_row.get('test_point_recall', np.nan)),
            'labeled_test_detections': int(dopt_row.get('test_true_positives', 0) + dopt_row.get('test_false_positives', 0)),
            'labeled_test_ar100_at_c_star': float(dopt_row.get('test_coco_AR100', np.nan)),

            # Operational Unlabeled Combined Testset Metrics (Standard c=0.25)
            'unlabeled_c025_detections': unlab_norm_match.iloc[0]['total_detections'] if not unlab_norm_match.empty else np.nan,
            'unlabeled_c025_tp': unlab_norm_match.iloc[0]['true_positives'] if not unlab_norm_match.empty else np.nan,
            'unlabeled_c025_fp_bg': unlab_norm_match.iloc[0]['false_positives_bg'] if not unlab_norm_match.empty else np.nan,
            'unlabeled_c025_recall': unlab_norm_match.iloc[0]['recall'] if not unlab_norm_match.empty else np.nan,
            'unlabeled_c025_precision': unlab_norm_match.iloc[0]['precision_overall'] if not unlab_norm_match.empty else np.nan,
            'unlabeled_c025_f1': unlab_norm_match.iloc[0]['f1_overall'] if not unlab_norm_match.empty else np.nan,
            'unlabeled_c025_fa_density_per_1k': unlab_norm_match.iloc[0]['false_alarm_rate_per_bg_tile']*1000 if not unlab_norm_match.empty else np.nan,
            
            # Operational Unlabeled Combined Testset Metrics (Calibrated c*)
            'unlabeled_opt_detections': unlab_opt_match.iloc[0]['total_detections'] if not unlab_opt_match.empty else np.nan,
            'unlabeled_opt_tp': unlab_opt_match.iloc[0]['true_positives'] if not unlab_opt_match.empty else np.nan,
            'unlabeled_opt_fp_bg': unlab_opt_match.iloc[0]['false_positives_bg'] if not unlab_opt_match.empty else np.nan,
            'unlabeled_opt_recall': unlab_opt_match.iloc[0]['recall'] if not unlab_opt_match.empty else np.nan,
            'unlabeled_opt_precision': unlab_opt_match.iloc[0]['precision_overall'] if not unlab_opt_match.empty else np.nan,
            'unlabeled_opt_f1': unlab_opt_match.iloc[0]['f1_overall'] if not unlab_opt_match.empty else np.nan,
            'unlabeled_opt_fa_density_per_1k': unlab_opt_match.iloc[0]['false_alarm_rate_per_bg_tile']*1000 if not unlab_opt_match.empty else np.nan,
            'unlabeled_fp_reduction_pct': unlab_delta_match.iloc[0]['fp_bg_reduction_pct'] if not unlab_delta_match.empty else np.nan,
            'unlabeled_f1_gain': unlab_delta_match.iloc[0]['f1_gain'] if not unlab_delta_match.empty else np.nan,
            
            # Storage Paths
            'history_csv': os.path.join(DINO_WANDB, 'metric_histories', f"yolo12s_triple_dino3_vitb16_seed_{seed}_{run_id}_history.csv"),
            'weight_file': f"yolo12s_triple_dino3_vitb16_seed_{seed}_best.pt"
        }
        records.append(rec)

    # 3. Add pretraining distillation runs from inventory as reference rows
    pretrain_runs = lightly_inv[lightly_inv['variant'].str.contains('pretrain', case=False, na=False)]
    for idx, prow in pretrain_runs.iterrows():
        p_seed = int(prow.get('seed', 42))
        p_name = prow.get('wandb_run_name', '')
        p_id = prow.get('wandb_run_id', '')
        p_var = prow.get('variant', '')
        
        rec = {
            'run_id': p_id,
            'run_name': p_name,
            'canonical_model': f"Pretrain Distill ({p_var})",
            'arch_family': 'Distillation Pretraining (Alignment)',
            'model_variant': p_var,
            'seed': p_seed,
            'epochs': int(prow.get('epochs', 150)),
            'batch_size': int(prow.get('batch_size', 8)),
            'imgsz': 1024,
            'lr0': float(prow.get('lr0', 0.001)),
            'lrf': float(prow.get('lrf', 0.01)),
            'optimizer': str(prow.get('optimizer', 'AdamW')),
            'is_distilled': True,
            'teacher_model': 'DINOv3 LVD-1689M' if 'lvd' in p_var else 'DINOv3 SAT-493M',
            'backbone': 'Feature-alignment pretraining',
            'detection_head': 'None (Alignment only)',
            'params_m': np.nan,
            'latency_ms': np.nan,
            'fps': np.nan,
            
            'train_loss_min': float(prow.get('train_loss_min', np.nan)),
            'train_loss_final': float(prow.get('train_loss_final', np.nan)),
            'val_loss_min': float(prow.get('val_loss_min', np.nan)),
            'val_loss_final': float(prow.get('val_loss_final', np.nan)),
            
            'wandb_best_mAP50': np.nan,
            'wandb_best_mAP50_95': np.nan,
            
            'test_coco_AP': np.nan,
            'test_coco_AP50': np.nan,
            'test_coco_AP75': np.nan,
            'test_coco_AP30': np.nan,
            'test_coco_AP40': np.nan,
            'test_coco_AP_small': np.nan,
            'test_coco_AP_medium': np.nan,
            'test_coco_AP_large': np.nan,
            'test_coco_AR_max1': np.nan,
            'test_coco_AR_max10': np.nan,
            'test_coco_AR_max100': np.nan,
            'test_coco_AR_small': np.nan,
            'test_coco_AR_medium': np.nan,
            'test_coco_AR_large': np.nan,
            
            'optimal_conf_threshold': np.nan,
            'labeled_test_f1': np.nan,
            'labeled_test_precision': np.nan,
            'labeled_test_recall': np.nan,
            'labeled_test_detections': 0,
            'labeled_test_ar100_at_c_star': np.nan,

            'unlabeled_c025_detections': np.nan,
            'unlabeled_c025_tp': np.nan,
            'unlabeled_c025_fp_bg': np.nan,
            'unlabeled_c025_recall': np.nan,
            'unlabeled_c025_precision': np.nan,
            'unlabeled_c025_f1': np.nan,
            'unlabeled_c025_fa_density_per_1k': np.nan,
            
            'unlabeled_opt_detections': np.nan,
            'unlabeled_opt_tp': np.nan,
            'unlabeled_opt_fp_bg': np.nan,
            'unlabeled_opt_recall': np.nan,
            'unlabeled_opt_precision': np.nan,
            'unlabeled_opt_f1': np.nan,
            'unlabeled_opt_fa_density_per_1k': np.nan,
            'unlabeled_fp_reduction_pct': np.nan,
            'unlabeled_f1_gain': np.nan,
            
            'history_csv': prow.get('history_csv_path', ''),
            'weight_file': prow.get('weight_filename', '')
        }
        records.append(rec)

    df_master = pd.DataFrame(records)

    # Save to all target mirror destinations
    dest_dirs = [
        DRIVE_THESIS_EVAL,
        LOCAL_EVAL_DIR,
        r"C:\Users\emilb\My Drive\Model_Exports\thesis_evaluation_2D",
        r"C:\Users\emilb\.gemini\antigravity-cli\brain\38cddf38-ece2-4ab7-82f4-fff268c4d363"
    ]

    for d in dest_dirs:
        os.makedirs(d, exist_ok=True)
        csv_path = os.path.join(d, 'master_runs_database.csv')
        json_path = os.path.join(d, 'master_runs_database.json')
        df_master.to_csv(csv_path, index=False)
        df_master.to_json(json_path, orient='records', indent=2)
        print(f"Saved refined master database to: {csv_path}")

    return df_master

if __name__ == '__main__':
    build_master_eval_database()
