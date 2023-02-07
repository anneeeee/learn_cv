_base_ = ['../_base_/models/resnet18.py', '../_base_/datasets/imagenet_bs32.py','../_base_/default_runtime.py']

model = dict(
    head=dict(
        num_classes=5,
        topk=(1,)
    ))

data =dict(
    samples_per_gpu=32,
    workers_per_gpu=2,
    train = dict (
        data_prefix= '.opt/ml/code/flower_dataset_Image_Net_4_1/train',
        ann_file='.opt/ml/code/flower_dataset_Image_Net_4_1/train.txt',
        classes='.opt/ml/code/flower_dataset_Image_Net_4_1/class.txt'
    ),
    val=dict(
        data_prefix= '.opt/ml/code/flower_dataset_Image_Net_4_1/val',
        ann_file='.opt/ml/code/flower_dataset_Image_Net_4_1/val.txt',
        classes='.opt/ml/code/flower_dataset_Image_Net_4_1/class.txt'
    )
)

optimizer = dict(type='SGD', lr=0.001, momentum=0.9,weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)

lr_config = dict(
    policy='step',
    step=[1]
)

runner = dict (type = 'EpochBasedRunner', max_epochs=100)

load_from = './opt/ml/code/mmclassification/checkpoints/resnet18_batch256_imagenet_20200708-34ab8f90.pth'