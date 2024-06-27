USE serverlessSQLdatabase
GO

CREATE OR ALTER PROC CreateSQLServerlessView_gold @viewName nvarchar(100)
AS
BEGIN

DECLARE @statement VARCHAR(MAX)

    SET @statement = N'CREATE OR ALTER VIEW ' + @viewName + ' AS 
        SELECT *
        FROM
            OPENROWSET(
            BULK ''https://klydatalake.dfs.core.windows.net/gold/SalesLT/' + @viewName + '/'',
            FORMAT = ''DELTA''
        ) as [result]
    '

EXEC (@statement)

END
GO