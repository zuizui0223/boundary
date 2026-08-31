from math import isclose, log

from boundary_model.bounded_proxy_drift import identify_under_bounded_proxy_drift
from boundary_model.calibration_transport_family import (
    anchor_ladder,
    breakdown_factor,
    observed_kappa,
    symmetric_interval,
)
from boundary_model.channel_identifiability import VitalRateState, construct_channel_loss_symmetry
from boundary_model.multichannel_identifiability import (
    log_gauge_basis,
    reconstruct_final_channel,
    residual_equivalence_dimension,
)
from boundary_model.proxy_calibration import identify_from_net_and_stable_proxy


def test_k_minus_one_minus_r_dimension_rule():
    assert residual_equivalence_dimension(channels=5, independent_anchors=0).residual_dimension == 4
    assert residual_equivalence_dimension(channels=5, independent_anchors=2).residual_dimension == 2
    assert residual_equivalence_dimension(channels=5, independent_anchors=4).residual_dimension == 0
    assert len(log_gauge_basis(5)) == 4
    assert isclose(reconstruct_final_channel(net_product=120, anchored_values=[2,3,4], channels=4), 5)


def test_gamma_family_and_breakdown_are_reference_invariant():
    point=1/1.34
    interval=symmetric_interval(point,gamma=1.2)
    assert isclose(interval.lower,point/1.2)
    assert isclose(interval.upper,point*1.2)
    down=breakdown_factor(point); up=breakdown_factor(1.34)
    assert isclose(down[0],1.34) and isclose(down[0],up[0])
    assert isclose(down[1],log(1.34))


def test_two_calibration_anchors_observe_transport():
    k=observed_kappa(proxy_0=2,channel_0=1,proxy_1=6,channel_1=2)
    assert isclose(k,1.5)
    assert anchor_ladder(0).identification=='non_identified'
    assert anchor_ladder(1).identification=='partially_identified'
    assert anchor_ladder(2).identification=='point_identified'


def test_joint_drift_set_preserves_net_ratio():
    rho_e=1/1.34; rho_x=0.8; rho_w=rho_x*rho_e
    result=identify_under_bounded_proxy_drift(net_ratio=rho_w,proxy_ratio=rho_x,delta=0.2)
    assert result.joint_log_segment.slope == -1
    assert result.joint_log_segment.satisfies_net_constraint()
    assert not isclose(result.fecundity.upper*result.establishment.upper,rho_w)


def test_net_only_channel_symmetry():
    s=VitalRateState((0,1,2),(2,3,4),(4,3,2))
    f,e,equal=construct_channel_loss_symmetry(s,(0.8,0.7,0.6))
    assert equal
    assert f.fecundity != e.fecundity
    assert f.establishment != e.establishment


def test_stable_proxy_identifies_relative_channels():
    r=identify_from_net_and_stable_proxy(net_before=[2],net_after=[1.5],proxy_before=[1],proxy_after=[0.5],proxy_channel='fecundity')
    assert isclose(r.fecundity_ratio[0],0.5)
    assert isclose(r.establishment_ratio[0],1.5)
