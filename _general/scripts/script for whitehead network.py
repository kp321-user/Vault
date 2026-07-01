from pathlib import Path

VAULT_ROOT = Path(r"C:\Users\Ken\CODE\Vault")
PHIL_DIR = VAULT_ROOT / "philosophy"
TOPICS_DIR = PHIL_DIR / "topics"

PHILOSOPHERS = [
    # (filename, full display name, dates)
    # --- Russell's table ---
    ("thales", "Thales", "c.624–546 BC"),
    ("pythagoras", "Pythagoras", "c.570–495 BC"),
    ("heraclitus", "Heraclitus", "c.535–475 BC"),
    ("parmenides", "Parmenides", "c.515–450 BC"),
    ("democritus", "Democritus", "c.460–370 BC"),
    ("protagoras", "Protagoras", "c.490–420 BC"),
    ("socrates", "Socrates", "470–399 BC"),
    ("plato", "Plato", "428–348 BC"),
    ("aristotle", "Aristotle", "384–322 BC"),
    ("epicurus", "Epicurus", "341–270 BC"),
    ("zeno", "Zeno of Citium", "c.334–262 BC"),
    ("plotinus", "Plotinus", "204–270 AD"),
    ("augustine", "Augustine", "354–430 AD"),
    ("anselm", "Anselm", "1033–1109"),
    ("aquinas", "Thomas Aquinas", "1225–1274"),
    ("ockham", "William of Ockham", "c.1287–1347"),
    ("machiavelli", "Niccolò Machiavelli", "1469–1527"),
    ("bacon", "Francis Bacon", "1561–1626"),
    ("hobbes", "Thomas Hobbes", "1588–1679"),
    ("descartes", "René Descartes", "1596–1650"),
    ("spinoza", "Baruch Spinoza", "1632–1677"),
    ("leibniz", "Gottfried Wilhelm Leibniz", "1646–1716"),
    ("locke", "John Locke", "1632–1704"),
    ("berkeley", "George Berkeley", "1685–1753"),
    ("hume", "David Hume", "1711–1776"),
    ("rousseau", "Jean-Jacques Rousseau", "1712–1778"),
    ("kant", "Immanuel Kant", "1724–1804"),
    ("hegel", "Georg Wilhelm Friedrich Hegel", "1770–1831"),
    ("schopenhauer", "Arthur Schopenhauer", "1788–1860"),
    ("marx", "Karl Marx", "1818–1883"),
    ("nietzsche", "Friedrich Nietzsche", "1844–1900"),
    ("mill", "John Stuart Mill", "1806–1873"),
    ("james", "William James", "1842–1910"),
    ("bergson", "Henri Bergson", "1859–1941"),
    ("dewey", "John Dewey", "1859–1952"),
    # --- Non-Russell table ---
    ("confucius", "Confucius", "551–479 BC"),
    ("laozi", "Laozi", "c.6th century BC"),
    ("zhuangzi", "Zhuangzi", "c.369–286 BC"),
    ("mencius", "Mencius", "372–289 BC"),
    ("nagarjuna", "Nagarjuna", "c.150–250 AD"),
    ("avicenna", "Avicenna (Ibn Sina)", "980–1037"),
    ("al-ghazali", "Al-Ghazali", "1058–1111"),
    ("averroes", "Averroes (Ibn Rushd)", "1126–1198"),
    ("maimonides", "Maimonides", "1138–1204"),
    ("ramanuja", "Ramanuja", "1017–1137"),
    ("kierkegaard", "Søren Kierkegaard", "1813–1855"),
    ("peirce", "Charles Sanders Peirce", "1839–1914"),
    ("husserl", "Edmund Husserl", "1859–1938"),
    ("wollstonecraft", "Mary Wollstonecraft", "1759–1797"),
    ("frege", "Gottlob Frege", "1848–1925"),
    ("heidegger", "Martin Heidegger", "1889–1976"),
    ("wittgenstein", "Ludwig Wittgenstein", "1889–1951"),
    ("sartre", "Jean-Paul Sartre", "1905–1980"),
    ("de-beauvoir", "Simone de Beauvoir", "1908–1986"),
    ("arendt", "Hannah Arendt", "1906–1975"),
    ("camus", "Albert Camus", "1913–1960"),
    ("foucault", "Michel Foucault", "1926–1984"),
    ("rawls", "John Rawls", "1921–2002"),
    # --- From Whitehead note, not yet in either table ---
    ("deleuze", "Gilles Deleuze", "1925–1995"),
    ("latour", "Bruno Latour", "1947–2022"),
    ("hartshorne", "Charles Hartshorne", "1897–2000"),
]

TOPICS = [
    "metaphysics",
    "epistemology",
    "philosophy-of-science",
    "consciousness",
    "philosophy-of-religion",
    "ethics",
    "political-philosophy",
]

SKIP = {"whitehead"}  # already exists with content


def philosopher_stub(display_name, dates):
    return f"""# {display_name} ({dates})

## In plain terms
*(your notes here)*

---

## Core ideas
*(your notes here)*

---

## Influences on {display_name.split()[0]}
-

## Who {display_name.split()[0]} influenced
-

## Key works
-

---

## Personal relevance
*(your notes here)*

---

## Connected problems
-
"""


def topic_stub(name):
    title = name.replace("-", " ").title()
    return f"""# {title}

## Overview
*(your notes here)*

---

## Key philosophers
-

## Key questions
-

## Connected topics
-
"""


def main():
    PHIL_DIR.mkdir(parents=True, exist_ok=True)
    TOPICS_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Philosopher files → {PHIL_DIR.resolve()}")
    print(f"Topic files       → {TOPICS_DIR.resolve()}")
    print()

    created = 0
    skipped = 0

    for slug, display_name, dates in PHILOSOPHERS:
        if slug in SKIP:
            print(f"  skipped: {slug}.md (already exists)")
            skipped += 1
            continue
        path = PHIL_DIR / f"{slug}.md"
        if path.exists():
            print(f"  skipped: {slug}.md (already exists)")
            skipped += 1
            continue
        path.write_text(philosopher_stub(display_name, dates), encoding="utf-8")
        print(f"  created: {path.resolve()}")
        created += 1

    for topic in TOPICS:
        path = TOPICS_DIR / f"{topic}.md"
        if path.exists():
            print(f"  skipped: topics/{topic}.md (already exists)")
            skipped += 1
            continue
        path.write_text(topic_stub(topic), encoding="utf-8")
        print(f"  created: {path.resolve()}")
        created += 1

    print(f"\nDone — {created} files created, {skipped} skipped.")


if __name__ == "__main__":
    main()
