"""Legacy additive-around-one calibration-drift calculations.

Canonical Paper A reporting uses the symmetric Gamma family in
``calibration_transport_family``. This module is retained only for reproducible
directional percentage translations.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import isclose, log
from typing import Literal

ChannelName=Literal["fecundity","establishment"]
Direction=Literal["decrease","increase","ambiguous"]
DriftPlacement=Literal["multiplicative","inverse"]

@dataclass(frozen=True)
class IdentifiedRatioInterval:
    point_under_stability: float
    lower: float
    upper: float
    multiplicative_width: float
    direction_at_declared_bound: Direction
    breakdown_delta: float
    breakdown_censored_at_one: bool
    calibration_placement: DriftPlacement
    @property
    def excludes_one(self): return self.upper<1.0 or self.lower>1.0

@dataclass(frozen=True)
class JointLogIdentifiedSegment:
    log_fecundity_at_kappa_lower: float
    log_establishment_at_kappa_lower: float
    log_fecundity_at_kappa_upper: float
    log_establishment_at_kappa_upper: float
    log_net_ratio: float
    slope: float=-1.0
    def satisfies_net_constraint(self):
        return isclose(self.log_fecundity_at_kappa_lower+self.log_establishment_at_kappa_lower,self.log_net_ratio) and isclose(self.log_fecundity_at_kappa_upper+self.log_establishment_at_kappa_upper,self.log_net_ratio)

@dataclass(frozen=True)
class BoundedProxyDriftResult:
    proxy_channel: ChannelName
    delta: float
    net_ratio: float
    proxy_ratio: float
    fecundity: IdentifiedRatioInterval
    establishment: IdentifiedRatioInterval
    joint_log_segment: JointLogIdentifiedSegment

def _interval(point:float,delta:float,placement:DriftPlacement):
    if placement=="multiplicative": lo,hi=point*(1-delta),point*(1+delta)
    else: lo,hi=point/(1+delta),point/(1-delta)
    direction="decrease" if hi<1 else "increase" if lo>1 else "ambiguous"
    if isclose(point,1): bd=0.0
    elif placement=="multiplicative": bd=(1/point-1) if point<1 else (1-1/point)
    else: bd=(1-point) if point<1 else (point-1)
    censored=bd>=1
    bd=min(max(bd,0),1)
    return IdentifiedRatioInterval(point,lo,hi,hi/lo,direction,bd,censored,placement)

def identify_under_bounded_proxy_drift(*,net_ratio:float,proxy_ratio:float,delta:float,proxy_channel:ChannelName="fecundity",tolerance:float=1e-12):
    w,x,d=float(net_ratio),float(proxy_ratio),float(delta)
    if w<=0 or x<=0: raise ValueError("ratios must be positive")
    if not 0<=d<1: raise ValueError("delta must satisfy 0 <= delta < 1")
    if proxy_channel=="fecundity":
        fp,ep=x,w/x; fplace,eplace="inverse","multiplicative"
        def pair(k): return x/k,(w/x)*k
    elif proxy_channel=="establishment":
        ep,fp=x,w/x; eplace,fplace="inverse","multiplicative"
        def pair(k):
            e=x/k; return w/e,e
    else: raise ValueError("unknown proxy_channel")
    flo,elo=pair(1-d); fhi,ehi=pair(1+d)
    seg=JointLogIdentifiedSegment(log(flo),log(elo),log(fhi),log(ehi),log(w))
    return BoundedProxyDriftResult(proxy_channel,d,w,x,_interval(fp,d,fplace),_interval(ep,d,eplace),seg)
