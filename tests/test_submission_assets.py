from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import subprocess,sys

ROOT=Path(__file__).resolve().parents[1]

def load(name):
    p=ROOT/'paper'/name; spec=spec_from_file_location(name.replace('.py',''),p); m=module_from_spec(spec); spec.loader.exec_module(m); return m

def test_submission_gate_passes():
    r=subprocess.run([sys.executable,'paper/check_submission.py'],cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    assert r.returncode==0,r.stdout
    assert 'boundary submission OK' in r.stdout

def test_figures_write(tmp_path):
    for script,name in [
        ('make_mechanistic_evidence_axis_figure.py','axes.png'),
        ('make_multichannel_anchor_figure.py','anchors.png'),
        ('make_boundary_identification_figure.py','gamma.png'),
    ]:
        out=tmp_path/name; assert load(script).build_figure(out)==out; assert out.exists() and out.stat().st_size>0

def test_claim_matrix_keeps_scope_guards():
    text=(ROOT/'paper/claim_evidence_matrix.md').read_text()
    assert 'Claim-escalation stop rule' in text
    assert 'k-1-r' in text
    assert 'statistical independence' in text

def test_repository_is_paper_a_only():
    paths=[p.as_posix().lower() for p in ROOT.rglob('*') if p.is_file() and '.git/' not in p.as_posix()]
    assert not any('mee_manuscript' in p for p in paths)
    assert not any('rach_seq' in p for p in paths)
    assert not any('g2_frozen' in p for p in paths)
