---
creation date: <% tp.file.creation_date() %>
modification date: <% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %>
tags:
  - "#Lecture"
year: <% tp.date.now("YYYY") %>
semester: <%tp.user.getSemester()%>
Lecture: <% tp.file.folder(true) %>
---
---
# [[<%tp.file.title%>]]


## Assignments

 ```dataview
table file.name, links
from "<%tp.file.folder(true)%>"
where contains(file.tags, "#Assignments") and contains(file.path, this.file.name)
```



## Notes


 ```dataview
table file.name, links
from "<%tp.file.folder(true)%>"
where contains(file.tags, "#Notes") and contains(file.path, this.file.name)
```



