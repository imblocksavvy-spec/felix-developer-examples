import { felix } from "./felix-client.mjs";

const symbol = (process.argv[2] ?? "BTC").toUpperCase();
if (!/^[A-Z0-9._:-]{1,32}$/.test(symbol)) throw new Error("Invalid symbol.");

const status = await felix("/v1/status", { auth: false });
const quote = await felix(`/v1/quotes/${encodeURIComponent(symbol)}`);
const research = await felix(`/v1/research/${encodeURIComponent(symbol)}?interval=1h&bars=250`);

console.log(JSON.stringify({ status, quote, research }, null, 2));
