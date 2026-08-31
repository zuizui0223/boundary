from pathlib import Path
import sys
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from boundary_model.multichannel_identifiability import residual_equivalence_dimension

OUT=Path(__file__).resolve().parent/'figures'/'multichannel_anchor_dimension.png'

def build_figure(output:Path=OUT)->Path:
    output.parent.mkdir(parents=True,exist_ok=True)
    fig,ax=plt.subplots(figsize=(6.4,4.6),constrained_layout=True)
    for k in (2,3,4,5):
        r=list(range(k))
        dims=[residual_equivalence_dimension(channels=k,independent_anchors=x).residual_dimension for x in r]
        ax.plot(r,dims,marker='o',linewidth=1.8,label=f'k={k}')
    ax.set_xlabel('Independent direct channel anchors, r')
    ax.set_ylabel('Residual unidentified dimension')
    ax.set_title(r'A $k$-channel product leaves $k-1-r$ unresolved dimensions')
    ax.legend(title='Chain length')
    fig.savefig(output,dpi=300,bbox_inches='tight'); plt.close(fig)
    return output

if __name__=='__main__': print(build_figure())
