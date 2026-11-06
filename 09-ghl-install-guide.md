# 09: Complete guide to putting the portfolio into GoHighLevel

You will build 8 + 11 pages. Each page is a normal GHL page with one **Custom Code** element per section. Nothing here needs a developer account; everything is pasted into the page builder.

## 0. What is in the zip (`ag-sections-v8.zip`)
- `sections/`: one `.html` file per section (what you paste).
- `assets/projects/`: the only images you must upload (project covers and screenshots, about 72 files, a few MB).
- `08-v7-page-map-and-assets.md`: the page map (kept for reference).
Everything else (hero portrait, avatars, 3D emoji, logo) is **already embedded inside the section files**. You do not upload it.

## 0b. Shortcut: one core block (`ghl/00-site-core.html`)
`00-loader`, `00-global`, `00-emoji-pack`, `00-avatars` and `00-projects` are also supplied already merged as `ghl/00-site-core.html`. Paste that single file once at the top of every page (or once in the site-wide Header code) **instead of** those five blocks, never both. Your image links go in its `00-projects` part.

## 1. Before you start
1. Unzip the file on your computer. Open files in a plain text editor (Notepad, VS Code). Do not use Word.
2. Open the file, press `Ctrl+A`, then `Ctrl+C`. Paste it whole into the GHL code box. Never paste half a file.
3. Large blocks: `00-avatars` (about 170 KB), `00-emoji-pack` (about 130 KB) and `home-hero` (about 85 KB) are the biggest. If a code box refuses one, see the Troubleshooting table (section 9).

## 2. Upload the project images first
1. In GHL go to **Media Storage** (left menu), create a folder named `portfolio-projects`.
2. Upload **every file** from `assets/projects/` (drag all at once).
3. For each file, open it and copy its link. Links look like `https://storage.googleapis.com/msgsndr/<id>/media/<id>.webp` (the exact form can vary). They do **not** keep the file name, so keep a note of which link belongs to which file.
4. Tip to save time: upload one file at a time in alphabetical order, paste the link into a text file next to its name as you go.

## 3. Put the image links into `00-projects`
`00-projects` is the single place that holds every project's text and image paths.
1. Open `sections/00-projects.html` in your text editor.
2. Find each path that starts `assets/projects/` (for example `assets/projects/cropzone-africa-cover.webp`). There are 72.
3. Use **Find and Replace** (`Ctrl+H` in VS Code): replace each `assets/projects/<name>.webp` with the full GHL link you noted.
4. Save the file. This is the version you will paste into GHL.
Do this once; the same block is reused on every page.

## 4. Create the pages
Funnels/Websites → **Websites** → your site (create one called "Azeez Gazalle" if needed) → **Pages** → **Add page**. Use these exact paths (the menu links depend on them):

| Page name | Path |
|---|---|
| Home | `/` (set as the home page) |
| Work | `work` |
| Services | `services` |
| Process | `process` |
| About | `about` |
| Contact | `contact` |
| Start a project | `start` |
| 11 project pages | `work/<slug>` (see table in section 6) |

If your GHL does not allow a slash in a path, create the page paths as `work-cropzone-africa` and so on, then change `work:'/work'` entries and the project links as described in section 8.

## 4b. Connecting the pages to each other (one table, in `00-global`)
All menu links, buttons and project cards are rewritten from a single table at the bottom of `00-global`, so you never edit links in other blocks. Every page must contain `00-global`.
1. Publish your pages and open each one in the browser. Note the real address of each (for example `https://yourdomain.com/work`).
2. In `00-global`, find `AG SITE LINKS` and edit:
   - `MAP`: put the real path of each page on the right-hand side, e.g. `'/work':'/our-work'`.
   - `PROJECTS`: `'/work/'` if your project paths are `work/<slug>`; `'/work-'` if GHL only allowed flat paths like `work-cropzone-africa`.
   - `BASE`: a prefix if all your pages sit under a folder, e.g. `'/portfolio'`.
   - `DOMAIN`: your full domain (e.g. `'https://www.azeezgazalle.com'`) if relative links do not work in your account, or while testing on a GHL preview address.
3. Re-paste `00-global` into every page (or, better, put it once in Settings, Custom Code, Header so all pages share it).
Links to pages that do not exist yet will 404, so create all pages first.

## 5. Build each page (blocks in this exact order)
For every block: in the builder add a **Section → Row → Column → Custom JS/HTML** element, paste the file contents, save. Use one section per block, set the section **padding to 0** and **background to none**, so GHL adds no extra spacing.

**Common top blocks** (every page): `00-loader`, `00-global`, `00-emoji-pack`, `00-avatars`, `00-projects`.
**Common bottom blocks** (every page): `footer`, `whatsapp-float`. Put `header` straight after the common top blocks.

