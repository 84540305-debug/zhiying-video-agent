# -*- coding: utf-8 -*-
"""知影 ZhiYing · 搭建流程文档生成器"""
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
import os

doc = Document()

# ============ 全局样式 ============
style = doc.styles['Normal']
style.font.name = '微软雅黑'
style.font.size = Pt(11)
style._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
style.paragraph_format.space_after = Pt(6)
style.paragraph_format.line_spacing = 1.5

# 标题样式
for i, sz in [(1,18),(2,15),(3,13),(4,12)]:
    hs = doc.styles[f'Heading {i}']
    hs.font.name = '微软雅黑'
    hs.font.size = Pt(sz)
    hs.font.color.rgb = RGBColor(0x2e, 0x7d, 0x4f)
    hs._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')

GREEN = RGBColor(0x2e, 0x7d, 0x4f)
DARK = RGBColor(0x1c, 0x32, 0x26)
MUTED = RGBColor(0x54, 0x70, 0x5e)

def add_code(text):
    """添加代码块"""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.2
    run = p.add_run(text)
    run.font.name = 'Consolas'
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x2e, 0x7d, 0x4f)
    # 背景色
    shading = p._element.get_or_add_pPr()
    bg = shading.makeelement(qn('w:shd'), {qn('w:val'):'clear', qn('w:fill'):'f0f7f3'})
    shading.append(bg)
    return p

def add_table(headers, rows):
    """添加表格"""
    t = doc.add_table(rows=1+len(rows), cols=len(headers))
    t.style = 'Light Grid Accent 1'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        cell = t.rows[0].cells[i]
        cell.text = h
        for p in cell.paragraphs:
            for r in p.runs:
                r.font.bold = True
                r.font.size = Pt(10)
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = t.rows[ri+1].cells[ci]
            cell.text = str(val)
            for p in cell.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(10)
    doc.add_paragraph()  # 间距
    return t

def p(text, bold=False, color=None, size=11):
    """添加段落"""
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.bold = bold
    if color: run.font.color.rgb = color
    if size: run.font.size = Pt(size)
    return para

# ============ 封面 ============
for _ in range(6): doc.add_paragraph()
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run('知影 ZhiYing')
run.font.size = Pt(36)
run.font.bold = True
run.font.color.rgb = GREEN

sub = doc.add_paragraph()
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = sub.add_run('大学生军事理论课 AI 视频成片 Agent')
run.font.size = Pt(16)
run.font.color.rgb = MUTED

sub2 = doc.add_paragraph()
sub2.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = sub2.add_run('搭建流程 · 技术文档 · 代码说明')
run.font.size = Pt(13)
run.font.color.rgb = MUTED

for _ in range(2): doc.add_paragraph()
info = doc.add_paragraph()
info.alignment = WD_ALIGN_PARAGRAPH.CENTER
for line, c in [('B/S 架构 · 单文件浏览器应用 · 零依赖', MUTED),
                ('三种创作模式 + 七步流水线 + 文生图 API', MUTED),
                ('版本 v2.7 · 2026-09-10', MUTED)]:
    r = info.add_run(line + '\n')
    r.font.size = Pt(11)
    r.font.color.rgb = c

doc.add_page_break()

# ============ 目录 ============
doc.add_heading('目 录', 1)
toc_items = [
    '一、项目概述',
    '二、技术架构',
    '三、功能清单',
    '四、本地运行',
    '五、功能详解',
    '  5.1 首页与模式选择',
    '  5.2 七步创作流水线',
    '  5.3 文件上传',
    '  5.4 军事理论课知识库',
    '  5.5 文生图 API 接入',
    '  5.6 演示页生成与导出',
    '六、代码结构',
    '七、GitHub 仓库部署',
    '八、GitHub Pages 在线部署',
    '九、文生图模型切换',
    '十、CORS 代理部署',
    '十一、维护与更新',
    '附录、关键代码与 API 速查',
]
for item in toc_items:
    para = doc.add_paragraph(item)
    para.paragraph_format.space_after = Pt(2)
    para.paragraph_format.line_spacing = 1.3
    for r in para.runs:
        r.font.size = Pt(11)

