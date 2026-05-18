# # #这段代码用于测试输出
# # #检测方式1，检测指定种类种类---------------------------------------------------
# from ultralytics import YOLO
# import cv2
#
# # 加载预训练模型（支持本地路径或官方模型名称）
# model = YOLO("visdrone.pt")  # 可选模型：yolo11n/s/m/l/x.pt
#
# # 读取测试图片
# image_path = "xxx\\0000002_00448_d_0000015.jpg"
# image = cv2.imread(image_path)
#
# # 执行推理（设置置信度阈值和类别过滤）
# results = model.predict(image, conf=0.5, classes=[0, 2, 5])  # 示例：仅检测人、车、公交车
#
# # 解析检测结果并绘制边框
# for result in results:
#     for box in result.boxes:
#         # 提取边框坐标和类别信息
#         x1, y1, x2, y2 = map(int, box.xyxy[0])
#         class_id = int(box.cls[0])
#         confidence = float(box.conf[0])
#         label = f"{model.names[class_id]} {confidence:.2f}"
#
#         # 绘制边框和标签
#         cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
#         cv2.putText(image, label, (x1, y1 - 10),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
#
# # 显示并保存结果
# cv2.imshow("Detection Result", image)
# cv2.waitKey(0)
# cv2.imwrite("result.jpg", image)
#


# #检测方式2，检测多个种类---------------------------------------------------
from ultralytics import YOLO

# 加载预训练模型
model = YOLO("visdrone.pt")  # 支持本地路径或官方模型名称
# 单张图片检测
#results = model.predict("./dataset/test.jpg", conf=0.5, save=True)

# 批量检测文件夹
# results = model.predict("C:/Users/ASUS/Desktop/检修库安全行为在线监测系统/实验数据/VisDrone2019/", save=True)


# #导入视频检测以及保存视频
from ultralytics import YOLO
import cv2

model = YOLO("visdrone.pt")
#model = YOLO("yolo11n.pt")
cap = cv2.VideoCapture("E:\视频\马赛克视频.mp4")
#cap = cv2.VideoCapture("playphone.mp4")
# 获取视频属性并初始化 VideoWriter
fps = cap.get(cv2.CAP_PROP_FPS)  # 获取原视频帧率
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 编解码器（支持 MP4/AVI）
output_path = "output.mp4"
video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret: break
    results = model.predict(frame, conf=0.5)
    annotated_frame = results[0].plot()  # 绘制检测框和标签
    cv2.imshow("YOLOv11 Video Detection", annotated_frame)
    video_writer.write(annotated_frame)  # 写入处理后的帧
    if cv2.waitKey(1) == 27: break

cap.release()
video_writer.release()  # 必须释放写入器资源
cv2.destroyAllWindows()

# 这段代码用于测试各个模型的准确率，输入一张图片输出画框后的图片


