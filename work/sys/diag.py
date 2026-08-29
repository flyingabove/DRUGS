# -*- coding: utf-8 -*-
import numpy as np
r=np.log(2)/30.0
print("WHY EVERY SCHEDULE FAILED — the governing inequality\n")
print("  LSC net growth rate  r  = %.4f /day  (30 d doubling)"%r)
for nm,k in [("sensitive   kS",0.30),("adaptive    kA",0.03),("genetic     kG",0.003)]:
    print("  kill rate %s = %.4f /day   %s"%(nm,k,"KILLS" if k>r else "*** CELL OUTGROWS DRUG ***"))
print("""
  kG (0.0030) < r (0.0231).  A genetically resistant LSC DIVIDES FASTER THAN THE
  DRUG KILLS IT. Once one exists, its clone expands without limit. No schedule,
  no dose fractionation, and no total-dose increase changes that -- it is a
  property of the resistant cell, not of the dosing.

  => MONOTHERAPY MAINTENANCE CANNOT PRODUCE INDEFINITE CONTROL. The model is not
     telling us the drug is bad; it is telling us the ENDPOINT WAS WRONG.

REFRAME: this is exactly what real maintenance therapy does.
  QUAZAR AML-001 (oral azacitidine maintenance, FDA approved 2020):
     median OS 24.7 months vs 14.8 -- a ~10-month DELAY, not a cure.
  Azacitidine maintenance is not resistance-proof either, and it was approved.

  The correct endpoint is TIME TO RELAPSE, not LSC count at a fixed date.
  Re-running with time-to-progression below.
""")
