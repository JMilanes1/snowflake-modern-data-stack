with gdp as (
    select
        gdp_date        as date,
        gdp_value
    from {{ ref('stg_gdp') }}
),

unemployment as (
    select
        unemployment_date   as date,
        unemployment_rate
    from {{ ref('stg_unemployment') }}
),

inflation as (
    select
        inflation_date      as date,
        cpi_value
    from {{ ref('stg_inflation') }}
),

joined as (
    select
        g.date,
        g.gdp_value,
        u.unemployment_rate,
        i.cpi_value
    from gdp g
    left join unemployment u on g.date = u.date
    left join inflation i on g.date = i.date
)

select * from joined
order by date
