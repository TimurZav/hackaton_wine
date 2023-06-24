ATTACH TABLE _ UUID 'ba905409-3c8d-4159-8b69-7b08e7250b67'
(
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
    `winecolor` Nullable(String),
    `quality` Nullable(Decimal(38, 19))
)
ENGINE = MergeTree
ORDER BY fixed_acidity
SETTINGS index_granularity = 8192
