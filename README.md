# PyLangGetter
Tiny utility to help you download Dofus Retro Lang files.

# Installation
`pip install pylanggetter`

## Usage
`python -m pylanggetter` to get all lang files in **all language** and **all build** \
`python -m pylanggetter fr` to get lang files in **fr** language and **all build** \
`python -m pylanggetter it de` to get lang files in **it** and **de** langage and **all build** \
`python -m pylanggetter --prod` to get all lang files in **all language** and only **prod** build \
`python -m pylanggetter fr --temporis` to get lang files in **fr** language and **temporis** build \
`python -m pylanggetter it de --betaenv` to get lang files in **it** and **de** langage and **betaenv** build \
`python -m pylanggetter es pt --prod --temporis` to get lang files in **es** and **pt** langage and **prod** and **temporis** build

Available language option : `fr, de, en, it, es, pt, nl` \
Available build option : `--prod, --betaenv, --temporis, --ephemeris2releasebucket, --t3mporis-release`

#### Build description:
- **prod**: official lang used on regular servers
- **betaenv**: beta lang used on beta servers
- **temporis**: temporis lang used on temporis servers
- **ephemeris2releasebucket**: special temporis lang used on temporis servers
- **t3mporis-release**: temporis lang used on temporis 3 servers
