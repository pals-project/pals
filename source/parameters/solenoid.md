%---------------------------------------------------------------------------------------------------
(s:solenoid.params)=
## SolenoidP: Solenoid Parameters

The `SolenoidP` parameter group describes a magnetic solenoid. 

The components of `SolenoidP` are:
```{code} yaml
SolenoidP:
  Ksol      # [1/m] Normalized solenoid strength.
  Bsol      # [T] Solenoid field.
```
The conversion between the field and normalized components is
```{math}
  Ksol = \frac{q}{P_0} \, Bsol
```
with {math}`q` being the charge of the reference particle and {math}`P_0` being the 
reference momentum.