
import aiohttp
import asyncio
from google.generativeai import configure, GenerativeModel
from PIL import Image
import logging

# 配置日志（简化输出）
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# API 配置 （硬编码警告！！！！！）
QWQ_API_KEY = ""
GEMINI_API_KEY = ""
configure(api_key=GEMINI_API_KEY, transport='rest')
QWQ_API_URL = "https://api.suanli.cn/v1/chat/completions"

# 从外部文件导入 Prompt 模板
from prompts import (
    IMAGE_TO_MARKDOWN_PROMPT,
    GENERATE_ANSWER_PROMPT,
    FORMAT_ANSWER_PROMPT
)


# 调用 Gemini API
async def call_gemini_api_async(prompt, image=None):
    model = GenerativeModel('gemini-2.0-flash')
    try:
        inputs = [prompt]
        if image:
            inputs.append(image)
        response = await asyncio.get_event_loop().run_in_executor(None, lambda: model.generate_content(inputs))
        return response.text.strip().replace("```", "")
    except Exception as e:
        logging.error(f"调用 Gemini API 失败: {str(e)}")
        return None


# 调用 QwQ API
async def call_qwq_api_async(prompt):
    headers = {
        "Authorization": f"Bearer {QWQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "free:QwQ-32B",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.36,
        "max_tokens": 1024  # 如果这里过大，会导致 API 调用失败 疑似是API网关或后端服务通常对单次请求的最大处理时间 有限制（如30秒）
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(QWQ_API_URL, headers=headers, json=data) as response:
                result = await response.json()
                return result["choices"][0]["message"]["content"]
    except Exception as e:
        logging.error(f"调用 QwQ API 失败: {str(e)}")
        return None


# 主处理逻辑
async def process_image_async(input_image_path, output_filename):
    image = Image.open(input_image_path)

    # 步骤1：图片转 Markdown
    markdown_content = await call_gemini_api_async(IMAGE_TO_MARKDOWN_PROMPT, image)
    if not markdown_content:
        logging.error(f"图片转 Markdown 失败: {input_image_path}")
        return False

    # 步骤2：生成答案
    answer_prompt = GENERATE_ANSWER_PROMPT.format(content=markdown_content)
    raw_answers = await call_qwq_api_async(answer_prompt)
    if not raw_answers:
        logging.error(f"生成答案失败: {input_image_path}")
        return False

    # 步骤3：格式整理
    format_prompt = FORMAT_ANSWER_PROMPT.format(
        original=markdown_content,
        answers=raw_answers
    )
    formatted_answers = await call_gemini_api_async(format_prompt)
    if not formatted_answers:
        logging.error(f"格式整理失败: {input_image_path}")
        return False

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(formatted_answers)
    return True


# 同步包装函数
def process_image(input_image_path, output_filename):
    return asyncio.run(process_image_async(input_image_path, output_filename))