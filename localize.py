#!/usr/bin/env python3
"""Shared single-pass text substitution for the chichenitzawalk.com generators.

WHY SINGLE PASS: applying a text map with repeated str.replace() re-scans text that
has already been translated. A short key like "Map" then matches inside an
already-produced "Mapa GPS" and yields "Mapaa GPS"; "Address" eats the schema.org
type name inside "PostalAddress". Both happened. A single regex pass over the
ORIGINAL string, longest alternative first, cannot cascade.

PROTECT holds literals that must survive intact even though a shorter key is a
substring of them (schema.org type names, brand names, URLs, class names).
"""
import re

# strings that must never be touched, even partially
PROTECT = [
    # schema.org vocabulary
    '"@type":"PostalAddress"', '"@type":"TouristAttraction"', '"@type":"GeoCoordinates"',
    '"@type":"Organization"', '"@type":"WebSite"', '"@type":"Person"', '"@type":"Product"',
    '"@type":"Offer"', '"@type":"Brand"', '"@type":"FAQPage"', '"@type":"Question"',
    '"@type":"Answer"', '"@type":"BreadcrumbList"', '"@type":"ListItem"',
    '"@type":"MerchantReturnPolicy"',
    'addressLocality', 'addressRegion', 'addressCountry', 'postalCode',
    'MerchantReturnNotPermitted', 'returnPolicyCategory', 'applicableCountry',
    'priceCurrency', 'availability', 'mainEntity', 'itemListElement',
    'inLanguage', 'knowsAbout', 'sameAs', 'publisher', 'position',
    # brand / product names
    'Google Maps', 'TouringBee', 'Tripadvisor', 'Viator', 'Tiqets', 'GetYourGuide',
    'Booking.com', 'App Store', 'iOS', 'Android', 'Instagram', 'YouTube', 'Stripe',
    'UNESCO', 'INAH', 'GPS',
]


def build_pattern(mapping):
    """Longest-first alternation over PROTECT + the map's keys."""
    keys = sorted(set(list(PROTECT) + list(mapping)), key=len, reverse=True)
    return re.compile('|'.join(re.escape(k) for k in keys))


def apply_map(html, mapping):
    """One left-to-right pass. Protected literals resolve to themselves."""
    pat = build_pattern(mapping)
    return pat.sub(lambda m: mapping.get(m.group(0), m.group(0)), html)


def unused_keys(html, mapping):
    return [k for k in mapping if k not in html]
