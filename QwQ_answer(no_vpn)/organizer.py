import os
import glob
import tkinter as tk
from tkinter import messagebox


def clear_folder(folder_path):
    """清空指定文件夹中的文件"""
    files = glob.glob(os.path.join(folder_path, "*"))
    for file in files:
        try:
            os.remove(file)
            print(f"✨ 已删除: {file}")
        except Exception as e:
            print(f"😢 删除失败: {file}, 原因: {e}")


def merge_md_files():
    """按特定顺序合并md文件"""
    md_files = glob.glob(os.path.join("output", "image_*.md"))
    if not md_files:
        print("😮 没有找到可合并的md文件~")
        return False

    # 提取文件编号并排序
    file_dict = {}
    for file in md_files:
        basename = os.path.basename(file)
        try:
            num = int(basename.replace("image_", "").replace(".md", ""))
            file_dict[num] = file
        except ValueError:
            print(f"😕 无法解析文件名: {basename}")

    if not file_dict:
        print("😮 没有有效的md文件可合并~")
        return False

    # 获取最大编号，用于确定开始文件
    max_num = max(file_dict.keys())

    # 按特定顺序排列: image_n.md + image_1.md + ... + image_(n-1).md
    order = [max_num] + list(range(1, max_num))

    # 合并文件内容
    merged_content = ""
    for num in order:
        if num in file_dict:
            try:
                with open(file_dict[num], 'r', encoding='utf-8') as f:
                    content = f.read()
                    merged_content += content + "\n\n\n"
                    print(f"✅ 已合并: {os.path.basename(file_dict[num])}")
            except Exception as e:
                print(f"😢 读取失败: {file_dict[num]}, 原因: {e}")

    # 写入合并文件
    try:
        with open(os.path.join("output", "all.md"), 'w', encoding='utf-8') as f:
            f.write(merged_content)
        print("🎉 合并完成! 已创建 all.md")
        return True
    except Exception as e:
        print(f"😢 创建合并文件失败: {e}")
        return False


def main():
    # 检查文件夹是否存在
    if not os.path.exists("images"):
        os.makedirs("images")
        print("🌟 创建了 images 文件夹")

    if not os.path.exists("output"):
        os.makedirs("output")
        print("🌟 创建了 output 文件夹")

    # 创建GUI
    root = tk.Tk()
    root.title("文件管理器")
    root.geometry("400x200")

    # 复选框变量
    clear_images_var = tk.BooleanVar()
    clear_output_var = tk.BooleanVar()
    merge_output_var = tk.BooleanVar()

    # 复选框
    tk.Checkbutton(root, text="清空 images 文件夹", variable=clear_images_var).pack(anchor=tk.W, padx=20, pady=10)
    tk.Checkbutton(root, text="清空 output 文件夹", variable=clear_output_var).pack(anchor=tk.W, padx=20, pady=10)
    tk.Checkbutton(root, text="合并 output 文件夹中的md文件", variable=merge_output_var).pack(anchor=tk.W, padx=20,
                                                                                              pady=10)

    def on_confirm():
        clear_images = clear_images_var.get()
        clear_output = clear_output_var.get()
        merge_output = merge_output_var.get()

        # 检查合并和清空output的冲突
        if merge_output and clear_output:
            messagebox.showwarning("警告", "无法同时合并和清空output文件夹 😅")
            print("⚠️ 警告: 无法同时合并和清空output文件夹")
            return

        # 执行操作
        if clear_images:
            clear_folder("images")
            print("🧹 已清空images文件夹")

        if clear_output:
            clear_folder("output")
            print("🧹 已清空output文件夹")

        if merge_output:
            merge_md_files()

        root.destroy()

    # 确定按钮
    tk.Button(root, text="确定", command=on_confirm, width=10).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"😢 发生错误: {e}")