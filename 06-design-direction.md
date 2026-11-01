# Design Direction (v3)

This replaces the earlier "glowing luxury" look. It is based on your feedback (it looked generic, it did not read as a web developer, it needed to feel like the references you sent) and on a study of the four sites below.

---

## 1. What I studied and what I took from each

| Site | What it does well | What I took (not copied) |
|------|------------------|--------------------------|
| **Yuyu** (yuyu.ng) | Personal presence: a cut-out portrait with a sticker outline, 3D memoji-style avatars and props around it, soft staggered fade-ins as you scroll, a clear run of sections (hero, tools, work, testimonials, experience, call to action). The whole page is light: about 33 requests and 5,400px of scroll. | A real person at the top of the page. Plain, predictable section order. Gentle reveal on scroll. A slot for your own portrait and, if you want, your own 3D avatar or props (you supply the images). |
| **Bruno Simon** (bruno-simon.com) | The site itself is the proof of skill: you drive a 3D car around a world and find the projects. | The principle: show technical ability instead of only claiming it. I did **not** copy the game. It is very heavy (it would not even finish loading in my browser pane), which goes against your "speed first" rule. |
| **Lynn Fisher** (lynnandtonic.com) | One strong idea carried through with craft: the site reads like a book, with a table of contents, custom lettering, paper texture and a version number. | Pick one idea and commit to it. Small details that show care. |
| **Stuff & Nonsense** (stuffandnonsense.co.uk) | Plain-language positioning ("I'm Andy Clarke and this is my website design studio…"), an availability note at the very top with a link, a row of real client names, one clear call to action ("Tell me your story"). | A short availability bar with a link. Say who you are and what you do in plain words. Proof near the top. One primary call to action. |

**The shared lesson:** each site makes you believe the person in the first few seconds, through a real person, a clear sentence, or visible proof. None of them relies on glow effects.

---

## 2. What "AI slop" looked like in my v2, and what is removed

Removed from the design:

- Gold-to-orange gradient text and gradient buttons
- Glowing orbs, radial "spotlights", floating gold dust and film grain
- Frosted-glass floating cards around the hero
- Rotating words in the headline
- A badge with a pulsing green dot ("Available for projects")
- A spinning 3D knot as the main visual
- Serif display headlines mixed with a sans, letter-spaced uppercase labels, scrolling outlined text strips
- Vague taglines in the headline ("Beyond Beautiful. Built to Perform.")
- Centered text on every section

Used instead:

- **One typeface: Figtree** (weights 400 to 800). It is clean and friendly, and it is the font you asked for.
- **One flat accent: gold** (`#E5B040`), taken from your logo. Used for buttons, links, active states and key details only. No gradients.
- **Near-black background** (`#060607`) and warm off-white text (`#F3EEE3`). Hairline borders at 10% white. Solid surfaces, not glass.
- **Left-aligned, plain-language copy.** The headline says what you do and for whom. Real numbers (6+ websites, 5+ landing pages, 5+ clients, 3 to 4 years) and your real tools sit right under it.
- **Motion kept small:** a short fade-up on load, a gentle tilt on the browser frame, and a small wireframe-to-finished animation. Everything respects "reduce motion".
- **No Three.js and no external scripts** on the hero. That keeps it fast and avoids problems inside GHL.

---

## 3. The idea behind the design

> **Show the work, say it plainly, make contacting you easy.**

- The hero's right side is a **browser frame**. Until you send screenshots it shows a small page building itself, from wireframe to finished, which is also what your process does. When you add screenshots of real projects (the `PROJECTS` list in `home-hero.html`), it becomes a slideshow of your actual work.
- Under the frame are your **real delivery times** (landing page 5 to 10 business days, business website 2 to 3 weeks, sales funnel 2 to 4 weeks). Concrete facts persuade more than adjectives.
- **Two ways to contact you, in order of priority:** the "Start a project" form (primary, gold button) and "Book a discovery call" (secondary, outlined button).

---

## 4. Tokens

```css
:root{
  --ag-bg:#060607; --ag-surface:#0e0e10; --ag-surface-2:#151518; --ag-line:rgba(255,255,255,.1);
  --ag-text:#f3eee3; --ag-muted:#a8a193;
  --ag-gold:#e5b040; --ag-gold-hover:#f2c35c; --ag-gold-ink:#1a1204;   /* text on gold buttons */
  --ag-radius:14px; --ag-radius-sm:10px; --ag-container:1200px;
  --ag-font:'Figtree',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
}
```

**Type scale**

| Role | Size | Weight |
|------|------|--------|
| Hero headline | `clamp(2rem, 2.5vw + 1.1rem, 3.35rem)` | 700, letter-spacing -0.03em, line-height 1.06 |
| Section headline | `clamp(2rem, 2.8vw + 1rem, 3.3rem)` | 700 |
| Body | 1rem to 1.2rem, line-height 1.65 | 400 |
| Small / meta | 0.85 to 0.95rem | 400 to 600 |

**Components:** buttons are 10px-radius rectangles (not pills), solid gold for primary and a 1px outline for secondary. Cards use the surface colour with a hairline border and a 14px radius. Focus rings are 2px gold.

---

## 5. Section order for each page

| Page | Sections |
|------|----------|
| **Home** | header, hero, selected work (3 projects), how I work (6 steps, short), services and "from" prices (short), testimonials, contact section, footer |
| **Work** | header, filter plus project cards, contact section, footer |
| **Project** (one template) | header, brief (problem, solution, role, stack, result), screenshots, next project, contact section, footer |
| **Services** | header, six services with starting prices, process, what happens after launch, payment terms, contact section, footer |
| **About** | header, story, experience and milestones, how I work, working with clients, contact section, footer |
| **Contact** | header, contact section, footer |

Header, footer and the WhatsApp button repeat on every page.

---

## 6. Where your own assets plug in

| Asset | Where |
|------|-------|
| Your photo (square) | `PHOTO_URL` in `home-hero.html`; also the About page |
| Project screenshots | `PROJECTS` list in `home-hero.html`; then the Work page |
| Optional 3D avatar or emoji props (like Yuyu's) | If you create these, I will add them as small images beside the hero. I'm not generating them, and I'd keep them to one or two so the page stays credible. |
| Calendly link | `CALENDLY_URL` in `contact-section.html` (and `home-hero.html`) |
| GHL webhook | `WEBHOOK_URL` in `contact-section.html` |
| Page URLs | `LINKS` at the top of the script in each section |

---

## 7. Decisions still open

1. Do you want a 3D avatar or emoji props beside your portrait (the Yuyu effect)? If so, you will need to create or buy the images.
2. Which project categories do you want on the Work page filter? Suggested, to match your services: Landing pages, Business websites, Sales funnels, Web applications, Redesigns.
3. Do you keep "Beyond Beautiful. Built to Perform." anywhere? It currently appears only as a small sign-off in the footer.
