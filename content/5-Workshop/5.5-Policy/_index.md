---
title : "Validate DynamoDB, indexes, and PITR"
date : 2026-07-09
weight : 5
chapter : false
pre : " <b> 5.5 </b> "
---

#### Goal

This section validates TaskManager DynamoDB tables, query indexes, and Point-in-Time Recovery (PITR) configuration.

#### Check DynamoDB tables

1. Open the **Amazon DynamoDB** console.
2. Choose **Tables**.
3. Review the tables with the `TaskManager` prefix.

![DynamoDB tables](/FCAJ_My_Workshop/images/5-Workshop/TaskManager/dynamodb.png)

Main tables:

- `TaskManager-ActivityLogs-dev`
- `TaskManager-Boards-dev`
- `TaskManager-Notifications-dev`
- `TaskManager-Tasks-dev`
- `TaskManager-Users-dev`

The tables are **Active** and use **On-demand** capacity mode, which is suitable for small or unpredictable workloads because read/write capacity does not need to be configured manually.

#### Check Global Secondary Index

Open the `TaskManager-Users-dev` table and choose the **Indexes** tab.

![DynamoDB indexes](/FCAJ_My_Workshop/images/5-Workshop/TaskManager/indextables.png)

The `TaskManager-Users-dev` table has this GSI:

- Index name: `EmailIndex`
- Partition key: `email`
- Status: `Active`
- Capacity: On-demand

This index allows the system to find users by email efficiently without scanning the entire table.

#### Check PITR on important tables

Point-in-Time Recovery allows DynamoDB to keep continuous backups for up to 35 days. This is useful when data is accidentally updated or deleted.

##### Enable PITR

![Edit PITR](/FCAJ_My_Workshop/images/5-Workshop/TaskManager/pitr-edit.png)

The **Edit point-in-time recovery settings** page shows PITR enabled with a 35-day backup recovery period.

##### Board table

![Boards PITR](/FCAJ_My_Workshop/images/5-Workshop/TaskManager/pitr-board.png)

`TaskManager-Boards-dev`:

- Partition key: `boardId`
- Capacity mode: On-demand
- Table status: Active
- PITR: On

##### Task table

![Tasks PITR](/FCAJ_My_Workshop/images/5-Workshop/TaskManager/pitr-tasks.png)

`TaskManager-Tasks-dev`:

- Partition key: `boardId`
- Sort key: `taskId`
- Capacity mode: On-demand
- Table status: Active
- PITR: On

##### User table

![Users PITR](/FCAJ_My_Workshop/images/5-Workshop/TaskManager/pitr-users.png)

`TaskManager-Users-dev`:

- Partition key: `userId`
- Capacity mode: On-demand
- Table status: Active
- PITR: On

#### Conclusion

DynamoDB is configured appropriately for TaskManager: tables are separated by domain, an email lookup index is available, on-demand capacity is enabled, and PITR protects important data tables.
