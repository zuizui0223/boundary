from __future__ import annotations
import hashlib,json,shutil,zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs/reviewer_bundle'
FILES=[
 'paper/manuscript.md','paper/literature_audit.md','paper/claim_evidence_matrix.md','paper/reviewer_objections.md',
 'boundary_model/__init__.py','boundary_model/multichannel_identifiability.py','boundary_model/calibration_transport_family.py','boundary_model/bounded_proxy_drift.py','boundary_model/channel_identifiability.py','boundary_model/proxy_calibration.py',
 'tests/test_boundary_core.py'
]
FIGURES=['mechanistic_evidence_axes.png','multichannel_anchor_dimension.png','boundary_identification_geometry.png']

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def build(output:Path=OUT):
    if output.exists(): shutil.rmtree(output)
    output.mkdir(parents=True)
    for rel in FILES:
        src=ROOT/rel; dst=output/('review_manuscript.md' if rel=='paper/manuscript.md' else rel)
        dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,dst)
    figdir=output/'figures'; figdir.mkdir()
    for name in FIGURES:
        src=ROOT/'paper/figures'/name
        if not src.exists() or src.stat().st_size==0: raise SystemExit(f'missing figure: {name}')
        shutil.copy2(src,figdir/name)
    reviewer_test=output/'tests/test_reviewer_snapshot.py'
    reviewer_test.write_text("""from pathlib import Path\n\nROOT=Path(__file__).resolve().parents[1]\n\ndef test_snapshot_is_boundary_only():\n    assert (ROOT/'review_manuscript.md').exists()\n    assert not (ROOT/'paper/mee_manuscript_draft.md').exists()\n    assert not any('rach_seq' in p.as_posix().lower() for p in ROOT.rglob('*') if p.is_file())\n    for name in ('mechanistic_evidence_axes.png','multichannel_anchor_dimension.png','boundary_identification_geometry.png'):\n        p=ROOT/'figures'/name\n        assert p.exists() and p.stat().st_size>0\n""",encoding='utf-8')
    (output/'README_FOR_REVIEW.md').write_text('# Anonymous Paper A reviewer bundle\n\nRun `PYTHONPATH=. python -m pytest -q tests`.\n',encoding='utf-8')
    manifest={'boundary_manuscript_included':True,'microdonta_method_paper_included':False,'files':{}}
    for p in sorted(x for x in output.rglob('*') if x.is_file()):
        rel=p.relative_to(output).as_posix(); manifest['files'][rel]={'bytes':p.stat().st_size,'sha256':sha(p)}
    (output/'bundle_manifest.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    z=output.parent/'reviewer_bundle.zip'
    if z.exists(): z.unlink()
    with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as a:
        for p in sorted(x for x in output.rglob('*') if x.is_file()): a.write(p,p.relative_to(output.parent))
    print(output/'bundle_manifest.json'); print(z)
    return output

if __name__=='__main__': build()
