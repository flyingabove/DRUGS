# -*- coding: utf-8 -*-
import numpy as np
B=dict(r=np.log(2)/30.,K=1e6,kS=.30,kA=.03,kG=.003,alpha=.05,beta=.10,mu=1e-7,EC50=1.)
REL=5e5
def kill(C,k,E): return k*C/(E+C)
def ttp(P,ortho=0.,S0=1e5,C0=1.,days=12000,dt=.25):
    """ortho = kill rate from an ORTHOGONAL-mechanism partner drug, applied to ALL
    states including the ferroptosis-incompetent clone."""
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
r=B['r']
print("THE PHASE TRANSITION — kG (kill rate on the resistant clone) vs r (its growth rate)")
print("  r = %.4f/day.  Everything hinges on whether the drug still kills faster than that.\n"%r)
print("%14s %10s %14s"%("kG (/day)","kG/r","TTP (months)"))
print("-"*42)
for kg in [0.000,0.001,0.005,0.010,0.020,0.0231,0.025,0.030,0.050]:
    P=dict(B);P['kG']=kg
    t=ttp(P); print("%14.4f %10.2f %14s"%(kg,kg/r,("%.1f"%t) if t<390 else ">390  (control)"))
print("\n  Sharp threshold at kG/r = 1. Below it the resistant clone expands and relapse")
print("  is inevitable. Above it, disease is controlled indefinitely.")

print("\n\nPARTNER DRUG: another ferroptosis arm vs an ORTHOGONAL death mechanism")
print("%-52s %14s"%("regimen","TTP (months)"))
print("-"*68)
rows=[("GPX4i alone",dict(),0.),
      ("+ FSP1i        (2nd ferroptosis arm)",dict(kA=.30,alpha=.005),0.),
      ("+ orthogonal partner, weak   (0.005/day)",dict(),0.005),
      ("+ orthogonal partner, modest (0.015/day)",dict(),0.015),
      ("+ orthogonal partner, r-matched (0.023/day)",dict(),0.0231),
      ("+ orthogonal partner, strong (0.030/day)",dict(),0.030)]
for n,mod,o in rows:
    P=dict(B);P.update(mod)
    t=ttp(P,ortho=o); print("%-52s %14s"%(n,("%.1f"%t) if t<390 else ">390  (controlled)"))
print("""
  A partner hitting a SECOND FERROPTOSIS ARM buys ~0 months: the escaping clone is
  ferroptosis-INCOMPETENT, so every ferroptosis arm is already irrelevant to it.
  A partner with an ORTHOGONAL death mechanism, even a WEAK one, converts the
  regimen from delay to control once its kill rate clears the LSC growth rate.""")
