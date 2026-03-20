// DevScroll API Contract
// Person A replaces BASE_URL with their deployed backend

const BASE_URL = "http://localhost:8000";

async function createSession(chips) {
  // MOCK: returns fake data so UI works without backend
  return {
    session_id: "mock-" + Date.now(),
    cards: [
      { id:1, type:"insight", title:"React 19 Compiler",
        body:"Auto-memoization is now built-in. No more useMemo.",
        tag:"React", next_action:"npx create-react-app@latest", emoji:"⚛️" },
      { id:2, type:"repo", title:"shadcn/ui hit 100k stars",
        body:"Copy-paste components. No dependency hell.",
        tag:"React", next_action:"npx shadcn@latest init", emoji:"⭐" },
      { id:3, type:"challenge", title:"Two Sum — but explain it",
        body:"Don't just solve it. Explain the hashmap trick in 30 seconds.",
        tag:"DSA", next_action:"leetcode.com/problems/two-sum", emoji:"🧩" },
      { id:4, type:"pattern", title:"System Design: Rate Limiting",
        body:"Token bucket vs sliding window. Know when to use each.",
        tag:"System Design", next_action:"Read: stripe.com/blog/rate-limiters", emoji:"⚡" },
      { id:5, type:"insight", title:"uv replaces pip",
        body:"100x faster Python package manager. Rust-powered.",
        tag:"Python", next_action:"pip install uv", emoji:"🐍" },
      { id:6, type:"repo", title:"LLM.c by Karpathy",
        body:"Training GPT-2 in pure C. 1000 lines. Read it.",
        tag:"AI", next_action:"github.com/karpathy/llm.c", emoji:"🤖" },
      { id:7, type:"challenge", title:"Explain Git rebase",
        body:"Not git merge. Rebase. Without Googling. Go.",
        tag:"DSA", next_action:"git rebase -i HEAD~3", emoji:"🔀" },
      { id:8, type:"pattern", title:"Async/Await is just Promises",
        body:"Under the hood, it's .then() chaining. Know both.",
        tag:"React", next_action:"mdn.io/async-function", emoji:"🔄" },
      { id:9, type:"insight", title:"Docker in 60 seconds",
        body:"Image = snapshot. Container = running instance. That's it.",
        tag:"AI", next_action:"docker run hello-world", emoji:"🐳" },
      { id:10, type:"challenge", title:"Build a CLI tool today",
        body:"One script. Takes input, gives output. Ship it to npm.",
        tag:"Python", next_action:"npm init && node index.js", emoji:"💻" }
    ]
  };
}

async function saveReflection(sessionId, cardIndex, text) {
  // MOCK: just resolves
  return { message: "Saved", streak: Math.floor(Math.random() * 5) + 1 };
}
