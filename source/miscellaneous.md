(c:misc)=
# Miscellaneous

%---------------------------------------------------------------------------------------------------
(s:set)=
## Set command

The `set` command is used for setting parameters. The components of `set` are:
```{code} yaml
parameter     # [String] Parmeter(s) to vary.
value         # [Expression] Value to set.
```
In the `value` expression, `parameter` can be used for the current value of the parameter being changed
and `self` can be used for the lattice element whose parameter is being changed. 
Example:
```{code} yaml
- B1a:
    kind: Bend
    BendP:
      e1: 0.1
      g_ref: 0.02

- set:
    parameter: B1.*>BendP.e1
    value: 2*parameter + atan(self.BendP.g_ref)
```
In this example, the `BendP.e1` parameter of all elements whose name begins with `B1` is modified.
This includes element `B1a`. 

Note: Pattern matching is not supported in the `value` expression.

%---------------------------------------------------------------------------------------------------
(s:extension-syntax)=
## Extension Syntax

An Extension is data added to a PALS lattice that is not part of the PALS standard.
For example, information specific to a particular machine that has no analogue with other
machines can be put in an extension. A list of "registered" extensions is in the 
[Extension List](#c:extension-list) section.

An extension section in a lattice file has a root node and sub-tree below this root
node is part of the extension. Extensions may be marked in a PALS lattice file using
an `extension` node to mark the root node. The syntax is:
```{code} yaml
<name>:
  - extension: <extension-type>
  ... extension info ...
```
where `<name>` is any name (since a given extension type might appear in multiple places in
the lattice file), and `<extension-type>` is the type of the extension. Example:
```{code} yaml
synchrotron-connect:
  extension: Cornell-CESR-Connections
  alarm-system:
    ...
```

Alternatively, Extension root node names may be "registered" using an `extension-names` node 
to be used as the root of the extension sub-tree. Example:
```{code} yaml
PALS:
  extension-names:
    -name: db_node
    -name: short_name

  facility:
    Q1_vary_long_string:
      short_name: Q1
      db_node:
        ... data base info ...
```
The `extension-names` node must appear as a child of the `PALS` root node.
