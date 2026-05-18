import os
import glob


def check_image_label_correspondence(image_dir, label_dir, image_ext='.jpg', label_ext='.txt'):
    """
    检查图片文件和标签文件的对应关系

    参数:
    image_dir: 图片文件目录
    label_dir: 标签文件目录
    image_ext: 图片文件扩展名
    label_ext: 标签文件扩展名

    返回:
    不匹配的文件列表和统计信息
    """
    # 获取所有图片文件和标签文件
    image_files = set([os.path.splitext(os.path.basename(f))[0]
                       for f in glob.glob(os.path.join(image_dir, f"*{image_ext}"))])
    label_files = set([os.path.splitext(os.path.basename(f))[0]
                       for f in glob.glob(os.path.join(label_dir, f"*{label_ext}"))])

    # 找出不匹配的文件
    images_without_labels = image_files - label_files
    labels_without_images = label_files - image_files
    matched_files = image_files & label_files

    # 打印结果
    print(f"图片目录: {image_dir}")
    print(f"标签目录: {label_dir}")
    print(f"图片文件总数: {len(image_files)}")
    print(f"标签文件总数: {len(label_files)}")
    print(f"匹配的文件对数量: {len(matched_files)}")
    print(f"缺少标签的图片数量: {len(images_without_labels)}")
    print(f"缺少图片的标签数量: {len(labels_without_images)}")

    # 显示部分不匹配的文件名（最多显示10个）
    if images_without_labels:
        print("\n缺少标签的图片文件示例:")
        for i, filename in enumerate(list(images_without_labels)[:10]):
            print(f"  {i + 1}. {filename}{image_ext}")
        if len(images_without_labels) > 10:
            print(f"  ... 还有 {len(images_without_labels) - 10} 个文件未显示")

    if labels_without_images:
        print("\n缺少图片的标签文件示例:")
        for i, filename in enumerate(list(labels_without_images)[:10]):
            print(f"  {i + 1}. {filename}{label_ext}")
        if len(labels_without_images) > 10:
            print(f"  ... 还有 {len(labels_without_images) - 10} 个文件未显示")

    # 返回结果
    return {
        'images_without_labels': list(images_without_labels),
        'labels_without_images': list(labels_without_images),
        'matched_files': list(matched_files)
    }


# 使用示例
if __name__ == "__main__":
    image_dir = r"E:\datasets\test\test2017"
    label_dir = r"E:\datasets\test\labels"

    result = check_image_label_correspondence(image_dir, label_dir)

    # 如果需要进一步处理结果，可以使用返回的字典
    # 例如：print(f"匹配的文件数量: {len(result['matched_files'])}")