#
# # 检测图片并输出图片框总数，准确平均精度
# from ultralytics import YOLO
# import cv2
# import os
# import numpy as np
#
# # 加载模型
# model = YOLO("yolov11.pt")
#
# # 图片路径
# image_path = 'C:\\Users\\ASUS\\Desktop\\检修库安全行为在线监测系统\\小论文\\test_photo\\4423.jpg'
#
# # 检测单张图片
# results = model.predict(image_path, conf=0.5, save=True)
#
# # 在窗口中显示结果
# for r in results:
#     im_array = r.plot()  # 绘制检测结果的numpy数组
#
#     # 获取检测框信息
#     boxes = r.boxes
#     if boxes is not None and len(boxes) > 0:
#         # 统计信息
#         num_boxes = len(boxes)
#         confidences = boxes.conf.cpu().numpy()  # 获取所有置信度
#
#         # 计算统计指标
#         avg_confidence = np.mean(confidences)  # 平均置信度
#         max_confidence = np.max(confidences)  # 最大置信度
#         min_confidence = np.min(confidences)  # 最小置信度
#
#         # 按类别统计
#         class_names = model.names  # 获取类别名称
#         class_counts = {}
#         class_confidences = {}
#
#         for box in boxes:
#             cls = int(box.cls.item())  # 类别ID
#             conf = box.conf.item()  # 置信度
#
#             if cls not in class_counts:
#                 class_counts[cls] = 0
#                 class_confidences[cls] = []
#
#             class_counts[cls] += 1
#             class_confidences[cls].append(conf)
#
#         # 在图片上添加统计信息
#         text_y = 30
#         cv2.putText(im_array, f"Total Boxes: {num_boxes}", (10, text_y),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
#         text_y += 30
#         cv2.putText(im_array, f"Avg Confidence: {avg_confidence:.3f}", (10, text_y),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
#         text_y += 30
#         cv2.putText(im_array, f"Max Confidence: {max_confidence:.3f}", (10, text_y),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
#         text_y += 30
#         cv2.putText(im_array, f"Min Confidence: {min_confidence:.3f}", (10, text_y),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
#
#         # 添加类别统计信息
#         text_y += 40
#         cv2.putText(im_array, "Class Statistics:", (10, text_y),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
#
#         for cls, count in class_counts.items():
#             text_y += 30
#             cls_avg_conf = np.mean(class_confidences[cls])
#             cls_name = class_names[cls]
#             cv2.putText(im_array, f"{cls_name}: {count} boxes, avg: {cls_avg_conf:.3f}",
#                         (20, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
#
#         # 在控制台输出详细统计信息
#         print("=" * 50)
#         print("检测结果统计:")
#         print(f"总框数: {num_boxes}")
#         print(f"平均置信度: {avg_confidence:.4f}")
#         print(f"最大置信度: {max_confidence:.4f}")
#         print(f"最小置信度: {min_confidence:.4f}")
#         print(f"置信度标准差: {np.std(confidences):.4f}")
#         print("\n按类别统计:")
#
#         for cls, count in class_counts.items():
#             cls_avg_conf = np.mean(class_confidences[cls])
#             cls_name = class_names[cls]
#             print(f"  {cls_name}: {count}个检测框, 平均置信度: {cls_avg_conf:.4f}")
#
#         print("=" * 50)
#
#         # 打印每个检测框的详细信息
#         print("\n每个检测框的详细信息:")
#         for i, box in enumerate(boxes):
#             cls = int(box.cls.item())
#             conf = box.conf.item()
#             xyxy = box.xyxy[0].cpu().numpy()  # 边界框坐标 [x1, y1, x2, y2]
#             cls_name = class_names[cls]
#
#             print(
#                 f"  框 {i + 1}: {cls_name}, 置信度: {conf:.4f}, 坐标: [{xyxy[0]:.1f}, {xyxy[1]:.1f}, {xyxy[2]:.1f}, {xyxy[3]:.1f}]")
#
#     else:
#         # 没有检测到任何目标
#         cv2.putText(im_array, "No objects detected", (10, 30),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
#         print("未检测到任何目标")
#
#     # 显示图片
#     cv2.imshow("YOLO Detection Result with Statistics", im_array)
#     cv2.waitKey(0)  # 等待按键
#     cv2.destroyAllWindows()

#画8个图片比较图
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.font_manager as fm
# import os
# from datetime import datetime


# # 设置中文字体显示（多种方案确保兼容性）
# def setup_chinese_font():
#     """设置中文字体，确保中文正常显示"""
#     try:
#         # 方案1：使用系统常见中文字体
#         plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimSun', 'KaiTi']
#         # 解决负号显示问题
#         plt.rcParams['axes.unicode_minus'] = False
#         # 设置字体大小
#         plt.rcParams['font.size'] = 10

#         # 验证字体是否设置成功
#         if 'SimHei' in plt.rcParams['font.sans-serif']:
#             print("中文字体设置成功：使用黑体")
#         else:
#             # 方案2：如果系统字体不可用，尝试直接指定字体路径
#             try:
#                 # Windows系统常见字体路径
#                 font_path = 'C:/Windows/Fonts/simhei.ttf'  # 黑体
#                 font_prop = fm.FontProperties(fname=font_path)
#                 plt.rcParams['font.family'] = font_prop.get_name()
#                 print("中文字体设置成功：使用路径指定字体")
#             except:
#                 print("警告：中文字体设置可能失败，中文可能显示为方框")
#     except Exception as e:
#         print(f"字体设置过程中出现错误：{e}")


# # 调用字体设置函数
# setup_chinese_font()

# # 从粘贴数据创建DataFrame
# data = {
#     "Model": ["TSMY", "Yolov11"],
#     "图片1总框数": [12, 10], "图片1平均置信度": [0.6936, 0.7354],
#     "图片2总框数": [11, 10], "图片2平均置信度": [0.7095, 0.7011],
#     "图片3总框数": [14, 12], "图片3平均置信度": [0.7115, 0.6720],
#     "图片4总框数": [14, 12], "图片4平均置信度": [0.7405, 0.7045],
#     "图片5总框数": [13, 12], "图片5平均置信度": [0.7464, 0.7138],
#     "图片6总框数": [12, 11], "图片6平均置信度": [0.7327, 0.6957],
#     "图片7总框数": [13, 11], "图片7平均置信度": [0.7408, 0.6946],
#     "图片8总框数": [12, 11], "图片8平均置信度": [0.7440, 0.7314]
# }

