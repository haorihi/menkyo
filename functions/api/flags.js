export async function onRequest(context) {
  const { request, env } = context;

  // OPTIONS method for CORS
  if (request.method === "OPTIONS") {
    return new Response(null, {
      headers: {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Authorization",
      }
    });
  }

  // Security: Check token
  const authHeader = request.headers.get("Authorization");
  const token = authHeader ? authHeader.replace("Bearer ", "") : "";

  if (env.SYNC_TOKEN && token !== env.SYNC_TOKEN) {
    return new Response("Unauthorized", { status: 401 });
  }

  const headers = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
  };

  if (request.method === "GET") {
    // Return flagged IDs from KV
    const data = await env.HISTORY_KV.get("flaggedIds");
    return new Response(data || "[]", { headers });
  }

  if (request.method === "POST") {
    // Save flagged IDs to KV
    try {
      const body = await request.json();
      if (!Array.isArray(body)) {
        return new Response("Bad Request: Expected JSON array", { status: 400 });
      }
      await env.HISTORY_KV.put("flaggedIds", JSON.stringify(body));
      return new Response(JSON.stringify({ success: true }), { headers });
    } catch (e) {
      return new Response("Bad Request: " + e.message, { status: 400 });
    }
  }

  return new Response("Method not allowed", { status: 405 });
}
