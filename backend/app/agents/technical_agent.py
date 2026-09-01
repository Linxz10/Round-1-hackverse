"""
PLACEHOLDER STUB — owned by Member 2 (backend/app/agents/technical_agent.py).

This stub exists only so Member 1's backend can run and be tested
end-to-end before Member 2's real implementation is merged in.
Do NOT build on top of this file if you are Member 1 — replace it with
Member 2's PR instead of editing it directly.
"""

import asyncio
import random
import time


async def technical_agent(symbol: str) -> dict:
    start = time.perf_counter()
    await asyncio.sleep(0.15)  # simulated I/O latency

    signal = random.choice(["BULLISH", "NEUTRAL", "BEARISH"])
    confidence = random.randint(55, 85)

    latency_ms = int((time.perf_counter() - start) * 1000)
    return {
        "name": "Technical Analysis Agent",
        "status": "completed",
        "signal": signal,
        "confidence": confidence,
        "summary": f"[PLACEHOLDER] Simulated technical read for {symbol}.",
        "evidence": ["Simulated RSI", "Simulated moving average crossover"],
        "source": "Simulated market data (placeholder)",
        "latency": latency_ms,
    }
