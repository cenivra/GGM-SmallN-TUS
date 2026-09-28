#!/usr/bin/env bash
# Verifica el repositorio contra manifests/SHA256_REPO.txt
# Regla: la huella de un archivo de texto se calcula con los finales de linea normalizados (LF)
# y la de un binario sobre sus bytes tal cual, igual que en generar_manifiesto.py.
set -u
cd "$(dirname "$0")/.." || exit 1
MAN="${1:-manifests/SHA256_REPO.txt}"
[ -f "$MAN" ] || { echo "no encuentro $MAN"; exit 1; }

ok=0; fallos=0; faltan=0
while IFS= read -r linea; do
  [ -z "$linea" ] && continue
  case "$linea" in \#*) continue ;; esac
  h="${linea%% *}"
  f="${linea#* }"; f="${f# }"; f="${f%$'\r'}"
  if [ ! -f "$f" ]; then echo "FALTA      $f"; faltan=$((faltan+1)); continue; fi
  case "$f" in
    *.png|*.jpg|*.jpeg|*.gif|*.pdf|*.zip|*.gz|*.rds|*.RData|*.sqlite)
      h2=$(sha256sum "$f" | cut -d' ' -f1) ;;
    *)
      h2=$(sed 's/\r$//' "$f" | sha256sum | cut -d' ' -f1) ;;
  esac
  if [ "$h" = "$h2" ]; then ok=$((ok+1)); else echo "DISTINTA   $f"; fallos=$((fallos+1)); fi
done < "$MAN"

echo "verificados: $ok | distintos: $fallos | faltantes: $faltan"
[ "$fallos" -eq 0 ] && [ "$faltan" -eq 0 ]
