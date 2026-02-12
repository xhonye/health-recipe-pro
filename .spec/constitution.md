# Project Constitution: Advanced Healthy Recipe Pro

## 1. Role Definition
你是一个精通全栈开发（前端 + 数据持久化）与临床营养学的 AI 智能体。

## 2. Tech Stack
- **Frontend**: 单文件 `index.html` (HTML5, Tailwind CSS CDN, ES6+).
- **Persistence**: 使用浏览器 `localStorage` 存储用户新增的食材，确保刷新页面后数据不丢失。

## 3. Data Structure (核心数据规范)
食材库 `foodDatabase` 的每个条目必须包含：
- `id`: 唯一标识
- `name`: 食材名称
- `category`: 类别 (Protein/Carb/Veg/Fat)
- `nutrient`: 核心营养素名称 (如：花青素、优质蛋白、膳食纤维)
- `amount`: 每100g含量 (数字)
- `unit`: 单位 (mg 或 g)
- `nrv`: 每日参考值百分比 (%)

## 4. Business Logic
- **初始化**: Agent 需预置 4 大类各 20 种食材（共 80 条基础数据）。
- **随机算法**: 保持 3+2+3+2 比例抽取，展示时需同步显示其营养素信息。
- **数据管理**: 
  - 提供一个“管理面板”视图。
  - 支持表格化展示所有食材。
  - 提供“新增食材”表单，包含上述所有字段。

## 5. UI Layout (界面要求)
- **主视图**: 
  - 极简卡片流，突出显示“食材名”和“特色营养素”。
  - 一个醒目的“生成/刷新”按钮。
  - 一个右下角的“⚙️ 管理数据”悬浮按钮。
- **管理面板**: 
  - 采用全屏遮罩（Modal）或折叠面板。
  - 包含一个数据表格和一个“添加新项”的输入区域。