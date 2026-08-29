import numpy as np, io, json, glob, os
def rdxyz(f):
    L=io.open(f,encoding='utf-8',errors='ignore').read().splitlines()
    n=int(L[0].split()[0]); el=[];x=[]
    for r in L[2:2+n]:
        p=r.split(); el.append(p[0]); x.append([float(v) for v in p[1:4]])
    return el,np.array(x)
def orb(f):
    ho=lu=None
    for L in io.open(f,encoding='utf-8',errors='ignore'):
        if "(HOMO)" in L: ho=float(L.split()[-2])
        if "(LUMO)" in L and lu is None: lu=float(L.split()[-2])
    return ho,lu
S=json.load(open("set.json"))
ML210_LUMO=-9.11
print("SOTA SCREEN — GFN2-xTB, implicit water, geometry optimised\n")
print("%-4s %-22s %6s %5s %7s %7s %8s %8s"%("tag","R-group (x2)","MW","Rg","intraHB","freeHBD","LUMO","dLUMO"))
print("-"*86)
res=[]
for r in S:
    t=r["tag"]
    if not os.path.exists(f"{t}_w.xyz"): 
        print("%-4s %-22s   [not finished]"%(t,r["R1"])); continue
    el,X=rdxyz(f"{t}_w.xyz"); ho,lu=orb(f"{t}.out")
    Rg=np.sqrt(((X-X.mean(0))**2).sum(1).mean())
    heavy=[i for i,e in enumerate(el) if e in ("N","O")]
    hb=fr=0
    for h in [i for i,e in enumerate(el) if e=="H"]:
        d=np.linalg.norm(X[heavy]-X[h],axis=1)
        if not len(np.where(d<1.25)[0]): continue
        if len(np.where((d>1.5)&(d<2.6))[0]): hb+=1
        else: fr+=1
    d=lu-ML210_LUMO
    res.append(dict(tag=t,R=r["R1"],MW=r["MW"],logP=r["logP"],TPSA=r["TPSA"],
                    Rg=Rg,intraHB=hb,freeHBD=fr,LUMO=lu,dLUMO=d,smiles=r["smiles"]))
    print("%-4s %-22s %6.1f %5.2f %7d %7d %8.2f %+8.3f"%(t,r["R1"],r["MW"],Rg,hb,fr,lu,d))
if res:
    # rank: donors must survive in water; warhead must stay intact
    res.sort(key=lambda r:(-r["freeHBD"], r["intraHB"], abs(r["dLUMO"])))
    print("\nRANKED (free donors desc, then least masking, then least warhead perturbation)")
    for i,r in enumerate(res[:5],1):
        print("  %d. %-22s freeHBD=%d intraHB=%d dLUMO=%+.3f  MW %.0f logP %.2f"%(
            i,r["R"],r["freeHBD"],r["intraHB"],r["dLUMO"],r["MW"],r["logP"]))
    json.dump(res,open("screen_results.json","w"),indent=1)
    print("\nWINNER: %s"%res[0]["R"]); print("  %s"%res[0]["smiles"])
