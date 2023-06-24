ATTACH TABLE _ UUID '83c716ed-f225-46bb-89a6-38856aebf7f4'
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
    `precipitation` Nullable(Int32)
)
ENGINE = MergeTree
ORDER BY id
SETTINGS index_granularity = 8192
