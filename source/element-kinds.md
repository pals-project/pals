(c:ele.kinds)=
# Element Kinds

Note: `name`, `length`, and `s_position` parameters stand alone and not part of any parameter group.

Example:
```{code} yaml
cleo:             # [string] user-defined name
  kind: Solenoid  # [string] element switch
  length: 3.74
  SolenoidP:
    Ksol: -0.15
```



%---------------------------------------------------------------------------------------------------
---
(s:magnets)=
## Magnets and RF Cavities

The following element kinds involve applied electromagnetic fields in vacuum.


%---------------------------------------------------------------------------------------------------
(s:ackicker)=
### ACKicker Element

An ACKicker element simulates a time-dependent kicker.
It is like a Kicker element except that the field varies in time.
This element requires a user supplied time-dependent expression.

Element parameter groups associated with this element kind are:
- [**ACKickerP**](#s:ackicker.params): AC kicker parameters.
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.

Example:
```{code} yaml
ack1:
  kind: ACKicker
  length: 0.3
  ACKickerP:
```


%---------------------------------------------------------------------------------------------------
(s:bend)=
###  Bend Elements: RBend and SBend

Dipole bend. There are two kinds of bends depending upon the "logical shape". 
The `RBend` element has a "rectangular" logical shape and the `SBend` element has a "sector"
logical shape.

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BendP**](#s:bend.params): Bend parameters
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**ElectricMultipoleP**](#s:elec.mult.params): Electric multipoles
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MagneticMultipoleP**](#s:mag.mult.params): Magnetic multipoles.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.

`RBend` and `SBend` elements are parameterized exactly the same way by the `BendP` parameter group. 
For example, `e1` and `e1_rect` have the same meaning for both kinds of bends.

The logical shape of a bend, in most situations, is irrelevant.
The only case where the logical shape can be used by a program is when the bend angle is varied.
In this case, for a `SBend`, the face angles `e1` and `e2` can be
held constant and `e1_rect` and `e2_rect` can be varied to keep the relationship
between `e1` and `e1_rect`, and `e2` and `e2_rect` satisfied as discussed in the
[`BendP`](#s:bend.params) documentation. Similarly, for a `RBend`,
the face angles `e1_rect` and `e2_rect` can be
held constant and `e1` and `e2` can be varied to keep the relationship
between `e1` and `e1_rect`, and `e2` and `e2_rect` satisfied.


%---------------------------------------------------------------------------------------------------
(s:crabcavity)=
### CrabCavity Element

A CrabCavity element is an zero length RF cavity that gives a longitudinal dependent
transverse kick. 

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**ElectricMultipoleP**](#s:elec.mult.params): Electric multipoles
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MagneticMultipoleP**](#s:mag.mult.params): Magnetic multipoles.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.

Example:
```{code} yaml
cc1:
  kind: CrabCavity
  RFP:
    frequency: 394.0e6 
    phase: 0.0
    voltage: 1.0e6
```

%---------------------------------------------------------------------------------------------------
(s:drift)=
### Drift Element

A `Drift` element is a space free and clear of any fields.

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.

Example:
```{code} yaml
d01:
  kind: Drift
  length: 2.07
  MetaP:
    description: "Blueprint: 4596-32A"
```

%---------------------------------------------------------------------------------------------------
(s:kicker)=
### Kicker Element

A Kicker element is an element that can deflect a beam transversely in both planes. 
It uses a zero-order (electric or magnetic) multipole field, determined by parameters in MagneticMultipoleP or ElectricMultipoleP such as Kn0, to deflect the beam in
horizontal and vertical directions.

Under Construction...

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**ElectricMultipoleP**](#s:elec.mult.params): Electric multipoles
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MagneticMultipoleP**](#s:mag.mult.params): Magnetic multipoles.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.


%---------------------------------------------------------------------------------------------------
(s:multipole)=
### Multipole Element

A general multipole element.  The fields are assumed to be uniform along the longitudinal direction,
and may contain (magnetic or electric) multipole contributions of any order.

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**ElectricMultipoleP**](#s:elec.mult.params): Electric multipoles
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MagneticMultipoleP**](#s:mag.mult.params): Magnetic multipoles.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.


%---------------------------------------------------------------------------------------------------
(s:octupole)=
### Octupole Element

An `octupole` is an element whose major field has a cubic field dependence with transverse offset.
Both electric and magnetic fields can be defined and additional multipole contributions are allowed.
In terms of functionality, an `octupole` is equivalent to a [`Multipole`](#s:multipole) element.

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**ElectricMultipoleP**](#s:elec.mult.params): Electric multipoles
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MagneticMultipoleP**](#s:mag.mult.params): Magnetic multipoles.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.

Example:
```{code} yaml
oct01w:
  kind: Octupole
  length: 0.4
  MagneticMultipoleP:
    Kn3: 1.0
```

%---------------------------------------------------------------------------------------------------
(s:quadrupole)=
### Quadrupole Element

A `quadrupole` is an element whose major field has a linear field dependence .with transverse offset.
Both electric and magnetic fields can be defined and the field is not restricted to be linear.
In terms of functionality, a `quadrupole` is equivalent to a [`Multipole`](#s:multipole) element

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**ElectricMultipoleP**](#s:elec.mult.params): Electric multipoles
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MagneticMultipoleP**](#s:mag.mult.params): Magnetic multipoles.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.

Example:
```{code} yaml
q01w:
  kind: Quadrupole
  length: 0.6
  MagneticMultipoleP:
    Kn1: 0.37
```

%---------------------------------------------------------------------------------------------------
(s:rfcavity)=
### RFCavity Element

An RFCavity element represents an RF cavity that accelerates or decelerates, and focuses or defocuses, a charged particle beam longitudinally and transversely using RF fields.

Under Construction...

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**ElectricMultipoleP**](#s:elec.mult.params): Electric multipoles
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MagneticMultipoleP**](#s:mag.mult.params): Magnetic multipoles.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**RFP**](#s:rf.params): RF parameters.
- [**SolenoidP**](#s:solenoid.params): Solenoid field.
- [**TrackingP**](#s:tracking.params): Tracking parameters.

Note: Multipole parameters represent DC fields. A common example is a DC solenoid field which
helps focusing.


%---------------------------------------------------------------------------------------------------
(s:sextupole)=
### Sextupole Element

A `sextupole` is an element whose major field has a quadratic field dependence with transverse offset.
Both electric and magnetic fields can be defined and additional multipole contributions are allowed.
In terms of functionality, a `sextupole` is equivalent to a [`Multipole`](#s:multipole) element.

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**ElectricMultipoleP**](#s:elec.mult.params): Electric multipoles
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MagneticMultipoleP**](#s:mag.mult.params): Magnetic multipoles.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.

Example:
```{code} yaml
s01w:
  kind: Sextupole
  length: 0.5
  MagneticMultipoleP:
    Kn2: 0.28
```


%---------------------------------------------------------------------------------------------------
(s:solenoid)=
### Solenoid Element

A `solenoid` is an element whose magnetic field is dominated by a field whose direction is aligned with the magnetic axis.
Additional magnetic (or electric) multipole contributions are allowed.

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**ElectricMultipoleP**](#s:elec.mult.params): Electric multipoles
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MagneticMultipoleP**](#s:mag.mult.params): Magnetic multipoles.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**SolenoidP**](#s:solenoid.params): Solenoid field.
- [**TrackingP**](#s:tracking.params): Tracking parameters.

Example:
```{code} yaml
sol01w:
  kind: Solenoid  
  length: 3.74
  SolenoidP:   
    Ksol: -0.15
```


%---------------------------------------------------------------------------------------------------
(s:wiggler)=
### Wiggler Element
A Wiggler element consists of a periodic array of alternating bending magnets. From a particle tracking perspective, it is equivalent to an undulator. Hereafter, the term "wiggler" will be used to denote either a wiggler or an undulator.

Under Construction...

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**ElectricMultipoleP**](#s:elec.mult.params): Electric multipoles
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MagneticMultipoleP**](#s:mag.mult.params): Magnetic multipoles.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.



%---------------------------------------------------------------------------------------------------
---
(s:beam)=   
## Beam and Plasma Elements 

The following element kinds involve interactions with the mean field of a particle distribution.


%---------------------------------------------------------------------------------------------------
(s:beambeam)=
### BeamBeam Element

A BeamBeam element defines the parameters of a oppositely moving "strong" beam that generates electromagnetic fields at the interaction point. This strong beam is assumed to have a three-dimensional (3D) Gaussian density distribution.

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BeamBeamP**](#s:beambeam.params): Beam-beam interaction parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.

Example:
```{code} yaml
bb1:
  kind: BeamBeam
  BeamBeamP:
    sigma_x: 0.1e-3
    sigma_y: 0.1e-3
    sigma_z: 5.0e-2
    energy: 1.0e10
    N_particle: 1.0e11
```

The length of this element is considered to be zero so if `length` is specified, it must be zero.



%---------------------------------------------------------------------------------------------------
---
(s:sources)=
## Sources and Collimation  

The following element kinds are for producing or removing beam particles. 


%---------------------------------------------------------------------------------------------------
(s:converter)=
### Converter Element

A Converter element represents a target (plate) onto which 
particles are slammed in order to generate
particles of a different type. For example, a tungsten plate which is bombarded with electrons to generate positrons.

Under Construction...

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**ElectricMultipoleP**](#s:elec.mult.params): Electric multipoles
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MagneticMultipoleP**](#s:mag.mult.params): Magnetic multipoles.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.

The length of this element is considered to be zero so if `length` is specified, it must be zero.


%---------------------------------------------------------------------------------------------------
(s:egun)=
### EGun Element
An EGun element represents an electron gun and encompasses a region starting from the cathode were
the electrons are generated.

Under Construction...

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**ElectricMultipoleP**](#s:elec.mult.params): Electric multipoles
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MagneticMultipoleP**](#s:mag.mult.params): Magnetic multipoles.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.


%---------------------------------------------------------------------------------------------------
(s:foil)=
### Foil Element

A Foil element represents a planar sheet of material which can strip electrons from a particle. In
conjunction, there will be scattering of the particle trajectory as well as an associated energy loss.
Material that can strip electrons from a particle
will also cause energy loss and diffusion.

Under Construction...

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.

The length of this element is considered to be zero so if `length` is specified, it must be zero.


%---------------------------------------------------------------------------------------------------                      
(s:mask)=
### Mask Element

A Mask element defines an aperture where the mask area can essentially have an arbitrary shape.
It is a collimation element to remove unwanted particles.

Under Construction...

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**ElectricMultipoleP**](#s:elec.mult.params): Electric multipoles
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MagneticMultipoleP**](#s:mag.mult.params): Magnetic multipoles.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.



%---------------------------------------------------------------------------------------------------
---
(s:instrumentation)=
## Instrumentation and Diagnostics

The following element kinds are for instrumentation and diagnostics.


%---------------------------------------------------------------------------------------------------
(s:instrument)=
### Instrument Element

An Instrument element is a measurement element for diagnostics.

Under Construction...

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**ElectricMultipoleP**](#s:elec.mult.params): Electric multipoles
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MagneticMultipoleP**](#s:mag.mult.params): Magnetic multipoles.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.



%---------------------------------------------------------------------------------------------------
---
(s:action)=
## Action Elements

The following element kinds specify an action that should be taken.  Typically, this is an abstract action
that is related to tracking or control.


(s:feedback)=
### Feedback Circuit 

A Feedback element is an element used to simulate a feedback circuit.
It gathers information about particle trajectories from the inputs
and uses this
to either adjust beam trajectories in the outputs and/or adjust parameters in the outputs.
A feedback element could be used, for example, to simulate RF feedback systems or beam position
feedback, or cooling of a proton beam by a beam of electrons.

Under Construction...

Note: This element does not have a `length` nor an `s_position`.


%---------------------------------------------------------------------------------------------------
(s:match)=
### Match Element

A Match element is used to match the orbit, Twiss, and dispersion parameters
 between two locations.

Under Construction...

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.

The length of this element is considered to be zero so if `length` is specified, it must be zero.


%---------------------------------------------------------------------------------------------------
(s:taylor)=
### Taylor Element

A Taylor element is a Taylor map that maps the input orbital phase space and possibly spin coordinates
of a particle at the entrance end of the element to the output orbital phase space and spin coordinates at the exit
end of the element. 

Under Construction...

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.

The length of this element is considered to be zero so if `length` is specified, it must be zero.



%---------------------------------------------------------------------------------------------------
---
(s:bookkeeping)=         
## Bookkeeping Elements                

The following element kinds provide relationships among branches and coordinate systems.


%---------------------------------------------------------------------------------------------------
(s:beginningele)=
### BeginningEle Element

A BeginningEle element is an initial element at start of a branch.
Under Construction...

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**TrackingP**](#s:tracking.params): Tracking parameters.

The length of this element is considered to be zero so if `length` is specified, it must be zero.


%---------------------------------------------------------------------------------------------------
(s:fiducial)=
### Fiducial Element

A Fiducial element is used to fix the position and orientation of the reference orbit within the global
coordinate system at the location of the fiducial element. A fiducial element will affect the global
floor coordinates of elements both upstream and downstream of the fiducial element.

Under Construction...

The length of this element is considered to be zero so if `length` is specified, it must be zero.


%---------------------------------------------------------------------------------------------------
(s:floorshift)=
### FloorShift Element

Global coordinates shift.

A `FloorShift` element shifts the reference curve in the global coordinate system without
affecting particle tracking. That is, in terms of tracking, a `FloorShift` element is equivalent
to a `Marker` element where a particle's position is unchanged going through the element.

Also see [`patch`](#s:patch) and [`fiducial`](#s:fiducial) elements.

Element parameter groups associated with this element kind are:
- [**FloorShiftP**](#s:floor.shift.params): Floor shift parameters.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.


%---------------------------------------------------------------------------------------------------
(s:fork)=
### Fork Element

A Fork element marks the start of an alternative branch for the beam (or X-rays or
other particles generated by the beam) to follow.
This element is used to connect lattice branches together.

Under Construction...

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.

The length of this element is considered to be zero so if `length` is specified, it must be zero.


%---------------------------------------------------------------------------------------------------
(s:marker)=
### Marker Element

A Marker element is a zero length element to mark a particular position.
The main purpose of this element is to name a position in the beamline.
`Marker` elements has a unit transport map. That is, a particle's phase space coordinates
are not altered with passage through the element

Element parameter groups associated with this element kind are:
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.

The `length` of this element must be zero.

`Marker` elements can be used, for example, to designate beam position monitor locations. In such
a case, the `BodyShiftP` parameter group can be used to misalign the BPM.

%---------------------------------------------------------------------------------------------------
(s:placeholder)=
### Placeholder Element

Placeholder element used for bookkeeping when constructing the expanded lattice.
This element has zero length and does nothing.
This element can be used as a [`base_item`](#s:placement) element for [superpositions](#s:superposition). 
Additionally, this element can be used, for example, to denote an invalid element in the internal
structures defined by a program.

`Placeholder` elements present in a lattice file will, as a part of lattice expansion, be removed.
That is, `Placeholder` elements will never be present in the final expanded lattice and
tracking through a `Placeholder` will never be needed.

This element does not have any associated parameter groups.

For other purposes, for example, to mark reference points, [Marker](#s:marker) elements may be used.


%---------------------------------------------------------------------------------------------------
(s:patch)=
### Patch Element

A Patch element is an element used to shift the reference orbit and time. 
A common application of this element is to orient two lines with respect 
to each other. For example,
to orient an injection line with the ring it is injecting into.

Under Construction...

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**PatchP**](#s:meta.params): Exit coordinates with respect to entrance coordinates.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.

Important: By convention, the energy shift is applied after a particle reaches the exit face.
This matters due to the dependence of the reference velocity on the the reference energy.


%---------------------------------------------------------------------------------------------------
(s:grouping)=         
## Structural and Grouping Elements

The following element kinds describe composite elements and support structures.


%---------------------------------------------------------------------------------------------------
(s:girder)=
### Girder Element

A Girder element is a support structure that orients the 
elements that are attached to it in space. This element can
be used to simulate any rigid support structure and there are 
no restrictions on how the lattice elements
that are supported are oriented with respect to one another.

Under Construction...

Note: This element does not have a `length` nor an `s_position`.


%---------------------------------------------------------------------------------------------------
(s:unionele)=
### UnionEle Element

The `UnionEle` element holds a set of overlapping elements.

Element parameter groups associated with this element kind are:
- [**ApertureP**](#s:aperture.params): Aperture parameters.
- [**BodyShiftP**](#s:bodyshift.params): Orientation of element with respect to its nominal position.
- **elements**: A list of contained element kinds.
- [**FloorP**](#s:floor.params): Floor position and orientation.
- [**MetaP**](#s:meta.params): Meta parameters.
- [**ReferenceP**](#s:ref.params): Reference parameters.
- [**ReferenceChangeP**](#s:ref.change.params): Reference energy change and/or reference time correction.
- [**TrackingP**](#s:tracking.params): Tracking parameters.

For each element contained in the `UnionEle`, the nominal position of the contained element is
such that the center of the contained element is at the center of the `UnionEle` with the
body coordinates of the contained element aligned with the body coordinates of the `UnionEle`.
Any contained element can be shifted from the nominal position by setting the contained element's
`BodyShiftP` parameters. The entire collection of elements can be oriented using the `UnionEle`'s
`BodyShiftP` parameters.

Example:
```{code} yaml
MMM:
  kind: UnionEle
  length: 2.1
  BodyShiftP:           # The UnionEle itself can be oriented.
    ...
  elements:
    Sa:
      kind: Solenoid    # Contained elements can be named.
      length: 1.3
      BodyShiftP:       # Orient the Solenoid
        x_offset: 0.03
        ...
    Ra:
      kind: RFCavity
      BodyShiftP:       # Orient the RFCavity
        y_rot: 0.012
        ...
```

Note: `UnionEle` shares the feature of describing elements that overlap physically, 
together with the [`placement`](#s:placement) construct within a `BeamLine` and the
[`superposition`](#s:superposition) construct.
