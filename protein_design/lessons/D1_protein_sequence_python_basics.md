# D1 教案｜蛋白质序列分析与 Python 编程基础

> 大分子 AIDD 系统课程 · Week 1 / Day 1  
> 方向：Protein Design / Protein Language Models / AIDD  
> 适用对象：具备 CADD 基础、Python 处于入门阶段的学习者  
> 课程方式：概念 → 伪代码 → 可运行示例 → 练习 → 结果检查  
> **注意：本教案包括参考实现，但不表示学习者已完成本机项目验收。**

## 一、教学目标

完成本课后，应能够：

1. 将氨基酸序列表示为 Python 字符串，认识简单的 FASTA 文件。
2. 使用变量、`len()`、`print()`、索引与切片处理蛋白序列。
3. 使用 `for`、`if` 和计数器统计指定氨基酸。
4. 使用列表（List）和字典（Dictionary）统计全部 20 种标准氨基酸。
5. 使用 `open()`、`readlines()` 和 `strip()` 读取两行、单条序列的 FASTA。
6. 实现、运行并核对泛素（Ubiquitin, 1UBQ）序列组成分析程序。

**研究任务：** `FASTA → 序列清理 → 氨基酸计数 → 组成比例 → 一致性检查`。

本课仅要求 CPU。GPU、深度学习框架及蛋白语言模型推理不属于 D1 必学内容。

## 二、课程安排

| 单元 | 核心知识 | 可观察成果 |
|---|---|---|
| D1-A | 变量、字符串、FASTA、伪代码 | 能计算序列长度 |
| D1-B | 零基索引、负数索引、切片 | 能读取指定残基/片段 |
| D1-C | `for`、`if`、计数器、比例 | 能统计 K 或其他指定氨基酸 |
| D1-D | 列表、字典、Key–Value | 能初始化并更新氨基酸计数表 |
| D1-E | 20 种标准氨基酸组成分析 | 能输出每种残基的数量与比例 |
| D1-F | FASTA 文件读取与文本清理 | 能读取简单 FASTA 的序列 |
| D1-G | 模块整合与结果验证 | 能运行完整序列分析程序 |

建议用约 4–6 小时完成讲解与练习，实际用时以编程熟练度为准。

---

## 三、D1-A｜变量、字符串、FASTA 与伪代码

蛋白序列通常使用氨基酸的单字母代码表示，例如：

```python
sequence = "MKTAYIAK"
length = len(sequence)
print(length)  # 8
```

- `sequence` 是变量；`"MKTAYIAK"` 是字符串（`str`）。
- `=` 用于赋值，不是比较相等。
- `len(sequence)` 返回字符数；`print()` 输出内容。
- FASTA 第一行以 `>` 开头表示标题，后面为序列内容。

本课使用的教学 FASTA：

```fasta
>1UBQ_A Ubiquitin
MQIFVKTLTGKTITLEVEPSDTIENVKAKIQDKEGIPPDQQRLIFAGKQLEDGRTLSDYNIQKESTLHLVLRLRGG
```

**伪代码**是用自然语言描述计算步骤，不必符合 Python 语法：

```text
输入 sequence
计算 sequence 的长度，保存为 length
输出 length
```

转成 Python 才需精确使用变量名、括号和符号。

### 小练习

给定 `"ACDEFG"`，指出 `sequence` 与 `"ACDEFG"` 分别是什么，以及 `len()` 的结果。

---

## 四、D1-B｜残基编号、索引和切片

在一般蛋白序列中，生物学序列位置从 1 起；Python 字符串索引从 0 起。

```text
氨基酸：       M  K  T  A  Y  I  A  K
生物学位置：   1  2  3  4  5  6  7  8
Python 索引：  0  1  2  3  4  5  6  7
```

```python
sequence = "MKTAYIAK"
print(sequence[0])   # M
print(sequence[3])   # A
print(sequence[-1])  # K
print(sequence[1:4]) # KTA
print(sequence[:3])  # MKT
print(sequence[-3:]) # IAK
```

切片 `sequence[start:end]` **包含 start、不包含 end**。

查询第 10 位残基：

```python
position = 10
aa = sequence[position - 1]
```

这里 `sequence` 应替换为实际完整蛋白序列。

> **结构生物学提醒：** PDB/mmCIF 中的残基编号可能受缺失残基、链号、插入码影响，不能一概直接等同于序列索引。D1 首先处理线性序列编号。

---

## 五、D1-C｜循环、条件判断与计数器

科研任务：统计序列中 K（赖氨酸）的数量。

**伪代码：**

```text
输入 sequence
初始化 count = 0
遍历 sequence 中每个氨基酸 aa：
    如果 aa 等于 K：
        更新 count 为 count + 1
输出 count
```

**Python：**

```python
sequence = "MKTAYIAK"
count = 0

for aa in sequence:
    if aa == "K":
        count = count + 1

length = len(sequence)
ratio = count / length

print("K count:", count)  # 2
print("K ratio:", ratio)  # 0.25
```

重点：

