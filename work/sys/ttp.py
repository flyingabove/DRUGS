# -*- coding: utf-8 -*-
import numpy as np, json
P=dict(r=np.log(2)/30.,K=1e6,kS=.30,kA=.03,kG=.003,alpha=.05,beta=.10,mu=1e-7,EC50=1.)
REL=5e5  # relapse threshold: LSC burden at which disease becomes clinically evident
def kill(C,k,E): return k*C/(E+C)
def ttp(sched,P=P,days=3000,dt=.25,S0=1e5):
    S,A,G=S0,0.,0.
    for i in range(int(days/dt)):
        t=i*dt; C=sched(t); N=S+A+G
        if N>=REL: return t/30.44   # months
        g=P['r']*(1-N/P['K']); f=C/(P['EC50']+C); h=P['EC50']/(P['EC50']+C)
        dS=g*S-kill(C,P['kS'],P['EC50'])*S-P['alpha']*f*S+P['beta']*h*A-P['mu']*S
        dA=g*A-kill(C,P['kA'],P['EC50'])*A+P['alpha']*f*S-P['beta']*h*A
        dG=g*G-kill(C,P['kG'],P['EC50'])*G+P['mu']*S
        S=max(0,S+dS*dt);A=max(0,A+dA*dt);G=max(0,G+dG*dt)
    return days/30.44
def pulsed(per,duty,auc=1.):
    a=auc/duty; return lambda t: a if (t%per)<(per*duty) else 0.
SCH=[("NO DRUG (control)",lambda t:0.),("continuous low",lambda t:1.),
     ("pulse 7d (2on/5off)",pulsed(7,2/7.)),("pulse 14d (3on/11off)",pulsed(14,3/14.)),
     ("pulse 28d (5on/23off)",pulsed(28,5/28.)),("continuous 2x dose",lambda t:2.),
     ("continuous 4x dose",lambda t:4.)]
print("TIER 5.4 - TIME TO RELAPSE (the QUAZAR endpoint)\n")
print("%-26s %14s %14s"%("schedule","TTP (months)","delay vs ctrl"))
print("-"*58)
base=None
for n,s in SCH:
    m=ttp(s)
    if base is None: base=m
    print("%-26s %14.1f %14s"%(n,m,"-" if n.startswith("NO DRUG") else "+%.1f mo"%(m-base)))
print("\n  benchmark: oral azacitidine maintenance delivered ~+9.9 months OS and was FDA approved.")
