from pathlib import Path
import sys
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from boundary_model.multichannel_identifiability import residual_equivalence_dimension
from boundary_model.observation_rank import log_linear_identification, scalar_observation_rank_gain

OUT=Path(__file__).resolve().parent/'figures'/'multichannel_anchor_dimension.png'


def build_figure(output:Path=OUT)->Path:
    output.parent.mkdir(parents=True,exist_ok=True)
    fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10.8,4.6),constrained_layout=True)

    # Panel A: the general rank criterion.  Start from a four-channel product
    # plus one direct channel anchor.  Several superficially different candidate
    # measurements remain in the existing row span; only a new direction buys
    # structural identification.
    channels=4
    existing=((1,0,0,0),)
    current=log_linear_identification(
        channels=channels,
        extra_observation_rows=existing,
    )
    candidates=[
        ('duplicate\nanchor',(1,0,0,0)),
        ('rescaled\nanchor',(3,0,0,0)),
        ('derived\nnet + anchor',(2,1,1,1)),
        ('new channel\nanchor',(0,1,0,0)),
    ]
    gains=[
        scalar_observation_rank_gain(
            channels=channels,
            existing_extra_rows=existing,
            candidate_row=row,
        )
        for _,row in candidates
    ]
    after_dims=[current.residual_dimension-gain for gain in gains]
    xpos=list(range(len(candidates)))
    ax1.bar(xpos,after_dims)
    ax1.axhline(current.residual_dimension,linestyle='--',linewidth=1.2)
    ax1.set_xticks(xpos,[label for label,_ in candidates])
    ax1.set_ylim(0,max(after_dims)+0.8)
    ax1.set_ylabel('Residual unidentified dimension')
    ax1.set_title('(A) Only a new observation direction reduces nullity')
    for x,(dim,gain) in enumerate(zip(after_dims,gains)):
        ax1.text(x,dim+0.08,f'rank gain = {gain}',ha='center',va='bottom',fontsize=8)
    ax1.text(
        0.02,0.96,
        f'current: rank={current.observation_rank}, residual={current.residual_dimension}',
        transform=ax1.transAxes,ha='left',va='top',fontsize=8,
    )

    # Panel B: the familiar direct-coordinate-anchor rule is a special case of
    # the general rank theorem.
    for k in (2,3,4,5):
        r=list(range(k))
        dims=[
            residual_equivalence_dimension(
                channels=k,
                independent_anchors=x,
            ).residual_dimension
            for x in r
        ]
        ax2.plot(r,dims,marker='o',linewidth=1.8,label=f'k={k}')
    ax2.set_xlabel('Independent direct channel anchors, r')
    ax2.set_ylabel('Residual unidentified dimension')
    ax2.set_title(r'(B) Coordinate-anchor corollary: $k-1-r$')
    ax2.legend(title='Chain length')

    fig.suptitle('Observation rank, not measurement count, controls structural identification')
    fig.savefig(output,dpi=300,bbox_inches='tight')
    plt.close(fig)
    return output


if __name__=='__main__':
    print(build_figure())
