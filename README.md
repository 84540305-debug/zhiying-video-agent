# 知影 ZhiYing · AI 视频成片 Agent（B/S 架构原型）

[![在线体验](https://img.shields.io/badge/在线体验-GitHub_Pages-2e7d4f?style=for-the-badge&logo=github&logoColor=white)](https://84540305-debug.github.io/zhiying-video-agent/)
[![代码仓库](https://img.shields.io/badge/代码仓库-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/84540305-debug/zhiying-video-agent)
[![License](https://img.shields.io/badge/License-MIT-2e7d4f?style=for-the-badge)](LICENSE)

> 🌐 **在线体验**：https://84540305-debug.github.io/zhiying-video-agent/
> 📦 **源码仓库**：https://github.com/84540305-debug/zhiying-video-agent

一句话，从脚本到成片。浏览器即开即用，无需安装。

## 一、运行方式

- **在线体验**（推荐）：直接打开 https://84540305-debug.github.io/zhiying-video-agent/ ，无需安装任何环境。
- **本地运行**：用 Chrome / Edge 打开 `index.html` 即可（本地单文件应用，零依赖、零构建）。
- **克隆源码**：`git clone https://github.com/84540305-debug/zhiying-video-agent.git`

> 录屏导出功能需在浏览器中允许屏幕捕获；旁白语音使用浏览器内置 TTS（中文女声）。

## 二、功能对照（需求 → 实现）

| 需求 | 实现 |
|---|---|
| B/S 模式 | 纯浏览器端单页应用，服务端仅在未来对接 AI API 时需要 |
| 两种创作模式 | 首页两张模式卡片：**图片轮播模式**（文生图分镜）、**HTML 视频模式**（网页动画分镜） |
| 创作流程 | 提示词 → **① 生成脚本 → ② 生成大纲 → ③ 拆分分镜 → ④ 生成分镜画面 → ⑤ 生成分镜声音 → ⑥ 预览&修改 → ⑦ 录屏输出**（严格七步，对话区内置步骤进度追踪器，每步产出独立可见产物） |
| 首页 | 品牌 Logo、名称（知影 ZhiYing）、两张创作模式卡片，点击进入创作页 |
| 三栏创作页 | 左：历史项目列表（localStorage 持久化）；中：视频预览区；右：AI 对话交互 |
| 预览区结构 | 上方画面预览（16:9 舞台），下方横向分镜小卡片，点击卡片即播放对应分镜 |
| 工具栏 | 播放/暂停、**字幕开关**、背景音乐切换、**全屏**、**录屏导出视频** |

## 三、技术实现

- **视觉风格**：《大学生军事理论课》主题 —— 军绿清新浅色系（主色 `#2e7d4f` 军绿 / `#5aa87a` 浅军绿渐变，浅绿白背景 `#f3f7f3`），金色五角星 Logo，徽章/按钮/进度条全套军绿配色；视频预览舞台与字幕条保留深色以突出画面
- **图片轮播模式**：程序化文生图引擎（Canvas，按分镜文本哈希做种子确定性生成配色/构图/粒子画面）+ Ken Burns 推拉摇移动效轮播
- **HTML 视频模式**：网页动画引擎，5 套动效模板（极光渐变 / 粒子星河 / 轨道环绕 / 数据律动 / 打字机），CSS 动画矢量渲染
- **演示页生成模式**：AI 自动生成 5-8 页演示稿大纲 + 多页面拆分 + 文生图配图，支持 **python-pptx 通道**（下载含完整页面数据的 .py 脚本，本地 `pip install python-pptx` 后运行即生成 .pptx）与 **可编辑 HTML 通道**（单文件 HTML，可在 Gamma / Canva 可画导入继续精修）；预览区 16:9 幻灯片画布 + 工具栏翻页 + 页面缩略图切换
- **旁白语音**：Web Speech API（`speechSynthesis`），逐镜随播随读，时长按语速智能匹配
- **背景音乐**：WebAudio 程序化生成 3 种风格（清新钢琴 / 舒缓氛围 / 节奏律动）
- **录屏导出**：`getDisplayMedia` 屏幕捕获 + BGM 音轨混流 + `MediaRecorder` 编码，自动下载 `.webm`
- **历史项目**：localStorage 持久化；分镜画面仅存"种子+配色"，演示稿配图剥离 dataURL，加载时确定性重生成

## 四、创作流水线（严格七步）

对话区顶部会展示一个「创作流水线 · 7 步」追踪器，跟随进度实时高亮「进行中／已完成」。

| 步骤 | 行为 | 对话区产物 |
|---|---|---|
| ① 生成脚本 | `generateScript()` 生成五段式完整文稿 | 脚本全文（等宽代码块） |
| ② 生成大纲 | `generateOutline()` 提炼逐段核心要点 + 视觉提示 | 大纲表格 |
| ③ 拆分分镜 | `splitStoryboard()` 分配时长/种子/配色/动效模板 | 分镜列表（含时长） |
| ④ 生成分镜画面 | 文生图引擎（图片模式）或网页动画引擎（HTML模式）逐镜生成 | 进度卡 1/N |
| ⑤ 生成分镜声音 | 旁白 TTS + 背景音乐匹配 | 声音卡（旁白/配乐说明） |
| ⑥ 预览 & 修改 | 分镜卡片点击预览单镜；对话指令「重新生成第N个分镜」「重新生成」「换背景音乐」 | 预览&修改面板 |
| ⑦ 录屏输出 | 点击工具栏高亮「录屏导出」→ 自动播放 → 下载 .webm | 操作引导 |

## 五、文件上传（📎 附件创作）

点击输入框左侧 📎 按钮打开「上传文件」弹窗，支持**点击选择 + 拖拽上传**，单文件 ≤10MB、单次 ≤8 个：

| 附件类型 | 格式 | 在流水线中的作用 |
|---|---|---|
| 脚本文稿 | .txt / .md / .csv / .json / .srt | 内容自动读取（≤2万字），注入**第①步脚本生成**：附件语句足够时直接采用真实文稿组织五段式脚本 |
| 图片素材 | .png / .jpg / .jpeg / .gif / .webp | 弹窗内缩略图预览；**图片轮播模式**下按顺序填充前 N 个分镜画面（`scene.imgUrl`），不足部分仍由文生图生成；HTML 视频模式下仅作参考 |
| 参考文档 | .doc / .docx / .pdf / .ppt 等 | 记录为参考资料随项目保存（文档正文解析需在工程化版本接入文档解析 API） |

- 附件在输入框上方以**附件托盘**（缩略图/图标 + 文件名 + 移除按钮）暂存，随提示词一并发送
- 用户消息中会显示附件摘要卡片；仅上传附件不输入文字也可创作（默认主题："根据上传的文件内容创作一支知识短片"）
- `重新生成第N个分镜` 会放弃该镜上传素材、改回 AI 生成画面
- 持久化时剥离图片 dataURL 以防 localStorage 超限，历史项目重新加载后画面回退为确定性重生成

## 六、AI 对话指令

- 任意描述文字 → 触发完整七步创作流水线
- `重新生成` / `修改脚本` / `换一版` → 同一提示词重走七步
- `重新生成第2个分镜` / `修改第2个分镜` / `重做第2个分镜` → 只重做该镜的画面与动效
- `换背景音乐` → 轮换配乐风格

## 七、真实 AI API 接入点（工程化升级路线）

> ✅ **已接入**：文生图 API 使用 **Pollinations.ai**（免费、无需 key、自动出图）；历史项目封面与封面图按需调用，失败回退到 Canvas 程序化生成（详见下方"文生图 API"行）。

当前原型用本地确定性引擎模拟 AI 能力，架构已预留替换点，均为**单函数替换**：

| 模块 | 当前（演示通道） | 接入真实 API 时替换 |
|---|---|---|
| 脚本生成 | `generateScript()` 模板引擎 + `MILITARY_KB` 军事知识库 | LLM API（如 GPT / 通义 / 混元），Prompt 要求输出 JSON 结构 |
| 大纲生成 | `generateOutline()` 从脚本提炼 | 同 LLM API，单独返回大纲 JSON |
| **文生图** | `genImageViaAPI()` → **Pollinations.ai**（已接入，渐进式加载，超时回退 Canvas） | 把 `_callPollinations()` 替换为其他文生图 API（Stable Diffusion / DALL·E / 混元生图） |
| 演示稿配图 | `renderSlideImage()` Canvas 程序化 | 同上，API 出图 + 回退 |
| 历史项目封面 | `loadProjectCover()` 异步调用 `genImageViaAPI()` | 已自动接入，prompt 智能增强（军事关键词→英文短句） |
| 网页动画 | `buildHtmlScene()` 本地动效模板 | LLM 生成 HTML/CSS 动画代码片段（沙箱 iframe 渲染） |
| 旁白语音 | 浏览器 `speechSynthesis` | TTS API（如 Edge-TTS / 火山 / 腾讯云），预合成音频文件 |
| 背景音乐 | WebAudio 程序化生成 | 音乐库 API 或版权曲库标签匹配 |
| 文档解析 | `kindOf()` 仅记录 .doc/.pdf 文件名 | 文档解析 API（如 TextIn / 腾讯云文档识别），抽取正文后走文稿注入通道 |

### 文生图 API 接入详情

**当前默认通道**：Pollinations.ai（https://image.pollinations.ai）
- ✅ 完全免费，无需 API key
- ✅ 支持中英文 prompt（内置 `enhancePrompt()` 把中文军事术语翻译成适合文生图的英文短句）
- ✅ 渐进式加载：API 出图期间显示程序化占位图，1-3 秒后被真实图替换
- ✅ 12 秒超时回退：网络问题/限流时自动回退到 Canvas 程序化生成
- 缺点：偶发限流；中文 prompt 直出质量一般

**切换到其他文生图 API**（Stable Diffusion / DALL·E / 文心一格 / 混元）：
只需替换 `_callPollinations()` 函数，返回 `Promise<dataURL>` 即可。函数签名：
```js
async function _callPollinations(prompt, w, h){
  // 调用任意文生图 API，返回 data:image/...;base64,xxx
  // 出错时 throw new Error()
}
```

### B/S 生产化建议

前端保留本套 UI 与播放器，新增 Node/Python 后端负责 AI 编排（任务队列 + SSE 进度推送），导出改用服务端 Puppeteer/FFmpeg 渲染，避免依赖浏览器录屏。文生图建议走服务端代理（避免前端 CORS 与限流问题）。
