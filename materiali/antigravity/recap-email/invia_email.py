"""Invia un'email di testo con Gmail.

Uso:
    python3 invia_email.py --oggetto "Recap del 03/11" --testo "..."

Mittente, password e destinatario stanno nel file .env accanto a questo
script: l'agente non li vede e non può cambiare il destinatario.
"""

import argparse
import smtplib
import sys
from email.mime.text import MIMEText
from pathlib import Path

ENV = Path(__file__).resolve().parent / ".env"


def leggi_env():
    valori = {}
    if ENV.exists():
        for riga in ENV.read_text(encoding="utf-8").splitlines():
            riga = riga.strip()
            if riga and not riga.startswith("#") and "=" in riga:
                chiave, valore = riga.split("=", 1)
                valori[chiave.strip()] = valore.strip().strip("\"'")
    return valori


def main():
    p = argparse.ArgumentParser(description="Invia un'email di testo con Gmail.")
    p.add_argument("--oggetto", required=True)
    p.add_argument("--testo", required=True)
    a = p.parse_args()

    env = leggi_env()
    mittente = env.get("GMAIL_INDIRIZZO")
    password = env.get("GMAIL_PASSWORD_APP")
    destinatario = env.get("DESTINATARIO") or mittente
    if not mittente or not password:
        print("ERRORE: manca il file .env con GMAIL_INDIRIZZO e GMAIL_PASSWORD_APP.", file=sys.stderr)
        return 1

    msg = MIMEText(a.testo, "plain", "utf-8")
    msg["Subject"] = a.oggetto
    msg["From"] = mittente
    msg["To"] = destinatario
    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as server:
            server.starttls()
            server.login(mittente, password)
            server.sendmail(mittente, [destinatario], msg.as_string())
    except Exception as e:
        print(f"ERRORE: email non inviata: {e}", file=sys.stderr)
        return 1
    print(f"OK: email inviata a {destinatario}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
