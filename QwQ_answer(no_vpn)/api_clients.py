import aiohttp
import base64
from io import BytesIO
from PIL import Image
from colorama import Fore, Style

# 配置API密钥 (硬编码警告)
API_KEYS = {
    "SILICONFLOW": "",
    "GLM": "",
    "QWQ": ""
}

# 可爱的日志函数
def log_info(msg): print(f"{Fore.GREEN}🌸 {msg}{Style.RESET_ALL}")
def log_warning(msg): print(f"{Fore.YELLOW}⚠️ {msg}{Style.RESET_ALL}")
def log_error(msg): print(f"{Fore.RED}💥 {msg}{Style.RESET_ALL}")

async def format_with_deepseek(original_content, raw_answers):
    """整理答案格式"""
    try:
        async with aiohttp.ClientSession() as session:
            payload = {
                "model": "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
                "messages": [{
                    "role": "user",
                    "content": f"请帮我整理以下内容格式：\n{original_content}\n生成的答案：\n{raw_answers}"
                }],
                "temperature": 0.7,
                "top_p": 0.7
            }
            async with session.post(
                url="https://api.siliconflow.cn/v1/chat/completions",
                headers={"Authorization": f"Bearer {API_KEYS['SILICONFLOW']}"},
                json=payload
            ) as resp:
                if resp.status != 200:
                    log_error(f"DeepSeek API 错误: HTTP {resp.status}")
                    return None
                data = await resp.json()
                return data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    except Exception as e:
        log_error(f"DeepSeek调用异常: {str(e)}")
        return None

async def image_to_markdown(image_path):
    """图片转Markdown"""
    try:
        # 图片转base64
        with Image.open(image_path) as img:
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

        async with aiohttp.ClientSession() as session:
            payload = {
                "model": "glm-4v-flash",
                "messages": [{
                    "role": "user",
                    "content": [
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_base64}"}},
                        {"type": "text", "text": "请将图片内容转写为Markdown格式"}
                    ]
                }]
            }
            async with session.post(
                url="https://open.bigmodel.cn/api/paas/v4/chat/completions",
                headers={"Authorization": f"Bearer {API_KEYS['GLM']}"},
                json=payload
            ) as resp:
                if resp.status != 200:
                    log_error(f"GLM API 错误: HTTP {resp.status}")
                    return None
                data = await resp.json()
                return data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    except Exception as e:
        log_error(f"图片处理异常: {str(e)}")
        return None

async def generate_answers(prompt, temperature=0.36, max_tokens=1024):
    """生成答案 (带温度控制)"""
    try:
        async with aiohttp.ClientSession() as session:
            payload  = {
        "model": "free:QwQ-32B",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.36,
        "max_tokens": 1024  # 如果这里过大，会导致 API 调用失败 疑似是API网关或后端服务通常对单次请求的最大处理时间 有限制（如30秒）
    }
            async with session.post(
                url="https://api.suanli.cn/v1/chat/completions",
                headers={"Authorization": f"Bearer {API_KEYS['QWQ']}"},
                json=payload
            ) as resp:
                if resp.status != 200:
                    log_error(f"QWQ API 错误: HTTP {resp.status}")
                    return None
                data = await resp.json()
                return data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    except Exception as e:
        log_error(f"答案生成异常: {str(e)}")
        return None