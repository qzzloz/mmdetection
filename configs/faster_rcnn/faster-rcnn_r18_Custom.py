# from mmengine import read_base
# from mmdet.datasets.coco_custom_dataset import CustomCocoDataset

_base_ = './faster-rcnn_r18_fpn_8xb8-amp-lsj-200e_coco.py'
data_root = '/data/ephemeral/home/minji/dataset/'

# with read_base():
#     _base_ = './faster-rcnn_r18_fpn_8xb8-amp-lsj-200e_coco.py'

model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=10)))

# # Modify dataset related settings
# metainfo = {
#     'classes': ("General trash", "Paper", "Paper pack", "Metal", "Glass", 
#            "Plastic", "Styrofoam", "Plastic bag", "Battery", "Clothing")
# }


# train_dataloader = dict(
#     batch_size=2,
#     dataset=dict(
#         type='RepeatDataset',
#         data_root=data_root,
#         metainfo=metainfo,
#         ann_file='train.json',
#         data_prefix=dict(img='./'),
#         filter_annotations=dict(min_bbox_size=32)))

# val_dataloader = train_dataloader

# test_dataloader = dict(
#     dataset=dict(
#         data_root=data_root,
#         metainfo=metainfo,
#         ann_file='test.json',
#         test_mode=True,
#         data_prefix=dict(img='./')))


# val_evaluator = dict(ann_file=data_root + 'train.json')

# test_evaluator = val_evaluator

work_dir = './work_dirs/faster-rcnn'

default_hooks = dict(
    visualization=dict(type='DetVisualizationHook', draw=True))

vis_backends = [dict(type='LocalVisBackend'),
                dict(type='TensorboardVisBackend')]
visualizer = dict(
    type='DetLocalVisualizer', vis_backends=vis_backends, name='visualizer')