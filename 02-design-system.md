# Azeez Gazalle: Design System

Built from your logo: a polished **gold monogram "AG" with a serif wordmark on black**. The system keeps that luxury feel and adds the glow and motion you liked on Yuyu's site.

> **Colour values below are a starting point sampled by eye from the logo.** Before building, pick the exact gold values from your logo file with an eyedropper and replace them. Keep the variable names.

---

## 1. Brand principles

1. **Black and gold first.** Gold is the single accent, so it stays rare and valuable.
2. **Premium, not flashy.** Glow is soft and reserved for actions and focal points.
3. **Developer credibility.** Clean grid, clear hierarchy and proof before decoration.
4. **Motion with purpose.** Animation guides attention and never blocks reading.

---

## 2. Colour tokens

```css
:root{
  /* Surfaces */
  --ag-bg:            #050505;   /* page background, near-black */
  --ag-bg-elevated:   #0d0d0f;   /* sections */
  --ag-card:          #141416;   /* cards */
  --ag-card-hover:    #1b1b1f;

  /* Text */
  --ag-text:          #f4ecdc;   /* warm off-white */
  --ag-text-muted:    #a79f90;
  --ag-text-dim:      #6e685d;   /* decorative only, never body copy */

  /* Gold (from logo) */
  --ag-gold-100:      #fff1c2;   /* highlight */
  --ag-gold-300:      #f6d36b;
  --ag-gold-500:      #e0a82e;   /* main brand gold */
  --ag-gold-700:      #a66f0f;
  --ag-gold-900:      #5a3a05;   /* deep shadow */

  /* Complementary accents */
  --ag-ember:         #ff8a3d;   /* warm secondary, for hovers and badges */
  --ag-indigo:        #3a2a8c;   /* cool complement, used only in background glows */

  /* Gradients */
  --ag-gold-gradient: linear-gradient(135deg,#fff1c2 0%,#f6d36b 28%,#e0a82e 60%,#a66f0f 100%);
  --ag-gold-text:     linear-gradient(100deg,#fff1c2,#e0a82e 55%,#f6d36b);

  /* Lines and effects */
  --ag-border:        rgba(246,211,107,.10);
  --ag-border-hover:  rgba(246,211,107,.28);
  --ag-glow:          0 0 40px rgba(224,168,46,.18);
  --ag-glow-strong:   0 0 60px rgba(224,168,46,.32);
  --ag-shadow:        0 10px 40px rgba(0,0,0,.45);

  /* Status */
  --ag-success:       #4ade80;
  --ag-error:         #f87171;
}
```

**Usage rules**
- Gold fills only on primary buttons, key words in headings, icons and thin lines.
- `--ag-indigo` appears only as a faint background glow behind the hero or cards, never as a UI colour.
- Body copy uses `--ag-text` or `--ag-text-muted`. Do not use `--ag-text-dim` for text people need to read.
- Check contrast: gold on black passes comfortably. Muted text on cards needs a check.

---

## 3. Typography

Premium tech sites get their punch from heavy, tight geometric type. The logo's serif wordmark is kept as the accent, so headings combine both.

| Role | Font (Google Fonts) | Weights | Use |
|------|---------------------|---------|-----|
| Headlines | **Sora** | 700, 800 | Big headings, tight tracking (-0.03em), white |
| Accent words | **Playfair Display** (italic) | 600 | The gold highlighted phrase in a heading, and the header wordmark (echoes the logo) |
| Body / UI | **Manrope** | 400, 500, 600, 700 | Paragraphs, buttons, nav |

**Scale (fluid)**

```css
--ag-fs-hero: clamp(2.05rem, 3.3vw + .95rem, 3.95rem);  /* Sora 800, line-height 1.02 */
--ag-fs-h2:   clamp(1.7rem, 2.4vw + 1rem, 2.5rem);
--ag-fs-h3:   1.25rem;
--ag-fs-body: 1rem;      /* line-height 1.65 */
--ag-fs-sm:   .875rem;
--ag-fs-xs:   .75rem;    /* letter-spacing .08em, uppercase labels */
```

