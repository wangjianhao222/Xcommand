import sys
import subprocess
import tkinter as tk
from tkinter import scrolledtext

class CommandExecutor:
    def __init__(self, root):
        self.root = root
        root.title("跨平台命令执行工具")
        root.geometry("800x600")
        
        # 目标系统选择
        self.system_var = tk.StringVar(value=self.detect_system())
        tk.Label(root, text="目标系统:").pack(pady=5)
        self.system_menu = tk.OptionMenu(root, self.system_var, "Windows", "Linux", "macOS")
        self.system_menu.pack(pady=5)
        
        # 命令输入
        self.command_entry = tk.Entry(root, width=80)
        self.command_entry.insert(0, "输入命令...")
        self.command_entry.pack(pady=10)
        
        # 执行按钮
        self.execute_btn = tk.Button(root, text="执行命令", command=self.execute_command)
        self.execute_btn.pack(pady=5)
        
        # 输出日志
        self.log = scrolledtext.ScrolledText(root, width=90, height=25)
        self.log.pack(pady=10)
    
    def detect_system(self):
        """检测当前操作系统"""
        system = sys.platform
        return {
            'win32': 'Windows',
            'linux': 'Linux',
            'darwin': 'macOS'
        }.get(system, 'Unknown')
    
    def execute_command(self):
        command = self.command_entry.get().strip()
        target_system = self.system_var.get()
        current_system = self.detect_system()
        
        if not command:
            self.log.insert(tk.END, "错误：命令不能为空！\n")
            return
        
        if target_system != current_system:
            self.log.insert(tk.END, f"警告：当前系统为 {current_system}，无法直接执行 {target_system} 命令。\n")
            return
        
        try:
            self.log.insert(tk.END, f"执行命令: {command} ({target_system})\n")
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True
            )
            if result.stdout:
                self.log.insert(tk.END, f"输出：\n{result.stdout}\n")
            if result.stderr:
                self.log.insert(tk.END, f"错误：\n{result.stderr}\n")
        except Exception as e:
            self.log.insert(tk.END, f"执行失败：{str(e)}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = CommandExecutor(root)
    root.mainloop()
