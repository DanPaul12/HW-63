
SELECT 
    product_id, 
    SUM(quantity) AS total_quantity_sold
FROM 
    factory_application.orders
GROUP BY 
    product_id
ORDER BY 
    total_quantity_sold DESC;
    
SELECT
	customer_id, SUM(total_price) AS total_paid
FROM 
    factory_application.orders
GROUP BY
	customer_id
HAVING total_paid > 0;



SELECT name, quantity_produced, date_produced
FROM production
join products on products.id = production.product_id
where date_produced in (
	select date_produced from production where date_produced = "2024-10-09");