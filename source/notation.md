(c:notation)=
# Syntax and Notation

%---------------------------------------------------------------------------------------------------
(s:keywords)=
## Keywords

The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](http://tools.ietf.org/html/rfc2119).

All keywords in this standard are case-sensitive.

%---------------------------------------------------------------------------------------------------
(s:syntax)=
## Syntax Used in this Document is YAML

The PALS [schema standard](#s:std.components) does not define any particular language to implement 
a lattice. Rather, there are associated
language specific standards that define grammars for YAML, JSON, Python, etc. Along with these
associated standards, there are packages that implement translation between lattice files and a 
representational internal format defined by the package.

While the standard itself is language agnostic, this document that describes the standard
needs to use some syntax and this syntax is based upon YAML.
YAML is [formally defined](https://yaml.org) and there are [tutorials to learn YAML](https://learnxinyminutes.com/yaml/).

%---------------------------------------------------------------------------------------------------
(c:yaml101)=
### YAML 101

In particular, there are dictionaries, which are unordered sets of key-value pairs, e.g.:

::::{tab-set}

:::{tab-item} YAML
:sync: yaml
```{code} yaml
this_dictionary:
  key1: value1
  key2: 2.0
  key3: true
```
:::
:::{tab-item} JSON
:sync: json
```{code} json
{"this_dictionary": {
  "key1": "value1",
  "key2": 2.0,
  "key3": true
}}
```
:::
:::{tab-item} TOML
:sync: toml
```{code} toml
[this_dictionary]
key1 = "value1"
key2 = 2.0
key3 = true
```
:::
:::{tab-item} Python
:sync: python
```{code} python
{"this_dictionary": {
  "key1": "value1",
  "key2": 2.0,
  "key3": True
}}
```
:::
:::{tab-item} C++17
:sync: cpp
```{code} c++
// insertion-order preserving dictionary
// alternatives: boost::multi_index_container, ryml::Tree, nlohmann::ordered_map, ...
using Dict = std::vector<std::pair<std::string, std::any>>;

Dict this_dictionary = {
    {"key1", "value1"s},
    {"key2", 2.0},
    {"key3", true}
};
```
:::
:::{tab-item} Julia
:sync: julia
```{code} julia
using OrderedCollections

this_dictionary = OrderedDict(
    "key1" => "value1",
    "key2" => 2.0,
    "key3" => true
)
```
:::

::::

And lists, which are ordered sets of items, e.g.:

::::{tab-set}

:::{tab-item} YAML
:sync: yaml
```{code} yaml
this_list:
  - entry1
  - entry2
  - more_entries
```
:::
:::{tab-item} JSON
:sync: json
```{code} json
{"this_list": [
  "entry1",
  "entry2",
  "more_entries"
]}
```
:::
:::{tab-item} TOML
:sync: toml
```{code} toml
this_list = [
  "entry1",
  "entry2",
  "more_entries"
]
```
:::
:::{tab-item} Python
:sync: python
```{code} python
{"this_list": [
  "entry1",
  "entry2",
  "more_entries"
]}
```
:::
:::{tab-item} C++17
:sync: cpp
```{code} c++
std::vector<std::string> this_list = {
    "entry1",
    "entry2",
    "more_entries"
};
```
:::
:::{tab-item} Julia
:sync: julia
```{code} julia
this_list = [
    "entry1",
    "entry2",
    "more_entries"
]
```
:::

::::

One can nest dictionaries into lists and other dictionaries, e.g.:

::::{tab-set}

:::{tab-item} YAML
:sync: yaml
```{code} yaml
this_list:
  - key1: value1
    key2: value2
  - named_dictionary:
      key3: value3
      key4: value4
```
:::
:::{tab-item} JSON
:sync: json
```{code} json
{"this_list": [
  {"key1": "value1",
   "key2": "value2"},
  {"named_dictionary": {
    "key3": "value3",
    "key4": "value4"
  }}
]}
```
:::
:::{tab-item} TOML
:sync: toml
```{code} toml
[[this_list]]
key1 = "value1"
key2 = "value2"

[[this_list]]
[this_list.named_dictionary]
key3 = "value3"
key4 = "value4"
```
:::
:::{tab-item} Python
:sync: python
```{code} python
{"this_list":
   [
     {"key1": "value1",
      "key2": "value2"},
     {"named_dictionary":
        {"key3": "value3",
         "key4": "value4"}
     }
   ]
}
```
:::
:::{tab-item} C++17
:sync: cpp
```{code} c++
std::vector<std::any> this_list = {
    Dict{{"key1", "value1"s}, {"key2", "value2"s}},
    Dict{{"named_dictionary", Dict{
        {"key3", "value3"s}, {"key4", "value4"s}
    }}}
};
```
:::
:::{tab-item} Julia
:sync: julia
```{code} julia
using OrderedCollections

this_list = [
    OrderedDict("key1" => "value1", "key2" => "value2"),
    OrderedDict("named_dictionary" => OrderedDict(
        "key3" => "value3", "key4" => "value4"
    ))
]
```
:::

::::

```{note}
   Developer note:
   PALS dictionaries should, when possible, implement a dictionary that preserves insertion order.

   While not strictly necessary, this helps with human readability:
   For example, having the [`kind`](#s:ele.syntax) key of an element as the first attribute enhances legibility.
```

(c:impl.fileformats)=
## File Formats

The PALS schema can be implemented in a variety of file formats.
It is highly recommended that the following self-describing file suffixes be used for 
top-level PALS files (files that contain the root `PALS` node):

* [YAML](https://yaml.org): `.pals.yaml`
* [JSON](https://www.json.org/json-en.html): `.pals.json`
* [TOML](https://toml.io): `.pals.toml`

For sub-level [included](#s:includefiles) PALS format files, replace `.pals` with `.subpals`.

Note: Not following the recommendation may lead to, for example, reader/visualization tools 
not auto discovering the file as PALS, which can create friction for users.

### Schema Files

Schema files for validation have not yet been developed.
A validation tool based on pydantic is in development.
See the [Libraries](#c:impl.libs) section.
