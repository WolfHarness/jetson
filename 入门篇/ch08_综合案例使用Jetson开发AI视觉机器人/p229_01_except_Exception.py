# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第8章 综合案例使用Jetson开发AI视觉机器人 · 印刷第229页 (PDF第239页)

        except Exception as e:
            print(f"初始化失败：{str(e)}")
            self.cleanup()
            sys.exit(1)
