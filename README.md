# Azure AI Foundry – Agent Evaluation CI Template

PR-gated **quality & safety** evaluations for Azure AI Foundry agents and RAG apps.

## What this repo does

- Runs automated evaluations (groundedness, relevance, fluency; jailbreak & harmful-content resistance) on every Pull Request.
- Enforces **policy-as-code** thresholds from `src/eval/metrics.yaml` and fails the build if not met.
- Uses synthetic datasets + safe red-team prompts—**no real data**.

## Quickstart

1. **Clone** this repo and create a Foundry project or use a local mock.
2. **Set GitHub secrets** in your repo settings:
   - `AZURE_AI_CONNECTION` – connection string or config JSON for your Foundry project.
   - `AZURE_OPENAI_ENDPOINT` – your Azure OpenAI endpoint.
   - `AZURE_OPENAI_KEY` – API key for the endpoint.
3. Push a branch and open a **PR** → the **Eval** workflow runs and uploads an artifact.

## Repo layout

```text
src/
  app/                    # minimal demo agent/RAG service
  eval/
    eval_runner.py        # runs Foundry/Eval SDK and writes JSON + JUnit
    metrics.yaml          # quality & safety thresholds (policy-as-code)
    safety_prompts.jsonl  # curated red-team prompts
    datasets/             # synthetic Q/A and task traces
  utils/telemetry.py      # optional App Insights helpers
.github/workflows/eval.yml
```

## Extend

- Add retrieval metrics and an Azure AI Search index.
- Log spans to Application Insights via `utils/telemetry.py`.
- Add multi-turn traces for agent tool use.

## Security & compliance

- No customer data; synthetic corpora only.
- `SECURITY.md` describes coordinated vulnerability disclosure (MSRC).
- Enable **Secret scanning**, **Dependabot**, and **CodeQL** in GitHub.

## Test Change

This is a sample update

## License

MIT © 2025
