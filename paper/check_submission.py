from __future__ import annotations
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MANUSCRIPT=ROOT/'paper/manuscript.md'
PROPOSAL=ROOT/'paper/ecology_letters_proposal.md'
EMAIL=ROOT/'paper/ecology_letters_proposal_email.md'
LIT=ROOT/'paper/literature_audit.md'
MATRIX=ROOT/'paper/claim_evidence_matrix.md'
WORD_RE=re.compile(r"\b[\w*<>/=+.-]+\b",re.UNICODE)

def words(text): return len(WORD_RE.findall(text))
def require(text,token):
    if token not in text: raise SystemExit(f'missing required token: {token}')
def forbid(text,token):
    if token.lower() in text.lower(): raise SystemExit(f'forbidden token: {token}')

def main():
    m=MANUSCRIPT.read_text(encoding='utf-8'); p=PROPOSAL.read_text(encoding='utf-8'); e=EMAIL.read_text(encoding='utf-8'); l=LIT.read_text(encoding='utf-8'); x=MATRIX.read_text(encoding='utf-8')
    abstract=m.split('## Abstract',1)[1].split('\n## ',1)[0]
    if words(abstract)>200: raise SystemExit(f'abstract >200 words: {words(abstract)}')
    proposal=p.split('## Proposal',1)[1].strip()
    paras=[z.strip() for z in re.split(r'\n\s*\n',proposal) if z.strip()]
    if len(paras)!=1: raise SystemExit('proposal must be one paragraph')
    if words(proposal)>300: raise SystemExit(f'proposal >300 words: {words(proposal)}')
    for token in ('identification axis','k-1-r','1/Gamma <= q_1/q_0 <= Gamma','breakdown factor','pollination','seed dispersal'):
        require(proposal,token)
    for token in ('k - 1 - r','Gamma*=max(rho_hat,1/rho_hat)','Design Rule 1','Design Rule 2','Figure 1. Biological proximity','Figure 2. Direct channel','Figure 3. Calibration transport'):
        require(m,token)
    for token in ('Ecology believes molecular data are mechanism and field data are pattern','Molecular data are not mechanistic','statistically independent'):
        forbid(m,token)
    require(e,'ecolets@cefe.cnrs.fr'); require(e,'ecolets2@cefe.cnrs.fr')
    require(l,'does **not** justify claiming that ecology formally endorses a universal one-dimensional hierarchy')
    require(x,'Claim-escalation stop rule')
    print('boundary submission OK')
    print(f'abstract words: {words(abstract)}')
    print(f'proposal words: {words(proposal)}')

if __name__=='__main__': main()
