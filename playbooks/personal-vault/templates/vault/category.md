```base
filters:
  and:
    - categories.contains(link("<Category>"))
    - not:
        - file.inFolder("templates")
views:
  - type: table
    name: All
    order:
      - file.name
      - summary
      - file.folder
      - tags
      - updated
    sort:
      - property: updated
        direction: DESC
  - type: table
    name: By domain
    groupBy:
      property: file.folder
      direction: ASC
    order:
      - file.name
      - summary
      - tags
```
