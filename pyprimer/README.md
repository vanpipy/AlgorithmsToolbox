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

### 测试脚本
- 查看帮助：
  - uv run tests -h
- 指定测试文件/目录（可重复）：
  - uv run tests -t test/test_array_queue.py
  - uv run tests -t test/test_array_queue.py -t test/test_dynamic_array_queue.py
- 关键字过滤（仅运行用例 id 含关键字，如 shrink）：
  - uv run tests -t test/test_dynamic_array_queue.py -k shrink
- 指定发现起点与模式：
  - uv run tests -s test -p "test_*.py"
- 静默输出：
  - uv run tests -q
- 运行全部测试：
  - uv run tests
