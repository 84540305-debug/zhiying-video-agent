# STORY.md · 知影 ZhiYing 汇报 PPT 叙事逻辑

## ① 用户意图对齐
- **目标受众**：课程汇报 / 项目展示，面向教师与同学
- **核心目标**：展示知影 ZhiYing 视频制作 Agent 的完整搭建流程、技术架构、核心功能与在线成果
- **PPT 长度**：20 页（Hero 页 4 页，Supporting 14 页，Transition 2 页）
- **视觉调性**：军绿清新、专业可信、技术感、教学场景
- **内容边界**：必讲（三模式+七步+军事知识库+文生图+部署）；不讲（商业分析）；禁碰（敏感数据）

## ② 页面布局骨架（20 页 / 5 章）
| 页码 | 标题 | type | role | rhythm | layout |
|---|---|---|---|---|---|
| 01 | 知影 ZhiYing 封面 | cover | hero | peak | 全屏视觉+大标题 |
| 02 | 目录 | catalog | transition | transition | 左标题+右内容 |
| 03 | 第一章 · 项目概述 | section | transition | transition | 全屏视觉+大标题 |
| 04 | 核心能力总览 | content | supporting | valley | 左标题+右内容 |
| 05 | 在线成果与文件清单 | content | supporting | valley | 非对称双栏 |
| 06 | 第二章 · 技术架构 | section | transition | transition | 全屏视觉+大标题 |
| 07 | 技术栈八层 | content | supporting | valley | 左标题+右内容 |
| 08 | 三栏布局架构 | content | supporting | peak | 左大图+右侧文字 |
| 09 | 第三章 · 功能详解 | section | transition | transition | 全屏视觉+大标题 |
| 10 | 三种创作模式 | content | supporting | valley | 非对称双栏 |
| 11 | 七步创作流水线 | content | supporting | peak | 左标题+右内容 |
| 12 | 军事理论课知识库 | content | supporting | valley | 巨型数字+洞察 |
| 13 | 文生图 API 接入 | content | supporting | valley | 左标题+右内容 |
| 14 | 演示页生成与导出 | content | supporting | valley | 非对称双栏 |
| 15 | 第四章 · 部署上线 | section | transition | transition | 全屏视觉+大标题 |
| 16 | GitHub 仓库部署 | content | supporting | valley | 左标题+右内容 |
| 17 | GitHub Pages 在线 | content | supporting | peak | 左大图+右侧文字 |
| 18 | CORS 代理部署 | content | supporting | valley | 非对称双栏 |
| 19 | 第五章 · 项目成果 | section | transition | transition | 全屏视觉+大标题 |
| 20 | 感谢与在线地址 | ending | hero | peak | 全屏视觉+大标题 |

**Hero 页**：01（封面）、08（架构图）、11（七步流水线）、17（Pages上线）、20（结束）= 5页，占25%✓
**非对称版式**：04/05/07/08/10/11/13/14/16/17/18 = 11页，占55%✓
**对称版式**：02/03/06/09/12/15/19/20 = 8页（含5个全屏视觉section/cover/ending）
**N卡片横排**：0次 ✓

## ③ 页面大纲

### 01 知影 ZhiYing 封面
- title: 知影 ZhiYing · 大学生军事理论课 AI 视频成片 Agent
- type: cover / role: hero / rhythm: peak
- layout: 全屏视觉+大标题
- visual: L1: 军绿渐变背景+金色五角星Logo
- visual_role: atmosphere
- density: 字数约40 / 留白约50%
- anti_pattern: 禁止标题栏+装饰小图；禁止等宽卡片
- description: 项目封面，军绿渐变底+金星Logo+项目名+副标题+日期

### 02 目录
- title: 目录
- type: catalog / role: transition / rhythm: transition
- layout: 左标题+右内容
- visual: L3: 五角星角标
- visual_role: evidence
- density: 字数约80 / 留白约30%
- anti_pattern: 禁止四卡片预览；禁止铺满正文
- description: 5章目录列表：项目概述/技术架构/功能详解/部署上线/项目成果

### 03 第一章 · 项目概述
- title: 第一章 · 项目概述
- type: section / role: transition / rhythm: transition
- layout: 全屏视觉+大标题
- visual: L1: 军绿渐变背景
- visual_role: atmosphere
- density: 字数约20 / 留白约60%
- anti_pattern: 禁止四卡片预览；禁止铺满正文段落
- description: 章节扉页，军绿底+章节标题居中

### 04 核心能力总览
- title: 核心能力总览
- type: content / role: supporting / rhythm: valley
- layout: 左标题+右内容
- visual: L3: 功能图标列表
- visual_role: evidence
- density: 字数约200 / 留白约25%
- anti_pattern: 禁止等宽卡片横排；禁止50:50等分
- description: 6项核心能力表格：三模式/七步/军事库/文生图/文件上传/双通道导出

### 05 在线成果与文件清单
- title: 在线成果与文件清单
- type: content / role: supporting / rhythm: valley
- layout: 非对称双栏
- visual: L2: 文件树结构图
- visual_role: evidence
- density: 字数约180 / 留白约25%
- anti_pattern: 禁止等宽四卡；禁止50:50等分
- description: 左栏：在线地址+仓库地址；右栏：文件清单（index.html/api/proxy.js/worker.js）

### 06 第二章 · 技术架构
- title: 第二章 · 技术架构
- type: section / role: transition / rhythm: transition
- layout: 全屏视觉+大标题
- visual: L1: 军绿渐变背景
- visual_role: atmosphere
- density: 字数约20 / 留白约60%
- anti_pattern: 禁止四卡片预览；禁止铺满正文
- description: 章节扉页

