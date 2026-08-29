# -*- coding: utf-8 -*-
import numpy as np, json
BASE=dict(r=np.log(2)/30.,K=1e6,kS=.30,kA=.03,kG=.003,alpha=.05,beta=.10,mu=1e-7,EC50=1.)
REL=5e5
def kill(C,k,E): return k*C/(E+C)
def ttp(P,S0=1e5,C0=1.,days=6000,dt=.25):
    S,A,G=S0,0.,0.
    for i in range(int(days/dt)):
        t=i*dt;N=S+A+G
        if N>=REL: return t/30.44
        C=C0; g=P['r']*(1-N/P['K']); f=C/(P['EC50']+C); h=P['EC50']/(P['EC50']+C)
        dS=g*S-kill(C,P['kS'],P['EC50'])*S-P['alpha']*f*S+P['beta']*h*A-P['mu']*S
        dA=g*A-kill(C,P['kA'],P['EC50'])*A+P['alpha']*f*S-P['beta']*h*A
        dG=g*G-kill(C,P['kG'],P['EC50'])*G+P['mu']*S
        S=max(0,S+dS*dt);A=max(0,A+dA*dt);G=max(0,G+dG*dt)
    return days/30.44
b=ttp(BASE)
print("TIER 5.2 SENSITIVITY — what actually controls time to relapse?")
print("baseline TTP = %.1f months\n"%b)
print("%-40s %10s %10s %10s"%("parameter varied","low","base","high"))
print("-"*74)
scans=[("kS  potency (kill rate, sensitive)","kS",[.10,.30,1.0]),
       ("kG  residual kill on resistant clone","kG",[.001,.003,.025]),
       ("mu  resistance emergence rate","mu",[1e-6,1e-7,1e-8]),
       ("alpha  adaptive induction rate","alpha",[.20,.05,.01]),
       ("beta  adaptive reversion rate","beta",[.02,.10,.50]),
       ("r   LSC growth rate","r",[np.log(2)/15,np.log(2)/30,np.log(2)/90])]
rank=[]
for lab,k,vals in scans:
    res=[]
    for v in vals:
        P=dict(BASE); P[k]=v; res.append(ttp(P))
    print("%-40s %10.1f %10.1f %10.1f"%(lab,res[0],res[1],res[2]))
    rank.append((lab,max(res)-min(res)))
print("\nSPREAD IN TTP (months) — biggest lever first:")
for l,s in sorted(rank,key=lambda x:-x[1]): print("   %-42s %6.1f"%(l,s))

print("\n\nSTARTING LSC BURDEN — does deeper initial remission beat a better drug?")
print("%-24s %12s"%("LSC burden at start","TTP (months)"))
print("-"*38)
for s0 in [1e6,1e5,1e4,1e3,1e2]:
    print("%-24s %12.1f"%("%.0e"%s0,ttp(BASE,S0=s0)))

print("\n\nTIER 5.3 — COMBINATION (FSP1 inhibitor closes the adaptive arm)")
print("%-46s %12s"%("regimen","TTP (months)"))
print("-"*60)
combos=[("GPX4i alone",dict()),
        ("GPX4i + FSP1i  (adaptive arm 10x less protective)",dict(kA=.30)),
        ("GPX4i + FSP1i  (also blocks induction)",dict(kA=.30,alpha=.005)),
        ("GPX4i + azacitidine (lowers emergence rate)",dict(mu=1e-8)),
        ("triple: GPX4i + FSP1i + aza",dict(kA=.30,alpha=.005,mu=1e-8))]
for n,mod in combos:
    P=dict(BASE); P.update(mod); print("%-46s %12.1f"%(n,ttp(P)))
