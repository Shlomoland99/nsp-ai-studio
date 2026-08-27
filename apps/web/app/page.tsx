"use client";
import { useState } from "react";

const providers = [
  ["ComfyUI", "Local generation", "Online-ready"],
  ["Gemini", "Reasoning + vision", "API connected"],
  ["PixVerse", "Video generation", "API ready"],
  ["HeyGen", "Avatar video", "API ready"],
  ["Canva", "Design systems", "API ready"],
  ["FLUX / SDXL", "Image generation", "ComfyUI"],
];

export default function Home() {
  const [intent, setIntent] = useState("");
  const [status, setStatus] = useState("");
  const [loading, setLoading] = useState(false);

  async function submit() {
    if (!intent.trim()) { setStatus("Describe something first."); return; }
    setLoading(true); setStatus("");
    try {
      const response = await fetch((process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000") + "/v1/jobs", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ intent, capabilities: ["text-to-image"], local_only: true }),
      });
      const body = await response.json();
      setStatus(response.ok ? `Queued on ${body.provider} · ${body.job_id}` : (body.detail || "The API rejected the request."));
    } catch { setStatus("API is not reachable. Start the backend or set NEXT_PUBLIC_API_URL."); }
    finally { setLoading(false); }
  }

  return <main>
    <nav className="nav shell">
      <a className="brand" href="#"><span className="brand-mark">N</span><span>NSP <em>AI Studio</em></span></a>
      <div className="nav-links"><a href="#platform">Platform</a><a href="#providers">Providers</a><a href="#api">API</a></div>
      <a className="nav-cta" href="#api">Open workspace <span>↗</span></a>
    </nav>

    <section className="hero shell">
      <div className="hero-copy">
        <p className="eyebrow"><span className="pulse" /> CREATIVE INTELLIGENCE, ORCHESTRATED</p>
        <h1>Make the idea.<br /><span>Move the world.</span></h1>
        <p className="lede">NSP AI Studio gives your creative work one calm command center—routing every request to the right local engine or cloud model.</p>
        <div className="hero-actions"><a className="button primary" href="#api">Start creating <span>→</span></a><a className="text-link" href="#platform">See how it works <span>↓</span></a></div>
      </div>
      <div className="orbital" aria-label="Abstract creative intelligence visualization">
        <div className="orbit orbit-one" /><div className="orbit orbit-two" /><div className="core"><span>NSP</span><small>CREATIVE<br />OS</small></div>
        <div className="node node-a">IMG</div><div className="node node-b">VID</div><div className="node node-c">API</div>
      </div>
    </section>

    <section id="platform" className="feature-strip"><div className="shell feature-grid">
      <div><span className="feature-number">01</span><h3>One intent</h3><p>Describe the result in plain language.</p></div>
      <div><span className="feature-number">02</span><h3>Smart routing</h3><p>Match capabilities to the right engine.</p></div>
      <div><span className="feature-number">03</span><h3>Clean delivery</h3><p>Keep providers, secrets, and outputs organized.</p></div>
    </div></section>

    <section id="providers" className="shell providers-section">
      <div className="section-heading"><div><p className="eyebrow">THE PROVIDER LAYER</p><h2>Your tools.<br /><span>One studio.</span></h2></div><p>Built around stable interfaces, so your stack can grow without rebuilding the core.</p></div>
      <div className="provider-grid">{providers.map(([name, desc, state]) => <article className="provider-card" key={name}><div className="provider-icon">{name.slice(0, 1)}</div><div><h3>{name}</h3><p>{desc}</p></div><span className="state">{state}</span></article>)}</div>
    </section>

    <section id="api" className="shell api-section">
      <div className="api-panel"><div><p className="eyebrow">LIVE API CONSOLE</p><h2>Turn a sentence<br />into a <span>job.</span></h2><p className="panel-copy">The website is connected to the FastAPI orchestration layer. Try a local text-to-image request.</p></div>
      <div className="console"><label htmlFor="intent">CREATIVE BRIEF</label><textarea id="intent" value={intent} onChange={e=>setIntent(e.target.value)} placeholder="A cinematic portrait in warm evening light…" /><button className="button primary console-button" onClick={submit} disabled={loading}>{loading ? "Routing…" : "Send to API"} <span>→</span></button>{status && <p className="status">{status}</p>}</div></div>
    </section>

    <footer className="shell footer"><a className="brand" href="#"><span className="brand-mark">N</span><span>NSP <em>AI Studio</em></span></a><p>Creative work, routed with intention.</p><span>© 2026 NSP</span></footer>
  </main>;
}
