from django import template

register = template.Library()

# Pairs chosen from the site's accent palette (see :root in style.css).
# Kept in this order deliberately — index picked via hash for a stable,
# non-random assignment per title.
_GRADIENTS = [
    "var(--coral), var(--gold)",
    "var(--teal), var(--gold)",
    "var(--plum), var(--coral)",
    "var(--teal), var(--plum)",
    "var(--gold), var(--plum)",
    "var(--coral), var(--teal)",
]


@register.filter
def accent_gradient(value):
    """Given any string (usually a title/slug), return a stable CSS gradient pair."""
    if not value:
        value = "x"
    index = sum(ord(c) for c in str(value)) % len(_GRADIENTS)
    stops = _GRADIENTS[index]
    return f"linear-gradient(135deg, {stops})"


@register.filter
def initials(value):
    """First letters of up to 2 words, for the placeholder card overlay."""
    if not value:
        return "?"
    words = str(value).split()
    letters = "".join(w[0] for w in words[:2] if w)
    return letters.upper() or "?"
