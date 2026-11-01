# Azeez Gazalle: Portfolio Implementation Plan

**Goal:** get business owners and anyone needing a modern website or web app to hire Azeez.
**Strength to lead with:** development (design supports it).
**Look:** black and gold, glowing, with strong motion and a little 3D.
**Host:** GoHighLevel (GHL) first, so everything must be plain HTML, CSS and vanilla JS that pastes into GHL custom code.

---

## 1. Site map (separate pages)

| # | Page | Purpose | Main call to action |
|---|------|---------|---------------------|
| 1 | **Home** | Hook, proof, featured work, pricing teaser | Start a Project |
| 2 | **Projects** | All work, filterable by category | Open a project |
| 3 | **Project (case study)** | One template, filled from a data object | Start a Project |
| 4 | **Pricing** | Packages per service | Choose a package |
| 5 | **About** | Career story, skills, photo | Start a Project |
| 6 | **Start a Project** | Conversational form | Submit |
| 7 | *Blog (later)* | Reserved route, not built in v1 | n/a |

**Note on the case-study page:** instead of creating one GHL page per project, build **one** case-study page that reads `?project=slug` and renders content from the `projects-data.html` block (see section 2). Adding a project then means adding one object, not building a new page. Test that GHL passes query strings through on your account before committing to this. The fallback is one GHL page per project using the same template.

Shared sections on every page: header (logo, nav, "Start a Project" button), footer and a WhatsApp floating button. Each one is its own pasteable section, not part of a page template.

---

## 2. Architecture for GHL: one code block per section

**Rule: every section is its own self-contained block.** In GHL you add a Custom Code (or Custom HTML/JS) element to each section and paste that section's file into it. Nothing is built "per page", so you can reorder, reuse or replace a section on any page without touching the rest.

### What a section file contains

Each file in `sections/` has the same three parts, in this order:

```html
<!-- ========== AG SECTION: hero ========== -->
<style>
  /* 1. Fallback tokens scoped to this section, so it renders correctly even if the Global block is missing */
  .ag-hero{ --ag-bg:#050505; --ag-text:#f4ecdc; --ag-gold-500:#e0a82e; /* …only the tokens this section uses */ }
  /* 2. All styles, every selector starting with .ag-hero */
</style>

<section class="ag-hero"> … markup … </section>

<script>
  (function(){            /* 3. Scoped, idempotent JS */
    var root=document.querySelector('.ag-hero'); if(!root||root.dataset.agInit) return; root.dataset.agInit='1';
    /* …this section's behaviour only… */
  })();
</script>
```

**Rules that make sections safe to paste anywhere**
- **Unique prefix per section** (`.ag-hero`, `.ag-pricing`, `.ag-form`…). No bare tags like `h2{}` or `body{}` in section CSS.
- **No dependence on other sections.** A section never reads another section's elements.
- **Idempotent JS**: the `data-ag-init` guard means pasting or previewing twice can't double-run it.
- **Fallback tokens inside each section**, so a section still looks right on its own. The Global block (below) overrides them with the full token set, so one change to the brand gold updates everything.
- **No external CSS or JS files required.** The only external script is Three.js on the hero, loaded by that section itself, once.
- Images are referenced by full URL (GHL media library or a CDN), never relative paths.

### The Global block (pasted once per site, not per page)

A small optional block that holds what is truly shared: the full token set, Google Fonts links, the base reset scoped under `[class*="ag-"]`, the reduced-motion rule, and the shared scroll-reveal observer. Put it in GHL's **site-wide header/custom code** area if your account offers one. Otherwise paste it as the first block of each page, and because sections carry their own fallbacks, a page still works if it is skipped.

### Section library

| File | Used on | Contains |
|------|---------|----------|
| `00-global.html` | Site-wide | Tokens, fonts, reduced-motion, reveal observer |
| `header.html` | All pages | Logo, nav, glass-on-scroll header, mobile menu, CTA button |
| `footer.html` | All pages | Logo, links, contacts, socials |
| `whatsapp-float.html` | All pages | Floating WhatsApp button |
| `home-hero.html` | Home | Headline, rotating words, portrait, 3D (Three.js, desktop only) |
| `home-tools-marquee.html` | Home | Scrolling strip of tools |
| `home-featured-projects.html` | Home | 3 to 4 featured cards |
| `home-services.html` | Home | Six category cards |
| `home-pricing-teaser.html` | Home | Short pricing summary |
| `home-testimonials.html` | Home, About | Slider |
| `cta-banner.html` | Most pages | "Ready to start?" banner |
| `projects-grid.html` | Projects | Filter chips plus project cards |
| `project-detail.html` | Project | Case-study layout, reads `?project=slug` |
| `projects-data.html` | Projects, Home, Project | **Data-only block**: the list of projects, see below |
| `pricing-plans.html` | Pricing | Package cards per service, billing toggle if needed |
| `pricing-faq.html` | Pricing | Accordion |
| `about-intro.html` | About | Portrait, career summary |
| `about-timeline.html` | About | Roles and experience |
| `about-skills.html` | About | Skills and tools |
| `start-form.html` | Start a Project | Conversational form, GHL webhook, WhatsApp fallback |