doc.add_page_break()

# ============ 一、项目概述 ============
doc.add_heading('一、项目概述', 1)

p('知影 ZhiYing 是一款面向大学生军事理论课的 AI 视频成片 Agent，采用 B/S 架构，浏览器即开即用，无需安装。', size=11)

doc.add_heading('1.1 核心能力', 2)
add_table(['能力', '说明'], [
    ['三种创作模式', '图片轮播（文生图分镜）/ HTML 视频（网页动画分镜）/ 演示页生成（PPT）'],
    ['七步流水线', '生成脚本 → 生成大纲 → 拆分分镜 → 生成画面 → 生成声音 → 预览修改 → 导出'],
    ['文生图 API', 'Pollinations.ai（免费免key）+ 可切换豆包/通义万相/Stability/DALL·E'],
    ['军事知识库', '8 大章节专业教学内容（国防/军事思想/信息化战争/军事高技术/国际战略/国防动员/人民防空/武装力量）'],
    ['文件上传', '文稿注入脚本生成 / 图片作分镜素材 / 文档作参考资料'],
    ['双通道导出', 'python-pptx 脚本（.pptx）/ 可编辑 HTML（Gamma/Canva 可画兼容）'],
])

doc.add_heading('1.2 在线访问', 2)
add_table(['类型', '地址'], [
    ['🌐 在线网站', 'https://84540305-debug.github.io/zhiying-video-agent/'],
    ['📦 代码仓库', 'https://github.com/84540305-debug/zhiying-video-agent'],
    ['本地文件', 'D:\\澳门科技大学 上课\\进阶教育技术\\跑项目\\视频制作Agent\\index.html'],
])

doc.add_page_break()

# ============ 二、技术架构 ============
doc.add_heading('二、技术架构', 1)

doc.add_heading('2.1 技术栈', 2)
add_table(['层', '技术', '说明'], [
    ['前端', '原生 HTML + CSS + JavaScript', '单文件，零依赖，零构建'],
    ['文生图', 'Pollinations.ai API', '免费免key，渐进式加载（Canvas占位→API真实图替换）'],
    ['语音合成', 'Web Speech API (speechSynthesis)', '浏览器内置中文 TTS，逐镜随播'],
    ['背景音乐', 'WebAudio API', '程序化生成 3 种风格（清新钢琴/舒缓氛围/节奏律动）'],
    ['录屏导出', 'getDisplayMedia + MediaRecorder', '屏幕捕获 + BGM 混流 → .webm 下载'],
    ['持久化', 'localStorage', '历史项目存储（剥离图片 dataURL 防超限）'],
    ['版本控制', 'Git + GitHub', 'main 分支，commit 历史完整'],
    ['在线托管', 'GitHub Pages', 'push 后自动重建，约 30 秒生效'],
])

doc.add_heading('2.2 架构图（文字描述）', 2)
p('首页（品牌 Logo + 三张模式卡片）')
p('  ↓ 点击卡片')
p('创作页（三栏布局）')
p('  左栏：历史项目列表（封面缩略图 + 标题 + 时间）')
p('  中栏：视频预览区（上方画面预览 + 下方分镜卡片列表）+ 工具栏（播放/字幕/全屏/录屏/翻页/导出）')
p('  右栏：AI 对话界面（七步流水线追踪器 + 对话气泡 + 输入框 + 文件上传）')

doc.add_page_break()

# ============ 三、功能清单 ============
doc.add_heading('三、功能清单', 1)

