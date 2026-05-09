# Learn Algorithmic Trading - Reloaded

本项目是对《Learn Algorithmic Trading》一书附带代码的修改和优化版本。

## 项目简介

本代码库包含了算法交易领域的多个核心概念实现，涵盖从技术指标计算到策略回测的完整流程。原书代码存在一些兼容性问题和逻辑错误，本版本对其进行了修复和改进。

**原书代码仓库**: [https://github.com/PacktPublishing/Learn-Algorithmic-Trading](https://github.com/PacktPublishing/Learn-Algorithmic-Trading)

## 主要修改内容

### 1. Chapter 5 - 统计套利策略
- 修复了 `stat_arb.py` 中协方差计算的数学逻辑错误
- 修正了 PnL（盈亏）计算中的逻辑问题
- 优化了未平仓量的计算方式

### 2. Chapter 7 - 交易模拟框架
- 修复了单元测试文件中的导入问题（`ModuleNotFoundError: No module named 'chapter7'`）
- 将绝对导入改为相对导入，确保模块正确加载

### 3. Chapter 8 - FIX 协议模拟器
- 修复了 `quickfix.Exception` 的兼容性问题，改为 `quickfix.FIXException`
- 修复了模块导入路径问题（`from sim import ...` → `from fixsim.sim import ...`）
- 修复了 `yaml.load()` 的安全性警告，添加 `Loader=yaml.SafeLoader` 参数

### 4. Chapter 9 - 数据存储与策略实现
- **hd5pandareader.py**: 修复了 pandas `to_hdf()` API 兼容性问题（添加 `key=` 参数）
- **hd5pandareader.py**: 创建模拟金融数据替代 Yahoo Finance 数据源（原数据源已失效）
- **kdb_data.py**: 用 pandas DataFrame 替代 pyq/KDB+ 数据库依赖（避免安装复杂的 KDB+ 环境）
- **TradingStrategyDualMA.py**: 发现并标记了重复调用 `handle_book_event` 的代码问题

## Python 版本和依赖

### Python 版本
- Python 3.12

### 核心依赖库

| 库名 | 版本 | 用途 |
|------|------|------|
| pandas | 3.0.2 | 数据分析和处理 |
| numpy | 2.4.4 | 数值计算 |
| matplotlib | 3.10.8 | 数据可视化 |
| scikit-learn | 1.5.0 | 机器学习算法 |
| quickfix | 1.15.1 | FIX 协议实现 |
| h5py | 3.16.0 | HDF5 数据存储 |
| tables | 3.11.1 | 高性能 HDF5 数据处理 |
| twisted | 24.3.0 | 异步网络编程 |
| pyyaml | 6.0.3 | YAML 配置文件处理 |
| pandas-datareader | 0.10.0 | 金融数据获取 |

### 安装依赖

```bash
# 使用 pip 安装所有依赖
pip install -r requirements.txt

# 或使用虚拟环境
e:\Code\python\Learn\py312\Scripts\pip.exe install -r requirements.txt
```

## 项目结构

```
Learn-Algorithmic-Trading-Reloaded/
├── Chapter1/              # 基础概念
├── Chapter2/              # 技术指标计算（SMA, EMA, MACD, RSI等）
├── Chapter3/              # 机器学习模型（KNN, Logistic, SVM等）
├── Chapter4/              # 交易策略（双均线、海龟交易等）
├── Chapter5/              # 统计套利策略
├── Chapter6/              # 风险管理
├── Chapter7/              # 交易模拟框架
├── Chapter8/              # FIX 协议模拟器
└── Chapter9/              # 数据存储与事件驱动回测
```

## 使用说明

### 运行 FIX 模拟器

```bash
# 启动 FIX Server
cd Chapter8/fixsim
python fixsim-server.py -ac fixsim-server.conf.ini -c fixsim-server.conf.yaml

# 启动 FIX Client（新开终端）
cd Chapter8/fixsim
python fixsim-client.py -ic fixsim-client.conf.ini -c fixsim-client.conf.yaml
```

### 运行 HDF5 示例

```bash
cd Chapter9
python hd5pandareader.py
```

### 运行 KDB+ 替代示例

```bash
cd Chapter9
python kdb_data.py
```

## 注意事项

1. **Yahoo Finance 数据源**: 原书使用的 Yahoo Finance API 已失效，部分代码使用模拟数据替代
2. **KDB+ 数据库**: `kdb_data.py` 已改用 pandas 实现，无需安装 KDB+
3. **quickfix 安装**: quickfix 包需要 C++ 编译环境，建议使用预编译版本

## 许可证

MIT License
