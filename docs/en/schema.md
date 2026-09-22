## Config
<a id="config"></a>
The complete configuration model - includes all others
### Fields
- **identity**: `Identity` (see [Identity](#Identity))
  - Identity configuration block
- **meta**: `Meta (Optional)` (see [Meta](#Meta))
  - Optional metadata for the configuration
- **profile**: `list[Profile]` (see [Profile](#Profile))
  - List of curriculum profiles

## Identity
<a id="identity"></a>
The identity model - holds the data for the user identification
### Fields
- **first_name**: `str`
- **family_name**: `str`

## Meta
<a id="meta"></a>
This is the overrides model - used for replacing values in templates
### Fields
- **overrides**: `Overrides (Optional)` (see [Overrides](#Overrides))

## Overrides
<a id="overrides"></a>
### Fields
- **titles**: `dict[str, str] (Optional)`

## Profile
<a id="profile"></a>
An identity can hold multiple profiles, each one contains the sections used in the template
### Fields
- **name**: `str`
- **skills**: `list[Skills] (Optional)` (see [Skills](#Skills))
- **language**: `list[Language] (Optional)` (see [Language](#Language))
- **experience**: `list[Experience] (Optional)` (see [Experience](#Experience))
- **project**: `list[Project] (Optional)` (see [Project](#Project))
- **education**: `list[Education] (Optional)` (see [Education](#Education))

## Education
<a id="education"></a>
Holds the info for the primary/higher education courses
### Fields
- **institution**: `str`
- **location**: `str`
- **level**: `str`
- **course**: `str`
- **start**: `str`
- **end**: `str`

## Experience
<a id="experience"></a>
Holds the professional experience, end times and actions are optional
### Fields
- **at**: `str`
- **role**: `str`
- **location**: `str (Optional)`
- **start**: `str`
- **end**: `str (Optional)`
- **actions**: `list[str] (Optional)`

## Language
<a id="language"></a>
Holds the information for language proficiencies, test proof codes are optional
### Fields
- **name**: `str`
- **level**: `str`
- **test**: `str (Optional)`
- **test_registration**: `str (Optional)`
- **test_code**: `str (Optional)`

## Project
<a id="project"></a>
Holds the information for coding (for now) projects, languages are optional
### Fields
- **name**: `str`
- **language**: `str (Optional)`
- **details**: `list[str]`

## Skills
<a id="skills"></a>
Holds the information for listing the skills in a list format, scoped
### Fields
- **scope**: `str`
- **values**: `list[str]`
