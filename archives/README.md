# Archives

Historical artifacts preserved per **Golden Rule #8: Archive Over Delete**.

## Purpose

This directory preserves files that are no longer actively used but provide:
- Historical context for system evolution
- Examples of anti-patterns to avoid
- Recovery options if decisions are reversed
- Audit trail for accountability

## Structure

| Directory | Contents |
|-----------|----------|
| `deprecated-templates/` | Templates superseded or identified as Documentation Theater |

## Naming Convention

Files are prefixed with their archive date:
```
YYYY-MM-DD_[original-filename]
```

## When NOT to Archive

Per Golden Rule #8, these should be DELETED instead:
1. Security-sensitive content (credentials, secrets)
2. Generated/temporary files (build artifacts)
3. Exact duplicates of existing content
4. Privacy-regulated data (GDPR compliance)
5. Malicious content
6. Large binary files with no historical value

---

_Last updated: 2026-01-05_
