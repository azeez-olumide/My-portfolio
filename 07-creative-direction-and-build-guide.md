# Azeez Gazalle Portfolio: Creative Direction and Build Guide (v6)

## 0. v6 update: the reference-video style

Rebuilt to follow the reference's hero and scroll feel while keeping separate pages and 3D emoji:
- **Hero:** giant gold "HI, I'M AZEEZ" behind a portrait placeholder (set `PHOTO_URL`), 3D emoji floating around it, rotating "I design and build ..." line, pill CTA bottom right.
- **Scroll mechanics:** giant outline titles that fill as you scroll, paragraphs whose words light up, parallax emoji props, dark/light rounded "sheets" that overlap, sticky stacked project cards, tilted moving testimonial wall, tile marquee.
- **Home order:** hero, logos, gallery, about, services (light), projects, process (light), testimonials, call to action (light), footer.
- **New config:** `PROJECTS` in `home-work`, `TESTIMONIALS` in `home-testimonials` (placeholders show until filled; no invented testimonials).
- **Not verified:** how GHL handles negative margins and `position:sticky` inside code blocks, and motion smoothness on real devices (I only saw still frames). Test one page first.
- Add `home-gallery` and `home-testimonials` to the Home page list; the Home page order above replaces the v5 table row.

### v6.1 changes
- Hero has fewer emoji (6 on desktop, 4 on mobile), including two 3D women (technologist, artist).
- The tile carousels are gone. One strip, "Skills I build with", now includes Supabase, Firebase and WordPress. `home-gallery` is removed from Home.
- "Let's get in touch" has a cartoon-portrait placeholder (`PHOTO_URL` in `home-cta`) with emoji flying around it.
- **New page `/start`**: paste only `start-form` on it (no header, footer or WhatsApp block). Every "Start a project" button points to `/start`. The X returns home. `/contact` stays for the call booking and direct details.
- **New `00-loader`**: paste at the very top of every page, including `/start`. Logo with a lightning ring shows when a page opens and for about 0.65s when a visitor clicks to another page.
- Woman emoji use skin-tone folders on jsDelivr, written as `Name|file@Medium-Dark` in `data-em`.
 What I observed on the four references, and what I take from them

I could inspect Yuyu, Lynn Fisher and Stuff & Nonsense directly earlier in this project. **I could not inspect Bruno Simon's site**: it hung my browser pane both times, so what I say about it comes from general knowledge, not observation.

| Reference | Observed | What I take (not copy) |
|-----------|----------|------------------------|
| **Yuyu** | A cut-out portrait with a white sticker outline, 3D emoji-style props around it, blur-and-fade reveals in sequence, a tools strip with logos, plain section order, light page weight. | A person at the centre of the hero, real 3D emoji props, blur-in reveals, a logo strip. Different layout, copy, colours and scene. |
| **Bruno Simon** | (Not inspected.) Known as a drivable 3D world where the site is the proof of skill. | The principle that the site itself demonstrates skill. Realised as a lightweight 3D hero scene, not a game. |
| **Lynn Fisher** | One strong visual idea carried through with craft and small details. | Commit to one identity: here, "gold light in a dark room, objects floating in depth". |
| **Stuff & Nonsense** | Plain-language positioning, an availability note with a link at the very top, one clear call to action. | The availability bar, direct positioning, and commercial clarity on Services and Process. |

## 2. Two directions, and the one I built

**A. Night studio (built).** Near-black room, one warm gold light source behind the portrait, 3D objects floating in real depth, gold dust, cinematic camera movement. Figtree only, with weight and size contrast. Fits your wish for a movie-like, glowing, 3D feel and your gold brand.
**B. Ivory editorial (not built).** Warm off-white pages, charcoal type, gold used sparingly, no 3D. Calm and credible, but it loses the memorable first impression you asked for.

I recommend A because the first five seconds decide whether a client keeps reading, and A is the only one that gives you both the 3D "wow" and the gold brand recognition.

## 3. Design system

| Token | Value | Use |
|-------|-------|-----|
| Background | `#07070A` | Page |
| Surface | `#101014` / `#16161B` | Panels |
| Line | `rgba(255,255,255,.12)` | Hairlines |
| Text | `#F8F3E9` | Headings and body (contrast about 17:1) |
| Muted | `#B9B1A1` | Secondary text (about 8:1) |
| Gold | `#F0B93E` | Single accent: buttons, key words, numerals |
| Gold highlight | `#FFD479` | Hover and glow |
| Gold ink | `#1A1204` | Text on gold buttons |

