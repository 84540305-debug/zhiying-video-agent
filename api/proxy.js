/**
 * 知影 ZhiYing · CORS 代理（Vercel Edge Function）
 *
 * 部署方式（1分钟）：
 *   1. 打开 https://vercel.com/new → 用 GitHub 登录
 *   2. Import 这个仓库（84540305-debug/zhiying-video-agent）
 *   3. 保持默认配置 → Deploy
 *   4. 部署后得到 https://zhiying-video-agent.vercel.app
 *   5. 在网站 ⚙️ 文生图设置 里把代理地址填为该 URL
 *
 * 路由映射：
 *   /api/proxy/doubao/*  → https://ark.cn-beijing.volces.com/*
 *   /api/proxy/wanx/*    → https://dashscope.aliyuncs.com/*
 *   /api/proxy/openai/*  → https://api.openai.com/*
 *   /api/proxy/stability/* → https://api.stability.ai/*
 */

export const config = { runtime: 'edge' };

const TARGETS = {
  doubao: 'https://ark.cn-beijing.volces.com',
  wanx: 'https://dashscope.aliyuncs.com',
  openai: 'https://api.openai.com',
  stability: 'https://api.stability.ai',
};

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
  'Access-Control-Allow-Headers': 'Authorization, Content-Type, X-DashScope-Async, Accept',
  'Access-Control-Max-Age': '86400',
};

export default async function handler(req) {
  // 预检请求
  if (req.method === 'OPTIONS') {
    return new Response(null, { status: 204, headers: CORS });
  }

  const url = new URL(req.url);
  const parts = url.pathname.split('/'); // ['', 'api', 'proxy', 'doubao', 'api', 'v3', ...]

  // 健康检查
  if (url.pathname === '/api/proxy' || url.pathname === '/api/proxy/') {
    return new Response(JSON.stringify({
      status: 'ok',
      service: 'ZhiYing CORS Proxy (Vercel Edge)',
      routes: Object.keys(TARGETS).map(k => '/api/proxy/' + k + '/*'),
    }, null, 2), { headers: { 'Content-Type': 'application/json', ...CORS } });
  }

  // 解析目标 API
  const targetKey = parts[3]; // /api/proxy/{target}/...
  const targetBase = TARGETS[targetKey];
  if (!targetBase) {
    return new Response(JSON.stringify({
      error: 'Unknown target. Use /api/proxy/doubao/*, /api/proxy/wanx/*, etc.',
      available: Object.keys(TARGETS),
    }), { status: 404, headers: { 'Content-Type': 'application/json', ...CORS } });
  }

  // 构建目标 URL
  const targetPath = '/' + parts.slice(4).join('/');
  const targetUrl = targetBase + targetPath + url.search;

  // 转发请求
  const fetchOpts = {
    method: req.method,
    headers: new Headers(req.headers),
  };
  fetchOpts.headers.delete('host');
  fetchOpts.headers.delete('x-forwarded-for');
  fetchOpts.headers.delete('x-real-ip');
  if (req.method !== 'GET' && req.method !== 'HEAD') {
    fetchOpts.body = req.body;
  }

  try {
    const response = await fetch(targetUrl, fetchOpts);
    const newHeaders = new Response(response.body, { status: response.status }).headers;
    Object.entries(CORS).forEach(([k, v]) => newHeaders.set(k, v));

    return new Response(response.body, {
      status: response.status,
      statusText: response.statusText,
      headers: newHeaders,
    });
  } catch (e) {
    return new Response(JSON.stringify({
      error: 'Proxy fetch failed',
      message: e.message,
      target: targetUrl,
    }), { status: 502, headers: { 'Content-Type': 'application/json', ...CORS } });
  }
}
