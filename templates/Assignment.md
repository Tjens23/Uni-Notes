---
creation date: <% tp.file.creation_date() %>
modification date: <% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %>
tags:
  - Assignments
year: <% tp.date.now("YYYY") %>
semester: <%tp.user.getSemester()%>
links:
---

---
# [[<%tp.file.title%>]]
