# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第141页 (PDF第151页)
# 上下文: 执行以下代码，评估模型性能。 ／ 说明模型在测试集上表现非常好，具有较强的分类能力。

# 性能分析
classification_rep = classification_report(all_labels, all_preds, target_names=[str(i) for i in range(10)])
print(classification_rep)
with open("classification_report.txt","w") as report_file:
report_file.write(classification_rep)
