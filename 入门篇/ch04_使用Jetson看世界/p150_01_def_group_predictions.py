# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第150页 (PDF第160页)
# 上下文: 下面根据预测结果和实际情况对图片进行分组处理。

# 根据预测结果和实际标签分组
def group_predictions(model, data_loader, class_names, num_samples):
    model.eval()
    correct_images = []
    incorrect_images = []
    correct_titles = []
    incorrect_titles = []
    correct_preds = []
    incorrect_preds = []

    with torch.no_grad():
        for images, labels in data_loader:
            images = images.to(device)
            labels = labels.to(device)
            outputs = model(images)
            _, preds = torch.max(outputs, 1)

            for i in range(images.size(0)):
                img = images[i].cpu()
                pred = class_names[preds[i].item()]
                actual = class_names[labels[i].item()]

                if pred == actual:
                    correct_images.append(img)
                    correct_titles.append(actual)
                    correct_preds.append(pred)
                else:
                    incorrect_images.append(img)
                    incorrect_titles.append(actual)
                    incorrect_preds.append(pred)

    # 随机抽样指定数量的正确和错误预测
    correct_images, correct_titles, correct_preds = get_random_samples(correct_images, correct_titles, correct_preds, num_samples)
    incorrect_images, incorrect_titles, incorrect_preds = get_random_samples(incorrect_images, incorrect_titles, incorrect_preds, num_samples)

    return correct_images, incorrect_images, correct_titles, incorrect_titles, correct_preds, incorrect_preds
