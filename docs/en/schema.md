## Config
<a id="config"></a>
Root of the configuration file; contains every other model
### Fields
- **identity**: `Identity` (see [Identity](#Identity))
  - Personal details of the CV owner
- **meta**: `Meta (Optional)` (see [Meta](#Meta))
  - Settings that customize how the CV is rendered
- **profile**: `list[Profile]` (see [Profile](#Profile))
  - CV profiles; each one is rendered to its own file

## Identity
<a id="identity"></a>
Personal details that identify the CV owner
### Fields
- **first_name**: `str`
  - Given name(s) of the person
- **family_name**: `str`
  - Family name(s) of the person; all but the last are abbreviated when shortened

## Meta
<a id="meta"></a>
Settings that customize how the CV is rendered
### Fields
- **overrides**: `Overrides (Optional)` (see [Overrides](#Overrides))
  - Optional overrides applied to template values

## Overrides
<a id="overrides"></a>
Values that replace the template defaults
### Fields
- **titles**: `dict[str, str] (Optional)`
  - Maps a section key to the title rendered in its place

## Profile
<a id="profile"></a>
One version of the CV; an identity can have several, each with its own sections
### Fields
- **name**: `str`
  - Profile name; also used to build the output file name
- **skills**: `list[Skills] (Optional)` (see [Skills](#Skills))
  - Scoped skill lists
- **language**: `list[Language] (Optional)` (see [Language](#Language))
  - Language proficiencies
- **experience**: `list[Experience] (Optional)` (see [Experience](#Experience))
  - Professional experience entries
- **project**: `list[Project] (Optional)` (see [Project](#Project))
  - Project entries
- **education**: `list[Education] (Optional)` (see [Education](#Education))
  - Education entries

## Education
<a id="education"></a>
A school or university course, from primary to higher education
### Fields
- **institution**: `str`
  - Name of the school or university
- **location**: `str`
  - Where the institution is located
- **level**: `str`
  - Degree or education level (e.g. Bachelor's)
- **course**: `str`
  - Name of the course or program
- **start**: `str`
  - When the course started
- **end**: `str`
  - When the course ended or is expected to end

## Experience
<a id="experience"></a>
A professional experience entry; the location, end date and actions are optional
### Fields
- **at**: `str`
  - Company or contractor the work was done for
- **role**: `str`
  - Position held
- **location**: `str (Optional)`
  - Where the work took place
- **start**: `str`
  - When the position started
- **end**: `str (Optional)`
  - When the position ended; omit if it is ongoing
- **actions**: `list[str] (Optional)`
  - Responsibilities and achievements, one per item

## Language
<a id="language"></a>
A language proficiency; the test details are optional
### Fields
- **name**: `str`
  - Name of the language
- **level**: `str`
  - Proficiency level (e.g. Fluent, Basic)
- **test**: `str (Optional)`
  - Name of the proficiency test taken (e.g. TOEFL)
- **test_registration**: `str (Optional)`
  - Label shown before the test code (e.g. Registration)
- **test_code**: `str (Optional)`
  - Code that proves the test result

## Project
<a id="project"></a>
A project entry, currently aimed at software; the language is optional
### Fields
- **name**: `str`
  - Name of the project
- **language**: `str (Optional)`
  - Main programming language used
- **details**: `list[str]`
  - Project highlights, one per item

## Skills
<a id="skills"></a>
A list of skills grouped under a scope
### Fields
- **scope**: `str`
  - Category the skills belong to
- **values**: `list[str]`
  - Skills listed under this scope
