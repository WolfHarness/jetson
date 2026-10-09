# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第142-143页 (PDF第152页, PDF第153页)
# 上下文: 像直接展示出来。 ／ 为了更直观地对比正误图像分类结果，可以使用如下方法将正确分类和错误分类的图

# 可视化正确分类和错误分类的图像
def imshow(img, title):
    img = img / 2 + 0.5  # 反归一化
    npimg = img if isinstance(img, np.ndarray) else img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)).squeeze(), cmap='gray')  # 显示灰度图像
    plt.title(title)
    plt.axis('off')

# 正确分类的图像
fig, axes = plt.subplots(2, 5, figsize=(15, 6))  # 调整子图数量为2x5
for i in range(10):
    correct_indices = [idx for idx, (label, pred) in enumerate(zip(all_labels, all_preds)) if label == pred and label == i]
    if correct_indices:
        idx = correct_indices[0]
        ax = axes[i // 5, i % 5]
        plt.sca(ax)
        imshow(all_images[idx], f'True: {all_labels[idx]}, Pred: {all_preds[idx]}')
plt.tight_layout()
fig.suptitle('Correctly Classified Images', fontsize=16)
plt.subplots_adjust(top=0.88)
plt.savefig('correct_classified_images.png')  # 保存正确分类的图像集合
plt.show()

# 错误分类的图像
fig, axes = plt.subplots(2, 5, figsize=(15, 6))  # 调整子图数量为2x5
for i in range(10):
    incorrect_indices = [idx for idx, (label, pred) in enumerate(zip(all_labels, all_preds)) if label != pred and label == i]
    if incorrect_indices:
        idx = incorrect_indices[0]
        ax = axes[i // 5, i % 5]
        plt.sca(ax)
        imshow(all_images[idx], f'True: {all_labels[idx]}, Pred: {all_preds[idx]}')
plt.tight_layout()
fig.suptitle('Incorrectly Classified Images', fontsize=16)
plt.subplots_adjust(top=0.88)
plt.savefig('incorrect_classified_images.png') # 保存错误分类的图像集合
plt.show()
