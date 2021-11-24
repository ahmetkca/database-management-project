#!/bin/bash
function exec_postgres () {
    docker-compose exec db psql -U postgres -d api-db -c "$1"
}


echo ' ... Create Views ... '
exec_postgres 'CREATE VIEW view1 AS select product_id as "Product ID", product_name as "Product Name", product_description as "Product Description", price as "Price", S1.product_specification_name as "Specification 1", S1.product_specification_value as "Specification 1 Value", S2.product_specification_name as "Specification 2", S2.product_specification_value as "Specification 2 Value", S3.product_specification_name as "Specification 3", S3.product_specification_value as "Specification 3 Value", PT.product_type_name as "Product Type" from api_product as P join api_producttype as PT on P.product_type_id = PT.product_type_id left outer join api_productspecification as S1 on P.spec1_id = S1.product_specification_id left outer join api_productspecification as S2 on P.spec2_id = S2.product_specification_id left outer join api_productspecification as S3 on P.spec3_id = S3.product_specification_id' && echo "View1 has been successfully created"

exec_postgres 'create view view2 as select api_producttype.product_type_name as "Product Type", count(*) as "Number of Products" from api_product right outer join api_producttype on api_producttype.product_type_id = api_product.product_type_id where api_product.product_type_id = any ( select product_type_id from api_producttype ) group by "Product Type"' && echo "View2 has been successfully created"

exec_postgres 'create view view3 as select employee_id as "Employee ID", first_name as "First Name", last_name as "Last Name", date_of_birth as "Date of Birth", work_place_id as "Works in Store with id:" from api_employee as E where extract(year from date_of_birth) in ( select min(extract(year from date_of_birth)) from api_employee where E.work_place_id = work_place_id )' && echo "View3 has been successfully created"

exec_postgres 'create view view4 as select api_order.order_id as "Order ID", first_name as "First Name", last_name as "Last Name" from api_customer full outer join api_order on api_customer.customer_id = "api_order".fk_customer_id order by api_order.order_id' && echo "View4 has been successfully created"

exec_postgres "create view view5 as select employee_id, gender, ssn, first_name, last_name, email, phone_number, work_place_id, address, date_of_birth from ( select * from api_employee where extract(year from api_employee.date_of_birth) > 2000 ) as E union select employee_id, gender, ssn, first_name, last_name, email, phone_number, work_place_id, address, date_of_birth from ( select * from api_firedemployee where extract(year from api_firedemployee.date_of_birth) < 2000 ) as FE" && echo "View5 has been successfully created"

exec_postgres "create view view8 as select product_id as \"Product id\", product_name as \"Product Name\", product_description as \"Product Description\", price as \"Price\", S1.product_specification_name as \"Specification 1\", S1.product_specification_value as \"Specification 1 Value\", S2.product_specification_name as \"Specification 2\", S2.product_specification_value as \"Specification 2 Value\", S3.product_specification_name as \"Specification 3\", S3.product_specification_value as \"Specification 3 Value\" from api_product as P join api_producttype as PT on P.product_type_id = PT.product_type_id left outer join api_productspecification as S1 on P.spec1_id = S1.product_specification_id left outer join api_productspecification as S2 on P.spec2_id = S2.product_specification_id left outer join api_productspecification as S3 on P.spec3_id = S3.product_specification_id where PT.product_type_name = 'Game'" && echo "View8 has been successfully created"

exec_postgres "create view view9 as select product_id as \"Product id\", product_name as \"Product Name\", product_description as \"Product Description\", price as \"Price\", S1.product_specification_name as \"Specification 1\", S1.product_specification_value as \"Specification 1 Value\", S2.product_specification_name as \"Specification 2\", S2.product_specification_value as \"Specification 2 Value\", S3.product_specification_name as \"Specification 3\", S3.product_specification_value as \"Specification 3 Value\" from api_product as P join api_producttype as PT on P.product_type_id = PT.product_type_id left outer join api_productspecification as S1 on P.spec1_id = S1.product_specification_id left outer join api_productspecification as S2 on P.spec2_id = S2.product_specification_id left outer join api_productspecification as S3 on P.spec3_id = S3.product_specification_id where PT.product_type_name = 'Hoodie'" && echo "View9 has been successfully created"

exec_postgres "create view view10 as select product_id as \"Product id\", product_name as \"Product Name\", product_description as \"Product Description\", price as \"Price\", S1.product_specification_name as \"Specification 1\", S1.product_specification_value as \"Specification 1 Value\", S2.product_specification_name as \"Specification 2\", S2.product_specification_value as \"Specification 2 Value\", S3.product_specification_name as \"Specification 3\", S3.product_specification_value as \"Specification 3 Value\" from api_product as P join api_producttype as PT on P.product_type_id = PT.product_type_id left outer join api_productspecification as S1 on P.spec1_id = S1.product_specification_id left outer join api_productspecification as S2 on P.spec2_id = S2.product_specification_id left outer join api_productspecification as S3 on P.spec3_id = S3.product_specification_id where PT.product_type_name = 'System'" && echo "View10 has been successfully created"

exec_postgres "create view view11 as select product_id as \"Product id\", product_name as \"Product Name\", product_description as \"Product Description\", price as \"Price\", S1.product_specification_name as \"Specification 1\", S1.product_specification_value as \"Specification 1 Value\", S2.product_specification_name as \"Specification 2\", S2.product_specification_value as \"Specification 2 Value\", S3.product_specification_name as \"Specification 3\", S3.product_specification_value as \"Specification 3 Value\" from api_product as P join api_producttype as PT on P.product_type_id = PT.product_type_id left outer join api_productspecification as S1 on P.spec1_id = S1.product_specification_id left outer join api_productspecification as S2 on P.spec2_id = S2.product_specification_id left outer join api_productspecification as S3 on P.spec3_id = S3.product_specification_id where PT.product_type_name = 'Monitor'" && echo "View11 has been successfully created"

exec_postgres "create view view12 as select product_id as \"Product id\", product_name as \"Product Name\", product_description as \"Product Description\", price as \"Price\", S1.product_specification_name as \"Specification 1\", S1.product_specification_value as \"Specification 1 Value\", S2.product_specification_name as \"Specification 2\", S2.product_specification_value as \"Specification 2 Value\", S3.product_specification_name as \"Specification 3\", S3.product_specification_value as \"Specification 3 Value\" from api_product as P join api_producttype as PT on P.product_type_id = PT.product_type_id left outer join api_productspecification as S1 on P.spec1_id = S1.product_specification_id left outer join api_productspecification as S2 on P.spec2_id = S2.product_specification_id left outer join api_productspecification as S3 on P.spec3_id = S3.product_specification_id where PT.product_type_name = 'Headset'" && echo "View12 has been successfully created"

exec_postgres "create view view13 as select product_id as \"Product id\", product_name as \"Product Name\", product_description as \"Product Description\", price as \"Price\", S1.product_specification_name as \"Specification 1\", S1.product_specification_value as \"Specification 1 Value\", S2.product_specification_name as \"Specification 2\", S2.product_specification_value as \"Specification 2 Value\", S3.product_specification_name as \"Specification 3\", S3.product_specification_value as \"Specification 3 Value\" from api_product as P join api_producttype as PT on P.product_type_id = PT.product_type_id left outer join api_productspecification as S1 on P.spec1_id = S1.product_specification_id left outer join api_productspecification as S2 on P.spec2_id = S2.product_specification_id left outer join api_productspecification as S3 on P.spec3_id = S3.product_specification_id where PT.product_type_name = 'Charger'" && echo "View13 has been successfully created"