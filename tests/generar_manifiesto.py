"""Regenera manifests/SHA256_REPO.txt con la huella de cada archivo versionado.

Regla: los archivos de texto se hashean con los finales de línea normalizados a LF y los binarios
sobre sus bytes tal cual. La misma regla usa tests/check_hashes.sh, o la verificación fallaría
entera por un cambio de terminador de línea entre máquinas. El manifiesto no se incluye a sí mismo.
"""
import hashlib
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "manifests" / "SHA256_REPO.txt"
BINARIOS = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".gz", ".rds", ".RData", ".sqlite"}


def husmear(p: Path) -> str:
    if p.suffix.lower() in BINARIOS:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    texto = p.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


archivos = subprocess.run(["git", "ls-files"], cwd=RAIZ, capture_output=True, text=True).stdout.split()
lineas = [f"{husmear(RAIZ / f)}  {f}" for f in sorted(archivos)
          if f != "manifests/SHA256_REPO.txt" and (RAIZ / f).is_file()]
SALIDA.parent.mkdir(parents=True, exist_ok=True)
SALIDA.write_text("\n".join(lineas) + "\n", encoding="utf-8", newline="\n")
print(f"archivos en el manifiesto: {len(lineas)}")
print("escrito:", SALIDA)