- `for` 后与 `if` 后都需要**英文半角冒号** `:`。
- 缩进属于代码语法的一部分。
- `=` 是赋值；`==` 是相等比较。
- `count + 1` 只计算表达式；`count = count + 1` 才真正更新计数器。
- 将 `count = 0` 放在循环内部会导致每次迭代重新计数。

如果只想更换目标氨基酸，可以引入 `target` 变量：

```python
target = "A"
count = 0
for aa in sequence:
    if aa == target:
        count = count + 1
print(count)  # 2
```

---

## 六、D1-D｜列表与字典

**列表（List）**保存一组元素；**字典（Dictionary）**保存键（Key）与值（Value）的对应关系。

```python
amino_acids = ["A", "C", "D", "E"]
print(amino_acids[2])  # D

counts = {"A": 2, "K": 1}
print(counts["K"])     # 1
```

与单变量计数不同，字典可同时统计多个残基：

```python
sequence = "MKTAYIAK"
amino_acids = ["M", "K", "T", "A", "Y", "I"]
counts = {}

# 第一个循环：初始化各残基计数器
for aa in amino_acids:
    counts[aa] = 0

# 第二个循环：遍历序列，累计出现次数
for aa in sequence:
    counts[aa] = counts[aa] + 1

print(counts["K"])  # 2
print(counts["A"])  # 2
```

若 `counts` 只包含 `"K"`，却在未判断的情况下读取 `counts["M"]`，会产生 `KeyError`。因此：

- **仅统计指定残基：** 用 `if aa == "K":` 筛选。
- **统计所有标准残基：** 先初始化全部需要统计的键，再累计。

循环执行次数取决于实际遍历对象，例如 6 种残基的列表初始化循环执行 6 次，8 aa 序列的计数循环执行 8 次。

---

## 七、D1-E｜20 种标准氨基酸组成

20 种标准氨基酸单字母代码：

```python
amino_acids = [
    "A", "C", "D", "E", "F",
    "G", "H", "I", "K", "L",
    "M", "N", "P", "Q", "R",
    "S", "T", "V", "W", "Y"
]
```

组成比例：

```text
f(aa) = 该氨基酸出现次数 / 蛋白序列总长度
```

对本课的 1UBQ 参考序列（76 aa），计算结果为：

| AA | Count | AA | Count | AA | Count | AA | Count |
|---|---:|---|---:|---|---:|---|---:|
| A | 2 | C | 0 | D | 5 | E | 6 |
| F | 2 | G | 6 | H | 1 | I | 7 |
| K | 7 | L | 9 | M | 1 | N | 2 |
| P | 3 | Q | 6 | R | 4 | S | 3 |
| T | 7 | V | 4 | W | 0 | Y | 1 |

合计：76。K 的比例为 `7 / 76 ≈ 0.0921053`（约 9.21%）。

此类组成特征有助于比较天然序列和生成序列，但**不能单凭氨基酸组成判断稳定性、结合能力或实验功能**。

---

## 八、D1-F｜读取 FASTA 文件

将下列内容保存为与 Python 脚本处于同一目录的 `ubiquitin.fasta`：

```fasta
>1UBQ_A Ubiquitin
MQIFVKTLTGKTITLEVEPSDTIENVKAKIQDKEGIPPDQQRLIFAGKQLEDGRTLSDYNIQKESTLHLVLRLRGG
```

读取程序：

```python
with open("ubiquitin.fasta", "r", encoding="utf-8") as file:
    lines = file.readlines()

header = lines[0].strip()
sequence = lines[1].strip()
length = len(sequence)

print(header)
print(length)  # 76
```

- `open(..., "r")` 按只读方式打开文件。
- `with` 代码块结束后会关闭文件。
- `readlines()` 读取全部文本行并返回列表。
- `lines[0]` 是标题；`lines[1]` 是序列所在行。
- `strip()` 去除字符串首尾的空白字符，例如行尾换行符 `\n`。
- `file.readlines` 是方法对象，**`file.readlines()` 才是调用方法**。

**适用边界：** 本课示例仅适用于“单条序列、标题一行、序列一行”的简单 FASTA。实际数据常有多行折叠序列、多个 FASTA 记录或非标准字符（例如 X），需要额外解析与校验。`strip()` 不会自动验证字符合法性。

---

## 九、D1-G｜综合项目：Ubiquitin Sequence Analyzer

### 9.1 项目目标

实现 `FASTA 输入 → 序列长度 → 20 种氨基酸计数 → 组成比例 → 总量一致性检查`。

### 9.2 完整参考程序

将以下代码保存为 `d1_sequence_analyzer.py`：

