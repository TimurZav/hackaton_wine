ATTACH TABLE _ UUID 'ab4ebf8a-55a0-4741-b69a-68f096e0957c'
(
    `id` String,
    `coordinate_x1` Nullable(Decimal(38, 19)),
    `coordinate_y1` Nullable(Decimal(38, 19)),
    `coordinate_x2` Nullable(Decimal(38, 19)),
    `coordinate_y2` Nullable(Decimal(38, 19)),
    `date` Nullable(Date),
    `temperature` Nullable(Int32),
    `airHumidity` Nullable(Int32),
    `windSpeed` Nullable(Int32),
    `precipitation` Nullable(Int32),
    `fixed_acidity` Decimal(38, 19),
    `volatile_acidity` Nullable(Decimal(38, 19)),
    `citric_acid` Nullable(Decimal(38, 19)),
    `residual_sugar` Nullable(Decimal(38, 19)),
    `chlorides` Nullable(Decimal(38, 19)),
    `free_sulfur_dioxide` Nullable(Decimal(38, 19)),
    `total_sulfur_dioxide` Nullable(Decimal(38, 19)),
    `density` Nullable(Decimal(38, 19)),
    `pH` Nullable(Decimal(38, 19)),
    `sulphates` Nullable(Decimal(38, 19)),
    `alcohol` Nullable(Decimal(38, 19)),
    `winecolor` Nullable(String)
)
ENGINE = MergeTree
ORDER BY id
SETTINGS index_granularity = 8192