# df = pd.DataFrame(data).set_index("Model")

# # 创建科学严谨的图表 - 调整尺寸以适应高分辨率
# plt.figure(figsize=(14, 10))

# # 设置颜色方案（更加科学严谨）
# colors = ['#2E86AB', '#A23B72']  # 蓝色和洋红色，色盲友好
# markers = ['o', 's']  # 圆形和方形标记

# # 1. 总框数对比图 (上方子图)
# plt.subplot(2, 1, 1)
# n_images = 8
# bar_width = 0.35
# x = np.arange(n_images)

# # 计算统计指标用于误差线
# TSMY_boxes = df[[f"图片{j + 1}总框数" for j in range(n_images)]].loc['TSMY']
# yolov11_boxes = df[[f"图片{j + 1}总框数" for j in range(n_images)]].loc['Yolov11']

# # 绘制分组柱状图
# for i, model in enumerate(df.index):
#     boxes = df[[f"图片{j + 1}总框数" for j in range(n_images)]].loc[model]
#     plt.bar(x + i * bar_width, boxes, width=bar_width,
#             label=model, alpha=0.8, edgecolor='black', color=colors[i])

#     # 添加数据标签
#     for j, val in enumerate(boxes):
#         plt.text(x[j] + i * bar_width, val + 0.1, str(val),
#                  ha='center', va='bottom', fontsize=9, fontweight='bold')

# # 图表装饰（使用中文标签）
# plt.ylabel('目标检测框数量', fontsize=12, fontweight='bold')
# plt.title('目标检测模型性能对比分析', fontsize=14, fontweight='bold')
# plt.xticks(x + bar_width / 2, [f'图片 {i + 1}' for i in range(n_images)], fontsize=10)
# plt.legend(title='检测模型', frameon=True, fancybox=True, shadow=True)
# plt.grid(axis='y', linestyle='--', alpha=0.3)
# plt.ylim(0, 16)
# plt.gca().spines['top'].set_visible(False)
# plt.gca().spines['right'].set_visible(False)

# # 2. 平均置信度对比图 (下方子图)
# plt.subplot(2, 1, 2)

# # 绘制折线图+点图
# for i, model in enumerate(df.index):
#     conf = df[[f"图片{j + 1}平均置信度" for j in range(n_images)]].loc[model]

#     # 计算统计指标
#     conf_mean = conf.mean()
#     conf_std = conf.std()

#     # 绘制均值线
#     plt.axhline(y=conf_mean, color=colors[i], linestyle='--', alpha=0.5,
#                 label=f'{model}均值: {conf_mean:.3f}')

#     # 绘制折线和数据点
#     plt.plot(x, conf, color=colors[i], marker=markers[i],
#              linewidth=2, markersize=6, label=model)

#     # 添加数据标签
#     for j, val in enumerate(conf):
#         plt.text(j, val + 0.008, f'{val:.3f}',
#                  ha='center', va='bottom', fontsize=8, fontweight='bold')

# # 图表装饰
# plt.ylabel('平均置信度', fontsize=12, fontweight='bold')
# plt.xlabel('测试图片编号', fontsize=12, fontweight='bold')
# plt.xticks(x, [f'图片 {i + 1}' for i in range(n_images)], fontsize=10)
# plt.legend(frameon=True, fancybox=True, shadow=True, ncol=2)
# plt.grid(True, linestyle='--', alpha=0.3)
# plt.ylim(0.65, 0.78)
# plt.gca().spines['top'].set_visible(False)
# plt.gca().spines['right'].set_visible(False)

# # 调整布局
# plt.tight_layout()

# # 获取当前工作目录
# current_dir = os.getcwd()
# print(f"图片将保存到当前目录: {current_dir}")

# # 保存高质量图片 - 修改为600dpi[6,7](@ref)
# output_filename = '目标检测模型性能科学对比_600dpi.png'
# output_path = os.path.join(current_dir, output_filename)

# plt.savefig(output_path, dpi=600, bbox_inches='tight',
#             facecolor='white', edgecolor='none',
#             metadata={'Title': '目标检测模型性能对比', 'Author': 'Python Matplotlib'})

# print(f"高分辨率图片已保存: {output_path}")
# print("图片参数: 600 DPI, PNG格式, 高质量输出")

# plt.show()