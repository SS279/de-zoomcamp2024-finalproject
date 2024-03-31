{{
    config(
        materialized='table'
    )
}}

with stg_data as 
(
  select *
  from {{ ref('stg_london_borough_crimes') }}
)

select
{{ dbt_utils.star(from=ref('stg_london_borough_crimes'), except=['london_boroughname', 'month_year', 'count_val']) }}
, london_boroughname as london_borough_name
, month_year
, count_val as no_of_crimes_committed
from stg_data