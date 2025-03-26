import os
from concurrent.futures import ThreadPoolExecutor
from process_image import process_image
import logging
from colorama import Fore, Style, init

# 初始化 colorama 并启用自动重置
init(autoreset=True)

# 自定义日志格式（添加颜文字和柔和颜色）
logging.basicConfig(
    level=logging.INFO,
    format=f"%(asctime)s {Fore.MAGENTA}%(levelname)s{Style.RESET_ALL} "
           f"[{Fore.CYAN}%(name)s{Style.RESET_ALL}] "
           f"{Fore.LIGHTWHITE_EX}%(message)s{Style.RESET_ALL}"
)


def batch_process_images(input_folder, specific_images=None, use_multithreading=False):
    # 获取并排序图片文件
    image_files = [
        f for f in os.listdir(input_folder)
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))
    ]

    if not image_files:
        logging.error(f"{Fore.LIGHTRED_EX}◕_◕✿ 文件夹里空空如也，没有找到任何图片文件呢～")
        return

    try:
        image_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))
    except (IndexError, ValueError):
        logging.error(f"{Fore.LIGHTYELLOW_EX}⚠️ 呀！图片命名格式不对啦～应该像 'img_1.png' 这样排列哦！")
        return

    # 创建输出目录
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    # 处理排除逻辑（添加粉色高亮）
    exclude_images = set()
    if specific_images is not None:
        specific_images = [specific_images] if not isinstance(specific_images, list) else specific_images

        for img in specific_images:
            try:
                if isinstance(img, (int, str)):
                    if str(img).isdigit():
                        idx = int(img) - 1
                        if 0 <= idx < len(image_files):
                            exclude_images.add(image_files[idx])
                    elif img in image_files:
                        exclude_images.add(img)
            except Exception as e:
                logging.error(f"{Fore.LIGHTMAGENTA_EX}😱 排除规则处理出错啦！错误信息：{e}")

        image_files = [f for f in image_files if f not in exclude_images]
        if exclude_images:
            logging.info(f"{Fore.LIGHTCYAN_EX}✂️ 已排除图片：{', '.join(exclude_images)}")
            logging.info(f"{Fore.LIGHTGREEN_EX}🖼️ 开始处理以下图片：{', '.join(image_files)}")

    # 处理单张图片（添加动态表情）
    def process_single_image(image_file):
        try:
            input_path = os.path.join(input_folder, image_file)
            output_path = os.path.join(output_folder, os.path.splitext(image_file)[0] + ".md")

            logging.info(f"{Fore.LIGHTYELLOW_EX}обрадуетесь! ヾ(●゜▽゜●) 正在处理：{image_file}")
            success = process_image(input_path, output_path)

            if success:
                logging.info(f"{Fore.LIGHTGREEN_EX}✨ 处理成功！保存路径：{output_path}")
            else:
                logging.warning(f"{Fore.LIGHTRED_EX}💢 处理失败：{image_file}")
            return (image_file, success)

        except Exception as e:
            logging.error(f"{Fore.RED}💥 糟糕！{image_file} 处理时发生异常：{str(e)}")
            return (image_file, False)

    # 执行批量处理（添加进度提示）
    logging.info(f"{Fore.LIGHTBLUE_EX}🚀 开始批量处理，使用多线程：{use_multithreading}")

    if use_multithreading:
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(process_single_image, image_files))
    else:
        results = [process_single_image(img) for img in image_files]

    # 结果汇总（添加完结表情）
    failed = [img for img, success in results if not success]
    if failed:
        logging.error(f"{Fore.RED}😭 呜呜～以下图片处理失败：{', '.join(failed)}")
    else:
        logging.info(f"{Fore.LIGHTGREEN_EX}🎉 恭喜！所有图片都处理完成啦～(๑•̀ㅂ•́)و✧")


if __name__ == "__main__":
    batch_process_images(
        input_folder="images",
        specific_images=[2,3], # 排除 img_X.png
        use_multithreading=True
    )