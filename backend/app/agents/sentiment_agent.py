"""
PLACEHOLDER STUB — owned by Member 2 (backend/app/agents/sentiment_agent.py).

This stub exists only so Member 1's backend can run and be tested
end-to-end before Member 2's real implementation is merged in.
Do NOT build on top of this file if you are Member 1 — replace it with
Member 2's PR instead of editing it directly.
"""

import asyncio
import random
import time


async def sentiment_agent(symbol: str, simulate_failure: bool = False) -> dict:
    start = time.perf_counter()
    await asyncio.sleep(0.12)  # simulated I/O latency

    if simulate_failure:
        latency_ms = int((time.perf_counter() - start) * 1000)
        return {
            "name": "News Sentiment Agent",
            "status": "unavailable",
            "signal": "UNAVAILABLE",
            "confidence": 0,
            "summary": "[PLACEHOLDER] News feed unavailable (simulated failure).",
            "evidence": [],
            "source": "Simulated news feed (placeholder)",
            "latency": latency_ms,
        }

    signal = random.choice(["BULLISH", "NEUTRAL", "BEARISH"])
    confidence = random.randint(50, 80)

    latency_ms = int((time.perf_counter() - start) * 1000)
    return {
        "name": "News Sentiment Agent",
        "status": "completed",
        "signal": signal,
        "confidence": confidence,
        "summary": f"[PLACEHOLDER] Simulated sentiment read for {symbol}.",
        "evidence": ["Simulated headline sample"],
        "source": "Simulated news feed (placeholder)",
        "latency": latency_ms,
    }
