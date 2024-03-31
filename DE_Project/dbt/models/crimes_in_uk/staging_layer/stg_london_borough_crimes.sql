{{
    config(
        materialized='table'
    )
}}

with unpivot_src_data as (
{{
    dbt_utils.unpivot(
        relation=ref("src_london_borough_crimes"),
        cast_to="integer",
        exclude=["crime_category", "crime_type", "london_boroughname"],
        field_name="month_year",
        value_name="count_val"
    )
}}

)

select
*
from unpivot_src_data
