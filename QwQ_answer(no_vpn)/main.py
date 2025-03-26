import os
import asyncio
from colorama import Fore, Style
from api_clients import *

# ===== 配置 =====
INPUT_DIR = "images"
OUTPUT_DIR = "output"
EXCLUDED_IMAGES = ["demo.png"]


# ===== 增强日志 =====
def log(title, content="", color=Fore.WHITE):
    icons = {"scan": "🔍", "exclude": "🚫", "process": "🔄",
             "success": "✅", "fail": "❌", "error": "💥"}
    print(f"{color}{icons.get(title, '')} {title.upper():<8}: {content}{Style.RESET_ALL}")


# ===== 修复编码问题 =====
async def process_image(img):
    log("process", img, Fore.LIGHTBLUE_EX)
    try:
        md_content = await image_to_markdown(f"{INPUT_DIR}/{img}")
        if not md_content:
            raise Exception("图片识别失败")

        answers = await generate_answers(f"请生成答案：\n{md_content}")
        if not answers:
            raise Exception("答案生成失败")

        formatted = await format_with_deepseek(md_content, answers)
        if not formatted:
            raise Exception("格式整理失败")

        # 关键修复：强制使用UTF-8编码写入
        with open(f"{OUTPUT_DIR}/{os.path.splitext(img)[0]}.md", "w", encoding="utf-8") as f:
            f.write(formatted)
        log("success", img, Fore.LIGHTGREEN_EX)

    except Exception as e:
        log("fail", f"{img} ({type(e).__name__}: {str(e)})", Fore.LIGHTRED_EX)


async def main():
    # 初始化
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"\n{Fore.CYAN}🌟 ANSWER PROCESSOR{Style.RESET_ALL}")

    # 扫描文件
    all_images = sorted(f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('.png', '.jpg')))
    to_process = [f for f in all_images if f not in EXCLUDED_IMAGES]

    # 打印扫描结果
    log("scan", f"共找到 {len(all_images)} 张图片", Fore.LIGHTYELLOW_EX)
    for img in all_images:
        if img in EXCLUDED_IMAGES:
            log("exclude", img, Fore.LIGHTMAGENTA_EX)
        else:
            log("process", img, Fore.LIGHTBLUE_EX)

    # 批量处理
    print("\n" + "━" * 30)
    await asyncio.gather(*[process_image(img) for img in to_process])
    print(f"\n{Fore.LIGHTCYAN_EX}📊 处理完成{Style.RESET_ALL}")


if __name__ == "__main__":
    asyncio.run(main())