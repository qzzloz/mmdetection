from mmdet.datasets import CocoDataset

class CustomCocoDataset(CocoDataset):
    def __init__(self, min_bbox_size=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_bbox_size = min_bbox_size

    def filter_annotations(self):
        """Filter annotations based on the minimum bounding box size."""
        valid_indices = []
        for idx, bbox in enumerate(self.ann_info['bboxes']):
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
            if width > self.min_bbox_size and height > self.min_bbox_size:
                valid_indices.append(idx)
        
        # Keep only valid annotations
        self.ann_info['bboxes'] = self.ann_info['bboxes'][valid_indices]
        self.ann_info['labels'] = self.ann_info['labels'][valid_indices]
