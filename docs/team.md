# Team: three subscriptions, one desk

*How Astra's three AI subscriptions split the work so no single one carries the load. Claude Opus 5.5 · 6 Oct 2026.*

## The rule
**The repo is the desk; the dashboard is the inbox.** Work moves as task cards in `handoffs/`; decisions move as assignments on the dashboard. Nobody passes work through chat history, so any assistant can pick up where another left off.

## Who does what
| Seat | Where it runs | Jobs | Uses whose usage |
| --- | --- | --- | --- |
| **Claude 1** (main account) | Claude app; owns the dashboard | Architecture, dashboard updates, the Monday brief (scheduled), merging work | Account 1 |
| **Claude 2** (second account) | Claude desktop or a separate browser profile, GitHub connected | Builder and red-team reviewer: cards marked `for: claude-2`, pull requests on `claude-2/*` branches | Account 2 |
| **Astra** (OpenAI) | ChatGPT desktop app | Eval panel judge 2, second opinion on the brief, research and drafting cards marked `for: astra-openai` | OpenAI subscription |
| **Chip** (on the dashboard) | Inside the dashboard, quick model | Plain-language answers, goals, navigation | Whichever Claude account has the dashboard open |
| **You** | Dashboard on iPad or desktop | Answer assignments, approve pull requests, pick the next card | Answering and ticking assignments uses **no AI at all** |

## A normal day
1. **At work (iPad):** open the dashboard, answer assignments, tick tasks. Zero AI usage. Ask Chip only when you need an explanation.
2. **At your desk:** give Claude 2 or Astra the next open card ("Take the next open card for claude-2 in findastra/data-dealer"). They work in the repo and report back there.
3. **Claude 1** reviews and merges their pull requests when you ask, and the Monday brief reads everything.

## Keeping usage spread out
- Put long jobs (building, research, drafting) on Claude 2 and Astra through cards.
- Keep Claude 1 for decisions that need the whole picture.
- Open the dashboard signed in as Claude 2 to have Chip's questions use account 2. This needs the dashboard shared with that account from its Share menu.

## Setup checklist
1. Claude 2: connect GitHub (access to `findastra/data-dealer`), paste its prompt from `handoffs/CONNECT.md`.
2. Astra: paste its prompt from `handoffs/CONNECT.md`; connect GitHub if your plan allows, otherwise she returns files for you to commit.
3. Dashboard: share it with your second Claude account (Share menu → invite that email). Only you can change sharing.
4. Desktop: Claude desktop app for one Claude account, a separate browser profile (or the web app) for the other, ChatGPT desktop for Astra.

## Limits
- Assistants can't message each other directly; the repo and the dashboard are how they coordinate.
- Production work (real money, real data) runs on company API keys, not personal subscriptions.
