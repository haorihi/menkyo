export async function onRequest(context) {
  const { request, env } = context;

  // OPTIONS method for CORS if needed (though usually same-origin for pages)
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
  // If SYNC_TOKEN is not set in env, we allow it (for local testing/fallback), 
  // but if set, we require it to match.
  const authHeader = request.headers.get("Authorization");
  const token = authHeader ? authHeader.replace("Bearer ", "") : "";
  
  if (env.SYNC_TOKEN && token !== env.SYNC_TOKEN) {
    return new Response("Unauthorized", { status: 401 });
  }

  // Setup basic CORS and JSON headers
  const headers = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
  };

  // Handle requests
  if (request.method === "GET") {
    // Return bookmarks from KV
    const data = await env.HISTORY_KV.get("bookmarkedIds");
    return new Response(data || "[]", { headers });
  }

  if (request.method === "POST") {
    // Save bookmarks to KV
    try {
      const body = await request.json();
      if (!Array.isArray(body)) {
        return new Response("Bad Request: Expected JSON array", { status: 400 });
      }
      await env.HISTORY_KV.put("bookmarkedIds", JSON.stringify(body));
      return new Response(JSON.stringify({ success: true }), { headers });
    } catch (e) {
      return new Response("Bad Request: " + e.message, { status: 400 });
    }
  }

  return new Response("Method not allowed", { status: 405 });
}