add_table(['功能模块', '实现状态', '说明'], [
    ['首页模式卡片', '✅', '图片轮播 / HTML 视频 / 演示页生成 三种模式'],
    ['七步流水线', '✅', '严格按步骤执行，对话区步骤追踪器实时高亮'],
    ['军事知识库', '✅', '8 大章节，关键词匹配自动路由到专业内容'],
    ['军事配色', '✅', '军绿迷彩/战旗红金/夜战深蓝/钢铁灰蓝 四套'],
    ['文生图 API', '✅', 'Pollinations.ai（默认）+ 5 模型可切换'],
    ['文件上传', '✅', '📎 弹窗，拖拽+点选，文稿/图片/文档三通道'],
    ['演示页生成', '✅', '七步流水线，多版式幻灯片，双通道导出'],
    ['历史项目', '✅', 'localStorage 持久化，封面缩略图异步加载'],
    ['录屏导出', '✅', 'getDisplayMedia + MediaRecorder → .webm'],
    ['PPTX 导出', '✅', '生成 python-pptx 脚本，本地运行产出 .pptx'],
    ['HTML 导出', '✅', '单文件 HTML，Gamma/Canva 可画兼容'],
    ['文生图设置', '✅', '⚙️ 弹窗，模型选择 + API Key 输入 + 代理地址'],
    ['CORS 代理', '✅', 'Vercel Edge Function + Cloudflare Workers 双方案'],
    ['GitHub Pages', '✅', '在线访问，push 后自动重建'],
])

doc.add_page_break()

# ============ 四、本地运行 ============
doc.add_heading('四、本地运行', 1)

doc.add_heading('4.1 直接打开', 2)
p('用 Chrome / Edge 打开 index.html 即可（本地单文件应用，零依赖、零构建）。')

doc.add_heading('4.2 克隆仓库', 2)
add_code('git clone https://github.com/84540305-debug/zhiying-video-agent.git\ncd zhiying-video-agent\n# 用浏览器打开 index.html')

doc.add_heading('4.3 注意事项', 2)
p('• 录屏导出功能需在浏览器中允许屏幕捕获权限')
p('• 旁白语音使用浏览器内置 TTS（中文女声）')
p('• 文生图 API 调用需要网络连接（Pollinations.ai 免费免key）')
p('• 首次使用文件上传功能时，浏览器可能需要用户交互才能触发 FileReader')

doc.add_page_break()

# ============ 五、功能详解 ============
doc.add_heading('五、功能详解', 1)

doc.add_heading('5.1 首页与模式选择', 2)
p('首页展示品牌 Logo（金色五角星）、名称（知影 ZhiYing）和三张创作模式卡片：')
add_table(['模式', '说明', '入口函数'], [
    ['图片轮播模式', '分镜画面由文生图 AI 生成静态图片，Ken Burns 镜头动效轮播', "enterEditor('image')"],
    ['HTML 视频模式', '分镜画面由 AI 生成网页动画（极光/粒子/轨道/数据律动/打字机）', "enterEditor('html')"],
    ['演示页生成模式', 'AI 生成 5-8 页演示稿，支持导出 .pptx 和可编辑 HTML', "enterEditor('ppt')"],
])

doc.add_heading('5.2 七步创作流水线', 2)
p('用户输入提示词后，对话区顶部生成「创作流水线·7步」追踪器，随进度实时高亮：')
add_table(['步骤', '行为', '对话区产物', '核心函数'], [
    ['①生成脚本', '五段式脚本文稿（起承转合升华）', '脚本全文（等宽代码块）', 'generateScript()'],
    ['②生成大纲', '逐段核心要点 + 视觉提示', '大纲表格', 'generateOutline()'],
    ['③拆分分镜', '时长/种子/配色/动效模板分配', '分镜列表', 'splitStoryboard()'],
    ['④生成画面', '文生图 API 逐镜生成（渐进式加载）', '逐镜进度 1/N', 'refreshImgWithAPI()'],
    ['⑤生成声音', '旁白 TTS + 背景音乐匹配', '声音说明卡', 'speak() + BGM.start()'],
    ['⑥预览修改', '分镜卡片点击预览/播放全部/换配乐/重新生成', '预览&修改面板', 'playScene() / playAll()'],
    ['⑦录屏导出', '录屏按钮高亮，引导用户导出 .webm', '操作引导', 'toggleRecord()'],
])
p('三级内容路由：上传文稿 > 军事知识库 > 通用模板')

