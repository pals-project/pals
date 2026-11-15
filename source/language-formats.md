(c:language-formats)=
# Language Formats

%---------------------------------------------------------------------------------------------------
(s:yaml.format)=
## YAML

In YAML, either single or double quotes may be used to [quote a string value](#s:constants).
A YAML reader will normally return `"Au+79"` and `Au+79` as the same string, so a parser must
keep track of whether a value was quoted in the file.
