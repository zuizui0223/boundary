"""Stable versus time-varying proxy-calibration constructions."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Literal, Sequence

ProxyChannel=Literal["fecundity","establishment"]

@dataclass(frozen=True)
class ChannelChangeRatios:
    fecundity_ratio: tuple[float,...]
    establishment_ratio: tuple[float,...]

def _positive(values:Sequence[float]):
    out=tuple(map(float,values))
    if not out or any(v<=0 for v in out): raise ValueError("positive nonempty values required")
    return out

def identify_from_net_and_stable_proxy(*,net_before:Sequence[float],net_after:Sequence[float],proxy_before:Sequence[float],proxy_after:Sequence[float],proxy_channel:ProxyChannel):
    w0,w1,x0,x1=map(_positive,(net_before,net_after,proxy_before,proxy_after))
    if len({len(w0),len(w1),len(x0),len(x1)})!=1: raise ValueError("series must share length")
    wr=tuple(a/b for a,b in zip(w1,w0)); xr=tuple(a/b for a,b in zip(x1,x0))
    if proxy_channel=="fecundity": return ChannelChangeRatios(xr,tuple(w/f for w,f in zip(wr,xr)))
    if proxy_channel=="establishment": return ChannelChangeRatios(tuple(w/e for w,e in zip(wr,xr)),xr)
    raise ValueError("unknown proxy_channel")

def construct_time_varying_proxy_symmetry(*,net_before,net_after,proxy_before,proxy_after,baseline_calibration,calibration_shift,proxy_channel:ProxyChannel="fecundity"):
    w0,w1,x0,x1,q0,h=map(_positive,(net_before,net_after,proxy_before,proxy_after,baseline_calibration,calibration_shift))
    if len({len(w0),len(w1),len(x0),len(x1),len(q0),len(h)})!=1: raise ValueError("series must share length")
    def ratios(q1):
        if proxy_channel=="fecundity":
            f0=tuple(x/q for x,q in zip(x0,q0)); f1=tuple(x/q for x,q in zip(x1,q1)); e0=tuple(w/f for w,f in zip(w0,f0)); e1=tuple(w/f for w,f in zip(w1,f1))
        else:
            e0=tuple(x/q for x,q in zip(x0,q0)); e1=tuple(x/q for x,q in zip(x1,q1)); f0=tuple(w/e for w,e in zip(w0,e0)); f1=tuple(w/e for w,e in zip(w1,e1))
        return ChannelChangeRatios(tuple(a/b for a,b in zip(f1,f0)),tuple(a/b for a,b in zip(e1,e0)))
    stable=q0; shifted=tuple(a*b for a,b in zip(h,q0))
    return ratios(stable),ratios(shifted)
