from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "paper" / "manuscript.md"


def test_all_reference_list_sources_are_used_in_body() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")
    body, references = text.split("## References", 1)
    required_body_tokens = (
        "Ballantyne et al. 2017",
        "Bellman & Åström 1970",
        "Correia et al. 2025",
        "Grace et al. 2025",
        "Manski 2003",
        "Rader et al. 2012",
        "Reynolds & Fenster 2008",
        "Rothenberg 1971",
        "Rudman et al. 2018",
        "Schupp et al. 2010",
        "Siegel & Dee 2025",
        "Smith et al. 2020",
        "Ungerer et al. 2008",
    )
    for token in required_body_tokens:
        assert token in body, f"reference listed but not cited in body: {token}"

    # Keep the three load-bearing literature roles visible in prose rather than
    # satisfying the check with a single citation dump.
    assert "Ungerer et al. 2008; Rudman et al. 2018" in body
    assert "Rader et al. 2012; Reynolds & Fenster 2008; Ballantyne et al. 2017" in body
    assert "Bellman & Åström 1970; Rothenberg 1971; Manski 2003" in body

    for surname in (
        "Ballantyne",
        "Bellman",
        "Correia",
        "Grace",
        "Manski",
        "Rader",
        "Reynolds",
        "Rothenberg",
        "Rudman",
        "Schupp",
        "Siegel",
        "Smith",
        "Ungerer",
    ):
        assert surname in references
