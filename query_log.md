```sql
SELECT COUNT(*) FROM default.births2000db;

```

```response from Databricks
[Row(count(1)=200)]
```

```sql
SELECT COUNT(*) FROM default.births1994db;

```

```response from Databricks
[Row(count(1)=200)]
```

```sql
SELECT DISTINCT year FROM default.births2000db
```

```response from Databricks
[Row(year=2000)]
```

```sql
SELECT DISTINCT year FROM default.births1994db
```

```response from Databricks
[Row(year=1994)]
```

```sql
SELECT t1.day_of_week, AVG(t1.births) AS avg_daily_births FROM default.births2000db t1 GROUP BY t1.day_of_week;
```

```response from Databricks
[Row(day_of_week=6, avg_daily_births=8914.310344827587), Row(day_of_week=2, avg_daily_births=12667.172413793103), Row(day_of_week=5, avg_daily_births=12372.785714285714), Row(day_of_week=3, avg_daily_births=12494.67857142857), Row(day_of_week=1, avg_daily_births=11408.793103448275), Row(day_of_week=7, avg_daily_births=7899.241379310345), Row(day_of_week=4, avg_daily_births=12570.785714285714)]
```
```sql
SELECT     COALESCE(t1.day_of_week, t2.day_of_week) AS day_of_week,    AVG(t1.births) AS avg_births_2000,    AVG(t2.births) AS avg_births_1994,    COUNT(t1.date_of_month) AS days_recorded_2000,    COUNT(t2.date_of_month) AS days_recorded_1994 FROM     default.births2000db t1 FULL OUTER JOIN     default.births1994db t2 ON t1.day_of_week = t2.day_of_week GROUP BY     COALESCE(t1.day_of_week, t2.day_of_week) ORDER BY     day_of_week;
```

```response from Databricks
[Row(day_of_week=1, avg_births_2000=11408.793103448275, avg_births_1994=10856.51724137931, days_recorded_2000=841, days_recorded_1994=841), Row(day_of_week=2, avg_births_2000=12667.172413793103, avg_births_1994=12030.344827586207, days_recorded_2000=841, days_recorded_1994=841), Row(day_of_week=3, avg_births_2000=12494.67857142857, avg_births_1994=11775.92857142857, days_recorded_2000=784, days_recorded_1994=784), Row(day_of_week=4, avg_births_2000=12570.785714285714, avg_births_1994=11816.285714285714, days_recorded_2000=784, days_recorded_1994=784), Row(day_of_week=5, avg_births_2000=12372.785714285714, avg_births_1994=11773.57142857143, days_recorded_2000=784, days_recorded_1994=784), Row(day_of_week=6, avg_births_2000=8914.310344827587, avg_births_1994=8894.310344827587, days_recorded_2000=841, days_recorded_1994=841), Row(day_of_week=7, avg_births_2000=7899.241379310345, avg_births_1994=8213.068965517241, days_recorded_2000=841, days_recorded_1994=841)]
```