---

## 4. Spacing, radius, layout

```css
--ag-space-1: 4px;  --ag-space-2: 8px;  --ag-space-3: 12px; --ag-space-4: 16px;
--ag-space-5: 24px; --ag-space-6: 32px; --ag-space-7: 48px; --ag-space-8: 72px; --ag-space-9: 120px;

--ag-radius-xs: 6px;  --ag-radius-sm: 10px;  --ag-radius: 16px;  --ag-radius-pill: 999px;

--ag-container: 1200px;
--ag-header-h: 72px;
--ag-ease: cubic-bezier(.4,0,.2,1);
--ag-ease-out: cubic-bezier(.2,.8,.2,1);
```

- Section padding: 72px mobile, 120px desktop.
- Grid: 12 columns on desktop, 1 column on mobile. Project cards: 3 per row, 2 on tablet, 1 on mobile.
- Breakpoints: 480, 768, 1024.

---

## 5. Components

| Component | Spec |
|-----------|------|
| **Header** | Transparent at top. After scroll: `rgba(10,10,10,.72)` with `backdrop-filter: blur(20px)` and a gold hairline border |
| **Primary button** | Pill, gold gradient fill, black text (600 weight), soft gold glow, shine sweep on hover |
| **Secondary button** | Pill, transparent, 1px gold border, gold text; fills faintly on hover |
| **Card** | `--ag-card` background, `--ag-border` hairline, 16px radius; on hover the border brightens and the card lifts 4px with a gold glow |
| **Project card** | Image on top (aspect 16:10), category pill, title, one-line result, "View project →" |
| **Category pill / filter chip** | Small pill; the active one gets gold fill |
| **Pricing card** | Card with price, bullet list and button; the "Most popular" card has a gold border and glow |
| **Stat block** | Large gold number, small label (for results like "+212% conversion") |
| **Testimonial** | Quote, name, role, company; slider or grid |
| **Form step** | Large question, one input, progress bar, Back and Continue buttons |
| **Footer** | Logo, nav, contact links, social icons, copyright |

**States:** every interactive element needs hover, focus-visible (2px gold ring with an offset), active and disabled states.

---

## 6. Motion tokens

| Effect | Spec |
|--------|------|
| Scroll reveal | `opacity 0 to 1`, `blur 8px to 0`, `translateY 30px to 0`, 0.8s `--ag-ease-out`, stagger 80ms |
| Button shine | A pseudo-element gradient sweeping left to right in 0.6s on hover |
| Card tilt | Max 8° rotate on pointer move, with `perspective: 800px` |
| Rotating hero word | Words swap every 2.4s, container width animates to fit |
| Marquee | Linear, 30 to 40s loop, pauses on hover |
| Hero portrait border | Slow rotating conic gradient in gold |
| Hero 3D | See the implementation plan, section 4 |

**Always include:**

```css
@media (prefers-reduced-motion: reduce){
  *,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}
}
```

---

## 7. Imagery and logo

- Export the logo as **SVG** or a transparent PNG so it sits cleanly on any background. The current file has a black background baked in.
- Provide a **monogram-only** version (the AG) for the favicon and header on mobile.
- Your **portrait**: ideally a clean, well-lit photo with a dark or neutral background so it blends into the dark theme. A subtle gold rim light or border works well.
- Project images: use a consistent frame (browser or device mockup) and 16:10 ratio, in WebP.
- OG image 1200 × 630: logo plus tagline on black.

---

## 8. Voice

Confident, clear and direct. Short sentences. Lead with outcomes.

- Instead of "I am a passionate developer…", use "I build fast, conversion-focused websites and web apps for growing businesses."
- Every project mentions a result, even a small one.