```python
# D1 Final Project: Ubiquitin Sequence Analyzer
# 适用于两行、单条序列的 FASTA

# 1. 读取序列
with open("ubiquitin.fasta", "r", encoding="utf-8") as file:
    lines = file.readlines()

sequence = lines[1].strip()
length = len(sequence)

# 2. 定义标准氨基酸
amino_acids = [
    "A", "C", "D", "E", "F",
    "G", "H", "I", "K", "L",
    "M", "N", "P", "Q", "R",
    "S", "T", "V", "W", "Y"
]

# 3. 创建字典并初始化
counts = {}
for aa in amino_acids:
    counts[aa] = 0

# 4. 统计
for aa in sequence:
    counts[aa] = counts[aa] + 1

# 5. 输出每种氨基酸的数量与比例
for aa in amino_acids:
    ratio = counts[aa] / length
    print(aa, counts[aa], ratio)

# 6. 独立核对计数总和
total = 0
for aa in amino_acids:
    total = total + counts[aa]

print("Protein length:", length)
print("K count:", counts["K"])
print("K ratio:", counts["K"] / length)
print("Total residue count:", total)
```

在终端中运行：

```bash
python d1_sequence_analyzer.py
```

若环境使用 Windows Python Launcher，也可以尝试：

```powershell
py d1_sequence_analyzer.py
```

### 9.3 预期关键结果

```text
Protein length: 76
K count: 7
K ratio: 0.09210526315789473
Total residue count: 76
```

### 9.4 项目验收清单

- [ ] `ubiquitin.fasta` 文件可以被程序成功读取
- [ ] `length == 76`
- [ ] `counts["K"] == 7`，`counts["L"] == 9`
- [ ] 20 种标准氨基酸计数总和为 76
- [ ] 能解释三个主要循环：初始化、计数、输出
- [ ] 能说明输入文件或字符异常时现有程序的局限

> 本程序只统计已初始化的 20 种标准氨基酸。若序列中出现未知字符，可能报 `KeyError`；若序列为空，比例计算将存在除零问题。这些输入校验属于后续课程内容。

---

## 十、常见错误与纠错指南

| 错误 | 常见表现 | 正确处理 |
|---|---|---|
| 把中文冒号写入代码 | `if aa == "K"：` | 改成英文 `:` |
| 忘记冒号 | `if aa == "K"` | 在条件末尾加 `:` |
| 未保存计数结果 | `count + 1` | `count = count + 1` |
| 初始化位置错误 | 在计数循环里写 `count = 0` | 将初始化移到循环前 |
| 未定义变量 | 直接使用 `length` | 先写 `length = len(sequence)` |
| 方法未调用 | `file.readlines` | `file.readlines()` |
| 访问不存在的键 | `counts["M"]` 但未初始化 | 先初始化或增加 `if` 筛选 |
| 误判循环次数 | 按不同残基种类估计循环数 | 按被遍历对象元素总数计算 |
| 将 PDB 编号当字符串索引 | 直接使用 `sequence[pdb_resid - 1]` | 先确认结构与序列编号映射 |

**自检顺序：** 变量是否已定义 → 括号/冒号是否正确 → 缩进位置 → 循环范围 → 结果是否符合数据约束。

---

## 十一、复习练习与参考答案

### 练习 1：索引和切片

```python
sequence = "MKTAYIAK"
print(sequence[2])
print(sequence[-2])
print(sequence[1:4])
```

**答案：** `T`、`A`、`KTA`。

### 练习 2：循环次数

```python
sequence = "AAKAK"
amino_acids = ["A", "K"]
```

若初始化循环遍历 `amino_acids`、计数循环遍历 `sequence`，分别执行几次？

**答案：** 2 次与 5 次。

### 练习 3：识别错误

```python
sequence = "AKKA"

for aa in sequence:
    count = 0
    if aa == "K":
        count = count + 1

print(count)
```

**问题：** `count = 0` 在循环内部，每次循环都会重置。  
**修正：** 把 `count = 0` 放在 `for` 之前；最终结果应为 2。

### 练习 4：字典 KeyError

```python
sequence = "MKA"
counts = {"K": 0}

for aa in sequence:
    counts[aa] = counts[aa] + 1
```

**问题：** 初始字典没有 `"M"` 和 `"A"` 这两个键。  
**修正：** 若只统计 K，使用已经学习的条件判断：

```python
sequence = "MKA"
counts = {"K": 0}

for aa in sequence:
    if aa == "K":
        counts[aa] = counts[aa] + 1

print(counts["K"])  # 1
```

---

## 十二、阶段评价与 D2 衔接

D1 训练覆盖：变量、字符串、索引、切片、循环、条件、字典、FASTA 读取与项目整合。此前随堂训练已完成，但**D1 最终项目的本机执行结果尚待实际验收**。

进入 D2 后，将学习：

1. 字符串拼接和突变位点前后片段提取；
2. 检查野生型残基是否与突变命名一致；
3. 生成泛素 `E24A` 单点突变序列；
4. 比较突变前后序列长度；
5. 扩展至单个位点的 19 种非野生型替换。

例如 D2 开始时的核心思路：

```python
sequence = "MKTAYIAK"
position = 4
new_aa = "G"

left = sequence[:position - 1]
right = sequence[position:]
mutant = left + new_aa + right

print(mutant)  # MKTGYIAK
```

该操作只生成**计算候选序列**，并不意味着该突变已被实验验证具有预期结构或功能。

---

## 参考资源

- RCSB PDB: [1UBQ](https://www.rcsb.org/structure/1UBQ)
- Python 官方教程：[Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- Python 官方教程：[Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
