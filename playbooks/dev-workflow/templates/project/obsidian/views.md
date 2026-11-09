# Views
<!-- Obsidian add-on (optional). Bases tables over frontmatter; files stay the truth. Delete this file and .obsidian/ to drop the add-on. Filter a column header or type in Obsidian search: path:archive repos:billing-api -->

## Tasks
```base
filters:
  and:
    - file.name == "task"
    - file.inFolder("tasks")
views:
  - type: table
    name: Active by status
    groupBy:
      property: status
      direction: ASC
    order:
      - file.folder
      - title
      - repos
      - type
      - updated
  - type: table
    name: By repo
    groupBy:
      property: repos
      direction: ASC
    order:
      - file.folder
      - title
      - status
      - updated
```

## Archive
```base
filters:
  and:
    - file.name == "task"
    - file.inFolder("archive")
views:
  - type: table
    name: Closed
    order:
      - file.folder
      - title
      - repos
      - type
      - status
      - updated
    sort:
      - property: updated
        direction: DESC
```

## Decisions
```base
filters:
  and:
    - file.inFolder("decisions")
    - file.hasProperty("status")
views:
  - type: table
    name: Current by repo
    filters:
      and:
        - 'status == "accepted"'
    groupBy:
      property: repos
      direction: ASC
    order:
      - file.name
      - date
      - decided-by
  - type: table
    name: Superseded
    filters:
      and:
        - 'status == "superseded"'
    order:
      - file.name
      - superseded-by
      - repos
      - date
```

## Ideas
```base
filters:
  and:
    - file.inFolder("ideas")
    - file.hasProperty("status")
views:
  - type: table
    name: All
    groupBy:
      property: status
      direction: DESC
    order:
      - file.name
      - verdict
      - value
      - effort
      - promoted-to
      - updated
```
