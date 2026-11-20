(c:language-formats)=
# Language Formats

%---------------------------------------------------------------------------------------------------
(s:yaml.format)=
## YAML

In YAML, either single or double quotes may be used to [quote a string value](#s:constants).
Many YAML readers will, by default, return `"Au+79"` (with quotes) and 
`Au+79` (no quotes) as the same string. 
Since the PALS standard relies on distinguishing the two to disambiguate between names and 
expressions, a parser must avoid readers that do not preserve quotation marks.
