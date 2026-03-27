from __future__ import annotations

import subprocess
import sys
from pathlib import Path

AGENTS = {
    "Agent_Bot": "Agents/Agent_Bot.py",
    "Memory_Agent": "Agents/Memory_Agent.py",
    "RAG_Agent": "Agents/RAG_Agent.py",
    "Drafter": "Agents/Drafter.py",
    "ReAct": "Agents/ReAct.py",
}


def main() -> int:
    project_root = Path(__file__).resolve().parent
    output_dir = project_root / "output"
    output_dir.mkdir(exist_ok=True)

    selected_agent = sys.argv[1] if len(sys.argv) > 1 else "Agent_Bot"
    script = AGENTS.get(selected_agent)
    if script is None:
        print("Unknown agent:", selected_agent)
        print("Available agents:", ", ".join(sorted(AGENTS)))
        return 1

    script_path = project_root / script
    completed = subprocess.run([sys.executable, str(script_path)], cwd=project_root)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
