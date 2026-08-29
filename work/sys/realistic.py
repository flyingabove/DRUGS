# -*- coding: utf-8 -*-
"""Re-run with kG constrained by the literature (ACSL4 loss ~ complete protection
against GPX4 inhibitors) instead of the optimistic assumed value.
Question: what benefit can this realistically claim, against the QUAZAR bar?"""
import numpy as np
B=dict(r=np.log(2)/30.,K=1e6,kS=.30,kA=.03,kG=.003,alpha=.05,beta=.10,mu=1e-7,EC50=1.)
REL=5e5
def kill(C,k,E): return k*C/(E+C)
def ttp(P,ortho=0.,S0=1e5,C0=1.,days=12000,dt=.25):
    S,A,G=S0,0.,0.
    for i in range(int(days/dt)):
        t=i*dt;N=S+A+G
        if N>=REL: return t/30.44
        C=C0;g=P['r']*(1-N/P['K']);f=C/(P['EC50']+C);h=P['EC50']/(P['EC50']+C)
        dS=g*S-(kill(C,P['kS'],P['EC50'])+ortho)*S-P['alpha']*f*S+P['beta']*h*A-P['mu']*S
        dA=g*A-(kill(C,P['kA'],P['EC50'])+ortho)*A+P['alpha']*f*S-P['beta']*h*A
        dG=g*G-(kill(C,P['kG'],P['EC50'])+ortho)*G+P['mu']*S
        S=max(0,S+dS*dt);A=max(0,A+dA*dt);G=max(0,G+dG*dt)
    return days/30.44
base=ttp(B,C0=0.)
print("LITERATURE-CONSTRAINED RE-RUN\n")
print("ACSL4 loss is near-complete protection specifically against GPX4 inhibitors,")
print("so kG should be near zero rather than the 0.003/day originally assumed.\n")
print("%-46s %12s %12s"%("scenario","TTP (mo)","delay"))
print("-"*72)
rows=[("no drug (control)",dict(),0.,0.),
      ("GPX4i, kG=0.003 (original optimistic)",dict(kG=.003),0.,1.),
      ("GPX4i, kG=0.0005 (literature-constrained)",dict(kG=.0005),0.,1.),
      ("GPX4i, kG=0 (complete escape)",dict(kG=0.),0.,1.),
      ("  + FSP1i (same disabled axis)",dict(kG=0.,kA=.30,alpha=.005),0.,1.),
      ("  + SLC7A11 agent (partly ACSL4-independent)",dict(kG=0.),0.008,1.),
      ("  + venetoclax (orthogonal, apoptosis)",dict(kG=0.),0.015,1.),
      ("  + azacitidine (lowers emergence)",dict(kG=0.,mu=1e-8),0.,1.),
      ("  + SLC7A11 + aza",dict(kG=0.,mu=1e-8),0.008,1.)]
for n,mod,o,c in rows:
    P=dict(B);P.update(mod)
    t=ttp(P,ortho=o,C0=c)
    print("%-46s %12s %12s"%(n,("%.1f"%t) if t<390 else ">390",
        "-" if c==0 else "+%.1f mo"%(t-base)))
print("""
BENCHMARK  oral azacitidine maintenance (QUAZAR AML-001): median OS 24.7 vs 14.8
           months = +9.9 months, and that was sufficient for FDA approval in 2020.""")