### 07 技术栈八层
- title: 技术栈八层
- type: content / role: supporting / rhythm: valley
- layout: 左标题+右内容
- visual: L3: 技术图标列表
- visual_role: evidence
- density: 字数约250 / 留白约15%
- anti_pattern: 禁止等宽卡片横排
- description: 8层技术栈表格：前端/文生图/语音/音乐/录屏/持久化/版本控制/在线托管

### 08 三栏布局架构
- title: 三栏布局架构
- type: content / role: hero / rhythm: peak
- layout: 左大图+右侧文字
- visual: L1: 三栏布局示意图（占左60%）
- visual_role: anchor
- density: 字数约150 / 图片1张 / 留白约25%
- anti_pattern: 禁止50:50等分双栏；禁止产品图缩小为200x70
- description: 左栏大图：首页→创作页三栏布局示意；右栏文字：左历史项目/中预览+分镜/右AI对话

### 09 第三章 · 功能详解
- title: 第三章 · 功能详解
- type: section / role: transition / rhythm: transition
- layout: 全屏视觉+大标题
- visual: L1: 军绿渐变背景
- visual_role: atmosphere
- density: 字数约20 / 留白约60%
- anti_pattern: 禁止四卡片预览
- description: 章节扉页

### 10 三种创作模式
- title: 三种创作模式
- type: content / role: supporting / rhythm: valley
- layout: 非对称双栏
- visual: L2: 模式对比表
- visual_role: evidence
- density: 字数约220 / 留白约20%
- anti_pattern: 禁止等宽三卡横排；禁止50:50等分
- description: 图片轮播/HTML视频/演示页生成三模式对比表格，含说明+入口函数

### 11 七步创作流水线
- title: 七步创作流水线
- type: content / role: hero / rhythm: peak
- layout: 左标题+右内容
- visual: L1: 七步流程图（占右60%）
- visual_role: anchor
- density: 字数约200 / 图1张 / 留白约20%
- anti_pattern: 禁止等宽卡片横排；禁止L3角标顶替L1
- description: 七步流水线表格：脚本→大纲→分镜→画面→声音→预览→导出，含函数名

### 12 军事理论课知识库
- title: 军事理论课知识库
- type: content / role: supporting / rhythm: valley
- layout: 巨型数字+洞察
- visual: L1: 巨型数字"8"（≥48px锚点）
- visual_role: anchor
- density: 字数约200 / 留白约25%
- anti_pattern: 禁止等宽卡片横排；禁止把核心数字塞进图表卡角落
- description: 巨型数字"8"大章节+知识库表格：国防/军事思想/信息化战争/军事高技术/国际战略/国防动员/人民防空/武装力量

### 13 文生图 API 接入
- title: 文生图 API 接入
- type: content / role: supporting / rhythm: valley
- layout: 左标题+右内容
- visual: L3: 模型图标列表
- visual_role: evidence
- density: 字数约250 / 留白约15%
- anti_pattern: 禁止等宽五卡横排
- description: 5个模型对比表格：Pollinations/豆包/通义万相/Stability/DALL-E，含费用+CORS+接入函数

### 14 演示页生成与导出
- title: 演示页生成与导出
- type: content / role: supporting / rhythm: valley
- layout: 非对称双栏
- visual: L2: 导出方式对比
- visual_role: evidence
- density: 字数约180 / 留白约25%
- anti_pattern: 禁止50:50等分
- description: 左栏：演示页七步+四种版式；右栏：双通道导出（python-pptx/可编辑HTML）

### 15 第四章 · 部署上线
- title: 第四章 · 部署上线
- type: section / role: transition / rhythm: transition
- layout: 全屏视觉+大标题
- visual: L1: 军绿渐变背景
- visual_role: atmosphere
- density: 字数约20 / 留白约60%
- anti_pattern: 禁止四卡片预览
- description: 章节扉页

### 16 GitHub 仓库部署
- title: GitHub 仓库部署
- type: content / role: supporting / rhythm: valley
- layout: 左标题+右内容
- visual: L3: Git命令代码块
- visual_role: evidence
- density: 字数约200 / 留白约20%
- anti_pattern: 禁止等宽卡片横排
- description: 左栏：PAT生成+创建仓库步骤；右栏：git init/commit/push命令代码块

### 17 GitHub Pages 在线
- title: GitHub Pages 在线部署
- type: content / role: hero / rhythm: peak
- layout: 左大图+右侧文字
- visual: L1: 在线网站截图（占左60%）
- visual_role: anchor
- density: 字数约150 / 图1张 / 留白约25%
- anti_pattern: 禁止50:50等分；禁止产品图缩小
- description: 左栏大图：在线网站截图/URL；右栏文字：API启用Pages→等待构建→访问地址

### 18 CORS 代理部署
- title: CORS 代理部署
- type: content / role: supporting / rhythm: valley
- layout: 非对称双栏
- visual: L2: 代理路由映射表
- visual_role: evidence
- density: 字数约200 / 留白约20%
- anti_pattern: 禁止50:50等分
- description: 左栏：Vercel Edge Function部署步骤；右栏：Cloudflare Workers方案+路由映射表

### 19 第五章 · 项目成果
- title: 第五章 · 项目成果
- type: section / role: transition / rhythm: transition
- layout: 全屏视觉+大标题
- visual: L1: 军绿渐变背景
- visual_role: atmosphere
- density: 字数约20 / 留白约60%
- anti_pattern: 禁止四卡片预览
- description: 章节扉页

### 20 感谢与在线地址
- title: 感谢与在线地址
- type: ending / role: hero / rhythm: peak
- layout: 全屏视觉+大标题
- visual: L1: 军绿渐变背景+金星Logo
- visual_role: atmosphere
- density: 字数约60 / 留白约50%
- anti_pattern: 禁止标题栏+装饰小图
- description: 结束页：感谢+在线地址+仓库地址+日期
