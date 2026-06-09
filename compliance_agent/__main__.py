"""Compliance Agent server entry point — port 10103."""

from __future__ import annotations

import asyncio
import logging
import os

import uvicorn
from dotenv import load_dotenv

load_dotenv()

from a2a.server.apps import A2AFastAPIApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill

from common.registry_client import register
from compliance_agent.agent_executor import ComplianceAgentExecutor

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [compliance_agent] %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

PORT = 10103
AGENT_ENDPOINT = f"http://localhost:{PORT}"


async def _register_with_retry(max_attempts: int = 10, delay: float = 2.0) -> None:
    """Retry registration until the registry is up."""
    info = {
        "agent_name": "compliance-agent",
        "version": "1.0",
        "description": "Regulatory compliance officer for SEC, SOX, FCPA, AML, and related topics",
        "tasks": ["compliance_question"],
        "endpoint": AGENT_ENDPOINT,
        "tags": ["compliance", "regulatory", "sec", "sox", "aml", "fcpa"],
    }
    for attempt in range(1, max_attempts + 1):
        try:
            await register(info)
            logger.info("Registered with registry (attempt %d)", attempt)
            return
        except Exception as exc:
            logger.warning(
                "Registry not ready (attempt %d/%d): %s — retrying in %.0fs",
                attempt, max_attempts, exc, delay,
            )
            await asyncio.sleep(delay)
    logger.error("Failed to register after %d attempts", max_attempts)


async def main() -> None:
    await _register_with_retry()

    agent_card = AgentCard(
        name="Compliance Agent",
        description=(
            "Regulatory compliance specialist for SEC, SOX, FCPA, AML, "
            "antitrust, and corporate governance questions"
        ),
        url=AGENT_ENDPOINT,
        version="1.0.0",
        capabilities=AgentCapabilities(streaming=False),
        default_input_modes=["text/plain"],
        default_output_modes=["text/plain"],
        skills=[
            AgentSkill(
                id="compliance_question",
                name="Compliance Question",
                description=(
                    "Answer questions about regulatory compliance, SEC enforcement, "
                    "SOX obligations, AML requirements, and corporate governance."
                ),
                tags=["compliance", "regulatory", "sec", "sox", "aml"],
            )
        ],
    )

    executor = ComplianceAgentExecutor()
    task_store = InMemoryTaskStore()
    request_handler = DefaultRequestHandler(
        agent_executor=executor,
        task_store=task_store,
    )
    app_builder = A2AFastAPIApplication(
        agent_card=agent_card,
        http_handler=request_handler,
    )
    app = app_builder.build()

    config = uvicorn.Config(app, host="0.0.0.0", port=PORT, log_level="info")
    server = uvicorn.Server(config)
    logger.info("Compliance Agent listening on port %d", PORT)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())