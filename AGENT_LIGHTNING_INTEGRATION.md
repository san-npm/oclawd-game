# Agent Lightning Integration with OpenClaw

**Installation Status:** ✅ Complete
- `agent-lightning` 0.3.1 installed (pip)
- `skills-repo` with 22 Trail of Bits plugins cloned to `/root/openclaw/skills-repo/plugins/`

**Quick Start with Agent Lightning:**

```python
import agentlightning as agl

# Start training with zero code changes
agl.emit_inference_started(agent="openclaw", task="user_request")
# ... agent runs ...
agl.emit_reward(reward=value, metadata={"reason": "task completed"})
```

**Available Trail of Bits Skills (22 total):**

**Vulnerability Scanners:**
- `/algorand-vulnerability-scanner`
- `/cairo-vulnerability-scanner`
- `/cosmos-vulnerability-scanner`
- `/solana-vulnerability-scanner`
- `/substrate-vulnerability-scanner`
- `/ton-vulnerability-scanner`

**Development & Review:**
- `/audit-context-building`
- `/code-maturity-assessor`
- `/differential-review`
- `/fix-review`
- `/guidelines-advisor`
- `/insecure-defaults`
- `/sharp-edges`
- `/spec-to-code-compliance`
- `/variant-analysis`

**Testing & Tools:**
- `/address-sanitizer`
- `/aflpp`
- `/atheris`
- `/cargo-fuzz`
- `/codeql`
- `/coverage-analysis`
- `/constant-time-analysis`
- `/constant-time-testing`
- `/fuzzing-dictionary`
- `/fuzzing-obstacles`
- `/harness-writing`
- `/libafl`
- `/libfuzzer`
- `/ossfuzz`
- `/property-based-testing`
- `/ruzzy`
- `/semgrep`
- `/semgrep-rule-creator`
- `/semgrep-rule-variant-creator`
- `/testing-handbook-generator`
- `/wycheproof`

**Utilities:**
- `/burpsuite-project-parser`
- `/claude-in-chrome-troubleshooting`
- `/constant-time-analysis`
- `/culture-index`
- `/interpreting-culture-index`
- `/dwarf-expert`
- `/firebase-apk-scanner`
- `/modern-python`
- `/skill-creator`
- `/agent-directory`
- `/healthcheck`

**To use a skill:**
```
/plugin install trailofbits/skills/plugins/<skill-name>
```