doc.add_heading('5.3 文件上传', 2)
p('点击输入框左侧 📎 按钮打开上传弹窗（点击选择 + 拖拽上传，单文件 ≤10MB、单次 ≤8 个）：')
add_table(['附件类型', '格式', '流水线作用'], [
    ['脚本文稿', '.txt/.md/.csv/.json/.srt', '内容注入 generateScript()，语句足够时直接用真实文稿组织五段式脚本'],
    ['图片素材', '.png/.jpg/.jpeg/.gif/.webp', '图片轮播模式下按顺序填充前 N 个分镜画面 scene.imgUrl'],
    ['参考文档', '.doc/.docx/.pdf/.ppt 等', '记录为参考资料（文档解析 API 预留）'],
])

doc.add_heading('5.4 军事理论课知识库', 2)
p('MILITARY_KB 常量包含 8 大章节专业知识库，每章 5 段教学级旁白文案：')
add_table(['章节 ID', '主题', '关键词示例'], [
    ['defense', '中国国防', '国防、国防建设、武装力量、边防海防'],
    ['thought', '军事思想', '孙子兵法、毛泽东军事思想、战争观'],
    ['infowar', '信息化战争', '信息战、网络战、制信息权、联合作战'],
    ['hitech', '军事高技术', '导弹、无人机、隐身、激光、北斗'],
    ['strategy', '国际战略环境', '地缘政治、大国关系、周边安全'],
    ['mobilize', '国防动员', '战争动员、民兵、预备役、经济动员'],
    ['airdef', '人民防空', '防空警报、防空洞、疏散、三防'],
    ['forces', '武装力量', '解放军、五大战区、武警、军种'],
])
p('matchMilitaryTopic(prompt) 关键词匹配 → 命中时脚本/演示稿自动使用专业内容。')
p('四套军事专属配色：army（军绿迷彩）/ flag（战旗红金）/ night（夜战深蓝）/ steel（钢铁灰蓝）。')

doc.add_heading('5.5 文生图 API 接入', 2)
p('IMG_CONFIG（localStorage 持久化）存储模型选择与 API 密钥。_callImageAPI 路由函数按 model 分发：')
add_table(['模型', '函数', '费用', 'CORS', '备注'], [
    ['Pollinations.ai', '_callPollinations()', '免费', '✅', '默认，免key'],
    ['豆包/火山引擎', '_callDoubao()', '按量', '❌ 需代理', '异步任务模式（POST→轮询60秒）'],
    ['通义万相', '_callWanx()', '按量', '❌ 需代理', '异步轮询（POST→30次轮询）'],
    ['Stability AI', '_callStability()', '按量', '✅', 'FormData 提交'],
    ['OpenAI DALL·E 3', '_callDallE()', '按量', '✅', 'b64_json 返回'],
])
p('enhancePrompt(zh) 函数内置 23 个军事关键词中英翻译映射，提升出图质量。')
p('渐进式加载：先程序化 Canvas 占位（立即可见）→ 1-3秒后 API 真实图淡入替换 → 失败静默保留占位。')
p('并发控制：_apiEnqueue 队列，最多同时 2 个请求，间隔 1.2 秒，避免限流。')

doc.add_heading('5.6 演示页生成与导出', 2)
p('演示页模式（mode=ppt）复用七步流水线，按教学章节结构生成 5-8 页：')
p('封面 → 引入 → 核心概念 → 关键特征 → 应用实践 → 案例分析 → 总结')
p('四种版式：title（居中标题页）/ content（项目符号页）/ two-col（图文双栏）/ summary（结语总结）')
p('导出方式：')
add_table(['导出', '函数', '产物'], [
    ['导出 PPTX', 'exportPptx()', 'python-pptx 生成脚本（.py），本地运行产出 .pptx'],
    ['导出可编辑 HTML', 'exportSlidesHtml()', '单文件 HTML，可在 Gamma/Canva 可画导入'],
])

