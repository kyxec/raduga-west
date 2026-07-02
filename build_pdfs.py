import os
import subprocess

# Define the HTML template with CSS styling optimized for 9:16 mobile screens
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <title>Raduga West 506 Offline Guide</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --color-bg-base: hsl(210, 30%, 97%);
            --color-bg-card: hsl(0, 0%, 100%);
            --color-bg-card-alt: hsl(38, 60%, 98%);
            --color-blue: hsl(207, 95%, 48%);
            --color-blue-dark: hsl(212, 95%, 35%);
            --color-blue-light: hsl(207, 95%, 94%);
            --color-amber: hsl(38, 92%, 50%);
            --color-amber-dark: hsl(38, 92%, 35%);
            --color-amber-light: hsl(38, 92%, 95%);
            --color-green: #25D366;
            --color-red: hsl(352, 85%, 52%);
            --color-red-light: hsl(352, 85%, 96%);
            --color-text-title: hsl(215, 50%, 15%);
            --color-text-body: hsl(215, 20%, 35%);
            --color-text-muted: hsl(215, 12%, 55%);
            --font-heading: 'Outfit', sans-serif;
            --font-body: 'Inter', sans-serif;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: var(--font-body);
            background-color: var(--color-bg-base);
            color: var(--color-text-body);
            line-height: 1.45;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }}

        /* Page definitions for Chrome PDF printing */
        @page {{
            size: 375px 812px;
            margin: 0;
        }}

        .page {{
            width: 375px;
            height: 812px;
            page-break-after: always;
            position: relative;
            overflow: hidden;
            padding: 24px 20px;
            background-color: var(--color-bg-base);
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }}

        /* Header / Footer elements inside slides */
        .slide-header-meta {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.65rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--color-text-muted);
            margin-bottom: 16px;
            font-family: var(--font-heading);
            font-weight: 700;
        }}

        .slide-header-meta .room-badge {{
            background-color: var(--color-blue-light);
            color: var(--color-blue-dark);
            padding: 2px 6px;
            border-radius: 4px;
        }}

        .slide-title-row {{
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 20px;
        }}

        .slide-icon-box {{
            width: 32px;
            height: 32px;
            background-color: var(--color-blue-light);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--color-blue);
        }}

        .slide-icon-box svg {{
            width: 18px;
            height: 18px;
            stroke-width: 2.5px;
        }}

        .slide-title-row h2 {{
            font-family: var(--font-heading);
            font-size: 1.25rem;
            color: var(--color-text-title);
            font-weight: 700;
        }}

        /* Slide 1: Cover Layout */
        .cover-page {{
            background-size: cover;
            background-position: center;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 40px 24px;
        }}

        .cover-overlay {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(to top, rgba(13, 37, 80, 0.95) 25%, rgba(13, 37, 80, 0.5) 60%, rgba(13, 37, 80, 0.2) 100%);
            z-index: 1;
        }}

        .cover-content {{
            position: relative;
            z-index: 2;
            color: #ffffff;
        }}

        .cover-logo-svg {{
            width: 38px;
            height: 38px;
            margin-bottom: 12px;
            color: var(--color-blue-light);
        }}

        .cover-title {{
            font-family: var(--font-heading);
            font-size: 1.8rem;
            font-weight: 800;
            line-height: 1.2;
            margin-bottom: 8px;
            letter-spacing: -0.01em;
        }}

        .cover-subtitle {{
            font-size: 0.85rem;
            color: var(--color-blue-light);
            margin-bottom: 24px;
            line-height: 1.4;
            font-weight: 500;
        }}

        .cover-badge {{
            display: inline-block;
            background: linear-gradient(135deg, var(--color-amber), hsl(38, 92%, 45%));
            color: #ffffff;
            font-family: var(--font-heading);
            font-weight: 700;
            font-size: 0.8rem;
            padding: 6px 16px;
            border-radius: 8px;
            letter-spacing: 0.05em;
        }}

        /* Elements & Card Layouts */
        .card {{
            background-color: var(--color-bg-card);
            border: 1px solid var(--color-border);
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 16px;
            box-shadow: 0 4px 15px -3px rgba(13, 37, 80, 0.03);
        }}

        .card-header-row {{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 8px;
        }}

        .card-header-row svg {{
            width: 16px;
            height: 16px;
            color: var(--color-blue);
        }}

        .card-header-row h3 {{
            font-family: var(--font-heading);
            font-size: 0.95rem;
            color: var(--color-text-title);
            font-weight: 700;
        }}

        .card p {{
            font-size: 0.78rem;
            line-height: 1.45;
            color: var(--color-text-body);
        }}

        /* Highlight Boxes */
        .highlight-box {{
            background-color: var(--color-amber-light);
            border-left: 3.5px solid var(--color-amber);
            border-radius: 0 8px 8px 0;
            padding: 10px 12px;
            display: flex;
            gap: 10px;
            align-items: flex-start;
            margin-top: 10px;
        }}

        .highlight-box.warning {{
            background-color: var(--color-red-light);
            border-left-color: var(--color-red);
        }}

        .highlight-box svg {{
            width: 15px;
            height: 15px;
            color: var(--color-amber-dark);
            flex-shrink: 0;
            margin-top: 1px;
        }}

        .highlight-box.warning svg {{
            color: var(--color-red);
        }}

        .highlight-text strong {{
            display: block;
            font-size: 0.75rem;
            font-family: var(--font-heading);
            color: var(--color-text-title);
            margin-bottom: 2px;
            font-weight: 700;
        }}

        .highlight-text p {{
            font-size: 0.72rem;
            line-height: 1.35;
            color: var(--color-text-body);
        }}

        /* Buttons in PDF */
        .btn {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            font-family: var(--font-heading);
            font-weight: 700;
            font-size: 0.8rem;
            padding: 10px 16px;
            border-radius: 10px;
            text-decoration: none;
            width: 100%;
            text-align: center;
            border: 1px solid transparent;
            margin-top: 10px;
        }}

        .btn-teal {{
            background: linear-gradient(135deg, var(--color-blue), var(--color-blue-dark));
            color: #ffffff;
        }}

        .btn-outline {{
            background-color: transparent;
            color: var(--color-blue-dark);
            border: 1.5px solid var(--color-blue);
        }}

        .btn-whatsapp {{
            background-color: var(--color-green);
            color: #ffffff;
        }}

        .btn-phone {{
            background-color: #ffffff;
            color: var(--color-text-title);
            border: 1px solid rgba(13, 37, 80, 0.12);
        }}

        .btn-svg {{
            width: 14px;
            height: 14px;
            fill: currentColor;
        }}

        .btn-svg-stroke {{
            width: 14px;
            height: 14px;
            fill: none;
            stroke: currentColor;
            stroke-width: 2px;
        }}

        /* Amenities layout */
        .amenities-grid {{
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}

        .amenity-card {{
            display: flex;
            gap: 12px;
            background-color: var(--color-bg-card);
            border: 1px solid var(--color-border);
            border-radius: 10px;
            padding: 12px;
        }}

        .amenity-card.warning-card {{
            border-left: 3.5px solid var(--color-red);
        }}

        .amenity-icon {{
            width: 28px;
            height: 28px;
            background-color: var(--color-blue-light);
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--color-blue);
            flex-shrink: 0;
        }}

        .amenity-icon.text-red {{
            color: var(--color-red);
            background-color: var(--color-red-light);
        }}

        .amenity-icon.text-amber {{
            color: var(--color-amber-dark);
            background-color: var(--color-amber-light);
        }}

        .amenity-icon svg {{
            width: 16px;
            height: 16px;
        }}

        .amenity-info {{
            flex: 1;
        }}

        .amenity-info h4 {{
            font-family: var(--font-heading);
            font-size: 0.85rem;
            color: var(--color-text-title);
            font-weight: 700;
            margin-bottom: 2px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .status-badge {{
            font-size: 0.6rem;
            padding: 1px 5px;
            border-radius: 4px;
            font-weight: 700;
        }}

        .status-badge.error {{
            background-color: var(--color-red-light);
            color: var(--color-red);
        }}

        .status-badge.success {{
            background-color: rgba(37, 211, 102, 0.08);
            color: #12b74b;
        }}

        .status-badge.info {{
            background-color: var(--color-blue-light);
            color: var(--color-blue-dark);
        }}

        .amenity-info p {{
            font-size: 0.72rem;
            line-height: 1.35;
            color: var(--color-text-body);
        }}

        /* Dining Layout */
        .dining-list {{
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}

        .dining-card {{
            padding: 12px 14px;
        }}

        .dining-badge {{
            display: inline-block;
            font-size: 0.58rem;
            font-weight: 700;
            color: #ffffff;
            padding: 2px 6px;
            border-radius: 3px;
            text-transform: uppercase;
            margin-bottom: 4px;
        }}

        .dining-card h3 {{
            font-family: var(--font-heading);
            font-size: 0.95rem;
            color: var(--color-text-title);
            font-weight: 700;
        }}

        .dining-cuisine {{
            font-size: 0.68rem;
            font-weight: 700;
            color: var(--color-blue-dark);
            text-transform: uppercase;
            margin-bottom: 4px;
        }}

        .dining-card p {{
            font-size: 0.72rem;
            line-height: 1.35;
        }}

        .dining-card .btn {{
            padding: 6px 12px;
            font-size: 0.72rem;
            margin-top: 6px;
        }}

        /* SPA Layout */
        .spa-list {{
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}

        .spa-card {{
            padding: 0;
            overflow: hidden;
        }}

        .spa-img-box {{
            width: 100%;
            height: 90px;
            position: relative;
        }}

        .spa-img-box img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}

        .spa-caption {{
            position: absolute;
            bottom: 6px;
            left: 8px;
            background-color: #ffffff;
            font-size: 0.58rem;
            font-weight: 700;
            color: var(--color-blue-dark);
            padding: 2px 6px;
            border-radius: 3px;
        }}

        .spa-card-content {{
            padding: 10px 12px;
        }}

        .spa-card-content h3 {{
            font-family: var(--font-heading);
            font-size: 0.85rem;
            color: var(--color-text-title);
            font-weight: 700;
            margin-bottom: 2px;
        }}

        .spa-card-content p {{
            font-size: 0.7rem;
            line-height: 1.35;
        }}

        /* Contact Layout */
        .contact-card {{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 20px;
        }}

        .contact-avatar {{
            width: 64px;
            height: 64px;
            border-radius: 50%;
            background-color: var(--color-blue-light);
            border: 2px solid var(--color-blue);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--color-blue-dark);
            margin-bottom: 10px;
            position: relative;
        }}

        .contact-avatar svg {{
            width: 32px;
            height: 32px;
        }}

        .contact-online-dot {{
            position: absolute;
            bottom: 2px;
            right: 2px;
            width: 12px;
            height: 12px;
            background-color: var(--color-green);
            border-radius: 50%;
            border: 2px solid #ffffff;
        }}

        .contact-card h3 {{
            font-family: var(--font-heading);
            font-size: 1.15rem;
            color: var(--color-text-title);
            font-weight: 700;
            margin-bottom: 2px;
        }}

        .contact-role {{
            font-size: 0.7rem;
            font-weight: 700;
            color: var(--color-blue-dark);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 8px;
        }}

        .contact-card p {{
            font-size: 0.75rem;
            line-height: 1.4;
            max-width: 280px;
            margin-bottom: 12px;
        }}

        .contact-buttons-stack {{
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}

        .footer-tagline {{
            text-align: center;
            font-size: 0.72rem;
            font-style: italic;
            color: var(--color-text-muted);
            margin-top: auto;
            line-height: 1.4;
        }}
    </style>
</head>
<body>

    <!-- PAGE 1: COVER -->
    <div class="page cover-page" style="background-image: url('hero_lake.png');">
        <div class="cover-overlay"></div>
        <div class="cover-content">
            <svg class="cover-logo-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/>
                <circle cx="12" cy="12" r="4"/>
                <path d="M2 18h20M4 21h16"/>
            </svg>
            <h1 class="cover-title">{cover_title}</h1>
            <p class="cover-subtitle">{cover_subtitle}</p>
            <span class="cover-badge">{cover_badge}</span>
        </div>
    </div>

    <!-- PAGE 2: CHECK-IN & RECEPTION -->
    <div class="page">
        <div class="slide-header-meta">
            <span>{meta_header_nav}</span>
            <span class="room-badge">{meta_header_room}</span>
        </div>
        <div class="slide-title-row">
            <div class="slide-icon-box">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
                    <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
                </svg>
            </div>
            <h2>{checkin_title}</h2>
        </div>

        <div class="card">
            <div class="card-header-row">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
                <h3>1. {checkin_step1_title}</h3>
            </div>
            <p>{checkin_step1_desc}</p>
        </div>

        <div class="card">
            <div class="card-header-row">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 2v6h-6M21 13a9 9 0 1 1-9-9c2.52 0 4.88 1.03 6.6 2.7L21 8"/></svg>
                <h3>2. {checkin_step2_title}</h3>
            </div>
            <p>{checkin_step2_desc}</p>
            
            <div class="highlight-box">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
                <div class="highlight-text">
                    <strong>{checkin_warning_title}</strong>
                    <p>{checkin_warning_desc}</p>
                </div>
            </div>
        </div>
    </div>

    <!-- PAGE 3: CHECK-OUT -->
    <div class="page">
        <div class="slide-header-meta">
            <span>{meta_header_nav}</span>
            <span class="room-badge">{meta_header_room}</span>
        </div>
        <div class="slide-title-row">
            <div class="slide-icon-box">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
                    <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
                </svg>
            </div>
            <h2>{checkin_title}</h2>
        </div>

        <div class="card">
            <div class="card-header-row">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                <h3>3. {checkin_step3_title}</h3>
            </div>
            <p>{checkin_step3_desc}</p>
            
            <div class="highlight-box warning">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/><path d="M12 8v4M12 16h.01"/></svg>
                <div class="highlight-text">
                    <strong>{checkin_checkout_warning_title}</strong>
                    <p>{checkin_checkout_warning_desc}</p>
                </div>
            </div>
        </div>
    </div>

    <!-- PAGE 4: LOCATION & PARKING -->
    <div class="page">
        <div class="slide-header-meta">
            <span>{meta_header_nav}</span>
            <span class="room-badge">{meta_header_room}</span>
        </div>
        <div class="slide-title-row">
            <div class="slide-icon-box">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
                    <polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"/>
                    <line x1="9" y1="3" x2="9" y2="18"/>
                    <line x1="15" y1="6" x2="15" y2="21"/>
                </svg>
            </div>
            <h2>{location_title}</h2>
        </div>

        <div class="card">
            <div class="card-header-row">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>
                <h3>{location_nav_title}</h3>
            </div>
            <p>{location_nav_desc}</p>
            
            <a href="https://2gis.kg/bishkek/geo/70000001027759284/76.621728,42.540510" class="btn btn-teal">
                <svg class="btn-svg-stroke" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                {location_btn_2gis}
            </a>
        </div>

        <div class="card">
            <div class="card-header-row">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><path d="M9 17V7h4a3 3 0 0 1 0 6H9"/></svg>
                <h3>{location_parking_title}</h3>
            </div>
            <p>{location_parking_desc}</p>
        </div>
    </div>

    <!-- PAGE 5: ROOM AMENITIES -->
    <div class="page">
        <div class="slide-header-meta">
            <span>{meta_header_nav}</span>
            <span class="room-badge">{meta_header_room}</span>
        </div>
        <div class="slide-title-row">
            <div class="slide-icon-box">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M2 20V9a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v11M2 17h20M2 14h20M6 7V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v3"/>
                </svg>
            </div>
            <h2>{amenities_title}</h2>
        </div>

        <div class="amenities-grid">
            <!-- WiFi -->
            <div class="amenity-card warning-card">
                <div class="amenity-icon text-red">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M5 12.55a11 11 0 0 1 14.08 0M1.42 9a16 16 0 0 1 21.16 0M8.53 16.11a6 6 0 0 1 6.95 0M12 20h.01"/>
                        <line x1="1" y1="1" x2="23" y2="23" stroke="currentColor" stroke-width="2"/>
                    </svg>
                </div>
                <div class="amenity-info">
                    <h4>
                        {amenities_wifi_title}
                        <span class="status-badge error">{amenities_wifi_status}</span>
                    </h4>
                    <p>{amenities_wifi_desc}</p>
                </div>
            </div>

            <!-- Mosquito -->
            <div class="amenity-card">
                <div class="amenity-icon text-amber">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="8" y="6" width="8" height="12" rx="4"/>
                        <path d="M12 2v4M12 18v4M4 8h4M4 12h4M4 16h4M16 8h4M16 12h4M16 16h4"/>
                    </svg>
                </div>
                <div class="amenity-info">
                    <h4>
                        {amenities_mosquito_title}
                        <span class="status-badge success">{amenities_mosquito_status}</span>
                    </h4>
                    <p>{amenities_mosquito_desc}</p>
                </div>
            </div>

            <!-- Kitchen -->
            <div class="amenity-card">
                <div class="amenity-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M18 8A6 6 0 0 0 6 8c0 7 6 13 6 13s6-6 6-13zM12 2v6M9 5h6"/>
                    </svg>
                </div>
                <div class="amenity-info">
                    <h4>
                        {amenities_kitchen_title}
                        <span class="status-badge info">{amenities_kitchen_status}</span>
                    </h4>
                    <p>{amenities_kitchen_desc}</p>
                </div>
            </div>

            <!-- Climate -->
            <div class="amenity-card">
                <div class="amenity-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M12 2v20M4.93 4.93l14.14 14.14M2 12h20M19.07 4.93L4.93 19.07"/>
                    </svg>
                </div>
                <div class="amenity-info">
                    <h4>
                        {amenities_comfort_title}
                        <span class="status-badge info">{amenities_comfort_status}</span>
                    </h4>
                    <p>{amenities_comfort_desc}</p>
                </div>
            </div>
        </div>
    </div>

    <!-- PAGE 6: RESTAURANTS -->
    <div class="page">
        <div class="slide-header-meta">
            <span>{meta_header_nav}</span>
            <span class="room-badge">{meta_header_room}</span>
        </div>
        <div class="slide-title-row">
            <div class="slide-icon-box">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
                </svg>
            </div>
            <h2>{dining_title}</h2>
        </div>

        <div class="dining-list">
            <!-- Madam Chen -->
            <div class="card dining-card">
                <span class="dining-badge bg-rose" style="background-color: hsl(350, 70%, 50%);">Madam Chen</span>
                <h3>Madam Chen</h3>
                <p class="dining-cuisine">{dining1_cuisine}</p>
                <p>{dining1_desc}</p>
                <a href="https://2gis.kg/bishkek/geo/70000001089728868" class="btn btn-outline">
                    <svg class="btn-svg-stroke" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                    {dining_btn_map}
                </a>
            </div>

            <!-- Ala Too -->
            <div class="card dining-card">
                <span class="dining-badge bg-amber" style="background-color: var(--color-amber);">{dining2_title}</span>
                <h3>{dining2_title}</h3>
                <p class="dining-cuisine">{dining2_cuisine}</p>
                <p>{dining2_desc}</p>
                <a href="https://2gis.kg/bishkek/geo/70000001100682112" class="btn btn-outline">
                    <svg class="btn-svg-stroke" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                    {dining_btn_map}
                </a>
            </div>
        </div>
    </div>

    <!-- PAGE 7: RESTAURANTS PART 2 & SPA -->
    <div class="page">
        <div class="slide-header-meta">
            <span>{meta_header_nav}</span>
            <span class="room-badge">{meta_header_room}</span>
        </div>
        
        <!-- Veranda -->
        <div class="card dining-card" style="margin-bottom: 20px;">
            <span class="dining-badge bg-blue" style="background-color: var(--color-blue);">{dining3_title}</span>
            <h3>{dining3_title}</h3>
            <p class="dining-cuisine">{dining3_cuisine}</p>
            <p>{dining3_desc}</p>
            <a href="https://2gis.kg/bishkek/geo/70000001079101925/76.627073,42.540434" class="btn btn-outline">
                <svg class="btn-svg-stroke" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                {dining_btn_map}
            </a>
        </div>

        <div class="slide-title-row" style="margin-top: 10px; margin-bottom: 12px;">
            <div class="slide-icon-box">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 2c-5.33 0-8 3-8 8 0 7 8 12 8 12s8-5 8-12c0-5-2.67-8-8-8z"/>
                    <path d="M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
                </svg>
            </div>
            <h2>{spa_title}</h2>
        </div>

        <div class="spa-list">
            <!-- Pool card -->
            <div class="card spa-card">
                <div class="spa-img-box">
                    <img src="spa_pool.png" alt="Thermal Pool">
                    <div class="spa-caption">{spa_pool_badge}</div>
                </div>
                <div class="spa-card-content">
                    <h3>{spa_pool_title}</h3>
                    <p>{spa_pool_desc}</p>
                </div>
            </div>
        </div>
    </div>

    <!-- PAGE 8: SPA PART 2 & SUPPORT -->
    <div class="page">
        <div class="slide-header-meta">
            <span>{meta_header_nav}</span>
            <span class="room-badge">{meta_header_room}</span>
        </div>
        
        <div class="spa-list" style="margin-bottom: 16px;">
            <!-- Spa massage card -->
            <div class="card spa-card">
                <div class="spa-img-box">
                    <img src="spa_massage.png" alt="Spa Treatment">
                </div>
                <div class="spa-card-content">
                    <h3>{spa_service_title}</h3>
                    <p>{spa_service_desc}</p>
                </div>
            </div>

            <!-- Playgrounds card -->
            <div class="card spa-card">
                <div class="spa-img-box">
                    <img src="spa_playground.png" alt="Kids Playground">
                </div>
                <div class="spa-card-content">
                    <h3>{spa_kids_title}</h3>
                    <p>{spa_kids_desc}</p>
                </div>
            </div>
        </div>
    </div>

    <!-- PAGE 9: CONTACT & ASSISTANCE -->
    <div class="page">
        <div class="slide-header-meta">
            <span>{meta_header_nav}</span>
            <span class="room-badge">{meta_header_room}</span>
        </div>
        <div class="slide-title-row">
            <div class="slide-icon-box">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
                </svg>
            </div>
            <h2>{contacts_title}</h2>
        </div>

        <div class="card contact-card">
            <div class="contact-avatar">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                    <circle cx="12" cy="7" r="4"/>
                </svg>
                <div class="contact-online-dot"></div>
            </div>
            
            <h3>{contacts_manager_name}</h3>
            <p class="contact-role">{contacts_manager_role}</p>
            <p>{contacts_pitch}</p>
            
            <div class="contact-buttons-stack">
                <a href="https://wa.me/996503971057" class="btn btn-whatsapp">
                    <svg class="btn-svg" viewBox="0 0 24 24">
                        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L0 24l6.335-1.662c1.746.953 3.71 1.454 5.709 1.455h.008c6.56 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/>
                    </svg>
                    {contacts_btn_whatsapp}
                </a>
                <a href="tel:+996503971057" class="btn btn-phone">
                    <svg class="btn-svg-stroke" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                    {contacts_btn_call}
                </a>
            </div>
        </div>

        <p class="footer-tagline">{footer_tagline}</p>
    </div>

</body>
</html>
"""

TRANSLATIONS = {
    "ru": {
        "lang": "ru",
        "meta_header_nav": "Радуга Вест",
        "meta_header_room": "Номер 506",
        "cover_title": "Добро пожаловать в «Радуга Вест»!",
        "cover_subtitle": "Гостевой гид по отдыху в номере 506",
        "cover_badge": "ОФЛАЙН-СПРАВОЧНИК",
        "checkin_title": "Заселение и выезд",
        "checkin_step1_title": "Прибытие и ресепшен",
        "checkin_step1_desc": "После въезда на территорию пансионата подойдите на стойку регистрации (ресепшен) в главном корпусе.",
        "checkin_step2_title": "Получение ключей и браслетов",
        "checkin_step2_desc": "Сообщите администратору свои данные и номер 506. Вам выдадут ключи от номера. Постельное белье, полотенца и желтые браслеты уже будут находиться в номере.",
        "checkin_warning_title": "Важно о желтых браслетах!",
        "checkin_warning_desc": "Браслеты являются электронными ключами для прохода на пляж. Всегда берите их с собой и старайтесь не терять.",
        "checkin_step3_title": "Правила выезда",
        "checkin_step3_desc": "Выезд из номера осуществляется строго до 12:00. При выезде не забудьте вернуть ключи на ресепшен, а браслеты оставьте в номере.",
        "checkin_checkout_warning_title": "Халаты и полотенца",
        "checkin_checkout_warning_desc": "Пожалуйста, не забывайте банные халаты и полотенца на пляже, обязательно приносите их обратно в номер.",
        "location_title": "Как добраться и парковка",
        "location_nav_title": "Навигация в 2ГИС",
        "location_nav_desc": "Для построения точного маршрута и навигации по территории воспользуйтесь нашей точкой в приложении 2ГИС.",
        "location_btn_2gis": "Открыть точку в 2ГИС",
        "location_parking_title": "Где оставить автомобиль?",
        "location_parking_desc": "Для всех гостей нашего номера предоставляется бесплатная охраняемая парковка, которая находится прямо напротив комплекса.",
        "amenities_title": "Что есть в номере",
        "amenities_wifi_title": "Wi-Fi Интернет",
        "amenities_wifi_status": "Временно недоступен",
        "amenities_wifi_desc": "По техническим причинам провайдера Wi-Fi в номере временно отключен. Приносим извинения за неудобства!",
        "amenities_mosquito_title": "Защита от комаров",
        "amenities_mosquito_status": "Есть в номере",
        "amenities_mosquito_desc": "Для спокойного сна в выдвижном ящике тумбочки лежит фумигатор. При необходимости вставьте его в розетку.",
        "amenities_kitchen_title": "Мини-кухня",
        "amenities_kitchen_status": "Оборудована",
        "amenities_kitchen_desc": "В номере установлены холодильник, электрочайник, посуда и столовые приборы.",
        "amenities_comfort_title": "Климат и ТВ",
        "amenities_comfort_status": "Кондиционер & Smart TV",
        "amenities_comfort_desc": "Мощный кондиционер для регулировки климата, плоский телевизор, обеденная зона.",
        "dining_title": "Кафе и рестораны комплекса",
        "dining1_cuisine": "Азиатская и европейская кухня",
        "dining1_desc": "Отличное место для любителей изысканных китайских блюд, суши, вок-меню, а также традиционной классической европейской кухни.",
        "dining_btn_map": "Найти в 2ГИС",
        "dining2_title": "Ала-Тоо",
        "dining2_cuisine": "Восточная и кыргызская кухня",
        "dining2_desc": "Попробуйте национальные кыргызские мясные блюда, свежий плов, шашлыки и традиционные лепешки в колоритном оформлении.",
        "dining3_title": "Veranda",
        "dining3_cuisine": "Восточная и кыргызская кухня",
        "dining3_desc": "Уютный ресторан с красивой террасой. Большой выбор блюд на гриле, прохладительных напитков и традиционных угощений.",
        "spa_title": "СПА-комплекс и развлечения",
        "spa_service_title": "Оздоровительный СПА",
        "spa_service_desc": "Расслабьтесь телом и душой. К услугам гостей профессиональные массажисты и физиопроцедуры.",
        "spa_pool_badge": "Горячий источник",
        "spa_pool_title": "Термальный бассейн",
        "spa_pool_desc": "На территории комплекса работает крытый бассейн с лечебной минеральной водой из подземного горячего источника. Открыт в любое время года.",
        "spa_kids_title": "Детские площадки",
        "spa_kids_desc": "Для маленьких гостей пансионата обустроены современные игровые зоны с горками и качелями, окруженные зелеными газонами.",
        "contacts_title": "Помощь и уборка",
        "contacts_manager_name": "Индира",
        "contacts_manager_role": "Координатор по заселению и уборке",
        "contacts_pitch": "По всем вопросам уборки, чистоты, бытовых мелочей в номере или помощи на территории пансионата пишите Индире.",
        "contacts_btn_whatsapp": "Написать в WhatsApp",
        "contacts_btn_call": "Позвонить",
        "footer_tagline": "Желаем вам приятного отдыха и незабываемых впечатлений на Иссык-Куле!"
    },
    "kg": {
        "lang": "kg",
        "meta_header_nav": "Радуга Вест",
        "meta_header_room": "Бөлмө 506",
        "cover_title": "«Радуга Вест» пансионатына кош келиңиздер!",
        "cover_subtitle": "506-бөлмөдө эс алуу үчүн оффлайн коноктук жол көрсөткүч",
        "cover_badge": "ОФФЛАЙН-МААЛЫМАТТАМА",
        "checkin_title": "Катталуу жана чыгуу",
        "checkin_step1_title": "Келүү жана ресепшен",
        "checkin_step1_desc": "Пансионаттын аймагына киргенден кийин, башкы корпустагы кабыл алуу столуна (ресепшен) барыңыз.",
        "checkin_step2_title": "Ачкычтарды жана билериктерди алуу",
        "checkin_step2_desc": "Администраторго маалыматыңызды жана 506-бөлмөнү айтыңыз. Сизге бөлмөнүн ачкычтары берилет. Шейшептер, сүлгүлөр жана сары билериктер бөлмөдө болот.",
        "checkin_warning_title": "Сары билериктердин маанилүүлүгү!",
        "checkin_warning_desc": "Бул билериктер пляжга өтүү үчүн электрондук ачкыч болуп саналат. Аларды дайыма жаныңызга алып жүрүңүз жана жоготпоого аракет кылыңыз.",
        "checkin_step3_title": "Чыгуу эрежелери",
        "checkin_step3_desc": "Бөлмөдөн чыгуу саат 12:00гө чейин жүргүзүлөт. Чыгып жатканда ачкычтарды ресепшенге тапшырууну унутпаңыз, ал эми билериктерди бөлмөдө калтырыңыз.",
        "checkin_checkout_warning_title": "Халаттар жана сүлгүлөр",
        "checkin_checkout_warning_desc": "Сураныч, халаттар менен сүлгүлөрдү пляжда калтырбаңыз, аларды сөзсүз бөлмөгө алып келиңиз.",
        "location_title": "Жол көрсөткүч жана унаа токтотуучу жай",
        "location_nav_title": "2ГИС боюнча навигация",
        "location_nav_desc": "Маршрутту так түзүү жана аймакта оңой багыт алуу үчүн 2ГИС тиркемесиндеги биздин чекитти колдонуңуз.",
        "location_btn_2gis": "2ГИС аркылуу ачуу",
        "location_parking_title": "Унааны кайда калтырса болот?",
        "location_parking_desc": "Биздин бөлмөнүн бардык коноктору үчүн комплекстин каршысында жайгашкан акысыз кайтарылган унаа токтотуучу жай каралган.",
        "amenities_title": "Бөлмөнүн шарттары",
        "amenities_wifi_title": "Wi-Fi Интернет",
        "amenities_wifi_status": "Убактылуу иштебейт",
        "amenities_wifi_desc": "Техникалык себептерден улам бөлмөдөгү Wi-Fi убактылуу өчүрүлгөн. Келтирилген ыңгайсыздыктар үчүн кечирим сурайбыз!",
        "amenities_mosquito_title": "Чиркейлерден коргоо",
        "amenities_mosquito_status": "Бөлмөдө бар",
        "amenities_mosquito_desc": "Тынч уктоо үчүн тумбочканын суурмасында чиркейге каршы фумигатор бар. Керек болсо розеткага сайып коюңуз.",
        "amenities_kitchen_title": "Мини-ашкана",
        "amenities_kitchen_status": "Жабдылган",
        "amenities_kitchen_desc": "Бөлмөдө муздаткыч, электр чайнеги, идиш-аяктар жана тамак-аш куралдары бар.",
        "amenities_comfort_title": "Климат жана ТВ",
        "amenities_comfort_status": "Кондиционер & Smart TV",
        "amenities_comfort_desc": "Абаны жөндөө үчүн кубаттуу кондиционер, жалпак телевизор жана ыңгайлуу тамактануучу жай.",
        "dining_title": "Аймактагы кафе жана ресторандар",
        "dining1_cuisine": "Азия жана европа ашканасы",
        "dining1_desc": "Кытай тамактарынын, суши, вок жана европалык классикалык ашкананын сүйүүчүлөрү үчүн эң сонун жай.",
        "dining_btn_map": "2ГИСтен табуу",
        "dining2_title": "Ала-Тоо",
        "dining2_cuisine": "Чыгыш жана кыргыз ашканасы",
        "dining2_desc": "Колориттүү дизайн менен даярдалган кыргыз улуттук эт тамактарын, жаңы палоону, шашлыктарды жана нандарды татып көрүңүз.",
        "dining3_title": "Veranda",
        "dining3_cuisine": "Чыгыш жана кыргыз ашканасы",
        "dining3_desc": "Кооз террасасы бар жагымдуу ресторан. Грильде бышырылган тамактардын, суусундуктардын жана салттуу даамдардын кеңири түрү.",
        "spa_title": "СПА-комплекс жана оюн-зооктор",
        "spa_service_title": "Сакайтуучу СПА",
        "spa_service_desc": "Денеңизди жана жан дүйнөңүздү эс алдырыңыз. Коноктор үчүн профессионалдык массаж жана физиопроцедуралар бар.",
        "spa_pool_badge": "Ысык булак",
        "spa_pool_title": "Термалдык бассейн",
        "spa_pool_desc": "Аймакта жер астындагы ысык булактан алынган дарылык минералдык суусу бар жабык бассейн иштейт. Жылдын каалаган убагында ачык.",
        "spa_kids_title": "Балдар аянтчалары",
        "spa_kids_desc": "Пансионаттын кичинекей коноктору үчүн жашыл газондор менен курчалган, слайддар жана селкинчектер менен жабдылган заманбап оюн аянтчалары каралган.",
        "contacts_title": "Суроолор жана тазалоо",
        "contacts_manager_name": "Индира",
        "contacts_manager_role": "Катталуу жана тазалык боюнча координатор",
        "contacts_pitch": "Бөлмөнү тазалоо, тиричилик маселелери же аймакта жардам алуу боюнча суроолор болсо, Индирага жазыңыз.",
        "contacts_btn_whatsapp": "WhatsApp аркылуу жазуу",
        "contacts_btn_call": "Чалуу",
        "footer_tagline": "Ысык-Көлдө жагымдуу эс алуу жана унутулгус таасирлер каалайбыз!"
    },
    "en": {
        "lang": "en",
        "meta_header_nav": "Raduga West",
        "meta_header_room": "Room 506",
        "cover_title": "Welcome to Raduga West!",
        "cover_subtitle": "Offline Guest Guide for Room 506 stays",
        "cover_badge": "OFFLINE GUIDE BOOK",
        "checkin_title": "Check-in & Departure",
        "checkin_step1_title": "Arrival & Reception",
        "checkin_step1_desc": "Upon entering the resort grounds, proceed to the main registration desk (reception) located in the main building.",
        "checkin_step2_title": "Obtaining Keys & Wristbands",
        "checkin_step2_desc": "State your details and room number 506 to the staff. They will provide room keys. Bed linen, towels, and yellow wristbands will already be inside the room.",
        "checkin_warning_title": "Important: Yellow Wristbands!",
        "checkin_warning_desc": "Wristbands serve as electronic keys for beach access. Always carry them with you and try not to lose them.",
        "checkin_step3_title": "Departure Guidelines",
        "checkin_step3_desc": "Check-out time is strictly before 12:00. Upon departure, remember to return the keys to reception and leave the wristbands in the room.",
        "checkin_checkout_warning_title": "Bathrobes & Towels",
        "checkin_checkout_warning_desc": "Please do not leave bathrobes and towels on the beach; make sure to bring them back to the room.",
        "location_title": "Directions & Parking",
        "location_nav_title": "2GIS Navigation",
        "location_nav_desc": "For precise routing and on-site resort navigation, please use our location point in the 2GIS app.",
        "location_btn_2gis": "Open Location in 2GIS",
        "location_parking_title": "Where to Park?",
        "location_parking_desc": "Free secured parking is provided for all of our guests directly opposite the complex entrance.",
        "amenities_title": "Room Amenities",
        "amenities_wifi_title": "Wi-Fi Internet",
        "amenities_wifi_status": "Temporarily Unavailable",
        "amenities_wifi_desc": "Due to provider technical issues, Wi-Fi in the room is temporarily offline. We apologize for the inconvenience!",
        "amenities_mosquito_title": "Mosquito Protection",
        "amenities_mosquito_status": "Available in room",
        "amenities_mosquito_desc": "For a peaceful sleep, a fumigator is located in the bedside drawer. Plug it in if needed.",
        "amenities_kitchen_title": "Kitchenette",
        "amenities_kitchen_status": "Equipped",
        "amenities_kitchen_desc": "The room is equipped with a refrigerator, electric kettle, dinnerware, and cutlery.",
        "amenities_comfort_title": "AC & Smart TV",
        "amenities_comfort_status": "AC & Smart TV",
        "amenities_comfort_desc": "Powerful air conditioner for climate control, flat-screen television, and a cozy dining table.",
        "dining_title": "On-site Dining & Cafes",
        "dining1_cuisine": "Asian & European Cuisine",
        "dining1_desc": "An excellent choice for fans of fine Chinese food, sushi, wok, and traditional classic European courses.",
        "dining_btn_map": "Find on 2GIS",
        "dining2_title": "Ala-Too",
        "dining2_cuisine": "Eastern & Kyrgyz Cuisine",
        "dining2_desc": "Taste traditional Kyrgyz meat specialties, fresh pilaf, shashlik, and traditional tandoor bread in a colorful setting.",
        "dining3_title": "Veranda",
        "dining3_cuisine": "Eastern & Kyrgyz Cuisine",
        "dining3_desc": "Cozy restaurant featuring a beautiful summer terrace. Great selection of grilled dishes, cold beverages, and traditional meals.",
        "spa_title": "SPA Center & Activities",
        "spa_service_title": "Wellness & Spa Treatments",
        "spa_service_desc": "Indulge in relaxation. Guests can book professional massages and physical therapy.",
        "spa_pool_badge": "Hot Spring Pool",
        "spa_pool_title": "Thermal Mineral Pool",
        "spa_pool_desc": "The resort features an indoor pool filled with natural, therapeutic hot mineral spring water. Open year-round.",
        "spa_kids_title": "Playgrounds",
        "spa_kids_desc": "Modern and safe children's outdoor play areas with slides and swings are set up on the resort lawns.",
        "contacts_title": "Housekeeping & Help",
        "contacts_manager_name": "Indira",
        "contacts_manager_role": "Check-in & Housekeeping Coordinator",
        "contacts_pitch": "For any questions regarding housekeeping, room details, or assistance on the resort grounds, please contact Indira.",
        "contacts_btn_whatsapp": "Message on WhatsApp",
        "contacts_btn_call": "Call Us",
        "footer_rights": "All rights reserved.",
        "footer_tagline": "We wish you a pleasant vacation and unforgettable memories at Issyk-Kul!"
    }
}

def build_pdfs():
    chrome_path = "C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"
    if not os.path.exists(chrome_path):
        print(f"Error: Google Chrome not found at {chrome_path}")
        return

    for lang, data in TRANSLATIONS.items():
        # Render the HTML content
        html_content = HTML_TEMPLATE.format(**data)
        
        # Write to a temporary HTML file
        temp_html_filename = f"temp_guide_{lang}.html"
        with open(temp_html_filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        # Render to PDF using headless Chrome
        pdf_filename = f"raduga_west_506_guide_{lang}.pdf"
        print(f"Generating {pdf_filename}...")
        
        abs_html_path = os.path.abspath(temp_html_filename)
        abs_pdf_path = os.path.abspath(pdf_filename)
        
        # Execute headless Chrome print-to-pdf command
        args = [
            chrome_path,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            f"--print-to-pdf={abs_pdf_path}",
            abs_html_path
        ]
        
        try:
            subprocess.run(args, check=True)
            print(f"Successfully generated {pdf_filename}!")
        except subprocess.CalledProcessError as e:
            print(f"Failed to generate PDF for {lang}: {e}")
        finally:
            # Clean up temporary HTML file
            if os.path.exists(temp_html_filename):
                os.remove(temp_html_filename)

if __name__ == "__main__":
    build_pdfs()
