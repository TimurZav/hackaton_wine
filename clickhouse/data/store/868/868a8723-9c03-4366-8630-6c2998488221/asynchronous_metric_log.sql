ATTACH TABLE _ UUID '0edb2af1-05dc-4803-94e3-114a761b1d33'
(
    `event_date` Date CODEC(Delta(2), ZSTD(1)),
    `event_time` DateTime CODEC(Delta(4), ZSTD(1)),
    `metric` LowCardinality(String) CODEC(ZSTD(1)),
    `value` Float64 CODEC(ZSTD(3))
)
ENGINE = MergeTree
PARTITION BY toYYYYMM(event_date)
ORDER BY (metric, event_date, event_time)
SETTINGS index_granularity = 8192
