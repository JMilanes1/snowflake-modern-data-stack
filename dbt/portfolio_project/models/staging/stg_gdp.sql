with source as (
    select
        date,
        value,
        series_id
    from {{ source('raw', 'gdp') }}
),

renamed as (
    select
        date                as gdp_date,
        value               as gdp_value,
        series_id           as series_id
    from source
)

select * from renamed
