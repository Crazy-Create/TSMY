import warnings

warnings.filterwarnings('ignore')
from ultralytics import YOLO
import torch  # 新增导入

import matplotlib
matplotlib.use('Agg')  # 使用非交互式后端
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 确保CUDA缓存清空
    torch.cuda.empty_cache()

    # 设置默认浮点精度
    torch.set_float32_matmul_precision('high')
    # Load a model
    #model = YOLO("last.pt")  # load a pretrained model (recommended for training)
    model = YOLO('yolo11-mambaV5.yaml')   #指定模型
    #model = YOLO('yolo11.yaml')  # 指定模型


    model.train(
        data=r"data.yaml",
        #data=r"coco.yaml",
        cache=False,
        imgsz=800,    # 640 改成 800
        epochs= 150,
        single_cls=False,
        batch =32,  # 减小的batch size
        close_mosaic=0,
        workers = 16,
        device='0,1',
        optimizer='SGD',
        amp=False,  # 关闭混合精度训练
        project='runs/train',
        name='exp',
        lr0=0.001,    #0.01
        resume=False,
        #fraction=0.1,  # 使用10%的数据进行测试
    )


