with source as (
    select
        date,
        value,
        series_id
    from {{ source('raw', 'inflation') }}
),

renamed as (
    select
        date                as inflation_date,
        value               as cpi_value,
        series_id           as series_id
    from source
)

select * from renamed