doc.add_page_break()

# ============ 六、代码结构 ============
doc.add_heading('六、代码结构', 1)

p('整个应用为单文件 index.html（约 2400 行），结构如下：')
add_code("""视频制作Agent/
├── index.html          # 主应用（HTML + CSS + JS 单文件）
├── README.md           # 设计说明与 API 接入指南
├── LICENSE             # MIT 开源协议
├── .gitignore          # Git 忽略规则
├── api/
│   └── proxy.js        # Vercel Edge Function CORS 代理
└── cors-proxy/
    └── worker.js       # Cloudflare Workers CORS 代理""")

doc.add_heading('6.1 index.html 内部结构', 2)
add_table(['区域', '行号范围', '内容'], [
    ['CSS 样式', '1-480', '军绿主题、三栏布局、幻灯片画布、弹窗、动画'],
    ['首页 HTML', '490-460', 'Logo、三张模式卡片、页脚'],
    ['编辑页 HTML', '460-640', '左栏历史项目、中栏预览+工具栏+分镜列表、右栏对话'],
    ['弹窗 HTML', '640-720', '上传弹窗、文生图设置弹窗'],
    ['JS：工具函数', '580-700', '$()、sleep()、hashStr()、mulberry32()、esc()、fmtTime()'],
    ['JS：调色板', '700-730', 'PALETTES（4 军事 + 6 通用）、pickPalette()、palOf()'],
    ['JS：文生图 API', '730-930', '_callPollinations/_callDoubao/_callWanx/_callStability/_callDallE + 路由 + 并发队列'],
    ['JS：文生图引擎', '799-870', 'renderSceneImage() Canvas 程序化生成 + imgFor/thumbFor'],
    ['JS：HTML 动画引擎', '880-980', 'HTPL 5 套模板、buildHtmlScene()'],
    ['JS：军事知识库', '1010-1080', 'MILITARY_KB 8 大章节、matchMilitaryTopic()'],
    ['JS：脚本生成', '1080-1120', 'generateScript()、vGeneric()、generateOutline()、splitStoryboard()'],
    ['JS：BGM 引擎', '1120-1200', 'BGM 对象、WebAudio 程序化生成 3 种风格'],
    ['JS：播放/录屏', '1200-1420', 'playScene()、playAll()、toggleRecord()、MediaRecorder'],
    ['JS：历史项目', '1420-1500', 'persist()、saveProject()、renderHistory()、loadProject()'],
    ['JS：七步流水线', '1500-1620', 'runPipeline()（视频）、runPptPipeline()（演示页）'],
    ['JS：演示页', '1620-2100', 'buildSlideHTML()、renderSlide()、generatePptScript()、exportPptx()、exportSlidesHtml()'],
    ['JS：文件上传', '1620-1700', 'openUpload()、addFiles()、confirmUpload()、attachSummary()'],
    ['JS：初始化', '2100-2400', 'DOMContentLoaded、事件绑定、mousemove 光晕'],
])

doc.add_page_break()

# ============ 七、GitHub 仓库部署 ============
doc.add_heading('七、GitHub 仓库部署', 1)

doc.add_heading('7.1 前置条件', 2)
p('• 安装 Git（https://git-scm.com）')
p('• 注册 GitHub 账号（https://github.com）')
p('• 生成 Personal Access Token（PAT）')

doc.add_heading('7.2 生成 PAT', 2)
p('1. 登录 GitHub → https://github.com/settings/tokens')
p('2. Generate new token (classic)')
p('3. Note: zhiying-push，Expiration: 90 days')
p('4. Scopes: 勾选 repo（第一个大项）')
p('5. Generate token → 复制 ghp_ 开头的 token')

