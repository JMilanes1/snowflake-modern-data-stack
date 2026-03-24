with source as (
    select
        date,
        value,
        series_id
    from {{ source('raw', 'unemployment') }}
),

renamed as (
    select
        date                as unemployment_date,
        value               as unemployment_rate,
        series_id           as series_id
    from source
)

select * from renamed
