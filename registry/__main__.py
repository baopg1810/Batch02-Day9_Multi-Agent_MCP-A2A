"""Registry Service — port 10000.

A lightweight FastAPI service that allows agents to self-register and
clients to discover agent endpoints by task name.

Endpoints:
  POST /register          — register an agent
  GET  /discover/{task}   — find an agent that handles the given task
  GET  /agents            — list all registered agents
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [registry] %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(title="A2A Registry", version="1.0.0")

# In-memory store: agent_name -> agent info dict
agents: dict[str, dict[str, Any]] = {}


class AgentRegistration(BaseModel):
    agent_name: str
    version: str = "1.0"
    description: str = ""
    tasks: list[str] = []
    endpoint: str
    tags: list[str] = []


@app.post("/register", status_code=200)
async def register(registration: AgentRegistration) -> dict:
    """Register or update an agent."""
    entry = registration.model_dump()
    entry["registered_at"] = datetime.now(timezone.utc).isoformat()
    agents[registration.agent_name] = entry
    logger.info(
        "Registered agent '%s' at %s (tasks=%s)",
        registration.agent_name,
        registration.endpoint,
        registration.tasks,
    )
    return {"status": "ok", "agent_name": registration.agent_name}


@app.get("/discover/{task}")
async def discover(task: str) -> dict:
    """Return the first agent whose task list contains *task*."""
    for agent in agents.values():
        if task in agent.get("tasks", []):
            logger.info("Discovered agent '%s' for task '%s'", agent["agent_name"], task)
            return {
                "agent_name": agent["agent_name"],
                "endpoint": agent["endpoint"],
                "description": agent.get("description", ""),
            }
    raise HTTPException(
        status_code=404,
        detail=f"No agent found for task '{task}'",
    )


@app.get("/agents")
async def list_agents() -> dict:
    """Return all registered agents."""
    return {"agents": list(agents.values())}


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "agent_count": len(agents)}


if __name__ == "__main__":
    logger.info("Starting Registry on port 10000")
    uvicorn.run(app, host="0.0.0.0", port=10000, log_level="info")