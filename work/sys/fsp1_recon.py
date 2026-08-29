# -*- coding: utf-8 -*-
"""Reconciling the model with the literature on FSP1.
Literature: high-FSP1 AML lines and FLT3-ITD+ blasts SURVIVE GPX4i but die when FSP1
is co-inhibited. My model said FSP1i adds nothing. Both can be true if they act on
DIFFERENT parameters: FSP1i changes BASELINE sensitivity (lowering S0 via deeper
kill), not the ACQUIRED ferroptosis-incompetent escape route (kG)."""
import numpy as np
B=dict(r=np.log(2)/30.,K=1e6,kS=.30,kA=.03,kG=.003,alpha=.05,beta=.10,mu=1e-7,EC50=1.)
REL=5e5
def kill(C,k,E): return k*C/(E+C)
def ttp(P,S0=1e5,C0=1.,days=12000,dt=.25):
    S,A,G=S0,0.,0.
    for i in range(int(days/dt)):
        t=i*dt;N=S+A+G
        if N>=REL: return t/30.44
        C=C0;g=P['r']*(1-N/P['K']);f=C/(P['EC50']+C);h=P['EC50']/(P['EC50']+C)
        dS=g*S-kill(C,P['kS'],P['EC50'])*S-P['alpha']*f*S+P['beta']*h*A-P['mu']*S
        dA=g*A-kill(C,P['kA'],P['EC50'])*A+P['alpha']*f*S-P['beta']*h*A
        dG=g*G-kill(C,P['kG'],P['EC50'])*G+P['mu']*S
        S=max(0,S+dS*dt);A=max(0,A+dA*dt);G=max(0,G+dG*dt)
    return days/30.44
print("RECONCILIATION — FSP1 inhibition acts on BASELINE SENSITIVITY, not on escape\n")
print("Scenario A — FSP1-LOW patient (GPX4i already works)")
print("   %-44s %s"%("GPX4i alone","%.1f mo"%ttp(B)))
print("   %-44s %s"%("+ FSP1i (no baseline benefit to add)","%.1f mo"%ttp(dict(B,kA=.30))))
print("\nScenario B — FSP1-HIGH patient (FLT3-ITD+; GPX4i alone barely works)")
Bh=dict(B,kS=.03)   # high FSP1 = intrinsically protected from GPX4i
print("   %-44s %s"%("GPX4i alone (intrinsically resistant)","%.1f mo"%ttp(Bh)))
print("   %-44s %s"%("+ FSP1i (restores GPX4i sensitivity)","%.1f mo"%ttp(dict(Bh,kS=.30))))
print("\nScenario C — FSP1i as DEEPER INITIAL CYTOREDUCTION (the S0 pathway)")
for s0,lab in [(1e5,"GPX4i alone, standard remission depth"),
               (1e4,"+ FSP1i, 1 log deeper initial kill"),
               (1e3,"+ FSP1i, 2 logs deeper initial kill")]:
    print("   %-44s %s"%(lab,"%.1f mo"%ttp(B,S0=s0)))
print("""
CORRECTED POSITION — both my model and the literature are right about different things:

  * FSP1i DOES matter for BASELINE sensitivity. In FSP1-high / FLT3-ITD+ disease it
    converts a non-responder into a responder (Scenario B: %.1f -> %.1f months).
    My earlier claim that "FSP1i does nothing" was too strong.

  * FSP1i does NOT rescue the long-term durability problem. The acquired escape route
    is ferroptosis INCOMPETENCE (ACSL4/LPCAT3 loss), against which every ferroptosis
    arm is irrelevant. That part of the original finding stands.

  => FSP1i is a PATIENT-SELECTION and DEPTH-OF-REMISSION tool, not a durability tool.
     The orthogonal-mechanism partner is still required for durability.
     These are two different partner drugs doing two different jobs."""%(ttp(Bh),ttp(dict(Bh,kS=.30))))
