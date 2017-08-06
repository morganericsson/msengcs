# Metadata 

The following meta data fields are used. If (OPT), the field is optional.

- `Name`: Name of the course.
- `PrelCode`: The course code used in the application.
- `HEC`: The number of (HE) credits.
- `Year`: Which year (1-5)
- `Period`: Which study period (1-4). Use ranges (e.g., 3-4) if a course spans multiple periods.
- `Examiner1` and `Examiner2`: Specifies the examiners for the course. Should always be two.
- `Status`: The status of the syllabus document (to track progress).
- `Mandatory`: If the course is mandatory or not (Yes/No).
- `Subject`: Subject, e.g., `ComputerScience`.
- `Type`: The type of the course. Currently only `Regular` or `Project`.
- `PreReq`: Prerequisites given as a `;`-separated list of course codes (OPT).

Need to add support to generate the various matrices. 

- `ACMCS13`
- `CDIOl2`
- `HF`
- `LG`