doc.add_heading('7.3 本地初始化与提交', 2)
add_code('''cd "D:\\澳门科技大学 上课\\进阶教育技术\\跑项目\\视频制作Agent"
git init -b main
git config user.name "你的用户名"
git config user.email "你的邮箱"
echo "*.log\\nnode_modules/\\n.DS_Store" > .gitignore
git add -A
git commit -m "知影 ZhiYing 初始版本"

# 添加远程仓库
git remote add origin https://github.com/用户名/zhiying-video-agent.git

# 用 PAT 推送（PAT 不会持久化到配置）
export GIT_TERMINAL_PROMPT=0
git -c credential.helper= push \\
  "https://用户名:ghp_xxx@github.com/用户名/zhiying-video-agent.git" \\
  main:main''')

doc.add_heading('7.4 创建远程仓库', 2)
p('方式 A（API 自动创建，需 Administration 权限的 PAT）：')
add_code('''curl -X POST -H "Authorization: token ghp_xxx" \\
  -H "Accept: application/vnd.github+json" \\
  https://api.github.com/user/repos \\
  -d '{"name":"zhiying-video-agent","private":false,"auto_init":false}' ''')
p('方式 B（网页手动创建）：')
p('1. 打开 https://github.com/new')
p('2. Repository name: zhiying-video-agent')
p('3. 选 Public')
p('4. 不勾选 README/gitignore/license（保持空仓库）')
p('5. Create repository')

doc.add_page_break()

# ============ 八、GitHub Pages 在线部署 ============
doc.add_heading('八、GitHub Pages 在线部署', 1)

doc.add_heading('8.1 启用 Pages', 2)
p('用 PAT 调用 GitHub API 启用 Pages：')
add_code('''curl -X POST \\
  -H "Authorization: token ghp_xxx" \\
  -H "Accept: application/vnd.github+json" \\
  https://api.github.com/repos/用户名/zhiying-video-agent/pages \\
  -d '{"source":{"branch":"main","path":"/"}}' ''')

doc.add_heading('8.2 等待构建', 2)
p('Pages 首次构建约 30-60 秒。查询构建状态：')
add_code('''curl -H "Authorization: token ghp_xxx" \\
  https://api.github.com/repos/用户名/zhiying-video-agent/pages/builds/latest
# status: "built" 表示构建完成''')

doc.add_heading('8.3 访问地址', 2)
p('构建完成后，在线访问地址为：')
p('https://用户名.github.io/zhiying-video-agent/', bold=True, color=GREEN, size=13)

doc.add_heading('8.4 自动更新', 2)
p('之后每次 git push 到 main 分支，Pages 会自动重建（约 30-60 秒），在线网站自动同步更新。')

doc.add_page_break()

# ============ 九、文生图模型切换 ============
doc.add_heading('九、文生图模型切换', 1)

doc.add_heading('9.1 设置入口', 2)
p('首页右上角 ⚙️「文生图设置」按钮 → 弹窗选择模型 + 填入 API Key')

doc.add_heading('9.2 各模型配置', 2)
add_table(['模型', 'API Key 获取地址', '代理需求'], [
    ['Pollinations.ai', '无需 Key', '无需代理'],
    ['豆包/火山引擎', 'https://console.volcengine.com/ark', '需 CORS 代理'],
    ['通义万相', 'https://dashscope.console.aliyun.com', '需 CORS 代理'],
    ['Stability AI', 'https://platform.stability.ai', '无需代理'],
    ['OpenAI DALL·E 3', 'https://platform.openai.com/api-keys', '部分地区需代理'],
])

