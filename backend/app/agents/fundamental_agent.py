"""
PLACEHOLDER STUB — owned by Member 3 (backend/app/agents/fundamental_agent.py).

This stub exists only so Member 1's backend can run and be tested
end-to-end before Member 3's real implementation is merged in.
Do NOT build on top of this file if you are Member 1 — replace it with
Member 3's PR instead of editing it directly.
"""

import asyncio
import random
import time


async def fundamental_agent(symbol: str) -> dict:
    start = time.perf_counter()
    await asyncio.sleep(0.18)  # simulated retrieval latency

    signal = random.choice(["BULLISH", "NEUTRAL", "BEARISH"])
    confidence = random.randint(60, 90)

    latency_ms = int((time.perf_counter() - start) * 1000)
    return {
        "name": "Fundamental Agent",
        "status": "completed",
        "signal": signal,
        "confidence": confidence,
        "summary": f"[PLACEHOLDER] Simulated fundamentals read for {symbol}.",
        "evidence": ["Simulated filing excerpt (p. 12)"],
        "source": "Simulated financial documents (placeholder)",
        "latency": latency_ms,
    }
