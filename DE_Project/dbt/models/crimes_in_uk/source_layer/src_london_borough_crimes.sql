with crime_data as 
(
  select *
  from {{ source('source','london_borough') }}
  where crime_category is not null 
)

select * from crime_data