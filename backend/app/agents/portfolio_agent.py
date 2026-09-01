"""
PLACEHOLDER STUB — owned by Member 3 (backend/app/agents/portfolio_agent.py).

This stub exists only so Member 1's backend can run and be tested
end-to-end before Member 3's real implementation is merged in.
Do NOT build on top of this file if you are Member 1 — replace it with
Member 3's PR instead of editing it directly.
"""

import asyncio
import random
import time


async def portfolio_agent(
    symbol: str, profile: str, investment_percentage: float = 14
) -> dict:
    start = time.perf_counter()
    await asyncio.sleep(0.10)

    # Conservative profiles have tighter exposure limits than aggressive ones.
    limit = 25 if profile == "conservative" else 45
    current_exposure = round(random.uniform(15, 35), 1)
    projected_exposure = round(current_exposure + investment_percentage, 1)

    if projected_exposure > limit:
        concentration = "HIGH"
        signal = "BEARISH"
        confidence = 65
    elif projected_exposure > limit * 0.7:
        concentration = "MODERATE"
        signal = "NEUTRAL"
        confidence = 72
    else:
        concentration = "LOW"
        signal = "BULLISH"
        confidence = 80

    latency_ms = int((time.perf_counter() - start) * 1000)
    return {
        "name": "Portfolio Risk Agent",
        "status": "completed",
        "signal": signal,
        "confidence": confidence,
        "summary": (
            f"[PLACEHOLDER] Simulated {profile} portfolio exposure check "
            f"for {symbol}."
        ),
        "evidence": [f"Sector exposure limit for {profile}: {limit}%"],
        "source": "Simulated portfolio data (placeholder)",
        "latency": latency_ms,
        "currentExposure": current_exposure,
        "projectedExposure": projected_exposure,
        "concentration": concentration,
    }
