.PHONY: wile alasa tenpo pali open pana

wile:
	pdm sync --dev

alasa:
	pdm run pytest -m "not skip"

tenpo:
	pdm run python -m kernprof -lv alasa/tenpo_ilo.py

pali:
	pdm run ${EDITOR} ilo/otokipona/__main__.py

open:
	pdm run python -m otokipona

pana:
	echo "mi ken ala pana lon tenpo ni."
	exit 1
