# -*- coding: utf-8 -*-
"""Tier 5.2/5.4 - LSC resistance dynamics under chronic vs pulsed GPX4 inhibition.
This is a REGIME EXPLORATION, not a prediction. Parameters are stated, varied,
and the output is which qualitative regime wins - not a number of cells."""
import numpy as np, json, itertools

# ---- states: S sensitive | A adaptively resistant (FSP1-high, REVERSIBLE) | G genetically resistant
# Parameters (all stated; scanned below)
P = dict(
  r        = np.log(2)/30.0,   # LSC net growth, doubling ~30 d (quiescent)
  K        = 1e6,              # carrying capacity of LSC niche
  kS       = 0.30,             # max kill rate/day, sensitive, at saturating drug
  kA       = 0.03,             # adaptive-resistant: 10x protected (FSP1 arm open)
  kG       = 0.003,            # genetic: 100x protected
  alpha    = 0.05,             # S->A induction rate/day at saturating drug (transcriptional)
  beta     = 0.10,             # A->S reversion rate/day when drug absent  <-- KEY PARAMETER
  mu       = 1e-7,             # S->G per day (genetic, irreversible)
  EC50     = 1.0,              # drug units
)

def kill(C, kmax, EC50): return kmax*C/(EC50+C)

def simulate(sched, days=720, P=P, dt=0.25):
    S,A,G = 1e5, 0.0, 0.0
    n=int(days/dt); traj=[]
    for i in range(n):
        t=i*dt; C=sched(t); N=S+A+G
        g=P['r']*(1-N/P['K'])
        dS = g*S - kill(C,P['kS'],P['EC50'])*S - P['alpha']*(C/(P['EC50']+C))*S + P['beta']*(P['EC50']/(P['EC50']+C))*A - P['mu']*S
        dA = g*A - kill(C,P['kA'],P['EC50'])*A + P['alpha']*(C/(P['EC50']+C))*S - P['beta']*(P['EC50']/(P['EC50']+C))*A
        dG = g*G - kill(C,P['kG'],P['EC50'])*G + P['mu']*S
        S=max(0,S+dS*dt); A=max(0,A+dA*dt); G=max(0,G+dG*dt)
        if i%int(1/dt)==0: traj.append((t,S,A,G))
    return np.array(traj)

# ---- dosing schedules, matched on TOTAL DOSE (area under curve)
AUC=1.0
def continuous(t): return AUC
def pulsed(period, duty):
    amp=AUC/duty
    return lambda t: amp if (t % period)<(period*duty) else 0.0

SCH=[("continuous low",continuous),
     ("pulse 7d  (2on/5off)", pulsed(7,2/7.)),
     ("pulse 14d (3on/11off)",pulsed(14,3/14.)),
     ("pulse 28d (5on/23off)",pulsed(28,5/28.)),
     ("pulse 28d (2on/26off)",pulsed(28,2/28.))]

print("TIER 5.2 - LSC RESISTANCE DYNAMICS, dose-matched schedules (2 years)")
print("all schedules deliver IDENTICAL total drug\n")
print("%-24s %10s %10s %10s %10s %8s"%("schedule","LSC final","%sensitive","%adaptive","%genetic","log10 red"))
print("-"*80)
out={}
for name,s in SCH:
    tr=simulate(s); S,A,G=tr[-1,1],tr[-1,2],tr[-1,3]; N=S+A+G
    out[name]=dict(N=N,S=S,A=A,G=G)
    print("%-24s %10.3g %9.1f%% %9.1f%% %9.1f%% %8.2f"%(
        name,N,100*S/N,100*A/N,100*G/N,np.log10(1e5/max(N,1e-9))))
tr=simulate(lambda t:0.0); print("%-24s %10.3g %9s %9s %9s %8s"%("NO DRUG (control)",tr[-1,1:].sum(),"-","-","-","-"))
json.dump({k:{kk:float(vv) for kk,vv in v.items()} for k,v in out.items()},open('resist_base.json','w'),indent=1)
