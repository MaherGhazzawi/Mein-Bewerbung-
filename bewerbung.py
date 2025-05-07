import random

# Begrüßung und Einleitung
print("Sehr geehrte Damen und Herren.")
print("Ich bewerbe mich bei Ihnen um einen Ausbildungsplatz als Fachinformatiker für Anwendungsentwicklung.\n")
print("Gerne möchte ich meine Kenntnisse auf kreative Weise präsentieren – vielleicht überrascht Sie dieser Ansatz.\n")

def erfahrung():
    """Wählt zufällig eine Programmiersprache aus und gibt Informationen dazu aus."""
    sprachen = ["Python", "C++", "HTML/CSS", "JavaScript"]
    gewaehlte_sprache = random.choice(sprachen)

    infos = {
        "Python": "Ich habe viele Projekte mit Python umgesetzt, z. B. eine Caesar-Verschlüsselung, einen Taschenrechner, einen Passwort-Generator und einen Pizza-Bestellservice.",
        "C++": "Mit C++ habe ich objektorientiert gearbeitet, z. B. an einem Kinosystem. Obwohl es nicht meine stärkste Sprache ist, komme ich gut damit zurecht.",
        "HTML/CSS": "Ich habe solide Kenntnisse in HTML, CSS und SCSS und kann ansprechende und strukturierte Webseiten erstellen.",
        "JavaScript": "Ich lerne gerade JavaScript. Ich kann einfache DOM-Manipulationen durchführen und arbeite daran, meine Kenntnisse zu vertiefen."
    }

    print(f"Zufällig ausgewählte Sprache: {gewaehlte_sprache}")
    print("Kenntnisse:", infos.get(gewaehlte_sprache, "Keine Information verfügbar."))
    print()

def schule():
    """Fragen zu meinen schulischen Qualifikationen und Sprachkenntnissen."""
    while True:
        try:
            frage = int(input("Was möchten Sie über mich wissen?\n1: Schulabschlüsse\n2: Zeugnisse\n3: Sprachkenntnisse\n0: Beenden\n> "))
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")
            continue

        if frage == 0:
            print("Vielen Dank für Ihr Interesse!")
            break
        elif frage == 1:
            print("Ich habe mein Fachabitur im Libanon abgeschlossen, mit einem Fokus auf Informatik.")
            print("Mein Schulabschluss wurde in Deutschland als Realschulabschluss anerkannt.\n")
        elif frage == 2:
            print("Aufgrund wirtschaftlicher Probleme und der Corona-Krise im Libanon habe ich keine detaillierten Noten erhalten.")
            print("Ich habe jedoch eine gute Logik, bin neugierig, kreativ und arbeite lösungsorientiert.\n")
        elif frage == 3:
            print("Ich habe erfolgreich die B1- und B2-Prüfungen in Deutsch absolviert.")
            print("Mein Deutsch ist noch nicht perfekt, aber ich lerne täglich und gebe nicht auf.\n")
        else:
            print("Ungültige Auswahl. Bitte wähle eine Zahl zwischen 0 und 3.\n")

def schlusswort():
    """Abschließende Worte und eine freundliche Einladung für Feedback."""
    abschnitt = [
        "Ich freue mich sehr auf die Möglichkeit, mich in einem Vorstellungsgespräch persönlich vorzustellen.",
        "Ich bin motiviert, lernbereit und bereit, gemeinsam mit Ihrem Team zu wachsen.",
        "Bitte lassen Sie mich wissen, wie ich mich verbessern kann – ich bin offen für jedes Feedback."
    ]
    for zeile in abschnitt:
        print(zeile)

# Ausführung der Funktionen
erfahrung()
schule()
schlusswort()
