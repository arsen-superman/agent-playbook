```base
filters:
  and:
    - file.inFolder(this.file.folder)
    - file.ext == "md"
    - file.path != this.file.path
views:
  - type: table
    name: Notes
    order:
      - file.name
      - summary
      - categories
      - tags
      - updated
    sort:
      - property: updated
        direction: DESC
  - type: table
    name: By category
    groupBy:
      property: categories
      direction: ASC
    order:
      - file.name
      - summary
      - tags
```
