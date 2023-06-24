ATTACH TABLE _ UUID 'd081c1ea-d22b-4dab-a052-6a8efc0a07f1'
(
    `_airbyte_ab_id` String,
    `_airbyte_data` String,
    `_airbyte_emitted_at` DateTime64(3, 'GMT') DEFAULT now()
)
ENGINE = MergeTree
PRIMARY KEY _airbyte_ab_id
ORDER BY _airbyte_ab_id
SETTINGS index_granularity = 8192
