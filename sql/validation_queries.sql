-- Validate total row count
SELECT COUNT(*) FROM your_schema.your_table;

-- Check for missing important data
SELECT * FROM your_schema.your_table WHERE important_column IS NULL;

-- Preview sample records
SELECT * FROM your_schema.your_table LIMIT 10;
