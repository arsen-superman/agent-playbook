```base
filters:
  and:
    - file.inFolder("ideas")
    - file.hasProperty("status")
views:
  - type: table
    name: Active
    filters:
      or:
        - 'status == "raw"'
        - 'status == "explored"'
    groupBy:
      property: status
      direction: DESC
    order:
      - file.name
      - verdict
      - value
      - effort
      - next
      - updated
  - type: table
    name: All
    order:
      - file.name
      - status
      - verdict
      - promoted-to
      - updated
    sort:
      - property: updated
        direction: DESC
```
