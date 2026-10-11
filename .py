[1mdiff --git a/.env.example b/.env.example[m
[1mindex d880c01..cd914e3 100644[m
[1m--- a/.env.example[m
[1m+++ b/.env.example[m
[36m@@ -1 +1 @@[m
[31m-TASK_MANAGER_ADMIN_PASSWORD=your_password_here[m
\ No newline at end of file[m
[32m+[m[32mTASK_MANAGER_ADMIN_PASSWORD=change_this_password[m
\ No newline at end of file[m
[1mdiff --git a/tasks.py b/tasks.py[m
[1mindex a7e1279..b258aa0 100644[m
[1m--- a/tasks.py[m
[1m+++ b/tasks.py[m
[36m@@ -41,7 +41,7 @@[m [mdef show_tasks(tasks):[m
                 tasks[i]["title"],[m
                 "-",[m
                 tasks[i]["status"],[m
[31m-                "- Priority Level:",[m
[32m+[m[32m              "- Task Priority:",[m
                 priority[m
             )[m
 [m
