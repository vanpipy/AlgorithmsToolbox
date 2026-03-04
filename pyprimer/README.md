# It is the algorithm exploring in the computer world

## uv 使用与校验
- 安装 uv（已安装则跳过）：参考 https://docs.astral.sh/uv/
- 初始化/同步环境（在项目根 pyprimer 目录执行）：
  - uv sync
- 激活虚拟环境（PowerShell）：
  - .venv\\Scripts\\Activate.ps1
- 运行示例（基于当前 src 布局，包名为 src）：
  - uv run python -c "from src import ArrayStack; s=ArrayStack(); print(len(s))"
- 添加依赖：
  - uv add <包名>
- 移除依赖：
  - uv remove <包名>
- 构建本地包：
  - uv build

## 结构说明
- 打包入口在 pyproject.toml，使用 [tool.hatch.build.targets.wheel].packages = ["src"]
- 源码放置在 src 目录，当前导出位于 src/__init__.py