doc.add_heading('9.3 代码接入点', 2)
p('所有模型接入函数返回 Promise<dataURL>，替换 _callPollinations 即可切换：')
add_code('''// 路由函数
function _callImageAPI(prompt, w, h){
  switch(IMG_CONFIG.model){
    case 'doubao':    return _callDoubao(prompt, w, h);
    case 'wanx':      return _callWanx(prompt, w, h);
    case 'stability': return _callStability(prompt, w, h);
    case 'dalle':     return _callDallE(prompt, w, h);
    default:          return _callPollinations(prompt, w, h);
  }
}''')

doc.add_page_break()

# ============ 十、CORS 代理部署 ============
doc.add_heading('十、CORS 代理部署', 1)

p('豆包/通义万相 API 不支持浏览器 CORS，需部署后端代理。提供双方案：')

doc.add_heading('10.1 方案 A：Vercel Edge Function（推荐）', 2)
p('仓库内已含 api/proxy.js，Vercel 部署步骤：')
p('1. 打开 https://vercel.com/new → 用 GitHub 登录')
p('2. Import 仓库 zhiying-video-agent')
p('3. 保持默认配置 → Deploy')
p('4. 得到 https://zhiying-video-agent.vercel.app')
p('5. 代理地址填：https://zhiying-video-agent.vercel.app/api/proxy/doubao')

p('路由映射：')
add_table(['路径', '转发到'], [
    ['/api/proxy/doubao/*', 'https://ark.cn-beijing.volces.com/*'],
    ['/api/proxy/wanx/*', 'https://dashscope.aliyuncs.com/*'],
    ['/api/proxy/openai/*', 'https://api.openai.com/*'],
    ['/api/proxy/stability/*', 'https://api.stability.ai/*'],
])

doc.add_heading('10.2 方案 B：Cloudflare Workers', 2)
p('仓库内已含 cors-proxy/worker.js，部署步骤：')
p('1. 打开 https://workers.cloudflare.com → 注册/登录')
p('2. Create Worker')
p('3. 粘贴 worker.js 全部内容 → Deploy')
p('4. 得到 https://xxx.workers.dev')
p('5. 代理地址填：https://xxx.workers.dev/doubao')

doc.add_page_break()

# ============ 十一、维护与更新 ============
doc.add_heading('十一、维护与更新', 1)

doc.add_heading('11.1 修改代码后推送到线上', 2)
add_code('''cd "D:\\澳门科技大学 上课\\进阶教育技术\\跑项目\\视频制作Agent"
git add -A
git commit -m "更新说明"
export GIT_TERMINAL_PROMPT=0
git -c credential.helper= push \\
  "https://用户名:ghp_xxx@github.com/用户名/zhiying-video-agent.git" \\
  main:main
# Pages 约 30-60 秒后自动重建''')

doc.add_heading('11.2 安全提醒', 2)
p('• PAT（ghp_ 开头）用完即删：https://github.com/settings/tokens')
p('• API Key 仅存本地 localStorage，不上传服务器')
p('• commit 里的邮箱公开可见，可用 GitHub noreply 邮箱替代')

doc.add_heading('11.3 文件清单', 2)
add_table(['文件', '大小', '说明'], [
    ['index.html', '约 2400 行 / 130KB', '主应用（HTML+CSS+JS 单文件）'],
    ['README.md', '约 100 行 / 7KB', '设计说明与 API 接入指南'],
    ['LICENSE', 'MIT', '开源协议'],
    ['.gitignore', '标准模板', 'Git 忽略规则'],
    ['api/proxy.js', '约 80 行', 'Vercel Edge Function CORS 代理'],
    ['cors-proxy/worker.js', '约 90 行', 'Cloudflare Workers CORS 代理'],
])

doc.add_page_break()

# ============ 附录 ============
doc.add_heading('附录、关键代码与 API 速查', 1)

