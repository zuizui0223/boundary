"""Exact two-channel multiplicative identifiability constructions."""
from __future__ import annotations
from dataclasses import dataclass
from math import isclose
from typing import Literal, Sequence

Channel=Literal["fecundity","establishment"]
ChannelConclusion=Literal["fecundity_only","establishment_only","mixed_or_unidentified","unchanged"]

@dataclass(frozen=True)
class VitalRateState:
    grid: tuple[float,...]
    fecundity: tuple[float,...]
    establishment: tuple[float,...]
    @property
    def net_performance(self): return tuple(f*e for f,e in zip(self.fecundity,self.establishment))

@dataclass(frozen=True)
class ChannelResolvedResult:
    conclusion: ChannelConclusion
    fecundity_ratio: tuple[float,...]
    establishment_ratio: tuple[float,...]

def apply_multiplicative_change(state:VitalRateState,attenuation:Sequence[float],*,channel:Channel)->VitalRateState:
    a=tuple(map(float,attenuation))
    if len(a)!=len(state.grid) or any(v<=0 for v in a): raise ValueError("positive attenuation with matching length required")
    if channel=="fecundity": return VitalRateState(state.grid,tuple(x*f for x,f in zip(a,state.fecundity)),state.establishment)
    if channel=="establishment": return VitalRateState(state.grid,state.fecundity,tuple(x*e for x,e in zip(a,state.establishment)))
    raise ValueError("unknown channel")

def construct_channel_loss_symmetry(baseline:VitalRateState,attenuation:Sequence[float]):
    f=apply_multiplicative_change(baseline,attenuation,channel="fecundity")
    e=apply_multiplicative_change(baseline,attenuation,channel="establishment")
    return f,e,all(isclose(x,y) for x,y in zip(f.net_performance,e.net_performance))

def reconstruct_from_net_and_one_channel(*,grid:Sequence[float],net_performance:Sequence[float],observed_channel_values:Sequence[float],observed_channel:Channel)->VitalRateState:
    g=tuple(map(float,grid)); w=tuple(map(float,net_performance)); o=tuple(map(float,observed_channel_values))
    if not(len(g)==len(w)==len(o)) or any(v<=0 for v in w+o): raise ValueError("positive equal-length inputs required")
    if observed_channel=="fecundity": return VitalRateState(g,o,tuple(x/y for x,y in zip(w,o)))
    if observed_channel=="establishment": return VitalRateState(g,tuple(x/y for x,y in zip(w,o)),o)
    raise ValueError("unknown channel")
