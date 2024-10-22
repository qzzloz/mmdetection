_base_ = './faster-rcnn_r50_fpn_1x_coco.py'

# Modify dataset related settings
data_root = '/data/ephemeral/home/minji/dataset/'
metainfo = {
    'classes': ("General trash", "Paper", "Paper pack", "Metal", "Glass", 
           "Plastic", "Styrofoam", "Plastic bag", "Battery", "Clothing")
}

train_dataloader = dict(
    batch_size=2,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='train.json',
        data_prefix=dict(img='./')))

val_dataloader = train_dataloader

test_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='test.json',
        test_mode=True,
        data_prefix=dict(img='./')))


val_evaluator = dict(ann_file=data_root + 'train.json')

test_evaluator = val_evaluator

train_pipeline = [
    dict(type='FilterAnnotations', min_gt_bbox_wh=(32, 32)),  # 크기 32x32 이하 필터링
]

work_dir = './work_dirs/faster-rcnn'

default_hooks = dict(
    visualization=dict(type='DetVisualizationHook', draw=True))

vis_backends = [dict(type='LocalVisBackend'),
                dict(type='TensorboardVisBackend')]
visualizer = dict(
    type='DetLocalVisualizer', vis_backends=vis_backends, name='visualizer')