Type: **Figtree** only (400 to 800). Hero headline `clamp(1.95rem, 1.9vw + 1.15rem, 3.1rem)`; section headlines `clamp(1.8rem, 2.1vw + 1rem, 3.05rem)`; body 1 to 1.18rem. Buttons are pills. Panels use 18 to 26px radii only where they hold content; services, process steps and principles are editorial lists and tables, not repeated cards.

Motion: blur-and-rise reveals, a rotating hero word, 3D tilt on mockups, an accordion, a timeline that fills as you scroll. Everything respects `prefers-reduced-motion`. No scroll-jacking.

## 4. Pages and sections (each file is one GHL Custom Code block)

| GHL page | Path | Sections, in order |
|----------|------|--------------------|
| Home | `/` | `home-hero`, `logo-marquee`, `home-about`, `home-work`, `home-services`, `home-process`, `home-cta` |
| Work | `/work` | `page-hero-work`, `work-showcase`, `home-cta` |
| Project (case study template) | `/work/project` | `project-detail`, `home-cta` |
| Services | `/services` | `page-hero-services`, `services-list`, `services-terms`, `home-cta` |
| Process | `/process` | `page-hero-process`, `process-steps`, `why-me`, `faq`, `home-cta` |
| About | `/about` | `page-hero-about`, `about-story`, `home-cta` |
| Contact | `/contact` | `contact-section` |

Every page also gets `header`, `footer` and `whatsapp-float`. Optional on every page: `00-global` (fonts and tokens) and `00-emoji-pack` (all 3D emoji embedded, about 125 KB, loads instantly and needs no CDN).

## 5. How to put it on GHL

1. Create the seven pages with the paths above (or change `LINKS` at the top of each section's script).
2. On each page add one **Custom Code** element per section and paste that section's file into it, in the order in the table.
3. Hero 3D: `home-hero` loads three.js r128 from cdnjs. If it cannot load, the hero shows a CSS version automatically.
4. Optional but recommended: paste `00-emoji-pack` at the top of each page so the 3D emoji never depend on a CDN.
5. Test the Phase 0 items on one page first, since I could not verify GHL itself: code block size limit, whether `<script>` runs inside blocks, and whether the CSS class names conflict with GHL's own.

## 6. What you configure

| What | Where |
|------|-------|
| Your portrait (transparent PNG) | `PHOTO_URL` in `home-hero`; `PHOTO_URL` in `home-about` and `about-story` (any photo, cropped to the arch) |
| Projects and screenshots | `PROJECTS` array in `home-work` and `work-showcase` (placeholders show until filled) |
| Calendly link | `CALENDLY_URL` in `contact-section` (empty means the button opens WhatsApp) |
| Form delivery | `WEBHOOK_URL` in `contact-section` (empty means the form hands off to WhatsApp). **Not connected or tested against a real GHL workflow.** |
| LinkedIn and GitHub | `SOCIAL` array in `footer` |
| Page paths | `LINKS` at the top of each section's script |

## 7. Content decisions I made, please confirm

- **Prices are now the ones in your latest brief**: $250, $600, $750, from $2,000 (subject to scope), $400, $75 per month. Earlier you gave $150, $400, $750, $1,000, $300, $75. I used the newer set.
- **Two revision rounds** and **14 days of post-launch support**, per your brief. This settles the earlier open question.
- Figures (6+ websites, 5+ landing pages, 3 to 4 years) are shown as self-reported. There are **no testimonials, client names or results anywhere**, and every project is labelled as a placeholder.
- I removed "5+ clients served" from the hero, since your latest brief does not list it. Tell me if you want it back.
- Maintenance excludes unlimited development, major redesigns, new features and third-party costs.

## 8. Still needed from you

1. Portrait photo(s).
2. Project details and screenshots (name, client or industry, category, objective, your role, decisions, deliverables, live link).
3. Calendly URL, GHL webhook URL, LinkedIn and GitHub links.
4. Testimonials, only if clients approve them.
5. Confirmation of the items in section 7.

## 9. Quality check I ran

Layout was tested at 1440px and 390px across all seven pages with no horizontal overflow and no script errors. The 3D hero was rendered with real three.js and the real emoji in a headless browser. **Not verified:** the look on real devices, GHL's handling of the code blocks, form delivery, and performance on a mid-range phone. Please open the preview on your phone and tell me if the hero feels slow.
