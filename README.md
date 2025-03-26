# QwQ-32B_Math_Solver

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

这是一个 Python 脚本项目，可以通过调用多种 AI API 来批量识别和解答图片中的数学题，并将结果保存为 Markdown 文件。

作者在学习大学数学的时候，经常遇到空有答案而无过程的习题，一道一道搜题效率低下且很多题目没有答案源。一次常微分课程上，老师说不能给我们答案，我心里郁闷，不给的话就自己弄一份，于是自己探索，先是一次调用API，再优化成了批量处理，解决了很多bug，最后到现在稍微整合就可以得到完美的答案。

项目包含两个版本：
*   **大陆版 (无需 VPN):** 代码位于 `QwQ_answer(no_vpn)/` 文件夹，主文件是 `main.py`。
*   **海外版 (需要 VPN):** 代码位于 `QwQ_answer/` 文件夹，主文件是 `batch_process.py`。

**仓库链接:** [https://github.com/Wing900/QwQ-32B_Math_Solver](https://github.com/Wing900/QwQ-32B_Math_Solver)

## 快速开始 (Quick Start)

**1. 获取代码**

*   在 PyCharm 中使用 "Get from VCS" 克隆上面的仓库链接。
*   或者，直接下载 ZIP 压缩包解压。

**2. 环境设置**

*   **安装依赖:** PyCharm 通常会提示你安装 `requirements.txt` 中的库。如果没有提示，可以在 PyCharm 的终端 (Terminal) 中运行 `pip install -r requirements.txt`。
*   **创建文件夹:** 在项目对应子目录下，手动创建两个空文件夹：`images` 和 `output`。

**3. 配置 API 密钥 (重要！)**

⚠️ **安全警告** ⚠️
*   本代码使用**硬编码**方式处理 API 密钥。GitHub 上的版本用了**留白** (如 "")。
*   你**必须手动编辑**代码文件，输入你自己的**真实 API 密钥**才能运行。
*   **请查找并修改以下文件中的空白：**
    *   `QwQ_answer(no_vpn)/api_clients.py` 
    *   `QwQ_answer/` 文件夹下的 `process_image.py` 文件
*   **绝对禁止将包含你真实密钥的文件上传到 GitHub！请妥善保管修改后的本地代码！**

**4. 使用方法**

*   **放入图片:** 将你的数学题图片文件 (jpg, png 等) 放入根目录下的 `images` 文件夹。
*   **运行脚本 (在 PyCharm 中):**
    *   **大陆版:** 右键点击 `QwQ_answer(no_vpn)/main.py` -> 选择 "Run 'main'"。
    *   **海外版 (需先连接 VPN):** 右键点击 `QwQ_answer/batch_process.py` -> 选择 "Run 'batch_process'"。
*   **查看结果:** 生成的 Markdown 文件会保存在对应子目录下的 `output` 文件夹中。

## 声明 (Disclaimer)

*   本项目仅供学习交流，**严禁用于学术不端行为**。
*   AI 解答可能出错，请自行核对。
*   用户需自行负责 API 密钥的安全（因需要手动编辑代码）和潜在的 API 使用费用。
*   作者不对任何因使用本项目造成的后果负责。

## 致谢 (Acknowledgements)
- 感谢 FreeQwQ 项目 提供的免费 API 支持。[https://qwq.aigpu.cn/]

- 感谢 智谱 AI / Google AI / 硅基流动 等提供的模型 API。
## 许可证 (License)

[MIT License](LICENSE)