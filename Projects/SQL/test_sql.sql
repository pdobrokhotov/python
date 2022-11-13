select 1 as RowNum
UNION
select 2 as RowNum
GO
select top 10 * 
FROM [AdventureWorks2014].[Person].[Person]