### How project data is shared without a shared file

Because sections can't depend on each other, project content lives in one small block, `projects-data.html`:

```html
<script>
  window.AG_PROJECTS = window.AG_PROJECTS || [ /* { slug, name, category, … } */ ];
</script>
```

Paste it above any section that needs the list (Home featured, Projects grid, Project detail). Each of those sections reads `window.AG_PROJECTS` and, if it is missing, falls back to a tiny built-in sample so nothing breaks. Adding a project means editing this one block and re-pasting it where it appears.

If you would rather each section carry its own copy of the data (more repetition, zero cross-dependency), say so and I'll build it that way.

### Page recipes (which sections go on which page)

| Page | Sections, top to bottom |
|------|--------------------------|
| **Home** | header, home-hero, home-tools-marquee, home-featured-projects, home-services, home-pricing-teaser, home-testimonials, cta-banner, footer, whatsapp-float |
| **Projects** | header, projects-data, projects-grid, cta-banner, footer, whatsapp-float |
| **Project** | header, projects-data, project-detail, cta-banner, footer, whatsapp-float |
| **Pricing** | header, pricing-plans, pricing-faq, cta-banner, footer, whatsapp-float |
| **About** | header, about-intro, about-timeline, about-skills, home-testimonials, cta-banner, footer, whatsapp-float |
| **Start a Project** | header, start-form, footer, whatsapp-float |

Header, footer and the WhatsApp button are repeated blocks. If GHL offers global or reusable sections on your account, use them for these three so one edit updates every page. I haven't verified that feature, so Phase 0 checks it.

### Repo layout (the source of truth; you paste from here)

```
azeez-portfolio/
  sections/
    00-global.html
    header.html  footer.html  whatsapp-float.html  cta-banner.html
    home-hero.html  home-tools-marquee.html  home-featured-projects.html
    home-services.html  home-pricing-teaser.html  home-testimonials.html
    projects-data.html  projects-grid.html  project-detail.html
    pricing-plans.html  pricing-faq.html
    about-intro.html  about-timeline.html  about-skills.html
    start-form.html
  assets/   img/ (logo, photo, project images)
  docs/     (these .md files)
```

Every file in `sections/` is deliverable as-is: open it, copy everything, paste into one GHL custom code element.

### What still needs testing on your GHL account (Phase 0)

I haven't verified these, so the first task is a throwaway test page:
- Maximum size of one custom code block (this decides whether the hero with Three.js logic fits in one block)
- Whether `<style>` and `<script>` inside a section run as expected, and whether GHL moves or strips them
- Whether external scripts (Three.js CDN, Google Fonts) load inside a block
- Whether query strings (`?project=slug`) survive on a GHL page
- Whether global or reusable sections and site-wide header code exist for your plan
- Whether the form can post to a GHL inbound webhook from the page

Other rules: keep the same prefix discipline (`ag-`) so GHL's own styles don't collide, remove default section padding in GHL where our section sets its own, and set each page's SEO title, description and social image in GHL's page settings.

---

## 3. The conversational form (lead capture)

Steps, one question at a time with a progress bar:

1. Name
2. Where are you based? (Nigeria, UK, US, UAE, Other)
3. Project type (matches the six categories)
4. Business or product name
5. Timeline
6. Budget (USD or ₦, with ranges)
7. Short brief
8. How should we send this? (WhatsApp, email, or "call me")
9. Contact details, then Submit

**Delivery**
- On submit, the JS `POST`s JSON to a **GHL Workflow "Inbound Webhook"** URL. The workflow creates or updates the contact, adds tags (`portfolio-lead`, the project type), and notifies you by email and SMS or WhatsApp.
- A "Send via WhatsApp" option opens `wa.me/<number>?text=` with the answers pre-filled.
- A hidden honeypot field and a minimum fill time reduce spam.
- Show a success state with what happens next ("I reply within X hours").

**Do not** place secrets or API keys in the page. The webhook URL is public by nature, so protect it with the honeypot and keep the workflow limited to creating a contact.

---

## 4. 3D and motion

**Hero 3D, three options (choose one)**

