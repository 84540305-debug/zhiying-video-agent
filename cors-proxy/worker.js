/**
 * 知影 ZhiYing · CORS 代理（Cloudflare Workers）
 *
 * 部署方式（30秒）：
 *   1. 打开 https://workers.cloudflare.com → 用 GitHub/Google 登录
 *   2. 点 "Create application" → "Create Worker"
 *   3. 把本文件全部内容粘贴到编辑器 → "Save and Deploy"
 *   4. 部署后得到 https://zhiying-cors-proxy.你的子域.workers.dev
 *   5. 在网站 ⚙️ 文生图设置 里把代理地址填为该 URL
 *
 * 使用方式（前端自动调用，无需手动操作）：
 *   豆包/火山引擎：{代理URL}/doubao/api/v3/contents/generations/tasks
 *   通义万相：     {代理URL}/wanx/api/v1/services/aigc/text2image/image-synthesis
 *
 * 原理：浏览器请求 → Cloudflare Worker → 火山引擎/阿里 API → 原路返回
 * Worker 只做透明转发 + 加 CORS 头，不存储任何数据
 */

export default {
  async fetch(request) {
    // CORS 响应头（允许浏览器跨域访问）
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Authorization, Content-Type, X-DashScope-Async, Accept',
      'Access-Control-Max-Age': '86400',
    };

    // 预检请求直接返回
    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: corsHeaders });
    }

    const url = new URL(request.url);
    let targetUrl = '';

    // 路径映射：/doubao/* → 火山引擎方舟
    if (url.pathname.startsWith('/doubao/')) {
      targetUrl = 'https://ark.cn-beijing.volces.com' + url.pathname.replace('/doubao', '') + url.search;
    }
    // 路径映射：/wanx/* → 阿里 DashScope
    else if (url.pathname.startsWith('/wanx/')) {
      targetUrl = 'https://dashscope.aliyuncs.com' + url.pathname.replace('/wanx', '') + url.search;
    }
    // 路径映射：/openai/* → OpenAI API
    else if (url.pathname.startsWith('/openai/')) {
      targetUrl = 'https://api.openai.com' + url.pathname.replace('/openai', '') + url.search;
    }
    // 路径映射：/stability/* → Stability AI
    else if (url.pathname.startsWith('/stability/')) {
      targetUrl = 'https://api.stability.ai' + url.pathname.replace('/stability', '') + url.search;
    }
    // 健康检查
    else if (url.pathname === '/' || url.pathname === '/health') {
      const targets = {
        doubao: 'https://ark.cn-beijing.volces.com',
        wanx: 'https://dashscope.aliyuncs.com',
        openai: 'https://api.openai.com',
        stability: 'https://api.stability.ai',
      };
      return new Response(JSON.stringify({
        status: 'ok',
        service: 'ZhiYing CORS Proxy',
        targets: Object.keys(targets).map(k => '/' + k + '/...'),
        usage: '在文生图设置中填入代理地址：' + url.origin + '/doubao',
      }, null, 2), {
        headers: { 'Content-Type': 'application/json', ...corsHeaders },
      });
    }
    // 未知路径
    else {
      return new Response(JSON.stringify({
        error: 'Unknown path. Use /doubao/*, /wanx/*, /openai/*, or /stability/*',
      }), {
        status: 404,
        headers: { 'Content-Type': 'application/json', ...corsHeaders },
      });
    }

    // 转发请求到目标 API
    const fetchOpts = {
      method: request.method,
      headers: new Headers(request.headers),
    };
    // 删除 host header（避免目标 API 拒绝）
    fetchOpts.headers.delete('host');
    // 非 GET 请求转发 body
    if (request.method !== 'GET' && request.method !== 'HEAD') {
      fetchOpts.body = request.body;
    }

    try {
      const response = await fetch(targetUrl, fetchOpts);

      // 构建响应（加 CORS 头）
      const newHeaders = new Headers(response.headers);
      Object.entries(corsHeaders).forEach(([k, v]) => newHeaders.set(k, v));

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
      }), {
        status: 502,
        headers: { 'Content-Type': 'application/json', ...corsHeaders },
      });
    }
  }
};
