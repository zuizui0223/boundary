from math import log
from pathlib import Path
import sys
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from boundary_model.calibration_transport_family import breakdown_factor,symmetric_interval

OUT=Path(__file__).resolve().parent/'figures'/'boundary_identification_geometry.png'

def _curve(rho_x,rho_e_hat,gamma,n=300):
    k=np.geomspace(1/gamma,gamma,n)
    return k,rho_x/k,rho_e_hat*k

def build_figure(output:Path=OUT)->Path:
    output.parent.mkdir(parents=True,exist_ok=True)
    rho_e_hat=1/1.34; rho_x=0.80; rho_w=rho_x*rho_e_hat; gamma=1.20
    _,f,e=_curve(rho_x,rho_e_hat,gamma)
    gamma_star,eta_star=breakdown_factor(rho_e_hat)
    _,fb,eb=_curve(rho_x,rho_e_hat,gamma_star)
    fstar=rho_x/gamma_star; estar=rho_e_hat*gamma_star
    fig,axes=plt.subplots(1,2,figsize=(10.2,4.3),constrained_layout=True)
    ax=axes[0]; ax.plot(fb,eb,linestyle='--',linewidth=1.1,label=r'to breakdown $\Gamma^*=1.34$'); ax.plot(f,e,linewidth=2.3,label=r'finite bound $\Gamma=1.20$'); ax.scatter([rho_x],[rho_e_hat],label=r'$\Gamma=1$'); ax.scatter([fstar],[estar],label='breakdown'); ax.axvline(1,linestyle=':'); ax.axhline(1,linestyle=':'); ax.set_xlabel(r'$\rho_F$'); ax.set_ylabel(r'$\rho_E$'); ax.set_title('Sharp joint set in ratio space'); ax.legend(fontsize=8)
    ax=axes[1]; lf=np.log(f); le=np.log(e); ax.plot(np.log(fb),np.log(eb),linestyle='--'); ax.plot(lf,le,linewidth=2.3); ax.scatter([log(rho_x)],[log(rho_e_hat)]); ax.scatter([log(fstar)],[log(estar)]); ax.axvline(0,linestyle=':'); ax.axhline(0,linestyle=':'); ax.set_xlabel(r'$\log \rho_F$'); ax.set_ylabel(r'$\log \rho_E$'); ax.set_title('Log-ratio geometry: slope = -1'); ax.annotate(rf'$\Gamma^*=1.34$, $\eta^*={eta_star:.3f}$',(log(fstar),log(estar)),xytext=(-100,20),textcoords='offset points',arrowprops={'arrowstyle':'->'})
    interval=symmetric_interval(rho_e_hat,gamma=gamma)
    assert interval.lower<rho_e_hat<interval.upper
    assert np.allclose(f*e,rho_w)
    assert np.allclose(lf+le,log(rho_w))
    assert np.isclose(estar,1.0) and np.isclose(gamma_star,1.34)
    fig.savefig(output,dpi=300,bbox_inches='tight'); plt.close(fig)
    return output

if __name__=='__main__': print(build_figure())