| Page | Blocks between header and footer |
|---|---|
| Home `/` | `home-hero`, `logo-marquee`, `home-about`, `home-services`, `home-work`, `home-process`, `home-testimonials`, `home-cta` |
| Work `/work` | `page-hero-work`, `work-showcase`, `home-cta` |
| Project `/work/<slug>` | `project-<slug>`, `home-cta` |
| Services | `page-hero-services`, `services-list`, `services-terms`, `home-cta` |
| Process | `page-hero-process`, `process-steps`, `why-me`, `faq`, `home-cta` |
| About | `page-hero-about`, `about-story`, `home-cta` |
| Contact | `contact-section` |
| Start | `start-form` |

Tip: build the Home page first, then use GHL's **Duplicate page** and swap the middle blocks, so the common blocks are already in place.

## 6. The 11 project pages
Each uses `project-<slug>.html` for its middle block.

| Page path | File |
|---|---|
| `/work/cropzone-africa` | `project-cropzone-africa` |
| `/work/nubid-engineering` | `project-nubid-engineering` |
| `/work/quietpalm` | `project-quietpalm` |
| `/work/caliph-engineering` | `project-caliph-engineering` |
| `/work/pilgrim-prive` | `project-pilgrim-prive` |
| `/work/proventa` | `project-proventa` |
| `/work/faucet-water-purifier-funnel` | `project-faucet-water-purifier-funnel` |
| `/work/ginseng-five-treasure-tea-funnel` | `project-ginseng-five-treasure-tea-funnel` |
| `/work/talk-to-ai-like-a-pro` | `project-talk-to-ai-like-a-pro` |
| `/work/adjustable-laptop-workstation` | `project-adjustable-laptop-workstation` |
| `/work/foldable-hand-fan` | `project-foldable-hand-fan` |

## 7. Page settings in GHL (do for every page)
1. **Page background**: set to `#07070A` (so there is no white flash).
2. **Hide GHL's own header/footer** and any default top padding. Make the page content width **Full width**.
3. **Settings → SEO**: give each page a title, for example "Azeez Gazalle, web designer and developer (Nigeria)". Add a short description. Add a favicon (use `assets/img/logo.png`).
4. **Tracking code** (Settings → Tracking Code): leave empty unless you use Meta Pixel.
5. Save, then **Preview** before publishing.

## 8. Things you can edit inside the blocks
Everything is at the top of each block's script, under the `EDIT` comment.

| What | Block | Name to look for |
|---|---|---|
| Menu and button paths | `header`, `footer`, others | `LINKS` |
| Social links | `footer` | `SOCIAL` (add `{label:'Instagram',url:'https://...'}`) |
| Contact form webhook | `contact-section`, `start-form` | `WEBHOOK_URL` (already set to your GHL webhook) |
| Calendly | same two blocks | `CALENDLY_URL` (already set) |
| Testimonials | `home-testimonials` | `TESTIMONIALS` |
| Project words and image links | `00-projects` | one place for everything |

## 9. Test before publishing
- Open the live URL on your **phone** and your laptop.
- Click every menu link and every "Start a project" button.
- Open two project pages and check that images load.
- Submit the contact form with a test message. In GHL open **Contacts** to confirm it arrived. If it does not, open the webhook's workflow and map the incoming fields.
- Use the light/dark toggle once.
- The loader shows only the first time per browser session; open a private window to see it again.

## 10. Troubleshooting

| Problem | Fix |
|---|---|
| Code box rejects a big block | Split it: paste into two Custom Code elements one above the other is **not** safe for scripts. Instead, move `00-avatars` and `00-emoji-pack` to **Settings → Custom Code → Header** (site-wide, once) and remove them from pages. |
| Page shows plain text / code | You pasted into a Text element. Use **Custom JS/HTML**. |
| Images missing in projects | A link in `00-projects` is wrong. Open the image link in a new tab to check it. |
| Gap or white strip between blocks | Set that section's padding and margin to 0. |
| Menu goes to a 404 | The page path does not match `LINKS`. Fix the path or edit `LINKS`. |
| Hero shows a flat 2D version | Normal fallback when the 3D library cannot load; it works but without depth. |
| Fonts look different | Check `00-global` is on the page. |

## 11. Suggested order of work (about 2 to 3 hours)
1. Upload images, edit `00-projects` (sections 2 and 3).
2. Build Home, preview, fix spacing.
3. Duplicate for Work, then Services, Process, About, Contact, Start.
4. Duplicate for the 11 project pages.
5. Connect your domain (Settings → Domains), publish, run the tests in section 9.

Note: I could not test inside GoHighLevel itself, so the first page you build is the test. If any step differs in your account (menu names, path rules, code size limit), tell me what you see and I will adjust the files.
