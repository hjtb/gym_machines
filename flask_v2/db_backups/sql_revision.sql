SELECT * FROM (
SELECT 
    main_contact,region, count(1) as number_companies, SUM(ytd_sales) AS 'total_sales', avg(ytd_sales) as average_sales
FROM
    training_schema.companies
WHERE
    region IN ('SWE' , 'IRE', "USA")
        AND ytd_sales > 3000
        AND name like '%d%'
GROUP BY main_contact,region
ORDER BY total_sales DESC) as test
where main_contact is not null
order by region;
