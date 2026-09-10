# -*- coding: utf-8 -*-
"""生成 PPT 配图：网页截图模拟 + 军事主题配图"""
from PIL import Image, ImageDraw, ImageFont
import os

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')
os.makedirs(ASSETS, exist_ok=True)

# 字体
def font(size):
    for p in ['C:/Windows/Fonts/msyh.ttc','C:/Windows/Fonts/simhei.ttf']:
        try: return ImageFont.truetype(p, size)
        except: pass
    return ImageFont.load_default()

GREEN = (46, 125, 79)
GREEN_L = (90, 168, 122)
GOLD = (255, 217, 122)
DARK = (28, 50, 38)
MUTED = (84, 112, 94)
WHITE = (255, 255, 255)
BG = (243, 247, 243)
LIGHT = (240, 247, 243)
RED = (224, 68, 56)

# ============ 1. 首页截图模拟 ============
def gen_homepage():
    w, h = 1280, 720
    img = Image.new('RGB', (w, h), BG)
    d = ImageDraw.Draw(img)
    # 顶部栏
    d.rectangle([0, 0, w, 70], fill=GREEN)
    # Logo 区
    d.text((50, 18), '★ 知影 ZhiYing', fill=GOLD, font=font(22))
    d.text((50, 48), 'AI VIDEO AGENT', fill=(200,230,210), font=font(11))
    d.text((900, 25), '⚙️ 文生图设置  B/S架构', fill=(200,230,210), font=font(13))
    # 三张模式卡片
    cards = [
        ('图片轮播模式', '文生图 AI 逐镜生成画面\nKen Burns 镜头动效', GREEN),
        ('HTML 视频模式', '极光/粒子/轨道/打字机\n矢量渲染丝滑流畅', GREEN_L),
        ('演示页生成模式', '导出 .pptx / 可编辑 HTML\npython-pptx 双通道', (60,140,100)),
    ]
    cw = 360; gap = 20; sx = (w - (cw*3 + gap*2)) // 2
    for i, (title, desc, color) in enumerate(cards):
        x = sx + i * (cw + gap)
        y = 120
        # 卡片
        d.rounded_rectangle([x, y, x+cw, y+420], radius=15, fill=WHITE, outline=color, width=2)
        # 图标区
        d.rounded_rectangle([x+20, y+20, x+cw-20, y+100], radius=10, fill=(*color,30) if len(color)==3 else color)
        # 图标
        icons = ['🖼', '✦', '🎖']
        d.text((x+cw//2-15, y+40), icons[i], fill=color, font=font(30))
        # 标题
        d.text((x+25, y+120), title, fill=DARK, font=font(20))
        # 描述
        for j, line in enumerate(desc.split('\n')):
            d.text((x+25, y+160+j*28), line, fill=MUTED, font=font(14))
        # 功能列表
        for j, feat in enumerate(['AI 文生图', '多引擎动画', '双通道导出']):
            d.ellipse([x+25, y+250+j*40, x+33, y+258+j*40], fill=color)
            d.text((x+42, y+245+j*40), feat, fill=MUTED, font=font(13))
        # 按钮
        d.rounded_rectangle([x+25, y+370, x+cw-25, y+405], radius=8, fill=color)
        d.text((x+cw//2-40, y+378), '开始创作 →', fill=WHITE, font=font(14))
    # 底部
    d.text((w//2-200, h-30), '知影 ZhiYing · 大学生军事理论课教学视频创作平台', fill=MUTED, font=font(12))
    img.save(os.path.join(ASSETS, 'homepage.png'))
    print('✅ homepage.png')

# ============ 2. 编辑器三栏布局截图模拟 ============
def gen_editor():
    w, h = 1280, 720
    img = Image.new('RGB', (w, h), (245,248,245))
    d = ImageDraw.Draw(img)
    # 左栏：历史项目
    d.rectangle([0, 0, 220, h], fill=(232,241,234))
    d.text((15, 15), '历史项目', fill=DARK, font=font(16))
    d.text((180, 15), '+ 新建', fill=GREEN, font=font(12))
    for i in range(4):
        y = 50 + i * 80
        # 封面缩略图
        d.rounded_rectangle([10, y, 74, y+36], radius=4, fill=GREEN if i==0 else (180,200,190))
        d.text((20, y+10), '🎖' if i==0 else '🖼', fill=WHITE, font=font(14))
        # 标题
        titles = ['信息化战争', '中国国防', '军事思想', '军事高技术']
        d.text((84, y+5), titles[i], fill=DARK, font=font(12))
        d.text((84, y+22), f'09-{10-i} · {5-i} 分镜', fill=MUTED, font=font(10))
    # 中栏：预览区
    d.rectangle([230, 10, w-340, 400], fill=(4,6,13))
    # 模拟画面
    d.text((w//2-100, 150), '🎬 分镜预览区', fill=(100,120,110), font=font(20))
    d.text((w//2-60, 200), '军事画面', fill=(150,170,160), font=font(16))
    # 工具栏
    d.rounded_rectangle([230, 410, w-340, 460], radius=8, fill=WHITE, outline=(200,210,205))
    tools = ['▶ 播放', '字幕', '🎵 音乐', '⛶ 全屏', '🔴 录屏']
    for i, t in enumerate(tools):
        d.text((240+i*90, 425), t, fill=MUTED, font=font(12))
    # 分镜列表
    d.text((240, 475), '分镜列表 · STORYBOARD', fill=MUTED, font=font(11))
    for i in range(5):
        x = 240 + i * 130
        d.rounded_rectangle([x, 495, x+120, 565], radius=8, fill=(11,17,34) if i>0 else GREEN)
        d.text((x+45, 520), f'{i+1}', fill=WHITE, font=font(16))
        d.text((x+5, 570), f'分镜{i+1}', fill=DARK, font=font(10))
    # 右栏：AI对话
    d.rectangle([w-330, 0, w, h], fill=(232,241,234))
    d.text((w-320, 15), '★ AI 创作 Agent', fill=GREEN, font=font(15))
    # 步骤追踪器
    steps = ['✅脚本', '✅大纲', '✅分镜', '✅画面', '✅声音', '▶预览', '⏳导出']
    for i, s in enumerate(steps):
        x = w-320 + (i%4)*72
        y = 50 + (i//4)*30
        d.rounded_rectangle([x, y, x+65, y+22], radius=4, fill=LIGHT if '✅' in s else (255,217,122) if '▶' in s else WHITE)
        d.text((x+3, y+4), s, fill=GREEN if '✅' in s else DARK, font=font(9))
    # 对话气泡
    d.rounded_rectangle([w-320, 140, w-20, 230], radius=10, fill=LIGHT)
    d.text((w-310, 150), 'Agent: 正在执行第6步\n预览&修改阶段...', fill=DARK, font=font(11))
    d.rounded_rectangle([w-250, 250, w-20, 300], radius=10, fill=GREEN)
    d.text((w-240, 260), '用户: 播放全部', fill=WHITE, font=font(11))
    # 输入框
    d.rounded_rectangle([w-320, h-60, w-70, h-25], radius=8, fill=WHITE, outline=(200,210,205))
    d.text((w-310, h-52), '输入创作指令...', fill=MUTED, font=font(12))
    d.rounded_rectangle([w-60, h-60, w-20, h-25], radius=8, fill=GREEN)
    d.text((w-52, h-50), '➤', fill=WHITE, font=font(16))
    img.save(os.path.join(ASSETS, 'editor.png'))
    print('✅ editor.png')

# ============ 3. 演示页幻灯片截图模拟 ============
def gen_slide():
    w, h = 1280, 720
    img = Image.new('RGB', (w, h), (10, 20, 16))
    d = ImageDraw.Draw(img)
    # 幻灯片画布
    sx, sy, sw, sh = 60, 40, w-120, h-120
    d.rounded_rectangle([sx, sy, sx+sw, sy+sh], radius=10, fill=WHITE)
    # 左侧装饰条
    d.rectangle([sx, sy, sx+8, sy+sh], fill=GREEN)
    # 标题
    d.text((sx+50, sy+30), '核心概念 · 定义阐释', fill=GREEN, font=font(18))
    d.text((sx+50, sy+60), '信息化战争的基本特征', fill=DARK, font=font(32))
    # 标题下划线
    d.rectangle([sx+50, sy+115, sx+110, sy+122], fill=GREEN)
    # 要点
    bullets = [
        '战场透明化：全维感知、实时共享、精确打击',
        '制信息权：谁掌握信息优势，谁就掌握战场主动',
        '指挥网络化：感知—决策—行动—评估闭环链路',
        '力量一体化：陆海空天电多维一体联合作战',
    ]
    for i, b in enumerate(bullets):
        y = sy+150 + i*55
        d.ellipse([sx+60, y+8, sx+72, y+20], fill=GREEN)
        d.text((sx+85, y), b, fill=DARK, font=font(16))
        if i < len(bullets)-1:
            d.line([sx+60, y+40, sx+sw-50, y+40], fill=(220,230,225), width=1)
    # 右上角导出按钮
    d.rounded_rectangle([w-250, 15, w-130, 40], radius=6, fill=(10,20,16))
    d.text((w-240, 18), '📥 导出 PPTX', fill=WHITE, font=font(12))
    d.rounded_rectangle([w-120, 15, w-20, 40], radius=6, fill=(10,20,16))
    d.text((w-110, 18), '📥 可编辑HTML', fill=WHITE, font=font(12))
    # 页码
    d.text((sx+sw-80, sy+sh-30), '4 / 7', fill=MUTED, font=font(12))
    img.save(os.path.join(ASSETS, 'slide.png'))
    print('✅ slide.png')

# ============ 4. 七步流水线示意图 ============
def gen_pipeline():
    w, h = 1200, 400
    img = Image.new('RGB', (w, h), WHITE)
    d = ImageDraw.Draw(img)
    steps = [
        ('①', '生成脚本', 'generateScript()'),
        ('②', '生成大纲', 'generateOutline()'),
        ('③', '拆分分镜', 'splitStoryboard()'),
        ('④', '生成画面', 'refreshImgWithAPI()'),
        ('⑤', '生成声音', 'speak()+BGM()'),
        ('⑥', '预览修改', 'playScene()'),
        ('⑦', '录屏导出', 'toggleRecord()'),
    ]
    bw = 140; gap = 18; sx = (w - (bw*7 + gap*6)) // 2
    for i, (num, title, func) in enumerate(steps):
        x = sx + i * (bw + gap); y = 80
        # 步骤卡片
        color = GREEN if i < 5 else GOLD if i == 5 else (200,200,200)
        d.rounded_rectangle([x, y, x+bw, y+200], radius=12, fill=LIGHT, outline=color, width=2)
        # 编号圆
        d.ellipse([x+bw//2-25, y+10, x+bw//2+25, y+60], fill=color)
        d.text((x+bw//2-12, y+18), num, fill=WHITE, font=font(20))
        # 标题
        d.text((x+15, y+75), title, fill=DARK, font=font(16))
        # 函数名
        d.text((x+10, y+110), func, fill=MUTED, font=font(11))
        # 状态
        states = ['✅', '✅', '✅', '✅', '✅', '▶', '⏳']
        d.text((x+bw//2-10, y+150), states[i], fill=color, font=font(20))
        # 箭头
        if i < 6:
            ax = x + bw + 2
            d.text((ax+2, y+90), '→', fill=MUTED, font=font(18))
    # 底部说明
    d.text((w//2-200, 310), '严格七步执行 · 每步完成后对话区步骤追踪器实时高亮', fill=MUTED, font=font(13))
    img.save(os.path.join(ASSETS, 'pipeline.png'))
    print('✅ pipeline.png')

# ============ 5. 军事知识库配图 ============
def gen_kb():
    w, h = 1200, 600
    img = Image.new('RGB', (w, h), WHITE)
    d = ImageDraw.Draw(img)
    # 巨型数字 "8"
    d.text((50, 50), '8', fill=GREEN, font=font(200))
    d.text((50, 280), '大章节', fill=MUTED, font=font(24))
    d.text((50, 320), '每章5段教学级旁白', fill=MUTED, font=font(14))
    # 右侧：8 个章节卡片
    chapters = [
        ('中国国防', '国防建设·武装力量·边防海防', GREEN),
        ('军事思想', '孙子兵法·毛泽东军事思想', (60,140,100)),
        ('信息化战争', '信息战·网络战·制信息权', (30,80,150)),
        ('军事高技术', '导弹·无人机·隐身·北斗', (100,110,130)),
        ('国际战略环境', '地缘政治·大国关系', (80,120,90)),
        ('国防动员', '战争动员·民兵·预备役', (60,140,80)),
        ('人民防空', '防空警报·防空洞·三防', (140,100,60)),
        ('武装力量', '解放军·五大战区·军种', (50,100,70)),
    ]
    for i, (title, kw, color) in enumerate(chapters):
        col = i % 4; row = i // 4
        x = 300 + col * 220; y = 50 + row * 250
        d.rounded_rectangle([x, y, x+200, y+220], radius=10, fill=LIGHT, outline=color, width=2)
        # 图标
        icons = ['🇨🇳','📜','💻','✈️','🌍','🏛','🚨','🎖']
        d.text((x+80, y+15), icons[i], fill=color, font=font(28))
        # 标题
        d.text((x+30, y+60), title, fill=DARK, font=font(16))
        # 关键词
        for j, line in enumerate(kw.split('·')):
            d.text((x+15, y+95+j*25), '• '+line, fill=MUTED, font=font(12))
        # 配色标签
        d.rounded_rectangle([x+10, y+185, x+190, y+210], radius=4, fill=color)
        pal_names = ['军绿迷彩','战旗红金','夜战深蓝','钢铁灰蓝','军绿迷彩','军绿迷彩','战旗红金','钢铁灰蓝']
        d.text((x+30, y+189), pal_names[i], fill=WHITE, font=font(10))
    img.save(os.path.join(ASSETS, 'knowledge_base.png'))
    print('✅ knowledge_base.png')

# ============ 6. GitHub Pages 部署示意图 ============
def gen_pages():
    w, h = 1200, 500
    img = Image.new('RGB', (w, h), WHITE)
    d = ImageDraw.Draw(img)
    # 流程：代码仓库 → Pages 服务 → 在线网站
    boxes = [
        ('📦 GitHub 仓库', 'git push main', GREEN),
        ('⚙️ GitHub Pages', '自动重建\n约30-60秒', GOLD),
        ('🌐 在线网站', 'xxx.github.io\n自动同步', GREEN_L),
    ]
    bw = 300; gap = 50; sx = (w - (bw*3 + gap*2)) // 2
    for i, (title, desc, color) in enumerate(boxes):
        x = sx + i * (bw + gap); y = 100
        d.rounded_rectangle([x, y, x+bw, y+250], radius=15, fill=LIGHT, outline=color, width=3)
        d.text((x+bw//2-60, y+20), title, fill=color, font=font(22))
        for j, line in enumerate(desc.split('\n')):
            d.text((x+bw//2-50, y+70+j*30), line, fill=DARK, font=font(16))
        # 状态图标
        icons = ['✅', '🔄', '🌐']
        d.text((x+bw//2-15, y+150), icons[i], fill=color, font=font(40))
        # 箭头
        if i < 2:
            d.text((x+bw+15, y+100), '→', fill=MUTED, font=font(30))
    # URL
    d.rounded_rectangle([100, 380, w-100, 430], radius=10, fill=GREEN)
    d.text((w//2-250, 390), 'https://84540305-debug.github.io/zhiying-video-agent/', fill=GOLD, font=font(18))
    img.save(os.path.join(ASSETS, 'pages_deploy.png'))
    print('✅ pages_deploy.png')

# ============ 执行 ============
gen_homepage()
gen_editor()
gen_slide()
gen_pipeline()
gen_kb()
gen_pages()
print(f'\n全部图片已生成到 {ASSETS}')
