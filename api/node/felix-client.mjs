const BASE_URL = "https://api.felix.trade";

export function requireKey() {
  const key = process.env.FELIX_API_KEY ?? "";
  if (!/^fk_[0-9a-f]{32}$/.test(key)) {
    throw new Error("Load a valid FELIX_API_KEY from your application secret manager.");
  }
  return key;
}

export async function felix(path, { method = "GET", body, idempotencyKey, auth = true } = {}) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 25_000);
  const headers = { Accept: "application/json" };
  if (auth) headers.Authorization = `Bearer ${requireKey()}`;
  if (body !== undefined) headers["Content-Type"] = "application/json";
  if (idempotencyKey) headers["Idempotency-Key"] = idempotencyKey;

  try {
    const response = await fetch(`${BASE_URL}${path}`, {
      method,
      headers,
      body: body === undefined ? undefined : JSON.stringify(body),
      signal: controller.signal,
    });
    const payload = await response.json().catch(() => null);
    if (!response.ok) {
      const code = payload?.error?.code ?? `http_${response.status}`;
      const message = payload?.error?.message ?? "Felix request failed.";
      throw new Error(`${code}: ${message}`);
    }
    return payload;
  } finally {
    clearTimeout(timer);
  }
}