doc.add_heading('A.1 七步流水线函数对照', 2)
add_table(['步骤', '视频模式函数', '演示页函数'], [
    ['①脚本', 'generateScript()', 'generatePptScript()'],
    ['②大纲', 'generateOutline()', 'generatePptOutline()'],
    ['③拆分', 'splitStoryboard()', 'splitPptPages()'],
    ['④画面', 'refreshImgWithAPI()', 'fillPptPageContent() + refreshAllSlideImages()'],
    ['⑤声音', 'speak() + BGM.start()', '（演示页无声音）'],
    ['⑥预览', 'playScene() / playAll()', 'renderSlide() / slidePrev() / slideNext()'],
    ['⑦导出', 'toggleRecord()', 'exportPptx() / exportSlidesHtml()'],
])

doc.add_heading('A.2 Pollinations.ai API 速查', 2)
add_code('''# 文生图（GET 请求，返回图片）
https://image.pollinations.ai/prompt/{prompt}?width=960&height=540&nologo=true&seed=42

# JavaScript 调用
const url = 'https://image.pollinations.ai/prompt/'
  + encodeURIComponent(prompt)
  + '?width=' + w + '&height=' + h + '&nologo=true&seed=' + seed;
const res = await fetch(url);
const blob = await res.blob();
const dataURL = await blobToDataURL(blob);''')

doc.add_heading('A.3 豆包 API 速查', 2)
add_code('''# 文生图（异步任务模式）
POST https://ark.cn-beijing.volces.com/api/v3/contents/generations/tasks
Headers: Authorization: Bearer {ARK_API_KEY}
Body: {
  "model": "doubao-seedream-3-0-t2a-250415",
  "content": [{"type":"text","text":"prompt"}],
  "ratio": "16:9"
}
→ 返回 {id: "task_id"}
→ 轮询 GET /api/v3/contents/generations/tasks/{task_id}
→ status: "succeeded" → content.data[0].url

# 视频生成
POST 同上 endpoint
Body: {
  "model": "doubao-seedance-2-5-260628",
  "content": [text + image_url + video_url + audio_url],
  "generate_audio": true,
  "ratio": "16:9",
  "duration": 5,
  "watermark": false
}''')

doc.add_heading('A.4 enhancePrompt 军事关键词映射', 2)
add_table(['中文', '英文 prompt'], [
    ['国防', 'national defense, military, soldiers, flag'],
    ['军事思想', 'military strategy, ancient chinese warrior, classical'],
    ['信息化战争', 'futuristic military command center, holographic displays, soldiers'],
    ['网络战', 'cyber war, hacker, dark digital matrix'],
    ['军事高技术', 'advanced military technology, stealth fighter, laser'],
    ['无人机', 'military drone, MQ-9, surveillance'],
    ['隐身', 'stealth aircraft, dark sky, radar evading'],
    ['导弹', 'missile launch, dramatic, military hardware'],
    ['北斗', 'navigation satellite, china, earth orbit'],
    ['国防动员', 'national mobilization, citizens, military training'],
    ['人民防空', 'civil defense shelter, air raid warning, underground'],
    ['武装力量', 'armed forces, modern military hardware, flag'],
])

doc.add_heading('A.5 Git 常用命令速查', 2)
add_code('''# 初始化
git init -b main
git config user.name "用户名"
git config user.email "邮箱"

# 提交
git add -A
git commit -m "提交信息"

# 推送（用 PAT 认证，不持久化）
export GIT_TERMINAL_PROMPT=0
git -c credential.helper= push \\
  "https://用户名:ghp_xxx@github.com/用户名/repo.git" main:main

# 查看状态
git status
git log --oneline -5
git remote -v

# GitHub API（用 PAT）
curl -H "Authorization: token ghp_xxx" https://api.github.com/user
curl -X POST -H "Authorization: token ghp_xxx" \\
  https://api.github.com/user/repos -d '{"name":"repo","private":false}' ''')

# ============ 保存 ============
output = os.path.join(os.path.dirname(os.path.abspath(__file__)), '知影ZhiYing搭建文档.docx')
doc.save(output)
print(f'文档已生成：{output}')
print(f'文件大小：{os.path.getsize(output)} bytes')
