"""Symmetric calibration-transport family for multiplicative ecological channels."""
from __future__ import annotations

from dataclasses import dataclass
from math import exp, isclose, log
from typing import Literal

IdentificationState = Literal["point_identified", "partially_identified", "non_identified"]
AnchorState = Literal["no_transport_calibration", "external_bound", "observed_transport"]

@dataclass(frozen=True)
class SymmetricCalibrationBound:
    gamma: float
    def __post_init__(self):
        if self.gamma < 1.0:
            raise ValueError("gamma must satisfy gamma >= 1")
    @property
    def eta(self): return log(self.gamma)
    @property
    def kappa_lower(self): return 1.0 / self.gamma
    @property
    def kappa_upper(self): return self.gamma
    @property
    def identification_state(self): return "point_identified" if isclose(self.gamma,1.0) else "partially_identified"
    @classmethod
    def from_eta(cls, eta: float):
        if eta < 0: raise ValueError("eta must satisfy eta >= 0")
        return cls(exp(float(eta)))

@dataclass(frozen=True)
class SymmetricIdentifiedInterval:
    point_under_stability: float
    gamma: float
    eta: float
    lower: float
    upper: float
    multiplicative_width: float
    breakdown_gamma: float
    breakdown_eta: float
    @property
    def excludes_one(self): return self.upper < 1.0 or self.lower > 1.0

@dataclass(frozen=True)
class AnchorLadderStep:
    anchors: int
    state: AnchorState
    identification: IdentificationState
    calibration_object: str
    consequence: str

def symmetric_interval(point_under_stability: float, *, gamma: float) -> SymmetricIdentifiedInterval:
    point=float(point_under_stability)
    if point <= 0: raise ValueError("point_under_stability must be strictly positive")
    bound=SymmetricCalibrationBound(float(gamma))
    return SymmetricIdentifiedInterval(point,bound.gamma,bound.eta,point/bound.gamma,point*bound.gamma,bound.gamma**2,max(point,1/point),abs(log(point)))

def breakdown_factor(point_under_stability: float):
    i=symmetric_interval(point_under_stability,gamma=1.0)
    return i.breakdown_gamma,i.breakdown_eta

def observed_kappa(*,proxy_0:float,channel_0:float,proxy_1:float,channel_1:float)->float:
    vals=[float(proxy_0),float(channel_0),float(proxy_1),float(channel_1)]
    if any(v<=0 for v in vals): raise ValueError("proxy and channel values must be strictly positive")
    return (vals[2]/vals[3])/(vals[0]/vals[1])

def identify_with_observed_kappa(*,net_ratio:float,proxy_ratio:float,kappa:float,proxy_channel:Literal["fecundity","establishment"]="fecundity"):
    w,x,k=map(float,(net_ratio,proxy_ratio,kappa))
    if min(w,x,k)<=0: raise ValueError("ratios and kappa must be strictly positive")
    if proxy_channel=="fecundity":
        f=x/k; e=w/f
    elif proxy_channel=="establishment":
        e=x/k; f=w/e
    else: raise ValueError("unknown proxy_channel")
    return f,e

def anchor_ladder(anchors:int)->AnchorLadderStep:
    if anchors==0: return AnchorLadderStep(0,"no_transport_calibration","non_identified","kappa unrestricted unless supplied by assumption","Unrestricted transport leaves channel change non-identified.")
    if anchors==1: return AnchorLadderStep(1,"external_bound","partially_identified","local q anchored; cross-regime Gamma remains external","A finite external transport bound gives a sharp identified set and breakdown factor.")
    if anchors==2: return AnchorLadderStep(2,"observed_transport","point_identified","q_0 and q_1 observed, hence kappa measured","Observed transport gives point identification.")
    raise ValueError("anchors must be one of 0, 1, 2")
