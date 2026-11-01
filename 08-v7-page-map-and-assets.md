# v7: page map, paste order and assets

## Pages (separate URLs, each its own GoHighLevel page)
| URL | Paste these blocks, top to bottom |
|---|---|
| `/` | 00-loader, 00-global, 00-emoji-pack, 00-avatars, 00-projects, header, home-hero, logo-marquee, home-about, home-services, home-work, home-process, home-testimonials, home-cta, footer, whatsapp-float |
| `/work` | 00-loader, 00-global, 00-emoji-pack, 00-avatars, 00-projects, header, page-hero-work, work-showcase, home-cta, footer, whatsapp-float |
| `/work/<slug>` (9 pages) | 00-loader, 00-global, 00-emoji-pack, 00-avatars, 00-projects, header, `project-<slug>`, home-cta, footer, whatsapp-float |
| `/services`, `/process`, `/about`, `/contact`, `/start` | unchanged from v6. `/about` and `/work` use the new page-hero text. |

## Project slugs and pages
| # | Project | Type | Page URL |
|---|---|---|---|
| 01 | Cropzone Africa | Website | /work/cropzone-africa |
| 02 | Nubid Engineering | Website | /work/nubid-engineering |
| 03 | QuietPalm | Website | /work/quietpalm |
| 04 | Caliph Engineering Limited | Website | /work/caliph-engineering |
| 05 | Pilgrim Privé | Website | /work/pilgrim-prive |
| 06 | Proventa Global Business Services Ltd. | Website | /work/proventa |
| 07 | 6-Layer Faucet Water Purifier Offer | Sales funnel | /work/faucet-water-purifier-funnel |
| 08 | Ginseng Five Treasure Tea Sales Funnel | Sales funnel | /work/ginseng-five-treasure-tea-funnel |
| 09 | "Talk to AI Like a Pro" Sales Page | Sales funnel | /work/talk-to-ai-like-a-pro |
| 10 | Adjustable Mobile Laptop Workstation Funnel | Sales funnel | /work/adjustable-laptop-workstation |
| 11 | Foldable Hand Fan Funnel | Sales funnel | /work/foldable-hand-fan |

The Work page filter has three buttons: All work, Websites, Sales funnels and landing pages. The Home stack shows the projects marked `featured` in `00-projects` (Cropzone, Pilgrim Privé, Proventa, Faucet Water Purifier).

## Editing project text
All project words and image addresses live in one block: `00-projects`. Change a line there and the Home stack, the Work page and the case study update.

## Project images (about 3 MB in total)
Upload every file in `assets/projects/` to the GHL media library. Then, in `00-projects`, replace each `assets/projects/...webp` path with the full https address GHL gives you (find and replace).
- `<slug>-cover.webp`: the designed mockup used on the cards and at the top of each case study.
- `<slug>-screen-NN.webp`: screenshots, with the browser frame and Windows taskbar cropped out.
Originals in the Portfoli Assets folder were not changed.

## Avatars and portrait
- Hero portrait: `assets/photos/hero-portrait.webp` (from `hero_image-removebg-preview.png`, transparent). Embedded in `home-hero`.
- Circular avatars: `assets/avatars/avatar-smile-badge.webp` and `avatar-neutral-badge.webp`. Face centred on the disc. The same smile badge is the loader image.
- CTA main image: `assets/avatars/avatar-smile.webp`; one circle: `avatar-neutral-badge.webp`.

## Facts taken from your info files, and fixes
Typos corrected: "Semptember" to September 2026, "Ltd" for "Lts.", "[cite: n]" removed, second person changed to first person. No results, metrics or testimonials were supplied, so none are shown; each case study ends with a factual "Status" line instead.

## v8 changes
- Projects 10 and 11 added (new project pages `project-adjustable-laptop-workstation` and `project-foldable-hand-fan`; upload their images from `assets/projects/`).
- Four real testimonials added to `home-testimonials`.
- Client name removed from Cropzone Africa.
- Footer: LinkedIn removed; Instagram and Facebook left out for now (add `{label:'Instagram',url:'...'}` to the `SOCIAL` array in `footer` later).