| Option | What it is | Effort | Why you might pick it |
|--------|-----------|--------|------------------------|
| **A. Gold particle "AG"** | Gold particles drift, then gather into the AG monogram as you move the cursor or scroll | Medium | Ties directly to your logo |
| **B. Metallic gold ring** | A glossy rotating torus/ribbon with reflections that reacts to the mouse | Medium | Closest to the logo's polished-metal look |
| **C. Tilting mockup cards** | CSS 3D tilt on project/device cards, no WebGL | Low | Lightest on mobile and in GHL |

**My recommendation:** B or A in the hero (Three.js r128 from a CDN), plus C's tilt effect on project cards.

**Rules**
- Disable WebGL on screens 768px wide or less and show a static image or CSS glow.
- Respect `prefers-reduced-motion` (Yuyu's site doesn't, so this is an easy improvement).
- Pause rendering when the hero is off-screen (`IntersectionObserver`).
- Cap the pixel ratio at 2.

**Motion kit (all CSS and vanilla JS)**
- Blur-up scroll reveal (opacity, blur, translateY, with staggered delays)
- Rotating words in the hero ("Websites / Stores / Funnels / Web Apps")
- Gold shine sweep on buttons
- Marquee strip of tools or categories
- Sticky header that turns to glass after scrolling
- Animated gold gradient border on the hero portrait
- Filter transitions on the projects grid

---

## 5. Phases

### Phase 0: Foundations
- [ ] Collect logo (SVG or transparent PNG), photo, project list, pricing, contact details (see `04-content-checklist.md`)
- [ ] Build the GHL test page and confirm: custom code limits, external scripts, query strings, fonts, webhook post
- [ ] Set up the `sections/` folder and confirm one section pastes and runs as a single custom code block

### Phase 1: Design system
- [ ] Finalise tokens, type, components (see `02-design-system.md`)
- [ ] Build `00-global.html` (tokens, fonts, reduced-motion, reveal observer)
- [ ] Build `header.html`, `footer.html`, `whatsapp-float.html` and `cta-banner.html` as standalone sections

### Phase 2: Sections, built and delivered one at a time
Each item is one standalone file you can paste right away.
- [ ] Home: `home-hero`, `home-tools-marquee`, `home-featured-projects`, `home-services`, `home-pricing-teaser`, `home-testimonials`
- [ ] Projects: `projects-data`, `projects-grid`
- [ ] Project: `project-detail`
- [ ] Pricing: `pricing-plans`, `pricing-faq`
- [ ] About: `about-intro`, `about-timeline`, `about-skills`

### Phase 3: Lead capture
- [ ] `start-form` section, GHL webhook workflow, WhatsApp fallback, success state
- [ ] Notifications and tags in GHL

### Phase 4: Motion and 3D
- [ ] Reveal, rotating words, marquee, tilt cards
- [ ] Hero 3D with mobile fallback and reduced-motion handling

### Phase 5: Quality and launch
- [ ] Mobile pass at 360, 390, 768, 1024 and 1440px
- [ ] Performance: images as WebP/AVIF with width and height, lazy loading, fonts with `display=swap`
- [ ] Accessibility: contrast, focus rings, alt text, keyboard-friendly form
- [ ] SEO: titles, descriptions, OG images, JSON-LD (`Person` and `ProfessionalService`)
- [ ] Analytics: GHL tracking plus GA4 and/or a Meta pixel
- [ ] Test the form end to end (webhook, contact created, notification received)
- [ ] Go live on GHL and connect the domain

### Phase 6: Later
- [ ] Blog (reserved route and nav slot, built after launch)
- [ ] More projects by editing `projects-data.html` and re-pasting it
- [ ] Testimonials and case-study metrics as they come in

---

## 6. Success checks

- Home loads in a few seconds on a mid-range Android phone over 4G
- A visitor can reach "Start a Project" from every page in one click
- A test submission creates a GHL contact and notifies you within a minute
- All six categories filter correctly
- No horizontal scroll on mobile
- Motion is skipped for users with reduced-motion enabled

---

## 7. Risks and mitigations

| Risk | Mitigation |
|------|-----------|
| GHL strips or limits scripts | Test in Phase 0 and keep a fully inlined fallback |
| Three.js is heavy on low-end phones | Desktop-only 3D, static fallback elsewhere |
| A shared change must be re-pasted in many places | Keep the Global block for tokens only; use GHL reusable sections for header and footer if available |
| One section's code is too large for a single block | Check the limit in Phase 0; split the hero's 3D into its own block if needed |
| Spam on the form | Honeypot, timing check, webhook limited to contact creation |
| Content arrives late | Build with placeholder projects and swap real ones later |
