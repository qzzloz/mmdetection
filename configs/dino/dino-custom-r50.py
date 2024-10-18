_base_ = 'dino-4scale_r50_8xb2-12e_coco.py'

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

work_dir = './work_dirs/dino'

default_hooks = dict(
    visualization=dict(type='DetVisualizationHook', draw=True))

vis_backends = [dict(type='LocalVisBackend'),
                dict(type='TensorboardVisBackend')]
visualizer = dict(
    type='DetLocalVisualizer', vis_backends=vis_backends, name='visualizer')